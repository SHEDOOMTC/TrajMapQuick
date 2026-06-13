"""Load a residue×frame matrix, render a trajectory heatmap, and save the PNG figure.
"""

import time
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from ..core.trajmap import trajmap
from ..utils.utils import csv2matrix, ensure_csv_extension, ensure_png_extension, parse_range


def trajmap_cli(args):
    start_time = time.perf_counter()
    print("")
    print("Plotting trajectory map...")
    prefix = "_pdb2csv_"
    file = ensure_csv_extension(args.out + prefix)
    matrix = csv2matrix(file)
    residue_start, residue_end = parse_range(args.resr)
    prefix1 = "_trajmap_"
    savename = ensure_png_extension(args.out + prefix1)

    fig = trajmap(matrix, residue_start, residue_end, args.max)

    fig.savefig(savename, dpi=800, bbox_inches='tight')
    print(f"Trajectory map saved to {savename}")
    plt.close(fig)
    total = time.perf_counter() - start_time
    print(f"Time taken to plot trajectory map: {total:.2f} seconds")
