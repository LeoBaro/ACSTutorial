#!/bin/bash

TUTORIAL_NAME=TUTORIAL_1

# the order is important!
TO_COMPILE=("idlHelloComp cppHelloComp pyHelloComp")

source /home/almamgr/ACSTutorial/scripts_util/make_all.sh "$TUTORIAL_NAME" "$TO_COMPILE"