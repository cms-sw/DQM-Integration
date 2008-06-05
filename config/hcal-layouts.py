def hcallayout(i, p, *rows): i["Hcal/Layouts/" + p] = DQMItem(layout=rows)

hcallayout(dqmitems, "HCAL OverView",
           [{ 'path': "Hcal/PedestalMonitor/HB/HB Subtracted Mean Values",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
            { 'path': "Hcal/PedestalMonitor/HE/HE Subtracted Mean Values",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
            { 'path': "Hcal/PedestalMonitor/HO/HO Subtracted Mean Values",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
            { 'path': "Hcal/PedestalMonitor/HF/HF Subtracted Mean Values",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
          [{ 'path': "Hcal/DigiMonitor/Digi Depth 1 Occupancy Map",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
           { 'path': "Hcal/DigiMonitor/Digi Depth 2 Occupancy Map",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
           { 'path': "Hcal/DigiMonitor/Digi Depth 3 Occupancy Map",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
           { 'path': "Hcal/DigiMonitor/Digi Depth 4 Occupancy Map",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
          [{ 'path': "Hcal/HotCellMonitor/HCAL/HCALProblemHotCells",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
           { 'path': "Hcal/DataFormatMonitor/Ev Frag Size 2d",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
           { 'path': "Hcal/DataFormatMonitor/EvN Inconsistent - HTR vs Ref HTR",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]           
           )

