""" Compute an element-wise average of input matrices 
and render a trajectory map figure

"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
from ..core.trajmap import trajmap



def avg_trajmap(residue_start, residue_end, vmax, *matrices):
    """
    Take the element-wise average of two or more matrices.
    All matrices must have the same shape.
    """
    
    mats = [np.asarray(m) for m in matrices]
    print("Loaded shapes:", [m.shape for m in mats])

    shapes = {m.shape for m in mats}
    if len(shapes) != 1:
        raise ValueError(f"All matrices must have the same shape, got: {shapes}")
    

    avg_array = np.nanmean(mats, axis=0)
    avg_array = np.nan_to_num(avg_array, nan=0.0)

    matrix = pd.DataFrame(avg_array)


    fig = trajmap(matrix, residue_start, residue_end, vmax)
    return fig
