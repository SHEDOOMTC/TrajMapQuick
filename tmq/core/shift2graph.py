""" Core logic for making the shift plot

"""


import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from ..utils.utils import auto_limits, rolling_average


def shift2graph(df, residue_label, window=10):
    roll_df = rolling_average(df, window)
    x_min, x_max, y_min, y_max = auto_limits(df)
    color = "blue"
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(df, linewidth=0.3, color=color, label=f"residues {residue_label}")
    ax.plot(roll_df, linewidth=3.0, color=color)
    ax.legend(loc='upper left', fancybox=True, shadow=True,
              prop={'size': 14, 'weight': 'bold'})

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    x_range = x_max - x_min
    if x_range <= 100:
        x_step = 10
    elif x_range <= 500:
        x_step = 50
    elif x_range <= 1000:
        x_step = 100
    else:
        x_step = 200
    ax.set_xticks(np.arange(x_min, x_max + 1, x_step))
    ax.tick_params(axis='x', labelsize=14)

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
    ax.tick_params(axis='y', labelsize=14)
    ax.set_yticklabels([f"{y:.2f}" for y in ax.get_yticks()])
    for tick in ax.get_xticklabels():
        tick.set_fontweight("bold")
    for tick in ax.get_yticklabels():
        tick.set_fontweight("bold")

    ax.set_title("Shift Graph", fontsize=20, fontweight="bold")
    ax.set_xlabel("Frames", fontsize=18, fontweight="bold")
    ax.set_ylabel("Shift / Å", fontsize=18, fontweight="bold")

    ax.yaxis.set_minor_locator(MultipleLocator((y_max - y_min) / 10))
    fig.tight_layout()
    plt.close(fig)
    return fig
