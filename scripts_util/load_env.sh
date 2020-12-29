#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "No arguments supplied. Terminating.."
    exit 1
fi

if [ ! -d $ACSROOT ]; then
   printf "\n\$ACSROOT is not defined!"

   else

      source $ACSROOT/config/.acs/.bash_profile.acs

      TUTORIAL_NAME=$1

      INTROOT="/home/almamgr/INTROOT_$TUTORIAL_NAME"

      if [ ! -d $INTROOT ]; then
         mkdir $INTROOT
      fi

      if [ -z "$(ls -A $INTROOT)" ]; then
         getTemplateForDirectory INTROOT $INTROOT
      fi

      export INTROOT="$INTROOT"
      source $ACSROOT/config/.acs/.bash_profile.acs

      DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

      export ACS_CDB="$DIR/../$TUTORIAL_NAME/WORKSPACE"

      echo "
           ___
     |     | |
    / \    | |
   |--o|===|-|
   |---|   | |   Environment loaded:
  /     \  | |           ACS is $ACSROOT
 | A     | | |       INTROOT is $INTROOT
 | C     |=| |       ACS_CDB is $ACS_CDB
 | S     | | |
 |_______| |_|
  |@| |@|  | |
___________|_|_
"



fi

