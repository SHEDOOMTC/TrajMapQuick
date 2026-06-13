""" This computes shift in Armstrongs for 
a given loop region of the protein

"""

import numpy as np
import pandas as pd
from ..utils.utils import matrix2shift


def shift(matrix, residue_start, residue_end):
    n_frames = matrix.shape[1]
    start_frame = 0
    end_frame = n_frames - 1
    params = [residue_start, residue_end, start_frame, end_frame]
    shift = matrix2shift(matrix, params)
    return shift