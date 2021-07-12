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

import read_meshio
import export_meshio
import importlib
importlib.reload(export_meshio)

def add_function_to_salome(salome_pluginsmanager):
  #read function
  salome_pluginsmanager.AddFunction('MeshIO/Import mesh', 'Import a mesh through MeshIO',
                                    read_meshio.meshio_read)
                                    
  #export function
  common = "MeshIO/Export to "
  salome_pluginsmanager.AddFunction(common+'Abaqus', 'Export mesh to Abacus format',
                                    export_meshio.export_abacus)
  salome_pluginsmanager.AddFunction(common+'LaGrit AVS-UCD', 'Export mesh to LaGrit AVS-UCD format',
                                    export_meshio.export_avs_ucd)
  salome_pluginsmanager.AddFunction(common+'Medit', 'Export mesh to Medit format',
                                    export_meshio.export_medit_ascii)
  salome_pluginsmanager.AddFunction(common+'Medit (binary)', 'Export mesh to Medit binary format',
                                    export_meshio.export_medit_binary)
  salome_pluginsmanager.AddFunction(common+'FLAC3D', 'Export mesh for FLAC3D',
                                    export_meshio.export_flac3d)
  salome_pluginsmanager.AddFunction(common+'Salome MED', 'Export mesh for FLAC3D',
                                    export_meshio.export_med_salome)

