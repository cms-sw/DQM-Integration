def hcallayout(i, p, *rows): i["Hcal/Layouts/" + p] = DQMItem(layout=rows)

hcallayout(dqmitems, "HCAL Dead Cell Check",
          [{ 'path': "Hcal/DeadCellMonitor_Hcal/ ProblemDeadCells",
             'description': "Potential dead cell candidates in all depths. Seriously dead if dead for >5% of a full run. iPhi (0 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
           [{ 'path': "Hcal/DeadCellMonitor_Hcal/Problem_TotalDeadCells_HCAL",
             'description': "Total number of dead cells found in HCAL"}],
           )

hcallayout(dqmitems, "HCAL Hot Cell Check",
          [{ 'path': "Hcal/HotCellMonitor_Hcal/ ProblemHotCells",
                   'description': "A cell is considered potentially hot if: Above a threshold energy; More than 3 sigma above its pedestal value; or Energy is especially large compared to its neighbors. Seriously hot if hot for >5% of a full run. All depths. iPhi (0 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
           )

hcallayout(dqmitems, "HCAL DataFormat Problems",
           [{ 'path': "Hcal/DataFormatMonitor/ HardwareWatchCells",
              'description': "A Data Format error indicates that the data received from this channel was somehow corrupted or compromised.  This plot is the sum of bad digis over all depths. iPhi (0 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
                                 )

hcallayout(dqmitems, "HCAL Unsuppressed Channels",
           [{ 'path': "Hcal/DataFormatMonitor/HTR Plots/Fraction UnSuppressed Events",
              'description': "This shows the fraction of unsuppressed events for each FED and SPIGOT. More (eventually)  at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
                      )
