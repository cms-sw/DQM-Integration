#! /bin/sh

export WorkDir=$(dirname $0)
YourEmail=lilopera@cern.ch
#source /nfshome0/cmssw2/scripts/setup.sh
if [ -d /home/dqm/rpms/slc4_ia32_gcc345/cms/dqmgui/5.0.2/etc/profile.d/ ]
then
  XPYTHONPATH=$PYTHONPATH
  source /home/dqm/rpms/slc4_ia32_gcc345/cms/dqmgui/5.0.2/etc/profile.d/env.sh
else
  source $WorkDir/env.sh
fi
export PYTHONPATH=$XPYTHONPATH:$PYTHONPATH
export $HOSTNAME

if [[ $1 == "" ]]
then
  echo No config file specifyed
  exit
fi
if [[ $2 == "" ]]
then
  echo No script file specifyed
  exit
fi
if [[ $(dirname $1) == "." ]]
then
  CFGFILE=$WorkDir/$1
else
  CFGFILE=$1
fi
EXE="$WorkDir/$2 $CFGFILE"
RUN_STAT=`ps -ef | grep "$2 $CFGFILE" | grep -v grep | wc | awk '{print $1}'`
PRETTY_NAME=`basename $2 | grep -oP ".*(?=\.[\d\s\w]+)|^\.[\d\s\w]+|^[\d\w]+"`
if [ $RUN_STAT -ne 0 ]
then
    echo $PRETTY_NAME is running
else
    echo $PRETTY_NAME stopped by unknown reason and restarted now.
    TIMETAG=$(date +"%Y%m%d_%H%M%S")
    LOG=$WorkDir/log/LOG.$PRETTY_NAME.$HOSTNAME.$TIMETAG
    $EXE >& $LOG &
    date >> $LOG
    echo $PRETTY_NAME stopped by unknown reason and restarted at $HOSTNAME. >> $LOG
    echo $PRETTY_NAME stopped by unknown reason and restarted now at $HOSTNAME. | mail -s "$PRETTY_NAME not Running" $YourEmail
fi
