def shifteblayout(i, p, *rows): i["Shift/EcalBarrel/" + p] = DQMItem(layout=rows)

shifteblayout(dqmitems, "01-Integrity",
  [{ 'path': "EcalBarrel/EBSummaryClient/EBIT integrity quality summary", 'description': "Quality map: checks that data follows all the formatting rules and all the constraints which are dictated by the design of the electronics - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteblayout(dqmitems, "02-PedestalOnline",
  [{ 'path': "EcalBarrel/EBSummaryClient/EBPOT pedestal quality summary G12", 'description': "Quality map: checks that the first 3 samples of the pulse shape are consistent with pedestal (mean and RMS of the pedestal distribution) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteblayout(dqmitems, "03-DCCOccupancy",
  [{ 'path': "EcalBarrel/EcalInfo/EBMM DCC", 'description': "1D distribution showing the occupancy of each DCC (= SM) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteblayout(dqmitems, "04-DigiOccupancy",
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT digi occupancy", 'description': "2D digis occupancy map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT digi occupancy projection eta", 'description': "eta projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" },
   { 'path': "EcalBarrel/EBOccupancyTask/EBOT digi occupancy projection phi", 'description': "phi projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteblayout(dqmitems, "05-RecHitOccupancy",
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy", 'description': "2D rec hits occupancy map of calibrated rechit with energy > 1 GeV - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy projection eta", 'description': "eta projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" },
   { 'path': "EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy projection phi", 'description': "phi projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteblayout(dqmitems, "06-TPDigisOccupancy",
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT TP digi occupancy", 'description': "2D TP digis occupancy map of the reconstructed TPG digis with energy > 5 GeV - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT TP digi occupancy projection eta", 'description': "eta projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" },
   { 'path': "EcalBarrel/EBOccupancyTask/EBOT TP digi occupancy projection phi", 'description': "phi projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteblayout(dqmitems, "07-RecHitAndTPProfiles",
  [{ 'path': "EcalBarrel/EcalInfo/EBMM hit number profile", 'description': "1D profile histogram of the rec hits occupancy: crystal number (y-axis) vs DCC number (x-axis) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalBarrel/EcalInfo/EBMM TP digi number profile", 'description': "1D profile histogram of the trigger primitives digis occupancy: trigger tower number (y-axis) vs DCC number - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteblayout(dqmitems, "08-Cosmics",
  [{ 'path': "EcalBarrel/EBSummaryClient/EBCT cosmic summary", 'description': "2D map of 3x3 matrices with E3x3>125 MeV (~1/2 of the average MIP deposit) around seeds, where seeds are made from all the channels exceeding 7 ADC counts with the time of the peak inside the interval 4-7.5 (clocks) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteblayout(dqmitems, "09-Timing",
  [{ 'path': "EcalBarrel/EBSummaryClient/EBTMT timing quality summary", 'description': "Quality map showing the agreement of the expected peak of the pulse shape and its RMS around the expected values - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteblayout(dqmitems, "10-ClustersEnergy",
  [{ 'path': "EcalBarrel/EBClusterTask/EBCLT BC energy map", 'description': "2D map of the reconstructed Basic Clusters energy - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalBarrel/EBClusterTask/EBCLT BC energy projection eta", 'description': "eta projection of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" },
   { 'path': "EcalBarrel/EBClusterTask/EBCLT BC energy projection phi", 'description': "phi projection of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteblayout(dqmitems, "11-ClustersOccupancy",
  [{ 'path': "EcalBarrel/EBClusterTask/EBCLT BC number map", 'description': "2D map of basic cluster number (occupancy in terms of clusters) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalBarrel/EBClusterTask/EBCLT BC size map", 'description': "2D map of basic clusters size (number of crystals composing each cluster) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteblayout(dqmitems, "12-Laser",
  [{ 'path': "EcalBarrel/EBSummaryClient/EBLT laser quality summary L1", 'description': "Quality map for laser events: checks the mean amplitude and RMS of the light pulses - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

