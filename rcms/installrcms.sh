#!/bin/bash

if [ "$1" = "live" ] ; then
  echo live

  ln -s  daq_dqm_sourceclient-live.cfg           dqmfu10-1.cfg 

  ln -s  sistrip_dqm_sourceclient-live.cfg       dqmfu15-1.cfg 
  ln -s  hlx_dqm_sourceclient-live.cfg           dqmfu15-2.cfg 

  ln -s  ee_dqm_sourceclient-live.cfg            dqmfu16-1.cfg 
  ln -s  eb_dqm_sourceclient-live.cfg            dqmfu16-2.cfg 
  ln -s  hcal_dqm_sourceclient-live.cfg          dqmfu16-3.cfg 
  ln -s  dt_dqm_sourceclient-live.cfg            dqmfu16-4.cfg 

  ln -s  hlt_dqm_sourceclient-live.cfg           dqmfu17-1.cfg 
  ln -s  l1t_dqm_sourceclient-live.cfg           dqmfu17-2.cfg 
  ln -s  l1temulator_dqm_sourceclient-live.cfg   dqmfu17-3.cfg 
  ln -s  rpc_dqm_sourceclient-live.cfg           dqmfu17-4.cfg 

  ln -s  pixel_dqm_sourceclient-live.cfg         dqmfu18-1.cfg 
  ln -s  csc_dqm_sourceclient-live.cfg           dqmfu18-2.cfg 
  ln -s  shipper_dqm_sourceclient-live.cfg       dqmfu18-3.cfg 
  cp ../python/test/*live_cfg.py .

#
elif [ "$1" = "playback" ] ; then
  echo playback
  ln -s ee_dqm_sourceclient-playback_cfg.py           dqmfu09-1_cfg.py  
  ln -s eb_dqm_sourceclient-playback_cfg.py           dqmfu09-2_cfg.py  
  ln -s l1t_dqm_sourceclient-playback_cfg.py          dqmfu09-3_cfg.py  
  ln -s l1temulator_dqm_sourceclient-playback_cfg.py  dqmfu09-4_cfg.py  
  ln -s hcal_dqm_sourceclient-playback_cfg.py         dqmfu10-1_cfg.py  
  ln -s csc_dqm_sourceclient-playback_cfg.py          dqmfu10-2_cfg.py  
  ln -s dt_dqm_sourceclient-playback_cfg.py           dqmfu10-3_cfg.py  
  ln -s rpc_dqm_sourceclient-playback_cfg.py          dqmfu10-4_cfg.py  
  ln -s fed_dqm_sourceclient-playback_cfg.py          dqmfu10-5_cfg.py  
  ln -s pixel_dqm_sourceclient-playback_cfg.py        dqmfu11-1_cfg.py  
  ln -s hlt_dqm_sourceclient-playback_cfg.py          dqmfu11-2_cfg.py  
  ln -s sistrip_dqm_sourceclient-playback_cfg.py      dqmfu11-4_cfg.py  
  cp ../python/test/*playback_cfg.py .
else
 echo specify live or playback

fi
