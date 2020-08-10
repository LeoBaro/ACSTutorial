#!/bin/bash

TUTORIAL_NAME=TUTORIAL_2

# the order is important!
TO_COMPILE=("idlTelescope cppTelescope pyTelescope idlConsole cppConsole pyConsole")

source /home/almamgr/ACSTutorial/scripts_util/make_all.sh "$TUTORIAL_NAME" "$TO_COMPILE"