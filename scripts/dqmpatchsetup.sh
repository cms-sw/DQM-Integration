#!/bin/bash

echo 
echo Please use DQMPATCH:02, i.e. type dqmpatchsetup.sh [-a] 2
echo 

if [ "$#" -lt 1 ] ; then  echo "  Usage $0 [-a ] dqmpatch" ;  exit  ; fi

while getopts a: opt
do
  case "$opt" in
     a) all="true" ; echo "  option a: will check out/update subsystem tags" ;  shift ;;
     h) echo "Option \"h\"" ; shift ;;
     *) all="false" ; break;;
  esac
done

dqmpatch=$1
echo "  dqmpatchversion: $dqmpatch"

if [ -z "$LOCALRT" ]; then echo "  First setup your scramv1 area for CMSSW_1_7_1 - exiting " ; exit ; fi
if [ $CMSSW_VERSION != CMSSW_1_7_1 ] ; then echo "  First setup your area for CMSSW_1_7_1 - exiting " ; exit ; fi
if [ $dqmpatch != "2" ]  ; then echo "  This DQM patch version not available - exiting " ; exit ; fi

echo "  installing tags for DQMPATCH:$dqmpatch in your project area:"
if [ $all != "true" ] ; 
then echo "  Note:"
echo "  only DQMServices and Integration packages will be checked out"
echo "  use option -a to checkout subsystem tags"
fi
#

cd $LOCALRT/src
source $CMS_PATH/utils/cmscvsroot.sh CMSSW

cvs co -r V00-05-12 DQMServices/Core
cvs co -r V00-05-12 DQMServices/CoreROOT
cvs co -r V00-05-11 DQMServices/Components
cvs co -r V00-05-11 DQMServices/Examples

cvs co -r V00-00-11 DQM/Integration
cvs co -r V00-00-08 DQM/RenderPlugins

if [ $all == "true" ] ; 
then echo "  now checking out subsystem tags  ... " ; sleep 2

cvs co -r V01-00-01 L1Trigger/HardwareValidation
cvs co -r V02-03-03-03 DataFormats/L1Trigger

cvs co -r V00-05-01 EventFilter/EcalRawToDigiDev

cvs co -r V00-07-05 DQM/HcalMonitorClient
cvs co -r V00-07-05 DQM/HcalMonitorTasks
cvs co -r V00-07-07 DQM/HcalMonitorModule 

cvs co -r V00-06-00 DQM/RPCMonitorDigi

cvs co -r V02-00-03 DQM/CSCMonitorModule 
cvs co -r V01-08-10 EventFilter/CSCRawToDigi 

cvs co -r V00-16-05 DQM/DTMonitorModule
cvs co -r V00-03-04 DQM/DTMonitorClient

fi

echo 
echo "  done. Now type scramv1 b to build the tags"

#scramv1 b


