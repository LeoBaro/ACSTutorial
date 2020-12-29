#!/bin/bash

TUTORIAL_NAME=TUTORIAL_4

# the order is important!
TO_COMPILE=("idlCustomTypes idlHelloComp cppHelloComp")

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

source $DIR/../scripts_util/make_all.sh "$TUTORIAL_NAME" "$TO_COMPILE"