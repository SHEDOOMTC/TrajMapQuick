<p align="center">
  <img src="https://github.com/SHEDOOMTC/TrajMapQuick/blob/main/assets/TrajMapQuick.png" alt="TrajMapQuick Logo" />
</p>

## **Overview**
**TrajMapQuick 1.0** is a light tool useful for visualization of trajectory maps and residual shifts within select regions of proteins, across several frames. It is built partially on the codes provided in the original work of Matej Kožić and Branimir Bertoša, 2024 : [**"Trajectory maps: molecular dynamics visualization and analysis"**](https://doi.org/10.1093/nargab/lqad114). **TrajMapQuick** extends the work by reconfiguring how the pdb files are parsed to generate the distance matrix, thereby improving speed dramatically. In addition, **TrajMapQuick** provides a CLI where the user can pass arguments for better throughput and batch processing. 
We have also extended the code to allow for automatic detection of regions with high residual fluctuations (named **"Hotspots"**) and  generation of the residual shifts of those regions. In addition, a python API has also been provided for python based community. In TrajMapQuick, the user can also choose between the backbone (**backbone**) atoms or the alpha carbon (**CA**) for computing the maps. 

## **Features**
- **Trajectory Map Visualization:** Generates a trajectory map of residual fluctuations across the select frames chosen by the user.
- **Residual shift calculation and visualization:** For a select range of residues (region), residual shifts are computed and visualized across select frames
- **Difference and Average map visualization** This computes the difference and average of two trajectories, respectively and display the resultant trajectory maps.
- **Hotspot Detection and Plotting:** This automatically probes and detects regions of high fluctuations and computes the residual shift for each region for downstream processing.
- **Hotspot Annotation:** An RMSF like plot is also generated with the key hotspots highlight for visual confirmation and inspection.

## **Project Structure**
<pre>
TrajMapQuick/
├── README.md                     # Project overview, installation, usage 
├── requirements.txt              # Python dependencies
├── setup.py                      # Packaging configuration
├── environment.yml               # Build config
├── pyproject.toml                # Build config 
├── LICENSE                       # MIT license
├── Manifest.in                   
├── tmq/                          # Source codes and CLI wrappers lives here
│   ├── cli.py/                   # Main command line launcher 
│   ├── __init__.py               # Main launcher for the python API
│   ├── core/                     # Python package folder
│   │   ├── __init__.py
│   │   ├── traj2pdb.py           # Converts trajectory to pdb
│   │   ├── pdb2csv.py            # Converts pdb to distance matrix
│   │   ├── trajmap.py            # plots the trajectory map
│   │   ├── csv2shift.py          # Core shift logic for a given loop
│   │   ├── shift2graph.py        # Makes shift plots for a given loop
│   │   ├── hotspot.py            # Automatic detection of regions with peak fluctuations
│   │   ├── diff2graph.py         # Computes and plot difference map for two trajectories
│   │   └── average_trajmap.py    # Computes and plot average map for two trajectories
│   ├── commands/                 # Main wrapper for the CLI
│   │   ├── __init__.py
│   │   ├── traj2pdb_cli.py       # CLI wrapper
│   │   ├── pdb2csv_cli.py        # CLI wrapper
│   │   ├── trajmap_cli.py        # CLI wrapper
│   │   ├── csv2shift_cli.py      # CLI wrapper
│   │   ├── shift2graph_cli.py    # CLI wrapper
│   │   ├── hotspot_cli.py        # CLI wrapper
│   │   ├── diff2graph_cli.py     # CLI wrapper
│   │   └── average_trajmap_cli.py# CLI wrapper
│   └── utils                     # Holds functions
│   │   ├── __init__.py
│   │   └── utils.py              # utility functions
├── docs/                         # docstrings for the modules
├── assets/                       # Container for images
├── Tests/                        # Containers for test trajectories and topologies
└── Conda/                        # Backup YAML files


</pre>

## **Installation**
```bash
# Clone the repo
git clone https://github.com/SHEDOOMTC/TrajMapQuick.git
cd TrajMapQuick

# In conda environment with pip
conda create -n tmq python=3.10 
conda activate tmq
conda install -c conda-forge mdtraj
pip install (-e) .

# In conda environment without pip
conda env create -f environment.yml
conda activate tmq

Use tmq --help to see the arguments
```
## **Commands**
```bash
#TrajMapQuick uses a two levell subcommand from the global "tmq" command
tmq  shift  : Extract matrices, compute residue-residue shifts and make plots: For more, use tmq shift --help

tmq hotspot : Detect hotspots in residue shifts and create plots: For more, use tmq hotspot --help

tmq diff      Computes difference between two matrices and creates the difference map: For more, use tmq diff --help

tmq average   Computes average of n matrices and creates the average map: For more, use tmq average --help

```
## **Usage (CLI)**
```bash
# For tmq shift, arguments are passed into the flags for trajectory, topology etc.

tmq shift --traj traj.pdb --top top.parmtop --str 1 --resr 1-300 --resrs 110-125 --cent backbone --plot --out shift_output

#for tmq hotspot, arguments are passed similiarly, except that the region of shift is not provided

tmq hotspot --traj traj.pdb --top top.parmtop --str 1 --resr 1-300 --cent backbone --out hotspot_output
```
## **Usage (Python API)**
The core modules in the tmq library are clearly demonstrated in the **[Python_API.ipynb](./Notebooks/Python_API.ipynb)** file

```python
#Typical modules are loaded and then used as explained in the jupyter notebook above:

from tmq.core.traj2pdb import traj2pdb
from tmq.core.pdb2csv import pdb2csv  
from tmq.core.trajmap import trajmap
from tmq.core.csv2shift import shift
from tmq.core.shift2graph import shift2graph
from tmq.core.hotspot import detect_shifts
from tmq.core.hotspot import create_submatrices
from tmq.core.hotspot import plot_hotspot_regions
from tmq.core.hotspot import slice_shifts
from tmq.core.hotspot import plot_slice_regions
from tmq.core.diff2graph import diff_map
from tmq.core.average_trajmap import avg_trajmap
```

```python
# To run the notebook
cd ./Notebooks/
jupyter notebook Python_API.ipynb
```

## **Requirements**
- Trajectory processing libraries (mdtraj, biopython)

- Data wrangling tools (numpy, pandas)

- Trajectories must have been preprocessed (strippin water, ions,) before feeding into TrajMapQuick


All library requirements are pre-installed installed via pip or conda and are available for use in CLI or via Python API

## **Examples**
Three trajectories and topologies files are included in the **[Test](./Test)** directory for users to try out the codes. Trajectory 1 has only 125 frames (from apo strucuture of PDB ID: 8EM8 with 789 residues) while others have 250 frames (from apo and bound strucutres of BACE1, with 389 residues). To get the full sized trajectories, see zenodo doi ....


The Utility of the shift command (using a 500 frame trajectory) was shown by the figure below:

![test_traj_2_shift_graph.png](https://github.com/SHEDOOMTC/TrajMapQuick/blob/main/assets/test_traj_2_shift_graph.png)


**And that of the hotspot command by:**


![test_traj_2_hotspot_graph.png](https://github.com/SHEDOOMTC/TrajMapQuick/blob/main/assets/test_traj_2_hotspot_graph.png)


To reproduce the figures above, download the full length trajectory (500 frames) from Zenodo doi .... and run the codes below on the CLI

```bash
#The exact codes used to produce the results above
tmq shift -tr traj_9NSR_500.nc -to topol_9NSR.prmtop -st 1 -rr 1-378 -rs 272-285 -ce backbone -ma 5 -o out

tmq hotspot -tr traj_9NSR_500.nc -to topol_9NSR.prmtop -st 1 -rr 1-378 -ce backbone -o out
```
 

## **Improvements (Speed, Throughput and Reliability)**
**1.** Batch processing over the CLI and Python API

**2.** A major improvement of TrajMapQuick over TrajMap is the speed across varying **residue lengths** and **number of frames**. We evaluated a 1000 frame trajectory (at 100 frame interval) over 800 residues (at 100 residue interval) in TrajMapQuick for both subcommands (shift & hotspot). The **performance plots below:** 

![performance plots](https://github.com/SHEDOOMTC/TrajMapQuick/blob/main/assets/Performance_shift_hotspot.png?raw=true) 

shows clear scaling with number of residues and frames, with completion time between **2-5 mins**. Compared to TrajMapQuick, a single 500 frame calculations across 800 residues took around **10 minutes** in TrajMap, besides the manual editing of input parameters.

**3.** The choice to select either the CA or backbone for shift calculations.

**4.** Automatic Detection of hotspots using RMSF plots and generation of associated shift plots.

**4.** TrajMapQuick allows you to work on any continous chunk of your protein, say residues 300-360 of a 500-residues protein. This reduces time and allows one to focus.

## **Contributing**
Contributions are welcome. Please submit a pull request with your changes.

## **License**
[**MIT License**](../License.md)

## **Contact**

Cite this as **Oluyemi et al 2026, "TrajMapQuick: Towards Fast Trajectory Map Analysis and Visualization" https://github.com/SHEDOOMTC/TrajMapQuick.git**

For questions or issues, please contact us @ [Reslar Labs](reslarscience@gmail.com)  **&copy; 2026**, or [Dr. Oluyemi](oluyemiwm@abuad.edu.ng) or [Shadrach Eze](shadrachchinecheremeze@gmail.com).
