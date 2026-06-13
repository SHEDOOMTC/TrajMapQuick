"""Load a distance matrix, compute residue-range shifts across frames, and write a shift CSV.
"""

import time
from ..core.csv2shift import shift
from ..utils.utils import csv2matrix, ensure_csv_extension, parse_range


def shift_cli(args):
    start_time = time.perf_counter()
    print("")
    prefix = "_pdb2csv_"
    file = ensure_csv_extension(args.out + prefix)
    matrix = csv2matrix(file)
    residue_start, residue_end = parse_range(args.resrs)
    n_frames = matrix.shape[1]
    print(f"Calculating shift for residues {residue_start} to {residue_end} "
          f"across frames 0 to {n_frames - 1}...")

    shifta = shift(matrix, residue_start, residue_end)

    prefix2 = "_shift_"
    savename = ensure_csv_extension(args.out + prefix2)
    shifta.to_csv(savename, index=False)
    print(f"Shift saved to {savename}")
    total = time.perf_counter() - start_time
    print(f"Time taken to calculate shift: {total:.2f} seconds")