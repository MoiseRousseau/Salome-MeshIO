#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.7.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh()
nodeID = Mesh_1.AddNode( 0, 0, 0 ) #1
nodeID = Mesh_1.AddNode( 0, 1, 0 ) #2
nodeID = Mesh_1.AddNode( 1, 1, 0 ) #3
nodeID = Mesh_1.AddNode( 1, 0, 0 ) #4
nodeID = Mesh_1.AddNode( 0, 0, 1 ) #5
nodeID = Mesh_1.AddNode( 0, 1, 1 ) #6
nodeID = Mesh_1.AddNode( 1, 1, 1 ) #7
nodeID = Mesh_1.AddNode( 1, 0, 1 ) #8
nodeID = Mesh_1.AddNode( 2, 0, 0 ) #9
nodeID = Mesh_1.AddNode( 2, 0, 1 ) #10
nodeID = Mesh_1.AddNode( 0.5, 0.5, 2 ) #11
nodeID = Mesh_1.AddNode( 1.5, 0.5, 2 ) #12

Mesh_1.AddVolume([1,2,3,4,5,6,7,8]) #hex
Mesh_1.AddVolume([4,3,9,8,7,10]) #prism
Mesh_1.AddVolume([5,6,7,8,11]) #pyr
Mesh_1.AddVolume([8,7,10,12]) #pyr


## Set names of Mesh objects
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
