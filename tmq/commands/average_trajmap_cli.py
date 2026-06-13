"""Parse input matrices, compute their element-wise average, 
and save an averaged trajectory map PNG.
"""

import time
from ..core.average_trajmap import avg_trajmap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from ..utils.utils import ensure_csv_extension, ensure_png_extension, parse_range, load_matrix_4_diff_map, csv2matrix


def avg_trajmap_cli(args):
    start_time = time.perf_counter()
    print("")
    print("Plotting Average map...")

    """split the matrix argument to get list of matrices
    """
    matrix_names = args.mat.split(",")
    prefix = "_pdb2csv_"
    matrices = [csv2matrix(ensure_csv_extension(name + prefix)) for name in matrix_names]

    residue_start, residue_end = parse_range(args.resr)

    """pass the matrices to the core function
    """
    fig = avg_trajmap(residue_start, residue_end, args.max, *matrices)

    prefix1 = "_average_map_"
    savename = ensure_png_extension(args.out + prefix1)
    fig.savefig(savename, dpi=800, bbox_inches='tight')
    print(f"Difference map saved to {savename}")
    plt.close(fig)
    total = time.perf_counter() - start_time
    print(f"Time taken to plot Difference map: {total:.2f} seconds")