#!/bin/bash

TUTORIAL_NAME=TUTORIAL_3

# the order is important!
TO_COMPILE=("idlTelescope idlConsole idlSimDatabase cppTelescope cppConsole")

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

source $DIR/../scripts_util/make_all.sh "$TUTORIAL_NAME" "$TO_COMPILE"