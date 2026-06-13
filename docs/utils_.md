# `tmq/utils/utils.py` — Function docstrings

This file collects concise docstrings for each public function defined in `tmq/utils/utils.py`.

---

## ensure_pdb_extension(name)
"""Ensure a filename ends with the `.pdb` extension.

Parameters:
- name (str): filename or path

Returns:
- str: filename ensuring `.pdb` suffix
"""

## load_traj(topology, trajectories, stride)
"""Load one or more trajectories using mdtraj.

Parameters:
- topology (str or mdtraj.Topology): topology file or object
- trajectories (str or list): trajectory filepath(s)
- stride (int): frame sampling stride

Returns:
- mdtraj.Trajectory: loaded trajectory (possibly strided)
"""

## select_backbone(traj)
"""Select backbone atoms from an mdtraj trajectory and return sliced trajectory.

Parameters:
- traj (mdtraj.Trajectory): input trajectory

Returns:
- mdtraj.Trajectory: atom-sliced trajectory containing backbone atoms
"""

## align_to_first_frame(traj)
"""Superpose all frames of `traj` onto the first frame.

Parameters:
- traj (mdtraj.Trajectory)

Returns:
- mdtraj.Trajectory: aligned trajectory (in-place superposition is used)
"""

## load_pdb_models(file)
"""Parse a PDB file and return a list of Bio.PDB Model objects.

Parameters:
- file (str): path to PDB file

Returns:
- list: Bio.PDB Model objects extracted from the structure
"""

## build_residue_lookup(model)
"""Build a mapping from residue sequence number to Bio.PDB Residue object for a model.

Parameters:
- model (Bio.PDB.Model): model from which to extract residues

Returns:
- dict: mapping {residue_number: Residue}
"""

## get_ca_coord(residue)
"""Return coordinates of the `CA` atom for a residue, or a zero vector if absent.

Parameters:
- residue (Bio.PDB.Residue)

Returns:
- np.ndarray: shape (3,) coordinates
"""

## get_backbone_com(residue, weights)
"""Compute a weighted center (approximate center of mass) of backbone atoms N, CA, C, O.

Parameters:
- residue (Bio.PDB.Residue)
- weights (dict): weight per atom name, e.g. `{ 'N':1.0, 'CA':1.0, ... }`

Returns:
- np.ndarray: shape (3,) weighted average coordinates, zeros if no backbone atoms present
"""

## distance(a, b)
"""Euclidean distance between two 3D coordinate arrays.

Parameters:
- a, b (array-like): length-3 coordinate vectors

Returns:
- float: Euclidean distance
"""

## ensure_csv_extension(name)
"""Ensure a filename ends with `.csv`.

Parameters:
- name (str)

Returns:
- str
"""

## csv2matrix(csv_file)
"""Load a CSV file into a pandas DataFrame.

Note: `csv2matrix` appears twice in the source with slightly different `index_col` usage; choose the variant appropriate for your caller.

Parameters:
- csv_file (str): path to CSV

Returns:
- pandas.DataFrame
"""

## matrix2shift(matrix, params)
"""Convert a residue×time matrix to a shift vector over a time window.

Parameters:
- matrix (DataFrame or array): input numeric matrix
- params (iterable): [res1, res2, time1, time2]

Returns:
- pandas.DataFrame or Series/array: averaged shift trace across residues in range
"""

## choose_cmap(cmap_choice)
"""Return a matplotlib colormap name for an integer choice.

Parameters:
- cmap_choice (int)

Returns:
- str: colormap name
"""

## choose_aspect(aspect)
"""Return an aspect string for plotting ('auto' or 'equal').

Parameters:
- aspect (int)

Returns:
- str
"""

## ensure_png_extension(name)
"""Ensure a filename ends with `.png`.

Parameters:
- name (str)

Returns:
- str
"""

## shift_to_dataframe(shift_data)
"""Load a shift file (CSV-like) into a float DataFrame and drop header rows.

Parameters:
- shift_data (str or file-like): CSV path

Returns:
- pandas.DataFrame: numeric data starting at row 3 of the file (source behavior)
"""

## rolling_average(df, window)
"""Compute a rolling mean over DataFrame `df` with window size `window`.

Parameters:
- df (pandas.DataFrame)
- window (int)

Returns:
- pandas.DataFrame: rolling mean
"""

## auto_limits(df)
"""Compute auto plot limits from a DataFrame of shift values.

Parameters:
- df (pandas.DataFrame)

Returns:
- tuple: (x_min, x_max, y_min, y_max)
"""

## parse_range(s)
"""Parse a range string like '110-125' into two integers (start, end).

Parameters:
- s (str)

Returns:
- tuple(int, int)

Raises:
- ValueError on invalid format
"""

## detect(matrix, window, mindist, hotspot)
"""Wrapper that calls `extract_residue_shift_regions` to detect fluctuation regions.

Parameters:
- matrix: numeric matrix
- window (int): smoothing window
- mindist (int): minimum peak distance
- hotspot (int): number of top regions

Returns:
- result of `extract_residue_shift_regions`
"""

## extract_residue_shift_regions(matrix, window, min_distance, top_n)
"""Detect prominent residue regions from a residue×time matrix by smoothing mean shifts and finding peaks.

Parameters:
- matrix (array-like or DataFrame)
- window (int): smoothing window size
- min_distance (int): minimum separation between peaks
- top_n (int): number of top peaks/regions to return

Returns:
- tuple: (regions_list, mean_shift_array, smooth_series) where regions_list contains (left, peak, right)
"""

## extract_region_submatrices(matrix, regions_only)
"""Extract submatrices corresponding to residue index intervals.

Parameters:
- matrix (pandas.DataFrame)
- regions_only (iterable): list of (start, end) indices

Returns:
- list of tuples: (start, end, numpy_submatrix)
"""

## slice_matrix2shift(matrix, params)
"""Compute a time-series shift by averaging rows in a residue slice over a time window.

Parameters:
- matrix (array-like or DataFrame)
- params (iterable): [res1, res2, time1, time2]

Returns:
- numpy.ndarray: 1D shift array of length (time2-time1)
"""

## load_matrix_4_diff_map(csv_path)
"""Load a CSV into a numeric NumPy matrix for difference mapping.

Parameters:
- csv_path (str)

Returns:
- numpy.ndarray
"""

## compute_mat_diff(A, B)
"""Compute the element-wise difference A - B after checking shape compatibility.

Parameters:
- A, B (numpy.ndarray)

Returns:
- numpy.ndarray: difference matrix

Raises:
- ValueError if shapes mismatch
"""

---

