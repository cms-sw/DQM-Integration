#! /bin/sh

WorkDir=$(dirname $0)
YourEmail=lilopera@cern.ch
#source /nfshome0/cmssw2/scripts/setup.sh

XPYTHONPATH=$PYTHONPATH
source /data/sw/slc4_ia32_gcc345/cms/dqmgui/5.0.2/etc/profile.d/env.sh
export PYTHONPATH=$XPYTHONPATH:$PYTHONPATH
if [[ $1 == "" ]]
then
  echo No config file specifyed
  exit
fi
if [[ $(dirname $1) == "." ]]
then
  CFGFILE=$WorkDir/$1
else
  CFGFILE=$1
fi
EXE="$WorkDir/fileClassifier $CFGFILE"
RUN_STAT=`ps -ef | grep "fileClassifier $CFGFILE" | grep -v grep | wc | awk '{print $1}'`

if [ $RUN_STAT -ne 0 ]
then
    echo fileClassifier is running
else
    echo fileClassifier stopped by unknown reason and restarted now.
    TIMETAG=$(date +"%Y%m%d_%H%M%S")
    LOG=$WorkDir/log/LOG.fileClassifier.$HOSTNAME.$TIMETAG
    $EXE >& $LOG &
    date >> $LOG
    echo fileClassifier stopped by unknown reason and restarted at $HOSTNAME. >> $LOG
    echo fileClassifier stopped by unknown reason and restarted now at $HOSTNAME. | mail -s "fileClassifier not Running" $YourEmail
fi
