#!/bin/bash

if [ "$1" = "live" ] ; then
    echo live
    echo "creating softlinks"
     ln -sfv eb_dqm_sourceclient-live_cfg.py                    dqmfu_06-1_cfg.py
     ln -sfv fedtest_dqm_sourceclient-live_cfg.py               dqmfu_06-2_cfg.py
     ln -sfv l1t_dqm_sourceclient-live_cfg.py                   dqmfu_06-3_cfg.py
     ln -sfv l1temulator_dqm_sourceclient-live_cfg.py           dqmfu_06-4_cfg.py
     ln -sfv hcal_dqm_sourceclient-live_cfg.py                  dqmfu_06-5_cfg.py
     ln -sfv physics_dqm_sourceclient-live_cfg.py               dqmfu_06-6_cfg.py
     ln -sfv info_dqm_sourceclient-live_cfg.py                  dqmfu_06-7_cfg.py 
     
     ln -sfv ee_dqm_sourceclient-live_cfg.py                    dqmfu_07-1_cfg.py
     ln -sfv rpc_dqm_sourceclient-live_cfg.py                   dqmfu_07-2_cfg.py
     ln -sfv csc_dqm_sourceclient-live_cfg.py                   dqmfu_07-3_cfg.py
     ln -sfv es_dqm_sourceclient-live_cfg.py                    dqmfu_07-4_cfg.py
     ln -sfv dt_dqm_sourceclient-live_cfg.py                    dqmfu_07-5_cfg.py
     ln -sfv castor_dqm_sourceclient_live_cfg.py                dqmfu_07-6_cfg.py
     
     ln -sfv pixel_dqm_sourceclient-live_cfg.py                 dqmfu_08-1_cfg.py
     ln -sfv sistrip_dqm_sourceclient-live_cfg.py               dqmfu_08-2_cfg.py
     ln -sfv beam_dqm_sourceclient-live_cfg.py                  dqmfu_08-3_cfg.py
     ln -sfv beampixel_dqm_sourceclient-live_cfg.py             dqmfu_08-4_cfg.py
     
     
     ln -sfv hlt_dqm_sourceclient-live_cfg.py                   dqmfu_09-1_cfg.py
     ln -sfv hlx_dqm_sourceclient-live_cfg.py                   dqmfu_09-2_cfg.py
     ln -sfv fed_dqm_sourceclient-live_cfg.py                   dqmfu_09-3_cfg.py
     ln -sfv hcalcalib_dqm_sourceclient-live_cfg.py             dqmfu_09-4_cfg.py
     
     ln -sfv ispy_dqm_sourceclient-live_cfg.py                  dqmfu_10-1_cfg.py
     ln -sfv ispyhltmon_dqm_sourceclient-live_cfg.py               dqmfu_10-2_cfg.py
     ln -sfv ispywide_dqm_sourceclient-live_cfg.py              dqmfu_10-3_cfg.py
     ln -sfv ispyexpress_dqm_sourceclient-live_cfg.py           dqmfu_10-4_cfg.py


  echo "copying cfg from python test"
  cp ../python/test/*live_cfg.py .
  echo "done"
  
elif [ "$1" = "playback" ] ; then
  echo playback
  echo "creating softlinks"
     ln -sfv eb_dqm_sourceclient-live_cfg.py                    dqmfu_13-1_cfg.py
     ln -sfv fedtest_dqm_sourceclient-live_cfg.py               dqmfu_13-2_cfg.py
     ln -sfv l1t_dqm_sourceclient-live_cfg.py                   dqmfu_13-3_cfg.py
     ln -sfv l1temulator_dqm_sourceclient-live_cfg.py           dqmfu_13-4_cfg.py
     ln -sfv hcal_dqm_sourceclient-live_cfg.py                  dqmfu_13-5_cfg.py
     ln -sfv physics_dqm_sourceclient-live_cfg.py               dqmfu_13-6_cfg.py
     ln -sfv info_dqm_sourceclient-live_cfg.py                  dqmfu_13-7_cfg.py 
     
     ln -sfv ee_dqm_sourceclient-live_cfg.py                    dqmfu_14-1_cfg.py
     ln -sfv rpc_dqm_sourceclient-live_cfg.py                   dqmfu_14-2_cfg.py
     ln -sfv csc_dqm_sourceclient-live_cfg.py                   dqmfu_14-3_cfg.py
     ln -sfv es_dqm_sourceclient-live_cfg.py                    dqmfu_14-4_cfg.py
     ln -sfv dt_dqm_sourceclient-live_cfg.py                    dqmfu_14-5_cfg.py
     ln -sfv castor_dqm_sourceclient_live_cfg.py                dqmfu_14-6_cfg.py
     
     ln -sfv pixel_dqm_sourceclient-live_cfg.py                 dqmfu_15-1_cfg.py
     ln -sfv sistrip_dqm_sourceclient-live_cfg.py               dqmfu_15-2_cfg.py
     ln -sfv beam_dqm_sourceclient-live_cfg.py                  dqmfu_15-3_cfg.py
     ln -sfv beampixel_dqm_sourceclient-live_cfg.py             dqmfu_15-4_cfg.py
     
     ln -sfv hlt_dqm_sourceclient-live_cfg.py                   dqmfu_16-1_cfg.py
     ln -sfv hlx_dqm_sourceclient-live_cfg.py                   dqmfu_16-2_cfg.py
     ln -sfv fed_dqm_sourceclient-live_cfg.py                   dqmfu_16-3_cfg.py
     ln -sfv hcalcalib_dqm_sourceclient-live_cfg.py             dqmfu_16-4_cfg.py
     
     ln -sfv ispy_dqm_sourceclient-live_cfg.py                  dqmfu_17-1_cfg.py
     ln -sfv ispyhltmon_dqm_sourceclient-live_cfg.py               dqmfu_17-2_cfg.py
     ln -sfv ispywide_dqm_sourceclient-live_cfg.py              dqmfu_17-3_cfg.py
     ln -sfv ispyexpress_dqm_sourceclient-live_cfg.py           dqmfu_17-4_cfg.py
  echo "copying cfg from python test"
  cp ../python/test/*live_cfg.py .

  echo "done"

else

 echo specify live, or playback

fi
