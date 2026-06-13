"""Run hotspot detection and save a summary hotspot-region plot PNG.
"""

import time
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from ..core.hotspot import create_submatrices, detect_shifts, plot_hotspot_regions, plot_shift_regions, plot_slice_regions, slice_shifts
from ..utils.utils import csv2matrix, ensure_csv_extension, ensure_png_extension, parse_range, shift_to_dataframe


def detect_shift_cli(args):
    print("")
    print("Detecting shift regions...")
    prefix = "_pdb2csv_"
    file = ensure_csv_extension(args.out + prefix)
    matrix = csv2matrix(file)
    mean_shift, smooth, regions = detect_shifts(
        matrix=matrix,
        window=args.window,
        mindist=args.mindist,
        hotspot=args.hot,)
    return mean_shift, smooth, regions


def create_submatrices_cli(args):
    print("")
    print("Extracting region submatrices...")
    prefix = "_pdb2csv_"
    file = ensure_csv_extension(args.out + prefix)
    matrix = csv2matrix(file)
    prefix1 = "_matrix_"
    savematrix = ensure_csv_extension(args.out + prefix1)
    matrix.to_csv(savematrix, index=False)

    """Call backend"""
    submatrices, regions, mean_shift, smooth = create_submatrices(
        matrix=matrix,
        window=args.window,
        mindist=args.mindist,
        hotspot=args.hot)
    return submatrices


def slice_shifts_cli(args):
    start_time = time.perf_counter()
    print("")
    print("Searching for hotspot regions and plotting individual shift graphs...")
    prefix = "_pdb2csv_"
    file = ensure_csv_extension(args.out + prefix)
    matrix = csv2matrix(file)

    """Backend: detect"""
    results = slice_shifts(
        matrix=matrix,
        window=args.window,
        mindist=args.mindist,
        hotspot=args.hot)
    
    for start, end, shift_data in results:
        fig = plot_slice_regions(shift_data, start, end)
        savename = f"{args.out}_shift_{start}_{end}.png"
        fig.savefig(savename, dpi=800, bbox_inches='tight')
        plt.close(fig)
        print(f"Hotspot region shift graph saved to {savename}")
    total = time.perf_counter() - start_time
    print(f"Time taken to search for hotspot regions: {total:.2f} seconds")


"""Hotspot region detection and plotting
"""
def run_hotspot_cli(args):
    start_time = time.perf_counter()
    print("")
    print("Detecting hotspot regions based on mean shift and plotting...")
    mean_shift, smooth, regions = detect_shift_cli(args)

    fig = plot_hotspot_regions(
        mean_shift,
        smooth,
        regions,
        title="Residue Shift Hotspots")
    savename = f"{args.out}_shift_hotspots.png"
    fig.savefig(savename, dpi=800, bbox_inches='tight')
    plt.close(fig)
    print(f"Hotspot region plot saved to {savename}")
    total = time.perf_counter() - start_time
    print(f"Time taken to detect hotspot regions: {total:.2f} seconds")
