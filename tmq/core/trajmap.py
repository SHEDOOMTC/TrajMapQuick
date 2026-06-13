""" This module instantiates the trajectory map plot 
for the residue range specified by the user

"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from ..utils.utils import choose_cmap, choose_aspect


def trajmap(matrix, residue_start, residue_end, vmax):
    x_minor = 20
    y_major = 50
    y_minor = 10
    vmin = matrix.iloc[:, 1:].values.min()
    cmap = choose_cmap('viridis_capped')
    aspect = choose_aspect('auto')
    frames = matrix.shape[1]
    if frames <= 100:
        x_step = 10
    elif frames <= 500:
        x_step = 50
    else:
        x_step = 100

    fig, ax = plt.subplots(figsize=(12, 8))
    im = ax.imshow(matrix, cmap=cmap, vmin=vmin, vmax=vmax, aspect=aspect)
    ax.invert_yaxis()

    ax.set_xticks(np.arange(0, frames + 1, step=x_step))
    ax.tick_params(axis='x', labelsize=14)
    ax.set_yticks(np.arange(residue_start, residue_end, step=y_major),)
    ax.tick_params(axis='y', labelsize=14)
    ax.yaxis.set_minor_locator(MultipleLocator(y_minor))
    ax.xaxis.set_minor_locator(MultipleLocator(x_minor))
    for tick in ax.get_xticklabels():
        tick.set_fontweight("bold")
    for tick in ax.get_yticklabels():
        tick.set_fontweight("bold")

    ax.set_title("Trajectory Map", fontsize=20, fontweight="bold")
    ax.set_ylabel("Residue", fontsize=18, fontweight="bold")
    ax.set_xlabel("Frames", fontsize=18, fontweight="bold")
    cbar = fig.colorbar(im, fraction=0.029, pad=0.028)
    cbar.set_label("Shift / Å", fontsize=12, fontweight="bold")
    fig.tight_layout()
    plt.close(fig)
    return fig