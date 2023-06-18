# Salome-MeshIO

GUI interface between the CAD software [Salome](https://salome-platform.org/) and the Python library [MeshIO](https://github.com/nschloe/meshio).


## Features

* Export Salome meshes natively from the SMESH module to any formats handled by MeshIO
* Import meshes from any formats handled by MeshIO in Salome


## Installation

Open Salome application and run in the Python console at bottom:
```
import pip
pip.main(["install", "SALOMExMeshIO"])
```


## Use

To import a mesh from a file into Salome, run `Mesh/SMESH plugins/MeshIO/Import mesh`, select the mesh file and click `Open`.

To export a mesh from Salome to a file, select the mesh under the objet browser, go on `Mesh/SMESH plugins/MeshIO/`, select the right output format and specify the output path.


## Uninstall

Open Salome application and run in the Python console at bottom:
```
import pip
pip.main(["uninstall", "-y", "SALOMExMeshIO"])
```

You will also have to remove the lines automatically added by SALOMExMeshIO in your `smesh_plugins.py` file (located in `$HOME/.config/salome/Plugins`.


## TODO

* Test Windows installation
* Export group
* Create a PyPi release

