""" This contains all the utility functions used in the core modules and CLI wrappers

"""

import numpy as np
import pandas as pd
import mdtraj as mdt
from Bio.PDB import PDBParser



def ensure_pdb_extension(name):
    return name if name.endswith(".pdb") else name + ".pdb"

def load_traj(topology, trajectories, stride):
    return mdt.load(trajectories, top=topology, stride=stride)

def select_backbone(traj):
    idx = traj.topology.select("backbone")
    return traj.atom_slice(idx)

def align_to_first_frame(traj):
    return traj.superpose(traj, 0)


def load_pdb_models(file):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("prot", file)
    return list(structure.get_models())

def build_residue_lookup(model):
    lookup = {}
    for residue in model.get_residues():
        het, resnum, icode = residue.get_id()
        if het == " ":
            lookup[resnum] = residue
    return lookup


def get_ca_coord(residue):
    if "CA" in residue:
        return np.array(residue["CA"].coord, dtype=float)
    return np.zeros(3)

def get_backbone_com(residue, weights):
    coords = []
    w = []
    for atom_name in ["N", "CA", "C", "O"]:
        if atom_name in residue:
            atom = residue[atom_name]
            coords.append(atom.coord * weights[atom_name])
            w.append(weights[atom_name])
    if coords:
        return np.sum(coords, axis=0) / np.sum(w)
    return np.zeros(3)

def distance(a, b):
    return np.linalg.norm(a - b)

def ensure_csv_extension(name):
    return name if name.endswith(".csv") else name + ".csv"


def csv2matrix(csv_file):
    matrix = pd.read_csv(csv_file, index_col=0)
    return matrix


def matrix2shift(matrix, params):

    matrix_array = np.array(matrix)

    res1 = params[0]
    res2 = params[1]
    time1 = params[2]
    time2 = params[3]

    output = pd.DataFrame(data=np.arange(time1, time2, 1, dtype=float))

    if res1 == res2:
        output = matrix_array[res1]
    else:
        y = matrix_array[res1:res2, time1:time2]

        i = 0
        while i < len(output):
            output.iloc[i] = np.average(y[:, i])
            i = i + 1

    return output


def csv2matrix(file):
    return pd.read_csv(file, index_col=None)

def choose_cmap(cmap_choice):
    if cmap_choice == 0:
        return "magma"
    elif cmap_choice == 1:
        return "seismic"
    elif cmap_choice == 5:
        return "Greys"
    elif cmap_choice == 6:
        return "turbo"
    return "viridis"

def choose_aspect(aspect):
    if aspect == 0:
        return "auto"
    elif aspect == 1:
        return "equal"
    return "auto"

def ensure_png_extension(name):
    return name if name.endswith(".png") else name + ".png"


def shift_to_dataframe(shift_data):
    df = pd.read_csv(shift_data, header=None)
    df = df.astype(float)
    df = df.iloc[2:].reset_index(drop=True)
    return df

def rolling_average(df, window):
    return df.rolling(window).mean()

def auto_limits(df):
    col = df.iloc[:, 0]
    y_min = float(col.min())
    y_max = float(col.max() + 0.5)
    x_min = 0
    x_max = len(df) - 1
    return x_min, x_max, y_min, y_max



def parse_range(s):
    """
    Parse a residue range string like '110-125' into (110, 125).
    """
    try:
        start, end = map(int, s.split("-"))
        return start, end
    except Exception:
        raise ValueError("Residue range must be in the form start-end, e.g., 110-125")


import numpy as np
import pandas as pd
from scipy.signal import find_peaks

def detect(matrix, window, mindist, hotspot):
    return extract_residue_shift_regions(
        matrix,
        window,
        mindist,
        hotspot,
    )


def extract_residue_shift_regions(matrix, window, min_distance, top_n):

    mat = np.array(matrix, dtype=float)

    mean_shift = mat.mean(axis=1)

    smooth = pd.Series(mean_shift).rolling(window, center=True).mean()
    smooth = smooth.bfill().ffill()

    peaks, props = find_peaks(smooth, distance=min_distance, prominence=0.1)

    if len(peaks) == 0:
        return []

    prominences = props["prominences"]
    ranked = np.argsort(prominences)[::-1]
    top_peaks = peaks[ranked][:top_n]

    regions = []
    for p in top_peaks:
        left = p
        while left > 0 and smooth[left] > smooth[p] * 0.5:
            left -= 1

        right = p
        while right < len(smooth)-1 and smooth[right] > smooth[p] * 0.5:
            right += 1

        regions.append((left, p, right))

    return regions, mean_shift, smooth


def extract_region_submatrices(matrix, regions_only):
    mat = matrix.values
    submatrices = []
    for start, end in regions_only:
        sub = mat[start:end+1, :]  
        submatrices.append((start, end, sub))
    return submatrices


def slice_matrix2shift(matrix, params):

    matrix_array = np.array(matrix)

    res1 = params[0]
    res2 = params[1]
    time1 = params[2]
    time2 = params[3]

    output = np.zeros(time2 - time1)

    if res1 == res2:
        output[:] = matrix_array[res1, time1:time2]
    else:
        y = matrix_array[res1:res2+1, time1:time2]
        for i in range(output.shape[0]):
            output[i] = np.mean(y[:, i])

    return output



def load_matrix_4_diff_map(csv_path):
    """Load a CSV file into a numeric matrix."""
    return pd.read_csv(csv_path, header=None).values

def compute_mat_diff(A, B):
    """Compute A - B with NaN mask."""
    if A.shape != B.shape:
        raise ValueError(f"Matrix shapes do not match: {A.shape} vs {B.shape}")
    return A - B