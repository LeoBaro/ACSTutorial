#!/bin/bash

function quit() {
    local error_msg=$1
echo "
  / _ \\
\_\(_)/_/
 _//o\\\_
  /   \\

Error: $error_msg  
"
    exit 1
}


if [ $# -eq 0 ]
  then
    echo "No arguments supplied. Terminating.."
    exit 1
fi

TUTORIAL_NAME=$1
TO_COMPILE=$2

echo "TUTORIAL_NAME: $TUTORIAL_NAME"
echo "TO_COMPILE: $TO_COMPILE"


BASE="/home/almamgr/ACSTutorial/$TUTORIAL_NAME/WORKSPACE"

i=0
for FOLDER in $TO_COMPILE
    do
        ((i++)) # first argument does not specify code to compile
        #echo "FOLDER: $FOLDER i: $i"
        if [[ "$i" == '1' ]]; then
            continue
        fi
        FOLDER_PATH="$BASE/$FOLDER/src"
        echo "FOLDER_PATH: $FOLDER_PATH"
        if [ ! -d "$FOLDER_PATH" ]; then
            quit "$FOLDER_PATH does not exist!"
        fi
        cd $FOLDER_PATH
        echo "Compiling $FOLDER..."
        
        if make clean ; then
            echo "make clean succeeded"
        else
            quit "make clean failed"
        fi
        if make all ; then
            echo "make all succeeded"
        else
            quit "make all failed"
        fi
        if make install ; then
            echo "make install succeeded"
        else
            quit "make install failed"
        fi


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
