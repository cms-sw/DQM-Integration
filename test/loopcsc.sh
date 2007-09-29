#!/bin/bash

cd $HOME/CMSSW_1_6_0_DAQ3/src/DQM/Integration/test
eval `scramv1 runtime -sh`


while ( true ) ; 
  do 
  echo "---------------------> Starting CMSRUN " 
  (set -x; cmsRun  csc_dqm_sourceclient-live.cfg; sleep 10 )
done



