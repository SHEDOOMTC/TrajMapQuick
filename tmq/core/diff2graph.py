""" Render a difference heatmap (A - B) and return the figure

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MultipleLocator
from ..utils.utils import compute_mat_diff




def diff_map(matrix1, matrix2, vmax, residue_start, residue_end):

    D = compute_mat_diff(matrix1, matrix2)

    # Internal style settings
    x_minor = 20
    y_major = 50
    y_minor = 10

    frames = D.shape[1]

    if frames <= 100:
        x_step = 10
    elif frames <= 500:
        x_step = 50
    else:
        x_step = 100

    fig, ax = plt.subplots(figsize=(12, 8))

    #handle NAN
    mask = np.isnan(D)

    sns.heatmap(D, cmap="bwr", center=0, vmin=-vmax, vmax=vmax, mask=mask, cbar=False)

    xticks = np.arange(0, frames + 1, x_step)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticks, rotation=0, fontsize=14)
    ax.xaxis.set_minor_locator(MultipleLocator(x_minor))

    for tick in ax.get_xticklabels():
        tick.set_fontweight("bold")

    # Y ticks
    residues = D.shape[0]
    ax.set_yticks(np.arange(0, residues, y_major))
    ax.set_yticklabels(np.arange(residue_start, residue_end, y_major), fontsize=14)
    ax.yaxis.set_minor_locator(MultipleLocator(y_minor))

    for tick in ax.get_yticklabels():
        tick.set_fontweight("bold")

    ax.invert_yaxis()

    # Labels
    ax.set_title("Difference Map", fontsize=20, fontweight="bold")
    ax.set_ylabel("Residue", fontsize=20, fontweight="bold")
    ax.set_xlabel("Frames", fontsize=20, fontweight="bold")

    # Colorbar
    im = ax.collections[0]
    cbar = fig.colorbar(im, fraction=0.029, pad=0.028)
    cbar.set_label("Shift (Å)", fontsize=14, fontweight="bold")

    for t in cbar.ax.get_yticklabels():
        t.set_fontweight("bold")
        t.set_fontsize(16)

    plt.tight_layout()
    plt.close()
    return fig
