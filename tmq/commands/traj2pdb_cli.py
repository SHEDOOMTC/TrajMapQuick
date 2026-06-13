"""Load a residue×frame matrix, render a trajectory heatmap, and save the PNG figure.
"""

import time
from ..core.traj2pdb import traj2pdb
from ..utils.utils import ensure_pdb_extension


def traj2pdb_cli(args):
    start_time = time.perf_counter()
    prefix = "_traj2pdb_"
    savename = ensure_pdb_extension(args.out + prefix)
    print("Loading trajectory...")
    traj = traj2pdb(args.top, args.traj, args.str)
    print("Selecting backbone...")
    print("Aligning...")
    print("Saving trajectory to", savename)
    traj.save_pdb(savename)
    end_time = time.perf_counter()
    total = end_time - start_time       
    print(f"Time taken to convert trajectory to PDB: {total:.2f} seconds")
