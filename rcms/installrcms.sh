#!/bin/bash

if [ "$1" = "live" ] ; then
    echo live
    echo "creating softlinks"
    ln -sfv eb_dqm_sourceclient-live_cfg.py                    dqmfu_06-1_cfg.py
    ln -sfv fedtest_dqm_sourceclient-live_cfg.py               dqmfu_06-2_cfg.py
    ln -sfv l1t_dqm_sourceclient-live_cfg.py                   dqmfu_06-3_cfg.py
    ln -sfv l1temulator_dqm_sourceclient-live_cfg.py           dqmfu_06-4_cfg.py
    ln -sfv hcal_dqm_sourceclient-live_cfg.py                  dqmfu_06-5_cfg.py
    ln -sfv physics_dqm_sourceclient-live_cfg.py                dqmfu_06-6_cfg.py
    
    ln -sfv ee_dqm_sourceclient-live_cfg.py                    dqmfu_07-1_cfg.py
    ln -sfv rpc_dqm_sourceclient-live_cfg.py                   dqmfu_07-2_cfg.py
    ln -sfv csc_dqm_sourceclient-live_cfg.py                   dqmfu_07-3_cfg.py
    ln -sfv es_dqm_sourceclient-live_cfg.py                    dqmfu_07-4_cfg.py
    ln -sfv dt_dqm_sourceclient-live_cfg.py                    dqmfu_07-5_cfg.py
    ln -sfv castor_dqm_sourceclient_live_cfg.py                dqmfu_07-6_cfg.py
    
    ln -sfv pixel_dqm_sourceclient-live_cfg.py                 dqmfu_08-1_cfg.py
    ln -sfv sistrip_dqm_sourceclient-live_cfg.py               dqmfu_08-2_cfg.py
    ln -sfv beam_dqm_sourceclient-live_cfg.py                  dqmfu_08-3_cfg.py
    
    ln -sfv hlt_dqm_sourceclient-live_cfg.py                   dqmfu_09-1_cfg.py
    ln -sfv hlx_dqm_sourceclient-live_cfg.py                   dqmfu_09-2_cfg.py
    ln -sfv fed_dqm_sourceclient-live_cfg.py                   dqmfu_09-3_cfg.py
    ln -sfv hcalcalib_dqm_sourceclient-live_cfg.py             dqmfu_09-4_cfg.py
    
    ln -sfv ispy_dqm_sourceclient-live_cfg.py                  dqmfu_10-1_cfg.py
    ln -sfv ispybptx_dqm_sourceclient-live_cfg.py              dqmfu_10-2_cfg.py
    ln -sfv ispyhltmon_dqm_sourceclient-live_cfg.py            dqmfu_10-3_cfg.py
    ln -sfv ispyexpress_dqm_sourceclient-live_cfg.py           dqmfu_10-4_cfg.py


  echo "copying cfg from python test"
  cp ../python/test/*live_cfg.py .
  echo "done"
  
elif [ "$1" = "playback" ] ; then
  echo playback
  echo "creating softlinks"
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
  echo "copying cfg from python test"
  cp ../python/test/*playback_cfg.py .

  echo "done"

elif [ "$1" = "fakelive" ] ; then
  echo fakelive
  echo "creating softlinks"

    ln -sf fedtest_dqm_sourceclient-live_cfg.py     dqmfu09-1_cfg.py
    ln -sf l1t_dqm_sourceclient-live_cfg.py         dqmfu09-2_cfg.py
    ln -sf l1temulator_dqm_sourceclient-live_cfg.py dqmfu09-3_cfg.py
    
    ln -sf hcal_dqm_sourceclient-live_cfg.py        dqmfu10-1_cfg.py
    ln -sf castor_dqm_sourceclient_live_cfg.py      dqmfu10-2_cfg.py
    ln -sf hlx_dqm_sourceclient-live_cfg.py         dqmfu10-3_cfg.py
    
    ln -sf ee_dqm_sourceclient-live_cfg.py          dqmfu11-1_cfg.py
    ln -sf rpc_dqm_sourceclient-live_cfg.py         dqmfu11-2_cfg.py
    ln -sf csc_dqm_sourceclient-live_cfg.py         dqmfu11-3_cfg.py
    
    ln -sf eb_dqm_sourceclient-live_cfg.py          dqmfu15-1_cfg.py
    ln -sf es_dqm_sourceclient-live_cfg.py          dqmfu15-2_cfg.py
    ln -sf dt_dqm_sourceclient-live_cfg.py          dqmfu15-3_cfg.py
    
    ln -sf pixel_dqm_sourceclient-live_cfg.py       dqmfu16-1_cfg.py
    ln -sf sistrip_dqm_sourceclient-live_cfg.py     dqmfu16-2_cfg.py
    ln -sf ispy_dqm_sourceclient-live_cfg.py        dqmfu16-3_cfg.py
    
    ln -sf fed_dqm_sourceclient-live_cfg.py         dqmfu17-1_cfg.py
    ln -sf hlt_dqm_sourceclient-live_cfg.py         dqmfu17-2_cfg.py
    ln -sf daq_dqm_sourceclient-live_cfg.py         dqmfu17-3_cfg.py
    ln -sf hcalcalib_dqm_sourceclient-live_cfg.py   dqmfu17-4_cfg.py

  echo "copying cfg from python test"
  cp ../python/test/*live_cfg.py .
  

  echo "done"

else

 echo specify live, or playback

fi
