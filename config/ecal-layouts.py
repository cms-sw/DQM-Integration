def ecallayout(i, p, *rows): i["Ecal/Layouts/" + p] = DQMItem(layout=rows)
def ecalbarrellayout(i, p, *rows): i["EcalBarrel/Layouts/" + p] = DQMItem(layout=rows)
def ecalendcaplayout(i, p, *rows): i["EcalEndcap/Layouts/" + p] = DQMItem(layout=rows)

ecallayout(dqmitems, "00-Global-Summary",
  [None,
   { 'path': "EcalEndcap/EESummaryClient/EE global summary EE +", 'description': "EcalEndcap (z>0) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" },
   None],
  [{ 'path': "EcalBarrel/EBSummaryClient/EB global summary", 'description': "EcalBarrel - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" }],
  [None,
   { 'path': "EcalEndcap/EESummaryClient/EE global summary EE -", 'description': "EcalEndcap (z<0) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" },
   None])

ecallayout(dqmitems, "01-Occupancy-Summary",
  [None,
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE +", 'description': "EcalEndcap (z>0) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" },
   None],
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy", 'description': "EcalBarrel - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" }],
  [None,
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE -", 'description': "EcalEndcap (z<0) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" },
   None])

ecallayout(dqmitems, "02-Cluster-Summary",
  [None,
   { 'path': "EcalEndcap/EEClusterTask/EECLT BC energy map EE +", 'description': "EcalEndcap (z>0) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" },
   None],
  [{ 'path': "EcalBarrel/EBClusterTask/EBCLT BC energy map", 'description': "EcalBarrel - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" }],
  [None,
   { 'path': "EcalEndcap/EEClusterTask/EECLT BC energy map EE -", 'description': "EcalEndcap (z<0) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" },
   None])

# EcalBarrel
ecalbarrellayout(dqmitems, "00-Global-Summary-EcalBarrel",
  [{ 'path': "EcalBarrel/EBSummaryClient/EB global summary", 'description': "EcalBarrel - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" }])

ecalbarrellayout(dqmitems, "01-Occupancy-Summary-EcalBarrel",
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy", 'description': "EcalBarrel - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" }])

ecalbarrellayout(dqmitems, "02-Cluster-Summary-EcalBarrel",
  [{ 'path': "EcalBarrel/EBClusterTask/EBCLT BC energy map", 'description': "EcalBarrel - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" }])


# EcalEndcap
ecalendcaplayout(dqmitems, "00-Global-Summary-EcalEndcap",
  [{ 'path': "EcalEndcap/EESummaryClient/EE global summary EE +", 'description': "EcalEndcap (z>0) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" },
   { 'path': "EcalEndcap/EESummaryClient/EE global summary EE -", 'description': "EcalEndcap (z<0) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" }])

ecalendcaplayout(dqmitems, "01-Occupancy-Summary-EcalEndcap",
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE +", 'description': "EcalEndcap (z>0) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" },
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE -", 'description': "EcalEndcap (z<0) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" }])

ecalendcaplayout(dqmitems, "02-Cluster-Summary-EcalEndcap",
  [{ 'path': "EcalEndcap/EEClusterTask/EECLT BC energy map EE +", 'description': "EcalEndcap (z>0) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" },
   { 'path': "EcalEndcap/EEClusterTask/EECLT BC energy map EE -", 'description': "EcalEndcap (z<0) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/EcalDQM>EcalDQM</a>" }])

