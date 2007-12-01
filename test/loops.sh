#! /bin/sh

CLIENTS="dt sistrip rpc csc l1t hcal ecal"
#MODE="playback"
MODE="live"

for c in $CLIENTS;
do
  echo "starting $c ... "
  ./loop_generic.sh $c $MODE &
done
