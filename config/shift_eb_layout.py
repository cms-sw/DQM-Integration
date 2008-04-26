def shiftebayout(i, p, *rows): i["Shift/EcalBarrel/" + p] = DQMItem(layout=rows)

shiftebayout(dqmitems, "01-Integrity",
  [{ 'path': "EcalBarrel/EBSummaryClient/EBIT integrity quality summary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shiftebayout(dqmitems, "02-PedestalOnline",
  [{ 'path': "EcalBarrel/EBSummaryClient/EBPOT pedestal quality summary G12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shiftebayout(dqmitems, "03-DCCOccupancy",
  [{ 'path': "EcalBarrel/EcalInfo/EBMM DCC", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shiftebayout(dqmitems, "04-DigiOccupancy",
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT digi occupancy", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT digi occupancy projection eta", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" },
   { 'path': "EcalBarrel/EBOccupancyTask/EBOT digi occupancy projection phi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shiftebayout(dqmitems, "05-RecHitOccupancy",
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy projection eta", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" },
   { 'path': "EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy projection phi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shiftebayout(dqmitems, "06-TPDigisOccupancy",
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT TP digi occupancy", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT TP digi occupancy projection eta", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" },
   { 'path': "EcalBarrel/EBOccupancyTask/EBOT TP digi occupancy projection phi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shiftebayout(dqmitems, "07-RecHitAndTPGProfiles",
  [{ 'path': "EcalBarrel/EcalInfo/EBMM hit number profile", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalBarrel/EcalInfo/EBMM TP digi number profile", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shiftebayout(dqmitems, "08-Cosmics",
  [{ 'path': "EcalBarrel/EBSummaryClient/EBCT cosmic summary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shiftebayout(dqmitems, "09-Timing",
  [{ 'path': "EcalBarrel/EBSummaryClient/EBTMT timing quality summary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shiftebayout(dqmitems, "10-ClustersEnergy",
  [{ 'path': "EcalBarrel/EBClusterTask/EBCLT BC energy map", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalBarrel/EBClusterTask/EBCLT BC energy projection eta", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" },
   { 'path': "EcalBarrel/EBClusterTask/EBCLT BC energy projection phi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shiftebayout(dqmitems, "11-ClustersOccupancy",
  [{ 'path': "EcalBarrel/EBClusterTask/EBCLT BC number map", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalBarrel/EBClusterTask/EBCLT BC size map", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shiftebayout(dqmitems, "12-Laser",
  [{ 'path': "EcalBarrel/EBSummaryClient/EBLT laser quality summary L1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

