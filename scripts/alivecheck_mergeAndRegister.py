#! /usr/bin/env python

import os
import smtplib
from email.MIMEText import MIMEText

MERGEEXE = '/cms/mon/data/dqm/mergeAndRegister_online.py'
RUN_STAT = int(os.popen('ps -ef | grep mergeAndRegister_online.py | grep -v grep | wc').read().split()[0])


if RUN_STAT != 0:
    print 'mergeAndRegister_online.py is running'
else:
    print 'mergeAndRegister_online.py stopped by unknown reason and restarted now.'
    #os.popen(MERGEEXE + ' &')

    #### send e-mail to a manager
    s=smtplib.SMTP("localhost")
    tolist=["Hyunkwan.Seo@cern.ch"]
    body="mergeAndRegister_online.py stopped by unknown reason and restarted now."
    msg = MIMEText(body)
    msg['Subject'] = "mergeAndRegister_online.py stopped by unknown reason and restarted now."
    msg['From'] = "cmsmon@cmscvs.cern.ch"
    msg['To'] = "Hyunkwan.Seo@cern.ch"
    s.sendmail("cmsmon@cmscvs.cern.ch",tolist,msg.as_string())
    s.quit()
