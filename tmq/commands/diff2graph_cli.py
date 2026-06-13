"""Load two matrices, render their difference heatmap (A−B), and save the figure PNG.
"""

import time
from ..core.diff2graph import diff_map
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from ..utils.utils import ensure_csv_extension, ensure_png_extension, parse_range, load_matrix_4_diff_map



def diff_map_cli(args):
    start_time = time.perf_counter()
    print("")
    print("Plotting Difference map...")

    prefix = "_pdb2csv_"
    file1 = ensure_csv_extension(args.mat1 + prefix)
    file2 = ensure_csv_extension(args.mat2 + prefix)

    A = load_matrix_4_diff_map(file1)
    B = load_matrix_4_diff_map(file2)

    residue_start, residue_end = parse_range(args.resr)

    fig = diff_map(A, B, args.max, residue_start, residue_end)

    prefix1 = "_diff_map_"
    savename = ensure_png_extension(args.out + prefix1)
    fig.savefig(savename, dpi=800, bbox_inches='tight')
    print(f"Difference map saved to {savename}")
    plt.close(fig)
    total = time.perf_counter() - start_time
    print(f"Time taken to plot Difference map: {total:.2f} seconds")