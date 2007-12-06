#! /bin/sh

CLIENTS="dt csc rpc l1t hcal"
#MODE="playback"
MODE="live"

for c in $CLIENTS;
do
  echo "starting $c ... "
  ./loop_generic.sh $c $MODE &
done
