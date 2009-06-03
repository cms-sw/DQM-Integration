#!/bin/bash

if [ "$1" = "live" ] ; then
  echo live

  ln -s daq_dqm_sourceclient-live_cfg.py              dqmfu10-1_cfg.py
<<<<<<< installrcms.sh

  ln -s eb_dqm_sourceclient-live_cfg.py               dqmfu12-2_cfg.py

  ln -s ee_dqm_sourceclient-live_cfg.py               dqmfu13-1_cfg.py

=======
  
>>>>>>> 1.11
  ln -s sistrip_dqm_sourceclient-live_cfg.py          dqmfu15-1_cfg.py 
  ln -s hlx_dqm_sourceclient-live_cfg.py              dqmfu15-2_cfg.py
<<<<<<< installrcms.sh
  ln -s hcaltiming_dqm_sourceclient-live_cfg.py       dqmfu15-3_cfg.py 
  ln -s iggi_2XX_dqm_sourceclient-live_cfg.py         dqmfu15-4_cfg.py
   
  ln -s es_dqm_sourceclient-live_cfg.py               dqmfu16-1_cfg.py 
=======
  ln -s hcaltiming_dqm_sourceclient-live_cfg.py       dqmfu15-3_cfg.py
  ln -s ispy_dqm_sourceclient-live_cfg.py             dqmfu15-4_cfg.py
  
  ln -s ee_dqm_sourceclient-live_cfg.py               dqmfu16-1_cfg.py
  ln -s eb_dqm_sourceclient-live_cfg.py               dqmfu16-2_cfg.py 
>>>>>>> 1.11
  ln -s hcal_dqm_sourceclient-live_cfg.py             dqmfu16-3_cfg.py
  ln -s dt_dqm_sourceclient-live_cfg.py               dqmfu16-4_cfg.py
  
  ln -s hlt_dqm_sourceclient-live_cfg.py              dqmfu17-1_cfg.py
  ln -s l1t_dqm_sourceclient-live_cfg.py              dqmfu17-2_cfg.py
  ln -s l1temulator_dqm_sourceclient-live_cfg.py      dqmfu17-3_cfg.py
  ln -s rpc_dqm_sourceclient-live_cfg.py              dqmfu17-4_cfg.py
  
  ln -s pixel_dqm_sourceclient-live_cfg.py            dqmfu18-1_cfg.py
  ln -s csc_dqm_sourceclient-live_cfg.py              dqmfu18-2_cfg.py
  ln -s fed_dqm_sourceclient-live_cfg.py              dqmfu18-3_cfg.py
  ln -s fedtest_dqm_sourceclient-live_cfg.py          dqmfu18-4_cfg.py
<<<<<<< installrcms.sh


=======
  
>>>>>>> 1.11

  cp ../python/test/*live_cfg.py .

#
elif [ "$1" = "playback" ] ; then
  echo playback
  ln -s ee_dqm_sourceclient-playback_cfg.py           dqmfu09-1_cfg.py  
  ln -s eb_dqm_sourceclient-playback_cfg.py           dqmfu09-2_cfg.py  
  ln -s l1t_dqm_sourceclient-playback_cfg.py          dqmfu09-3_cfg.py  
  ln -s l1temulator_dqm_sourceclient-playback_cfg.py  dqmfu09-4_cfg.py
  ln -s ispy_dqm_sourceclient-playback_cfg.py         dqmfu09-5_cfg.py
   
  ln -s hcal_dqm_sourceclient-playback_cfg.py         dqmfu10-1_cfg.py  
  ln -s csc_dqm_sourceclient-playback_cfg.py          dqmfu10-2_cfg.py  
  ln -s dt_dqm_sourceclient-playback_cfg.py           dqmfu10-3_cfg.py  
  ln -s rpc_dqm_sourceclient-playback_cfg.py          dqmfu10-4_cfg.py  
  ln -s fed_dqm_sourceclient-playback_cfg.py          dqmfu10-5_cfg.py
    
  ln -s pixel_dqm_sourceclient-playback_cfg.py        dqmfu11-1_cfg.py  
  ln -s hlt_dqm_sourceclient-playback_cfg.py          dqmfu11-2_cfg.py  
  ln -s hcaltiming_dqm_sourceclient-playback_cfg.py   dqmfu11-3_cfg.py  
  ln -s sistrip_dqm_sourceclient-playback_cfg.py      dqmfu11-4_cfg.py
  ln -s es_dqm_sourceclient-playback_cfg.py           dqmfu11-5_cfg.py
  cp ../python/test/*playback_cfg.py .
else
 echo specify live or playback

fi
