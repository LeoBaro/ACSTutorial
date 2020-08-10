#!/bin/bash


source /alma/ACS-2020JUN/ACSSW/config/.acs/.bash_profile.acs

TUTORIAL_NAME=TUTORIAL_5

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

echo "INTROOT is $INTROOT"
echo "ACS_CDB is $ACS_CDB"
