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

from SALOMExMeshIO import read
from SALOMExMeshIO import export

def add_functions_to_salome(salome_pluginsmanager):
  #read function
  salome_pluginsmanager.AddFunction('MeshIO/Import mesh', 'Import a mesh through MeshIO',
                                    read.meshio_read)
                                    
  #export function
  common = "MeshIO/Export to "
  salome_pluginsmanager.AddFunction(common+'Abaqus', 'Export mesh to Abacus format',
                                    lambda context: export.meshio_export(context, "inp"))
  salome_pluginsmanager.AddFunction(common+'ANSYS msh', 'Export mesh to ANSYS format',
                                    lambda context: export.meshio_export(context, "msh"))
  salome_pluginsmanager.AddFunction(common+'LaGrit AVS-UCD', 'Export mesh to LaGrit AVS-UCD format',
                                    lambda context: export.meshio_export(context, "avs"))
  salome_pluginsmanager.AddFunction(common+'CGNS', 'Export mesh to the CFD General Notation System format',
                                    lambda context: export.meshio_export(context, "cgns"))
  salome_pluginsmanager.AddFunction(common+'DOLPHIN XML', 'Export mesh to Dolphin format',
                                    lambda context: export.meshio_export(context, "xml"))
  salome_pluginsmanager.AddFunction(common+'Exodus', 'Export mesh to Exodus format',
                                    lambda context: export.meshio_export(context, "exo"))
  salome_pluginsmanager.AddFunction(common+'FLAC3D', 'Export mesh for FLAC3D',
                                    lambda context: export.meshio_export(context, "f3grid"))
  salome_pluginsmanager.AddFunction(common+'H5M', 'Export mesh to H5M format',
                                    lambda context: export.meshio_export(context, "h5m"))
  salome_pluginsmanager.AddFunction(common+'Kratos-MDPA', 'Export mesh to Kratos format',
                                    lambda context: export.meshio_export(context, "mdpa"))
  salome_pluginsmanager.AddFunction(common+'Medit', 'Export mesh to Medit format',
                                    lambda context: export.meshio_export(context, "mesh"))
  salome_pluginsmanager.AddFunction(common+'Medit (binary)', 'Export mesh to Medit binary format',
                                    lambda context: export.meshio_export(context, "meshb"))
  salome_pluginsmanager.AddFunction(common+'Salome MED', 'Export mesh to Salome MED format',
                                    lambda context: export.meshio_export(context, "med"))
  salome_pluginsmanager.AddFunction(common+'NETGEN', 'Export mesh to NETGEN format',
                                    lambda context: export.meshio_export(context, "vol"))
  salome_pluginsmanager.AddFunction(common+'NETGEN (compressed)', 'Export mesh to NETGEN format with gunzip compression',
                                    lambda context: export.meshio_export(context, "vol.gz"))
  salome_pluginsmanager.AddFunction(common+'Gmsh, Neuroglancer', 'Export mesh to Gmsh and Neuroglancer precomputed format',
                                    lambda context: export.meshio_export(context, "msh"))
  salome_pluginsmanager.AddFunction(common+'OBJ', 'Export mesh to Wavefront OBJ format',
                                    lambda context: export.meshio_export(context, "obj"))
  salome_pluginsmanager.AddFunction(common+'OFF', 'Export mesh to Object File Format format',
                                    lambda context: export.meshio_export(context, "off"))
  salome_pluginsmanager.AddFunction(common+'PERMAS', 'Export mesh to PERMAS format',
                                    lambda context: export.meshio_export(context, "post"))
  salome_pluginsmanager.AddFunction(common+'PERMAS (compressed)', 'Export mesh to PERMAS with gunzip compression',
                                    lambda context: export.meshio_export(context, "post.gz"))
  salome_pluginsmanager.AddFunction(common+'PLY', 'Export mesh to Polygon File Format format',
                                    lambda context: export.meshio_export(context, "ply"))
  salome_pluginsmanager.AddFunction(common+'STL', 'Export mesh to Standford Triangle format',
                                    lambda context: export.meshio_export(context, "stl"))
  salome_pluginsmanager.AddFunction(common+'Tecplot DAT', 'Export mesh to Tecplot format',
                                    lambda context: export.meshio_export(context, "dat"))
  salome_pluginsmanager.AddFunction(common+'TetGen', 'Export mesh to TetGen format',
                                    lambda context: export.meshio_export(context, "ele"))
  salome_pluginsmanager.AddFunction(common+'SU2', 'Export mesh to SU2 format',
                                    lambda context: export.meshio_export(context, "su2"))
  salome_pluginsmanager.AddFunction(common+'VTK', 'Export mesh to legacy Visualization Toolkit format',
                                    lambda context: export.meshio_export(context, "vtk"))
  salome_pluginsmanager.AddFunction(common+'VTU', 'Export mesh to Visualization Toolkit format',
                                    lambda context: export.meshio_export(context, "vtu"))
  salome_pluginsmanager.AddFunction(common+'WKT', 'Export mesh to Well-known text  format',
                                    lambda context: export.meshio_export(context, "wkt"))
  salome_pluginsmanager.AddFunction(common+'XDMF', 'Export mesh to XDMF format',
                                    lambda context: export.meshio_export(context, "xdmf"))

