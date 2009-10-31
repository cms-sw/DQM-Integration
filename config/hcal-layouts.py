def hcallayout(i, p, *rows): i["Hcal/Layouts/" + p] = DQMItem(layout=rows)

hcallayout(dqmitems, "01 HCAL Shifter Checklist Plots - Summaries",
           [{ 'path':"Hcal/EventInfo/reportSummaryMap",
             'description':"This shows the fraction of bad cells in each subdetector.  All subdetectors should appear green"}]
           )

hcallayout(dqmitems, "HCAL Data Format",
           [{ 'path': "Hcal/DataFormatMonitor/ HardwareWatchCells",
              'description': "A Data Format error indicates that the data received from this channel was somehow corrupted or compromised.  This plot is the sum of bad digis over all d\epths. iPhi (1 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistogra\ms>HcalDQMHistograms</a>" }]
           )

hcallayout(dqmitems, "HCAL Trigger Primitives",
           [{ 'path': "Hcal/TrigPrimMonitor/Summary",
              'description': "See details at: <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
           [{ 'path': "Hcal/TrigPrimMonitor/Summary for ZS run",
              'description': "See details at: <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
           )

hcallayout(dqmitems, "HCAL Dead Cell Check",
          [{ 'path': "Hcal/DeadCellMonitor_Hcal/ ProblemDeadCells",
             'description': "Potential dead cell candidates in all depths. Seriously dead if dead for >5% of a full run. iPhi (1 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
           [{ 'path': "Hcal/DeadCellMonitor_Hcal/TotalDeadCells_HCAL_vs_LS",
             'description': "Total number of dead cells found in HCAL vs luminosity section"}],
           )

hcallayout(dqmitems, "HCAL Hot Cell Check",
          [{ 'path': "Hcal/HotCellMonitor_Hcal/ ProblemHotCells",
                   'description': "A cell is considered potentially hot if it is above some threshold energy, or if it is persistently below some (lower) threshold enery for a number of consecutive events. Seriously hot if hot for >5% of a full run. All depths. iPhi (1 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
           [{ 'path': "Hcal/HotCellMonitor_Hcal/TotalHotCells_HCAL_vs_LS",
              'description': "Total number of hot cells found in HCAL vs luminosity section"}],
           )

hcallayout(dqmitems, "HCAL Digi Problems",
          [{ 'path': "Hcal/DigiMonitor_Hcal/ ProblemDigis",
                   'description': "A digi cell is considered bad if the capid rotation for that digi was incorrect, if the digi's data valid/error flags are incorrect, or if there is an IDLE-BCN mismatch.  Currently, only digis with IDLE-BCN mismatches are displayed.  This plot is the sum of bad digis over all depths. iPhi (1 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
           [{ 'path': "Hcal/DigiMonitor_Hcal/bad_digis/1D_digi_plots/BadDigisVsLB",
              'description': "Total number of bad digis found in HCAL vs luminosity section"}],
           )

