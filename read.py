# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/
#
# Author : Moise Rousseau (2021), email at rousseau.moise@gmail.ca

import meshio
import salome
import SMESH
from salome.smesh import smeshBuilder
from qtsalome import QFileDialog, QMessageBox

import SALOMExMeshIO
from SALOMExMeshIO.common import ext_to_mesh_format


def gui_input_file():
  f_type = ext_to_mesh_format
  dialog = QFileDialog()
  exts = "All File (*);;"
  for ext,des in f_type.items():
    exts += f"{des} (*.{ext});;"
  f_in = dialog.getOpenFileName(None, "Select an input mesh", 
                                 "", exts)
  f_in = f_in[0]
  if not f_in:
    return None
  return f_in


def meshio_read(context):
  
  #read mesh
  src = gui_input_file()
  if src is None:
    return
  print("Read mesh through meshio")
  src_mesh = meshio.read(src)
  #create salome mesh
  smesh = smeshBuilder.New()
  mesh = smesh.Mesh()
  #mesh.SetName(name)
  print("Add vertices")
  for (X,Y,Z) in src_mesh.points:
    mesh.AddNode(float(X),float(Y),float(Z))
  print("Add cells")
  for cell_type, cells in src_mesh.cells:
    if cell_type in ["triangle", "triangle6", "triangle7", "quad", "quad8", "quad9"]:
      for cell in cells:
        mesh.AddFace([int(x)+1 for x in cell])
    elif cell_type in ["tetra", "pyramid", "wedge", "hexahedron",
                       "tetra10", "pyramid13", "wedge15", "hexahedron20",
                       "hexahedron27"]:
      for cell in cells:
        mesh.AddVolume([int(x)+1 for x in cell])
    elif cell_type in ["wedge12", "pyramid14", "hexahedron24"]:
      print("Skip cell {i} with type {cell_type}: cell type doesn't exist in Salome")
    else:
      print(f"Unknown cell type {cell_type}, please open an issue in SALOMExMeshIO repository")
  print("Create groups")
  #if src_mesh.cell_data:
  #  grp = mesh.CreateEmptyGroup(SMESH.VOLUME, "inside")
  #  for i,val in enumerate(src_mesh.cell_data["medit:ref"][0]):
  #    if val == 3: grp.Add([int(i)+1])
  if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser()
  print("End!")
  return
  
  

