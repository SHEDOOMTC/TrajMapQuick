<p align="center">
  <img src="https://raw.githubusercontent.com/SHEDOOMTC/TrajMapQuick/main/assets/TrajMapQuick.png" alt="TrajMapQuick Logo" />
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

## **Installation**

### **From Source**
```bash
# Clone the repo
git clone https://github.com/SHEDOOMTC/TrajMapQuick.git && cd TrajMapQuick

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

### **From PyPI**
```bash
pip install tmquick
conda install -c conda-forge mdtraj
```


## **Usage**

**See [Github](https://github.com/SHEDOOMTC/TrajMapQuick/blob/main/README.md)**


## **License**
[**MIT License**](../License.md)

## **Contact**

For questions or issues, please contact us @ [Reslar Labs](reslarscience@gmail.com)  **&copy; 2026**, or [Dr. Oluyemi](oluyemiwm@abuad.edu.ng) or [Shadrach Eze](shadrachchinecheremeze@gmail.com).


## **Citation**

If you use TrajMapQuick, please cite: SHEDOOMTC. (2026). TrajMapQuick: Towards Fast Trajectory Map Analysis and Visualization (v1.0). Zenodo. https://doi.org/10.5281/zenodo.20681061

**Software:**  
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20681061-3C5A99?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.20681061)


**Dataset:**  
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20681326-3C5A99?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.20681326)




