#!/bin/bash

TUTORIAL_NAME=TUTORIAL_4

# the order is important!
TO_COMPILE=("idlCustomTypes idlHelloComp cppHelloComp")

source /home/almamgr/ACSTutorial/scripts_util/make_all.sh "$TUTORIAL_NAME" "$TO_COMPILE"