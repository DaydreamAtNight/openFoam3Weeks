#!/bin/bash

cd c1
sh run_mesh.sh
laplacianFoam | tee log
touch c1.OpenFOAM
cd ..

cd c2
sh run_mesh.sh
laplacianFoam | tee log
touch c2.OpenFOAM
cd ..

cd c3
sh run_mesh.sh
laplacianFoam | tee log
touch c3.OpenFOAM
cd ..