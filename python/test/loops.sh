#! /bin/sh


if [ $HOSTNAME == "srv-C2D05-09" ]; then
CLIENTS="hlx ecal hlt l1t l1temulator"
fi
if [ $HOSTNAME == "srv-C2D05-10" ]; then
CLIENTS="hcal csc dt rpc"
fi
if [ $HOSTNAME == "srv-C2D05-11" ]; then
CLIENTS="pixel sistrip"
fi

MODE="playback"
#MODE="live"

for c in $CLIENTS;
do
  echo "starting $c ... "
  ./loop_generic.sh $c $MODE &
done
