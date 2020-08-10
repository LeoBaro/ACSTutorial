#!/bin/bash

TUTORIAL_NAME=TUTORIAL_5

# the order is important!
TO_COMPILE=("idlErrors idlTelescope idlConsole cppTelescope cppConsole")

source /home/almamgr/ACSTutorial/scripts_util/make_all.sh "$TUTORIAL_NAME" "$TO_COMPILE"