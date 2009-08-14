#! /bin/sh

WorkDir=/nfshome0/dqmpro/filecollector
YourEmail=lilopera@cern.ch
source /nfshome0/cmssw2/scripts/setup.sh

XPYTHONPATH=$PYTHONPATH
source /home/dqm/rpms/slc4_ia32_gcc345/cms/dqmgui/5.0.2/etc/profile.d/env.sh
export PYTHONPATH=$XPYTHONPATH:$PYTHONPATH

EXE=$WorkDir/fileRegister.py
RUN_STAT=`ps -ef | grep fileRegister.py | grep -v grep | wc | awk '{print $1}'`

if [ $RUN_STAT -ne 0 ]
then
    echo fileRegister.py is running
else
    echo fileRegister.py stopped by unknown reason and restarted now.
    TIMETAG=$(date +"%Y%m%d_%H%M%S")
    LOG=$WorkDir/log/LOG.fileRegister.$HOSTNAME.$TIMETAG
    $EXE >& $LOG &
    date >> $LOG
    echo fileRegister.py stopped by unknown reason and restarted at $HOSTNAME. >> $LOG
    echo fileRegister.py stopped by unknown reason and restarted now at $HOSTNAME. | mail -s "fileRegister not Running" $YourEmail
fi
