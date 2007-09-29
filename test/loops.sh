#! /bin/sh

CLIENTS="csc l1t dt hcal ecal"
MODE="playback"
#MODE="live"

for c in $CLIENTS;
do
  echo "starting $c ... "
  ./loop_generic.sh $c &
done
