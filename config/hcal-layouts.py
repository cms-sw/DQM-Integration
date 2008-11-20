def hcallayout(i, p, *rows): i["Hcal/Layouts/" + p] = DQMItem(layout=rows)

hcallayout(dqmitems, "HCAL Pedestals",
          [{ 'path': "Hcal/PedestalMonitor_Hcal/HB HF Depth 1 Pedestal Mean Map ADC",
                   'description': "Should be fairly uniform in color, except two vertical red stripes at abs(ieta) 28. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
           { 'path': "Hcal/PedestalMonitor_Hcal/HB HF Depth 2 Pedestal Mean Map ADC",
                   'description': "Should be fairly uniform in color, except two vertical red stripes at abs(ieta) 28.. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
          [{ 'path': "Hcal/PedestalMonitor_Hcal/HE Depth 1 Pedestal Mean Map ADC",
                   'description': "Should be fairly uniform in color, except two vertical red stripes at abs(ieta) 28. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
           { 'path': "Hcal/PedestalMonitor_Hcal/HE Depth 2 Pedestal Mean Map ADC",
                   'description': "Should be fairly uniform in color, except two vertical red stripes at abs(ieta) 28.. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
          [{ 'path': "Hcal/PedestalMonitor_Hcal/HE Depth 3 Pedestal Mean Map ADC",
                   'description': "Should be fairly uniform in color, except two vertical red stripes at abs(ieta) 28. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
           { 'path': "Hcal/PedestalMonitor_Hcal/HO ZDC Pedestal Mean Map ADC",
                   'description': "Should be fairly uniform in color, except two vertical red stripes at abs(ieta) 28.. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],)

hcallayout(dqmitems, "HCAL Trigger Primitives",
          [{ 'path': "Hcal/TrigPrimMonitor/Energy Plots/ADC spectrum positive TP",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
          [{ 'path': "Hcal/TrigPrimMonitor/Electronics Plots/TP vs Digi",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
           )

hcallayout(dqmitems, "HCAL Dead Cell Check",
          [{ 'path': "Hcal/DeadCellMonitor_Hcal/ ProblemDeadCells",
                   'description': "Potential dead cell candidates in all depths. Seriously dead if dead for >5% of a full run. iPhi (0 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
           )

hcallayout(dqmitems, "HCAL Hot Cell Check",
          [{ 'path': "Hcal/HotCellMonitor_Hcal/ ProblemHotCells",
                   'description': "A cell is considered potentially hot if: Above a threshold energy; More than 3 sigma above its pedestal value; or Energy is especially large compared to its neighbors. Seriously hot if hot for >5% of a full run. All depths. iPhi (0 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
           )

hcallayout(dqmitems, "HCAL Data Integrity Problems",
          [{ 'path': "Hcal/DigiMonitor/HCAL/HCALProblemDigiCells",
                   'description': "A digi cell is considered bad if there was no digi for that cell in the event, if the capid rotation for that digi was incorrect, or if the sum of ADC counts over all time slices for the digi is 0. If zero-suppression of the HCAL is enabled for a run, this plot may have high occupancy, and you should check the expert plots for more detailed information.All depths. iPhi (0 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
           )



