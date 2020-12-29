#!/bin/bash

TUTORIAL_NAME=TUTORIAL_8

# the order is important!
TO_COMPILE=("idlNCModule idlSupplier idlConsumer pySupplier pyConsumer")

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

source $DIR/../scripts_util/make_all.sh "$TUTORIAL_NAME" "$TO_COMPILE"