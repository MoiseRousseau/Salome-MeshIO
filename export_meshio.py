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

import export_processer
import importlib
importlib.reload(export_processer)

def export_abacus(context):
  export_processer.main("inp")
  
def export_ansys(context):
  export_processer.main("msh")

def export_avs_ucd(context):
  export_processer.main("avs")

def export_cgns(context):
  export_processer.main("cgns")

def export_dolfin(context):
  export_processer.main("xml")

def export_exodus(context):
  export_processer.main("exo")

def export_flac3d(context):
  export_processer.main("f3grid")

def export_h5m(context):
  export_processer.main("h5m")

def export_kratos(context):
  export_processer.main("mdpa")

def export_medit_ascii(context):
  export_processer.main("mesh")

def export_medit_binary(context):
  export_processer.main("meshb")

def export_med_salome(context):
  export_processer.main("med")

def export_netgen(context):
  export_processer.main("vol")

def export_obj(context):
  export_processer.main("obj")

def export_off(context):
  export_processer.main("off")

def export_permas(context):
  export_processer.main("post")

def export_ply(context):
  export_processer.main("ply")

def export_tecplot(context):
  export_processer.main("dat")

def export_stl(context):
  export_processer.main("stl")

def export_su2(context):
  export_processer.main("su2")

def export_ugrid(context):
  export_processer.main("ugrid")

def export_vtk(context):
  export_processer.main("vtk")

def export_vtu(context):
  export_processer.main("vtu")

def export_wkt(context):
  export_processer.main("wkt")




