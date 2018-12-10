#!/bin/bash
cd ${0%/*} || exit 1                        # Run from this directory
. $WM_PROJECT_DIR/bin/tools/RunFunctions    # Tutorial run functions

cp -r $FOAM_TUTORIALS/incompressible/pimpleFoam/RAS/TJunction ./
cd TJunction/
foamRunTutorials

mv system/controlDict system/controlDict.old
cp ../src/controlDict system/

runApplication postProcess -fields '(p U)'
cp ../src/move.py ./

paraview --state=nomove.py
