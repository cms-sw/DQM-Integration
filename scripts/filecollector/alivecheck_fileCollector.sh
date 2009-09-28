#! /bin/sh

export WorkDir=$(dirname $0)
YourEmail=lilopera@cern.ch
source $WorkDir/env.sh
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

EXE="$WorkDir/fileCollector.py $CFGFILE"
RUN_STAT=`ps -ef | grep "fileCollector.py $CFGFILE" | grep -v grep | wc | awk '{print $1}'`

if [ $RUN_STAT -ne 0 ]
then
    echo fileCollector.py is running at $HOSTNAME.
else
    echo fileCollector.py stopped by unknown reason and restarted now.
    LOG=$WorkDir/log/LOG.fileCollector.$HOSTNAME.$$
    date >& $LOG
    echo fileCollector.py stopped by unknown reason and restarted at $HOSTNAME. >> $LOG
    $EXE >> $LOG 2>&1 & 
    echo fileCollector.py stopped by unknown reason and restarted now at $HOSTNAME. | mail -s "fileCollector not Running" $YourEmail
fi
