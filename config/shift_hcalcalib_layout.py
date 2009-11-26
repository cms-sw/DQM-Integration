def shifthcalcaliblayout(i, p, *rows): i["00 Shift/HcalCalib/" + p] = DQMItem(layout=rows)

shifthcalcaliblayout(dqmitems, "01 HcalCalib Summary",
           [{ 'path':"HcalCalib/EventInfo/reportSummaryMap",
             'description':"This shows the fraction of bad cells in each subdetector.  All subdetectors should appear green.  Values should all be above 98%."}]
           )

shifthcalcaliblayout(dqmitems, "HcalCalib Pedestal Check",
                     [{ 'path': "HcalCalib/HcalDetDiagPedestalMonitor/Summary Plots/HBHEHF pedestal mean map",
                        'description': "Pedestal mean values calculated from orbit gap events for HB, HE, and HF"},
                      { 'path': "HcalCalib/HcalDetDiagPedestalMonitor/Summary Plots/HBHEHF pedestal rms map",
                        'description': "Pedestal RMS values calculated from orbit gap events for HB, HE, and HF"}],  
                     [{ 'path': "HcalCalib/HcalDetDiagPedestalMonitor/Summary Plots/HO pedestal mean map",
                        'description': "Pedestal mean values calculated from orbit gap events for HO"},
                      { 'path': "HcalCalib/HcalDetDiagPedestalMonitor/Summary Plots/HO pedestal rms map",
                        'description': "Pedestal RMS values calculated from orbit gap events for HO"}]  
           )

shifthcalcaliblayout(dqmitems, "HcalCalib Laser Check",
                [{ 'path':"HcalCalib/HcalDetDiagLaserMonitor/Summary Plots/Laser Energy HBHEHF",
                   'description':"Laser Average energy in HBHEHF"},
                 { 'path':"HcalCalib/HcalDetDiagLaserMonitor/Summary Plots/Laser Energy HO",
                   'description':"Laser Average timing in HO"}],
                
                [{ 'path':"HcalCalib/HcalDetDiagLaserMonitor/Summary Plots/Laser Timing HBHEHF",
                   'description':"Laser Average energy in HBHEHF"},
                 { 'path':"HcalCalib/HcalDetDiagLaserMonitor/Summary Plots/Laser Timing HO",
                   'description':"Laser Average timing in HO"}]
                )


shifthcalcaliblayout(dqmitems, "HcalCalib RecHit Energies",
                [{'path': "HcalCalib/RecHitMonitor_Hcal/rechit_1D_plots/HB_energy_1D",
                  'description':"Average energy/hit for each of the 2592 channels in HB"},

                 {'path': "HcalCalib/RecHitMonitor_Hcal/rechit_1D_plots/HE_energy_1D",
                  'description':"Average energy/hit for each of the 2592 channels in HE"}],
                [{'path': "HcalCalib/RecHitMonitor_Hcal/rechit_1D_plots/HF_energy_1D",
                  'description':"Average energy/hit for each of the 1728 channels in HF"},
                 {'path': "HcalCalib/RecHitMonitor_Hcal/rechit_1D_plots/HO_energy_1D",
                  'description':"Average energy/hit for each of the 2160 channels in HO.  (You may see fewer entries than 2160 because of ~30 known dead cells in HO.)"}]
                )
