#!/bin/bash

cd $HOME/$CMSSW_VERSION/src/DQM/Integration/test
eval `scramv1 runtime -sh`


while ( true ) ; 
  do 
  echo "---------------------> Starting CMSRUN " 
  (set -x; cmsRun  ecal_dqm_sourceclient-live.cfg; sleep 10 )
done




