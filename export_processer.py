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

import numpy as np

import salome
import SMESH
from salome.smesh import smeshBuilder
from qtsalome import QFileDialog, QMessageBox

import meshio

      

def gui_output_file(out_format):
  f_type = {"inp":"Abaqus meshes", "avs":"LaGrit AVS-UCD meshes", "mesh":"Medit meshes", 
             "meshb":"Medit binary meshes", "f3grid":"FLAC3D meshes", "ply":"Polygon File Format meshes",
            "stl":"Stereolithography CAD files"}
  dialog = QFileDialog()
  f_out = dialog.getSaveFileName(None, "Select an output filename", 
                                 "", 
                                 f"{f_type[out_format]} (*.{out_format})")
  f_out = f_out[0]
  if out_format not in f_out:
    f_out += '.'+out_format
  return f_out

def get_input_mesh():
  objId = salome.sg.getSelected(0)
  if objId is None:
    print("No mesh selected")
    info = QMessageBox()
    info.setText("No mesh selected!")
    info.setIcon(QMessageBox.Warning)
    info.setStandardButtons(QMessageBox.Ok)
    info.setWindowTitle("Salome-MeshIO")
    info.exec_()
    return None
  selectedMesh = salome.IDToObject(objId)
  mesh = selectedMesh.GetMesh()
  return mesh
  
def get_mesh_vertices(mesh):
  #TODO: this suppose vertices are numeroted consecutively
  n_nodes = mesh.NbNodes()
  vertexArray = np.zeros((n_nodes, 3), dtype='f8')
  for i in range(n_nodes):
    X,Y,Z = mesh.GetNodeXYZ(i+1)
    vertexArray[i,:] = [X,Y,Z]
  return vertexArray
 

def get_mesh_cells(mesh):
  cells = {}
  if mesh.NbVolumes() == 0:
    elems = mesh.GetElementsByType(SMESH.FACE)
    tri = []
    tri6 = []
    tri7 = []
    quad = []
    quad8 = []
    quad9 = []
    for elem in elems:
      elem_type = mesh.GetElementGeomType(elem)
      nodes = mesh.GetElemNodes(elem)
      if elem_type == SMESH.Entity_Triangle:
        tri.append([x-1 for x in nodes])
      elif elem_type == SMESH.Entity_Quad_Triangle:
        tri6.append([x-1 for x in nodes])
      elif elem_type == SMESH.Entity_BiQuad_Triangle:
        tri7.append([x-1 for x in nodes])
      elif elem_type == SMESH.Entity_Quadrangle:
        quad.append([x-1 for x in nodes])
      elif elem_type == SMESH.Entity_Quad_Triangle:
        quad8.append([x-1 for x in nodes])
      elif elem_type == SMESH.Entity_BiQuad_Triangle:
        quad9.append([x-1 for x in nodes])
    if tri: cells["triangle"] = tri
    if tri6: cells["triangle6"] = tri6
    if tri7: cells["triangle7"] = tri7
    if quad: cells["quad"] = quad
    if quad8: cells["quad8"] = quad8
    if quad9: cells["quad9"] = quad9
  else:
    elems = mesh.GetElementsByType(SMESH.VOLUME)
    salome_to_meshio_order = {
      "tetra" : [1,0,2,3],
      "tetra10" : [1,0,2,3,4,6,5,8,7,9],
      "hexa":[1,0,3,2,5,4,7,6],
      "hexa20":[1,0,3,2,5,4,7,6,8,11,10,9,12,15,14,13,17,16,19,18],
      "hexa27":[1,0,3,2,5,4,7,6,8,11,10,9,12,15,14,13,17,16,19,18,22,24,21,23,20,25,26],
      "wedge":[],
      "wedge12":[],
      "wedge15":[],
      "pyr":[1,0,3,2,4],
      "pyr13":[1,0,3,2,4,5,8,7,6,10,9,12,11],
    }
    tetra = []
    tetra10 = []
    hexa = []
    hexa20 = []
    hexa27 = []
    pyr = []
    pyr13 = []
    for elem in elems:
      elem_type = mesh.GetElementGeomType(elem)
      nodes = mesh.GetElemNodes(elem)
      if elem_type == SMESH.Entity_Tetra:
        ordered_nodes = [nodes[i]-1 for i in salome_to_meshio_order["tetra"]]
        tetra.append(ordered_nodes)
      elif elem_type == SMESH.Entity_Quad_Tetra:
        ordered_nodes = [nodes[i]-1 for i in salome_to_meshio_order["tetra10"]]
        tetra10.append(ordered_nodes)
      elif elem_type == SMESH.Entity_Hexa:
        ordered_nodes = [nodes[i]-1 for i in salome_to_meshio_order["hexa"]]
        hexa.append(ordered_nodes)
      elif elem_type == SMESH.Entity_Quad_Hexa:
        ordered_nodes = [nodes[i]-1 for i in salome_to_meshio_order["hexa20"]]
        hexa20.append(ordered_nodes)
      elif elem_type == SMESH.Entity_BiQuad_Hexa:
        ordered_nodes = [nodes[i]-1 for i in salome_to_meshio_order["hexa27"]]
        hexa27.append(ordered_nodes)
      elif elem_type == SMESH.Entity_Pyramid:
        ordered_nodes = [nodes[i]-1 for i in salome_to_meshio_order["pyr"]]
        pyr.append(ordered_nodes)
      elif elem_type == SMESH.Entity_Quad_Pyramid:
        ordered_nodes = [nodes[i]-1 for i in salome_to_meshio_order["pyr13"]]
        pyr13.append(ordered_nodes)
      else:
        print("TODO")
      #elif elem_type == SMESH.Entity_Penta:
      #  prisms.append([x-1 for x in nodes])
      if tetra: cells["tetra"] = tetra
      if tetra10: cells["tetra10"] = tetra10
      if hexa: cells["hexahedron"] = hexa
      if hexa20: cells["hexahedron20"] = hexa20
      if hexa27: cells["hexahedron27"] = hexa27
      if pyr: cells["pyramid"] = pyr
      if pyr13: cells["pyramid13"] = pyr13
  return cells

def create_cell_point_data_from_groups(mesh, grp_type):
  cell_group = []
  mesh_elems = mesh.GetElementsByType(grp_type)
  grps = mesh.GetGroups(grp_type)
  for grp in grps:
    data = np.zeros(len(mesh_elems),dtype='i8')
    
  return cell_groups
  
  

def main(out_format):
  src = get_input_mesh()
  if src is None: return
  #get output file
  out = gui_output_file(out_format)
  #create meshio Mesh instance
  vertices = get_mesh_vertices(src)
  cells = get_mesh_cells(src)
  mesh = meshio.Mesh(vertices, cells)
  #write output
  mesh.write(out)
  print("Mesh successfully exported in " + out)
  return
  


