"""Load a shift CSV, plot the time-series with rolling-average, and save a PNG graph.
"""

import time
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from ..core.shift2graph import shift2graph
from ..utils.utils import ensure_csv_extension, ensure_png_extension, shift_to_dataframe


def shift2graph_cli(args):
    start_time = time.perf_counter()
    print("")
    print("Plotting shift graph...")
    prefix = "_shift_"
    file = ensure_csv_extension(args.out + prefix)
    prefix1 = "_shift_graph_"
    savename = ensure_png_extension(args.out + prefix1)
    df = shift_to_dataframe(file)

    fig = shift2graph(df, args.resrs)

    fig.savefig(savename, dpi=800, bbox_inches='tight')
    print(f"Shift graph saved to {savename}")
    plt.close(fig)
    total = time.perf_counter() - start_time
    print(f"Time taken to plot shift graph: {total:.2f} seconds")

