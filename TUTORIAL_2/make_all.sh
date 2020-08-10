#!/bin/bash

TUTORIAL_NAME=TUTORIAL_2

BASE="/home/almamgr/ACSTutorial/$TUTORIAL_NAME/WORKSPACE"

# the order is important!
TO_COMPILE=("idlTelescope cppTelescope pyTelescope idlConsole cppConsole pyConsole")

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
