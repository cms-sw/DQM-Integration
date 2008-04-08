#! /usr/bin/env python

import os
import time
import sys

DIR = '/afs/cern.ch/user/h/hkseo/public/DQM/dropbox'
#os.system('touch -t 01010000 '+ DIR +'/timeTag')

####### ENDLESS LOOP WITH SLEEP
while 1:
    
    count = 0
    for NEW in os.popen('find '+ DIR +'/ -type f -name "DQM_*_R?????????.root" -newer '+ DIR +'/timeTag'):
        NEW = NEW.strip()
        print NEW
        count += 1
        if count == 1:
            os.system('touch '+ DIR +'/timeTag')

        #### extract run number of new file
        run = NEW[-14:-5]

        #### check if merged file exist & the size of the last merged file
        FILE_EXIST = int(os.popen('ls '+ DIR + '/DQM_V* | wc').read().split()[0])
        SIZE_LIMIT = 10000000

        if FILE_EXIST > 0:
            FILE_SIZE = int(os.popen('ls -lrt '+ DIR +'/DQM_V* | tail -1').read().split()[4])
            if FILE_SIZE > SIZE_LIMIT: FILE_EXIST = 0

        if FILE_EXIST > 0:
            FILE = os.popen('ls -rt '+ DIR + '/DQM_V* | tail -1').read()
            FILE = FILE.strip()
            ver = int(FILE[-30:-27])
            irun = FILE[-25:-16]
            frun = FILE[-14:-5]

            ### create the name of new merged file
            if run > frun:
                frun = run
            elif run < irun:
                irun = run

            ver += 1
            if ver < 10:
                ver = '00' + str(ver)
            elif ver < 100:
                ver = '0' + str(ver)
                
            NEW_MERGED = DIR + '/DQM_V' + ver + '_R' + irun + '-R' + frun + '.root'
                
            ### check if the name of new merged file is unique
            if os.path.exists(NEW_MERGED):
                print NEW_MERGED + ' already exist.: Error'
                sys.exit(1)

            ### merge new file
            time.sleep(1)
            hadd NEW_MERGED NEW FILE
            os.system('rm '+FILE)
        else:
            irun = run
            frun = run
            os.system('cp '+NEW+' '+ DIR+'/DQM_V001_R'+irun+'-R'+frun+'.root')

        time.sleep(300)
