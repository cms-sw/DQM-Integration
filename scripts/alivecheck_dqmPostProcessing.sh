#! /bin/csh -f

source /cms/mon/data/dqm/filereg_test/setupForFileReg.csh
set EXE=/cms/mon/data/dqm/filereg_test/dqmPostProcessing_online.py
set RUN_STAT = `ps -ef | grep dqmPostProcessing_online.py | grep -v grep | wc | awk '{print $1}'`

if ($RUN_STAT != 0) then
echo dqmPostProcessing_online.py is running
else
echo dqmPostProcessing_online.py stopped by unknown reason and restarted now.
set LOG=/cms/mon/data/dqm/filereg_test/log/LOG.postprocess.$$
$EXE >& $LOG &
date >> $LOG
echo dqmPostProcessing_online.py stopped by unknown reason and restarted at $HOST. >> $LOG
echo dqmPostProcessing_online.py stopped by unknown reason and restarted now at $HOST. | mail Hyunkwan.Seo@cern.ch
endif
