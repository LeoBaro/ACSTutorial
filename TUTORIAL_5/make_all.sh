#!/bin/bash

TUTORIAL_NAME=TUTORIAL_3

BASE="/home/almamgr/ACSTutorial/$TUTORIAL_NAME/WORKSPACE"

# the order is important!
TO_COMPILE=("idlErrors idlTelescope cppTelescope")

for FOLDER in $TO_COMPILE
    do
        cd "$BASE/$FOLDER/src"
        echo "Compiling $FOLDER..."
        make clean all install
    done

cd "$BASE/.."


echo "
       _
      / )
    .' /
---'  (____
          _)
          __)
         __)
---.______)  Compilation terminated.
"
