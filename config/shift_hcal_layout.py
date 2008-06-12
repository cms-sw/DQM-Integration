def shiftHcalLayout(i, p, *rows): i["00 Shift/Hcal/" + p] = DQMItem(layout=rows)


shiftHcalLayout(dqmitems,"Shifter Hcal Summary",
          [{ 'path': "Hcal/DataFormatMonitor/Number of Event Fragments by FED ID",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
           { 'path': "Hcal/DataFormatMonitor/Common Data Format violations",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
          [{ 'path': "Hcal/DataFormatMonitor/DCC Event Format violation",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
           { 'path': "Hcal/DataFormatMonitor/EvN Inconsistent - HTR vs Ref HTR",
                   'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]           
           )

