"""Convert a multi-model PDB (produced from trajectories) into a residue×frame distance CSV.
"""

import time
from ..utils.utils import parse_range, ensure_csv_extension
from ..core.pdb2csv import pdb2csv 


def pdb2csv_cli(args):
    start_time = time.perf_counter()
    prefix = "_pdb2csv_"
    prefix2 = "_traj2pdb_"
    savename = ensure_csv_extension(args.out + prefix)
    pdb_file = args.out + prefix2 + ".pdb"
    start, end = parse_range(args.resr)
    mode = args.cent
    print("")
    print("Converting PDB to CSV distance matrix...")

    matrix= pdb2csv(
        pdb_file=pdb_file,
        residue_start=start,
        residue_end=end,
        mode=mode)

    matrix.to_csv(savename)
    print(f"Distance matrix saved to {savename}")
    total = time.perf_counter() - start_time
    print(f"Time taken to convert PDB to CSV: {total:.2f} seconds")
