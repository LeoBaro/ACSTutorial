#!/bin/bash


source /alma/ACS-2020JUN/ACSSW/config/.acs/.bash_profile.acs

TUTORIAL_NAME=TUTORIAL_1

if [ ! -d ./INTROOT ]; then
   mkdir /home/almamgr/ACSTutorial/"$TUTORIAL_NAME"/INTROOT
fi

if [ -z "$(ls -A ./INTROOT)" ]; then
   getTemplateForDirectory INTROOT /home/almamgr/ACSTutorial/"$TUTORIAL_NAME"/INTROOT
fi

export INTROOT="~/ACSTutorial/$TUTORIAL_NAME/INTROOT"
source /alma/ACS-2020JUN/ACSSW/config/.acs/.bash_profile.acs
export ACS_CDB="~/ACSTutorial/$TUTORIAL_NAME/WORKSPACE"

echo "INTROOT is $INTROOT"
echo "ACS_CDB is $ACS_CDB"
