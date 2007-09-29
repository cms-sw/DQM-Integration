#!/bin/bash

cd $HOME/CMSSW_1_6_0_DAQ3/src/DQM/Integration/test
eval `scramv1 runtime -sh`


while ( true ) ; 
  do 
  date 
  echo "---------------------> Starting CMSRUN " 
  #(set -x; cmsRun  l1t_dqm_sourceclient-live.cfg; sleep 10 )
  (set -x; cmsRun  l1t_dqm_sourceclient-playback.cfg; sleep 10 )
done




