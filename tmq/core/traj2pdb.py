""" This is the engine for the conversion of trajectory files into multi-model PDB

"""

from ..utils.utils import (load_traj, select_backbone, align_to_first_frame)


def traj2pdb(topology, trajectory, stride):
    traj = load_traj(topology, trajectory, stride)
    traj = select_backbone(traj)
    traj = align_to_first_frame(traj)
    return traj