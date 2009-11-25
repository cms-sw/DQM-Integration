def shifthcallayout(i, p, *rows): i["00 Shift/Hcal/" + p] = DQMItem(layout=rows)

# Report Summary Map
shifthcallayout(dqmitems, "Hcal Report Summary",
                [{'path':"Hcal/EventInfo/reportSummaryMap",
                  'description':  "Shows average fraction of good cells per event in each Hcal subdetector (HB/HE/HO/HF/HO0/HO12/HFLumi).  Values should be greater than 0.98.  There are known dead cells in HO, so the HO/HO0/HO12 values will usually be lower than those of the other subdetectors.  This summary is fed by the results from the other plots on this page, so when a value is less than 0.95, you can use the other tests to determine the type of failure."}]
                )

shifthcallayout(dqmitems, "HCAL Data Format",
                [{ 'path': "Hcal/DataFormatMonitor/ HardwareWatchCells",
                   'description': "A Data Format error indicates that the data received from this channel was somehow corrupted or compromised.  This plot is the sum of bad digis over all depths. iPhi (1 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
                )

shifthcallayout(dqmitems, "HCAL Trigger Primitives",
                [{ 'path': "Hcal/TrigPrimMonitor/Summary for ZS run",
                   'description': "See details at: <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
                )

shifthcallayout(dqmitems, "HCAL Dead Cell Check",
                [{ 'path': "Hcal/DeadCellMonitor_Hcal/ ProblemDeadCells",
                   'description': "Potential dead cell candidates in all depths. Seriously dead if dead for >5% of a full run. iPhi (1 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
                [{ 'path': "Hcal/DeadCellMonitor_Hcal/TotalDeadCells_HCAL_vs_LS",
                   'description': "Total number of dead cells found in HCAL vs luminosity section"}],
                )

shifthcallayout(dqmitems, "HCAL Hot Cell Check",
                [{ 'path': "Hcal/HotCellMonitor_Hcal/ ProblemHotCells",
                   'description': "A cell is considered potentially hot if it is above some threshold energy, or if it is persistently below some (lower) threshold enery for a number of consecutive events. Seriously hot if hot for >5% of a full run. All depths. iPhi (1 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
                [{ 'path': "Hcal/HotCellMonitor_Hcal/TotalHotCells_HCAL_vs_LS",
                   'description': "Total number of hot cells found in HCAL vs luminosity section"}],
                )

shifthcallayout(dqmitems, "HCAL Digi Problems",
                [{ 'path': "Hcal/DigiMonitor_Hcal/ ProblemDigis",
                   'description': "A digi cell is considered bad if the capid rotation for that digi was incorrect, if the digi's data valid/error flags are incorrect, or if there is an IDLE-BCN mismatch.  Currently, only digis with IDLE-BCN mismatches are displayed.  This plot is the sum of bad digis over all depths. iPhi (1 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
                [{ 'path': "Hcal/DigiMonitor_Hcal/bad_digis/1D_digi_plots/BadDigisVsLB",
                   'description': "Total number of bad digis found in HCAL vs luminosity section"}],
                )

shifthcallayout(dqmitems, "HCAL Lumi Problems",
                [{'path': "Hcal/BeamMonitor_Hcal/ ProblemBeamMonitor",
                  'description':"This shows problems only in the sections of HF used for luminosity monitoring.  Channels that are hot or dead are considered as problems, where the definitions of 'hot' and 'dead' are slightly different than in the normal HCAL monitors.  More details at  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
                )

shifthcallayout(dqmitems, "HCAL RecHit Energies",
                [{'path': "Hcal/RecHitMonitor_Hcal/rechit_1D_plots/HB_energy_1D",
                  'description':"Average energy/hit for each of the 2592 channels in HB"},
                 
                 {'path': "Hcal/RecHitMonitor_Hcal/rechit_1D_plots/HE_energy_1D",
                  'description':"Average energy/hit for each of the 2592 channels in HE"}],
                [{'path': "Hcal/RecHitMonitor_Hcal/rechit_1D_plots/HF_energy_1D",
                  'description':"Average energy/hit for each of the 1728 channels in HF"},
                 {'path': "Hcal/RecHitMonitor_Hcal/rechit_1D_plots/HO_energy_1D",
                  'description':"Average energy/hit for each of the 2160 channels in HO.  (You may see fewer entries than 2160 because of ~30 known dead cells in HO.)"}]
                )
