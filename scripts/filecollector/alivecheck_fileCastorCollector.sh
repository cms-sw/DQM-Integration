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
EXE="$WorkDir/fileCastorCollector $CFGFILE"
RUN_STAT=`ps -ef | grep "fileCastorCollector $CFGFILE" | grep -v grep | wc | awk '{print $1}'`

if [ $RUN_STAT -ne 0 ]
then
    echo fileCastorCollector is running
else
    echo fileCastorCollector stopped by unknown reason and restarted now.
    TIMETAG=$(date +"%Y%m%d_%H%M%S")
    LOG=$WorkDir/log/LOG.fileCastorCollector.$HOSTNAME.$TIMETAG
    $EXE >& $LOG &
    date >> $LOG
    echo fileCastorCollector stopped by unknown reason and restarted at $HOSTNAME. >> $LOG
    echo fileCastorCollector stopped by unknown reason and restarted now at $HOSTNAME. | mail -s "fileCastorCollector not Running" $YourEmail
fi
