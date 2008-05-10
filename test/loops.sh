#! /bin/sh

CLIENTS="l1temulator"
#CLIENTS="hcal"
#MODE="playback"
MODE="live"

for c in $CLIENTS;
do
  echo "starting $c ... "
  ./loop_generic.sh $c $MODE &
done
