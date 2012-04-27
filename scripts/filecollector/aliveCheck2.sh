#! /bin/bash

#export WorkDir=$(dirname $0)
YourEmail=sdutta@cern.ch
#source /nfshome0/cmssw2/scripts/setup.sh

export SCRAM_ARCH=slc5_amd64_gcc462
if [[ ! $HOME =~ /nfshome0/dqm* ]]
then 
  HOME=/nfshome0/${USER/local/}
fi
if [[ -d ${HOME}/prod || -d ${HOME}/dev ]] 
then
  source /nfshome0/dqmpro/bin/setup_cmssw.sh
  [[ -d ${HOME}/prod ]] && cd ${HOME}/prod || cd ${HOME}/dev
  eval `scram runtime -sh`
else
  source $WorkDir/env3.sh
fi
export PYTHONPATH=$XPYTHONPATH:$PYTHONPATH
export HOSTNAME=$HOSTNAME

if [[ $USER =~ 'dqmpr.*' ]]
then
  EXE="/nfshome0/dqmpro/filecollector/fileCollector2.py /home/dqmprolocal/output /home/dqmprolocal/done /dqmdata/dqm/uploads"
else
  EXE="/nfshome0/dqmpro/filecollector/fileCollector2.py /home/dqmdevlocal/output /home/dqmdevlocal/done /dqmdata/dqmintegration/upload"
fi
WorkDir=$( dirname ${EXE/.*} )
[[ -e $WorkDir/.start ]] && [[ -e $WorkDir/.stop ]] && rm $WorkDir/.stop
[[ -e $WorkDir/.stop ]] && echo Found stop file not starting the agents && exit 0
RUN_STAT=`ps -ef | grep "$EXE" | grep -v grep | wc | awk '{print $1}'`
PRETTY_NAME=fileCollector2 #`basename $2 | grep -oP ".*(?=\.[\d\s\w]+)|^\.[\d\s\w]+|^[\d\w]+"`
if [ $RUN_STAT -ne 0 ]
then
    echo $PRETTY_NAME is running
else
    echo $PRETTY_NAME stopped by unknown reason and restarted now.
    TIMETAG=$(date +"%Y%m%d_%H%M%S")
    LOG=$WorkDir/log/LOG.$PRETTY_NAME.$HOSTNAME.$TIMETAG
    $EXE >& $LOG &
    date >> $LOG
    [[ ! -e $WorkDir/.start ]] && 
         echo $PRETTY_NAME stopped by unknown reason and restarted at $HOSTNAME. >> $LOG ||
         echo $PRETTY_NAME Found .start file, starting
    [[ ! -e $WorkDir/.start ]] && echo $PRETTY_NAME stopped by unknown reason and restarted now at $HOSTNAME. | mail -s "$PRETTY_NAME not Running" $YourEmail
fi
if [[ -e $WorkDir/.start ]]
then
  sleep 10
  master=$(cat $WorkDir/.start)
  [[ $(hostname -s) == $master ]] && rm $WorkDir/.start
fi 
