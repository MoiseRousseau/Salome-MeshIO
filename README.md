# Salome-MeshIO

GUI interface between the CAD software [Salome](https://salome-platform.org/) and the Python library [MeshIO](https://github.com/nschloe/meshio).


## Features

* Export Salome meshes natively from the SMESH module to any formats handled by MeshIO
* Import meshes from any formats handled by MeshIO in Salome


## Installation

1. Open a terminal in the folder `$HOME/.config/salome/Plugins/` and clone this repository under the folder `SALOMExMeshIO`:
```
sudo apt install git
git clone https://github.com/MoiseRousseau/Salome-MeshIO.git SALOMExMeshIO
```

2. Open `smesh_plugin.py` and add it at the end the two following lines:
```
import SALOMExMeshIO
SALOMExMeshIO.init(salome_pluginsmanager)
```

3. Open a terminal into the Salome installation directory to set the Salome context and install the library `MeshIO`:
```
./salome context
pip install meshio
```

The plugin is installed.



## Use

To import a mesh from a file into Salome, run `Mesh/SMESH plugins/MeshIO/Import mesh`, select the mesh file and click `Open`.

To export a mesh from Salome to a file, select the mesh under the objet browser, go on `Mesh/SMESH plugins/MeshIO/`, select the right output format and specify the output path.



## Notes

For instance, only the meshes are exported, not the groups. 
This is because the MeshIO version installed in Salome is 4.4.6, while the latest version on which the MeshIO `cell_sets` mesh attribute is only defined from version 5.0. 
MeshIO 5.0 requires Python 3.7, while Salome is 3.6.5.
Exporting groups will be implemented in the near futur with the new version of Salome.

This plugin was also only lightly tested. If you got any problem with it, please open an issue or discuss in the discussion section.

I have also other Salome related projects, please see my other repositories.

Don't forget to star this project!

