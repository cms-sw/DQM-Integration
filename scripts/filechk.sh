#!/bin/bash
set -o nounset

exedir='/home/dqmprolocal/filecopy/'
inputFile=$1

root -l -b -q $exedir/filechk.C"(\"$inputFile\")"
exit 0
