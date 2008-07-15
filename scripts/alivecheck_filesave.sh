#! /bin/csh -f

source /cms/mon/data/dqm/filereg/setupForFileReg.csh
set EXE=/cms/mon/data/dqm/filereg/filesave_online.py
set RUN_STAT = `ps -ef | grep filesave_online.py | grep -v grep | wc | awk '{print $1}'`

if ($RUN_STAT != 0) then
echo filesave_online.py is running at $HOST.
else
echo filesave_online.py stopped by unknown reason and restarted now.
set LOG=/cms/mon/data/dqm/filereg/log/LOG.filesave.$HOST.$$
$EXE >& $LOG &
date >> $LOG
echo filesave_online.py stopped by unknown reason and restarted at $HOST. >> $LOG
echo filesave_online.py stopped by unknown reason and restarted now at $HOST. | mail Hyunkwan.Seo@cern.ch
endif
