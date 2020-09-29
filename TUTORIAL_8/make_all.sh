#!/bin/bash

TUTORIAL_NAME=TUTORIAL_8

# the order is important!
TO_COMPILE=("idlNCModule idlSupplier idlConsumer pySupplier pyConsumer")

source /home/almamgr/ACSTutorial/scripts_util/make_all.sh "$TUTORIAL_NAME" "$TO_COMPILE"