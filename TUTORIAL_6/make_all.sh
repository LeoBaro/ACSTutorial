#!/bin/bash

TUTORIAL_NAME=TUTORIAL_1

# the order is important!
TO_COMPILE=("idlGenericComponent")

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

source $DIR/../scripts_util/make_all.sh "$TUTORIAL_NAME" "$TO_COMPILE"