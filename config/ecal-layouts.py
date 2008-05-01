def ecallayout(i, p, *rows): i["Ecal/Layouts/" + p] = DQMItem(layout=rows)

ecallayout(dqmitems, "00-Global-Summary",
  [None,
   { 'path': "EcalEndcap/EESummaryClient/EE global summary EE +", 'description': "EcalEndcap (z>0) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" },
   None],
  [{ 'path': "EcalBarrel/EBSummaryClient/EB global summary", 'description': "EcalBarrel - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" }],
  [None,
   { 'path': "EcalEndcap/EESummaryClient/EE global summary EE -", 'description': "EcalEndcap (z<0) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" },
   None])

