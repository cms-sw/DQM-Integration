#! /bin/csh -f

set EXE=/cmsnfshome0/nfshome0/cmsmon/filereg_test/filesave_online.py
set RUN_STAT = `ps -ef | grep filesave_online.py | grep -v grep | wc | awk '{print $1}'`

if ($RUN_STAT != 0) then
echo filesave_online.py is running at $HOST.
else
echo filesave_online.py stopped by unknown reason and restarted now.
set LOG=/cmsnfshome0/nfshome0/cmsmon/filereg_test/log/LOG.filesave.$$
$EXE >& $LOG &
date >> $LOG
echo filesave_online.py stopped by unknown reason and restarted at $HOST. >> $LOG
echo filesave_online.py stopped by unknown reason and restarted now at $HOST. | mail Hyunkwan.Seo@cern.ch
endif
