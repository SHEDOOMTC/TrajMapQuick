# `tmq/commands` — CLI function docstrings

This file contains short, one-line docstrings for each command function in `tmq/commands`.

---

## average_trajmap_cli.avg_trajmap_cli(args)
"""Parse input matrices, compute their element-wise average, and save an averaged trajectory map PNG."""

## csv2shift_cli.shift_cli(args)
"""Load a distance matrix, compute residue-range shifts across frames, and write a shift CSV."""

## diff2graph_cli.diff_map_cli(args)
"""Load two matrices, render their difference heatmap (A−B), and save the figure PNG."""

## hotspot_cli.detect_shift_cli(args)
"""Detect hotspot regions in a distance matrix and return mean/smoothed series plus region indices."""

## hotspot_cli.create_submatrices_cli(args)
"""Extract and return submatrices corresponding to detected hotspot residue ranges."""

## hotspot_cli.slice_shifts_cli(args)
"""Find hotspot regions, compute per-region shift series, and save individual shift graphs."""

## hotspot_cli.run_hotspot_cli(args)
"""Run hotspot detection and save a summary hotspot-region plot PNG."""

## pdb2csv_cli.pdb2csv_cli(args)
"""Convert a multi-model PDB (produced from trajectories) into a residue×frame distance CSV."""

## shift2graph_cli.shift2graph_cli(args)
"""Load a shift CSV, plot the time-series with rolling-average, and save a PNG graph."""

## traj2pdb_cli.traj2pdb_cli(args)
"""Load a trajectory, select backbone, align frames, and write a combined PDB file."""

## trajmap_cli.trajmap_cli(args)
"""Load a residue×frame matrix, render a trajectory heatmap, and save the PNG figure."""

---

Notes:
- Each CLI accepts an `args` namespace (from argparse) and uses utility functions to read/write files and render figures.
