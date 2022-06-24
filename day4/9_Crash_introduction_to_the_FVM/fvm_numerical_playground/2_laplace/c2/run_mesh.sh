#!/bin/bash

foamCleanTutorials
foamCleanPolyMesh 
fluentMeshToFoam geo_mesh/ascii.cas
autoPatch 45 -overwrite -noFunctionObjects
createPatch -overwrite
cp system/boundary constant/polyMesh/
extrudeMesh
transformPoints -translate '(0 0 -0.014142136)'