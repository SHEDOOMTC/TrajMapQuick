""" Core logic for generating shift graphs of detected 
peak regions of a protein in an automated way

"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from ..utils.utils import detect, extract_region_submatrices, slice_matrix2shift, auto_limits


def detect_shifts(matrix, window, mindist, hotspot):
    regions, mean_shift, smooth = detect(
        matrix=matrix,
        window=window,
        mindist=mindist,
        hotspot=hotspot,)
    return mean_shift, smooth, regions

def create_submatrices(matrix, window, mindist, hotspot):
    regions, mean_shift, smooth = detect(
        matrix=matrix,
        window=window,
        mindist=mindist,
        hotspot=hotspot)
    
    regions_only = [(start, end) for (start, peak, end) in regions]
    submatrices = extract_region_submatrices(matrix, regions_only)
    return submatrices, regions, mean_shift, smooth

def plot_shift_regions(shift_data, start_residue, end_residue, color="blue", window=10, title=None):
    df = pd.DataFrame(shift_data)
    roll = df.rolling(window, center=True, min_periods=1).mean()
    x_min, x_max, y_min, y_max = auto_limits(df)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df, linewidth=0.3, color=color,
            label=f"residues {start_residue}-{end_residue}")
    ax.plot(roll, linewidth=3.0, color=color)
    ax.legend(loc='upper left', fancybox=True, shadow=True,
              prop={'size': 14, 'weight': 'bold'})

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    x_range = x_max - x_min
    if x_range <= 500:
        x_step = 50
    elif x_range <= 1000:
        x_step = 100
    else:
        x_step = 200
    ax.set_xticks(np.arange(x_min, x_max + 1, x_step))
    ax.tick_params(axis='x', labelsize=16)
    y_range = y_max - y_min
    if y_range <= 2:
        y_step = 0.2
    elif y_range <= 5:
        y_step = 0.5
    elif y_range <= 10:
        y_step = 1
    else:
        y_step = 5
    ax.set_yticks(np.arange(y_min, y_max + 0.5, y_step))
    ax.tick_params(axis='y', labelsize=16)
    ax.set_yticklabels([f"{y:.2f}" for y in ax.get_yticks()])
    for tick in ax.get_xticklabels():
        tick.set_fontweight("bold")
    for tick in ax.get_yticklabels():
        tick.set_fontweight("bold")
    ax.set_title(title if title else f"Shift Graph {start_residue}-{end_residue}",
                 fontsize=20, fontweight="bold")
    ax.set_xlabel("Frames", fontsize=20, fontweight="bold")
    ax.set_ylabel("Shift / Å", fontsize=20, fontweight="bold")
    ax.xaxis.set_minor_locator(MultipleLocator((x_max - x_min) / 50))
    fig.tight_layout()
    plt.close(fig)
    return fig


def slice_shifts(matrix, window, mindist, hotspot):
    regions, mean_shift, smooth = detect(
        matrix=matrix,
        window=window,
        mindist=mindist,
        hotspot=hotspot)

    regions_only = [(start, end) for (start, peak, end) in regions]
    submatrices = extract_region_submatrices(matrix, regions_only)
    results = []

    for start, end, submatrix in submatrices:
        params = [0, submatrix.shape[0] - 1, 0, submatrix.shape[1] - 1]
        shift_data = slice_matrix2shift(submatrix, params)
        shift_data = shift_data[2:]
        results.append((start, end, shift_data))
    return results


def plot_slice_regions(shift_data, start, end):
    return plot_shift_regions(
        shift_data=shift_data,
        start_residue=start,
        end_residue=end,
        title=f"Region {start}-{end}" )


def plot_hotspot_regions(mean_shift, smooth, regions, title="Residue Shift Hotspots"):
    residues = np.arange(len(mean_shift))
    df = pd.DataFrame(mean_shift)
    x_min, x_max, y_min, y_max = auto_limits(df)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(residues, mean_shift, color="gray", alpha=0.4, linewidth=0.8, label="Mean shift")
    ax.plot(residues, smooth, color="blue", linewidth=3.5, label="Smoothed")

    for (start, peak, end) in regions:
        ax.axvspan(start, end, color="white", alpha=0.7)
        ax.plot(peak, smooth[peak], "ro")
        ax.text(peak, smooth[peak], f" {peak}", color="red", fontsize=9, fontweight="bold")

    ax.legend(loc='upper left', fancybox=True, shadow=True,
              prop={'size': 8, 'weight': 'bold'})
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    x_range = x_max - x_min
    if x_range <= 200:
        x_step = 25
    elif x_range <= 500:
        x_step = 50
    elif x_range <= 1000:
        x_step = 100
    else:
        x_step = 200
    ax.set_xticks(np.arange(x_min, x_max + 1, x_step))
    ax.tick_params(axis='x', labelsize=12)

    y_range = y_max - y_min
    if y_range <= 2:
        y_step = 0.2
    elif y_range <= 5:
        y_step = 0.5
    elif y_range <= 10:
        y_step = 1
    else:
        y_step = 5
    ax.set_yticks(np.arange(y_min, y_max + 0.5, y_step))
    ax.tick_params(axis='y', labelsize=12)
    for tick in ax.get_xticklabels():
        tick.set_fontweight("bold")
    for tick in ax.get_yticklabels():
        tick.set_fontweight("bold")

    ax.set_title(title, fontsize=18, fontweight="bold")
    ax.set_xlabel("Residue index", fontsize=16, fontweight="bold")
    ax.set_ylabel("Mean shift / Å", fontsize=16, fontweight="bold")
    ax.xaxis.set_minor_locator(MultipleLocator((x_max - x_min) / 50))
    ax.yaxis.set_minor_locator(MultipleLocator((y_max - y_min) / 50))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    plt.close(fig)
    return fig
