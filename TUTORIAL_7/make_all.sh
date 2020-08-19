#!/bin/bash

TUTORIAL_NAME=TUTORIAL_7

# the order is important!
TO_COMPILE=("idlHelloComp idlDefaultComp pyHelloComp pyDefaultComp")

source /home/almamgr/ACSTutorial/scripts_util/make_all.sh "$TUTORIAL_NAME" "$TO_COMPILE"