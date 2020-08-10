#!/bin/bash

TUTORIAL_NAME=TUTORIAL_3

# the order is important!
TO_COMPILE=("idlTelescope idlConsole idlSimDatabase cppTelescope cppConsole")

source /home/almamgr/ACSTutorial/scripts_util/make_all.sh "$TUTORIAL_NAME" "$TO_COMPILE"