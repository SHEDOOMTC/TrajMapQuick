""" This module loops over the Multi-model pdb and 
compute residual fluctuations across the frames

"""

import pandas as pd
import numpy as np
from ..utils.utils import (load_pdb_models, build_residue_lookup, get_ca_coord, get_backbone_com, distance)


def pdb2csv(pdb_file, residue_start, residue_end, mode):
    weights = {"N": 14.0, "CA": 12.0, "C": 12.0, "O": 16.0}
    residue_numbers = list(range(residue_start, residue_end + 1))

    models = load_pdb_models(pdb_file)
    n_frames = len(models)

    ref_lookup = build_residue_lookup(models[0])

    ref_coords = {}
    for resnum in residue_numbers:
        if resnum in ref_lookup:
            residue = ref_lookup[resnum]
            if mode == "ca":
                ref_coords[resnum] = get_ca_coord(residue)
            else:
                ref_coords[resnum] = get_backbone_com(residue, weights)
        else:
            ref_coords[resnum] = np.zeros(3)

    matrix = pd.DataFrame(0.0, index=residue_numbers, columns=range(n_frames))

    """ Compute distances for frames 1..N-1
    """

    for t in range(1, n_frames):
        lookup = build_residue_lookup(models[t])

        for resnum in residue_numbers:
            ref = ref_coords[resnum]

            if resnum in lookup:
                residue = lookup[resnum]
                if mode == "ca":
                    cur = get_ca_coord(residue)
                else:
                    cur = get_backbone_com(residue, weights)
            else:
                cur = np.zeros(3)

            matrix.loc[resnum, t] = distance(cur, ref)

    return matrix
