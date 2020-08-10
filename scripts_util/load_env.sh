#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "No arguments supplied. Terminating.."
    exit 1
fi

TUTORIAL_NAME=$1

source /alma/ACS-2020JUN/ACSSW/config/.acs/.bash_profile.acs

INTROOT="/home/almamgr/INTROOT_$TUTORIAL_NAME"

if [ ! -d $INTROOT ]; then
   mkdir $INTROOT
fi

if [ -z "$(ls -A $INTROOT)" ]; then
   getTemplateForDirectory INTROOT $INTROOT
fi

export INTROOT="$INTROOT"
source /alma/ACS-2020JUN/ACSSW/config/.acs/.bash_profile.acs
export ACS_CDB="~/ACSTutorial/$TUTORIAL_NAME/WORKSPACE"

echo "
           ___
     |     | |
    / \    | |
   |--o|===|-|
   |---|   | |   Environment loaded:
  /     \  | |       INTROOT is $INTROOT
 | A     | | |       ACS_CDB is $ACS_CDB
 | C     |=| |
 | S     | | |
 |_______| |_|
  |@| |@|  | |
___________|_|_
"

