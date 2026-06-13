# `tmq/core/traj2pdb.py` — Function docstrings

This file collects concise docstrings for functions defined in `tmq/core/traj2pdb.py`.

---

## traj2pdb(topology, trajectory, stride)
"""Load a trajectory, select backbone atoms, and align frames to the first frame.

Parameters:
- topology (str or mdtraj.Topology): path to topology file or an mdtraj topology object used when loading the trajectory.
- trajectory (str or list): path to trajectory file(s) or iterable of trajectory paths/objects recognizable by mdtraj.
- stride (int): frame stride used when loading the trajectory (sample every `stride` frames).

Returns:
- mdtraj.Trajectory: the loaded trajectory after backbone atom selection and superposition onto the first frame.


---

## pdb2csv(pdb_file, residue_start, residue_end, mode)
"""Compute a residue×frame distance matrix from a multi-model PDB.

Parameters:

Returns:
"""

---

## csv2shift.shift(matrix, residue_start, residue_end)
"""Compute a time-series shift by averaging a residue range across all frames.

Parameters:
- matrix (pandas.DataFrame or array): residue×frame numeric matrix
- residue_start (int), residue_end (int): inclusive residue index range

Returns:
- numpy.ndarray or pandas-compatible sequence: 1D shift series over frames
"""

---


## shift2graph(df, residue_label, window=10)
"""Plot a shift time-series with a rolling-average overlay and return the figure.

Parameters:
- df (pandas.DataFrame or Series): time-series data for residues
- residue_label (str): label shown in the legend
- window (int): window size for rolling average (default 10)

Returns:
- matplotlib.figure.Figure: closed figure containing the shift plot
"""

---

## trajmap(matrix, residue_start, residue_end, vmax)
"""Render a trajectory heatmap figure from a residue×frame matrix.

Parameters:
- matrix (pandas.DataFrame): residue × time matrix of shifts
- residue_start (int), residue_end (int): residue index range shown on y-axis
- vmax (float): maximum colorbar value

Returns:
- matplotlib.figure.Figure: figure containing the trajectory map (closed)
"""

---

## detect_shifts(matrix, window, mindist, hotspot)
"""Return mean shift, smoothed series, and detected hotspot regions.
"""

## create_submatrices(matrix, window, mindist, hotspot)
"""Return submatrices for each detected region plus region metadata.
"""

## plot_shift_regions(shift_data, start_residue, end_residue, color="blue", window=10, title=None)
"""Plot a shift time-series for a residue interval and return the figure.
"""

## slice_shifts(matrix, window, mindist, hotspot)
"""Extract per-region 1D shift arrays from detected submatrices.
"""

## plot_slice_regions(shift_data, start, end)
"""Convenience wrapper to plot a sliced region's shift series.
"""

## plot_hotspot_regions(mean_shift, smooth, regions, title="Residue Shift Hotspots")
"""Plot mean shift and highlighted hotspot regions; returns a Figure.
"""

---

## diff2graph.diff_map(matrix1, matrix2, vmax, residue_start, residue_end)
"""Render a difference heatmap (A - B) and return the figure.

Parameters:
- matrix1, matrix2 (array-like): residue×frame numeric matrices
- vmax (float): absolute value used to scale the colormap
- residue_start (int), residue_end (int): residue indices for y-axis labeling

Returns:
- matplotlib.figure.Figure: closed figure containing the difference heatmap
"""
---

## average_trajmap.avg_trajmap(residue_start, residue_end, vmax, *matrices)
"""Compute an element-wise average of input matrices and render a trajectory map figure.

Parameters:
- residue_start (int), residue_end (int): residue range shown on y-axis
- vmax (float): maximum colorbar value forwarded to the map renderer
- *matrices: two or more residue×frame numeric matrices (array-like or DataFrame)

Returns:
- matplotlib.figure.Figure: closed figure produced by `trajmap` for the averaged matrix
"""







