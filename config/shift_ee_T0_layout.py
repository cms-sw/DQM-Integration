def shifteelayout(i, p, *rows): i["00 Shift/EcalEndcap/" + p] = DQMItem(layout=rows)

shifteelayout(dqmitems, "01-Integrity",
  [{ 'path': "EcalEndcap/EESummaryClient/EEIT EE - integrity quality summary", 'description': "Quality map: checks that data follows all the formatting rules and all the constraints which are dictated by the design of the electronics - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EESummaryClient/EEIT EE + integrity quality summary", 'description': "Quality map: checks that data follows all the formatting rules and all the constraints which are dictated by the design of the electronics - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteelayout(dqmitems, "02-PedestalOnline",
  [{ 'path': "EcalEndcap/EESummaryClient/EEPOT EE - pedestal quality summary G12", 'description': "Quality map: checks that the first 3 samples of the pulse shape are consistent with pedestal (mean and RMS of the pedestal distribution) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EESummaryClient/EEPOT EE + pedestal quality summary G12", 'description': "Quality map: checks that the first 3 samples of the pulse shape are consistent with pedestal (mean and RMS of the pedestal distribution) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteelayout(dqmitems, "03-DCCOccupancy",
  [{ 'path': "EcalEndcap/EcalInfo/EEMM DCC", 'description': "1D profile histogram showing the DCC occupancy: number of events (y-axis) vs DCC number (x-axis) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }],
  [{ 'path': "EcalEndcap/EcalInfo/EEMM digi number profile", 'description': "1D profile histogram of the digis occupancy: number of crystals (y-axis) vs DCC number (x-axis) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "04-DigiOccupancy",
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -", 'description': "2D digis occupancy map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE - projection R", 'description': "R projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE - projection phi", 'description': "phi projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "05-DigiOccupancy",
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +", 'description': "2D digis occupancy map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE + projection R", 'description': "R projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE + projection phi", 'description': "phi projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "06-RecHitOccupancy",
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE -", 'description': "2D rec hits occupancy map of calibrated rechit with energy > 1 GeV - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE - projection R", 'description': "R projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE - projection phi", 'description': "phi projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "07-RecHitOccupancy",
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE +", 'description': "2D rec hits occupancy map of calibrated rechit with energy > 1 GeV - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE + projection R", 'description': "R projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE + projection phi", 'description': "phi projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "08-TPDigisOccupancy",
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT TP digi occupancy EE -", 'description': "2D TP digis occupancy map of the reconstructed TPG digis with energy > 5 GeV - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT TP digi occupancy EE - projection R", 'description': "R projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT TP digi occupancy EE - projection phi", 'description': "phi projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "09-TPDigisOccupancy",
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT TP digi occupancy EE +", 'description': "2D TP digis occupancy map of the reconstructed TPG digis with energy > 5 GeV - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT TP digi occupancy EE + projection R", 'description': "R projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT TP digi occupancy EE + projection phi", 'description': "phi projections of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "10-RecHitAndTPProfiles",
  [{ 'path': "EcalEndcap/EcalInfo/EEMM hit number profile", 'description': "1D profile histogram of the rec hits occupancy: number of crystals (y-axis) vs DCC number (x-axis) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }],
  [{ 'path': "EcalEndcap/EcalInfo/EEMM TP digi number profile", 'description': "1D profile histogram of the trigger primitives digis occupancy: number of trigger primitives (y-axis) vs DCC number (x-axis) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "11-Cosmics",
  [{ 'path': "EcalEndcap/EESummaryClient/EECT EE - cosmic summary", 'description': "2D map of 3x3 matrices with E3x3>125 MeV (~1/2 of the average MIP deposit) around seeds, where seeds are made from all the channels exceeding 7 ADC counts with the time of the peak inside the interval 4-7.5 (clocks) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EESummaryClient/EECT EE + cosmic summary", 'description': "2D map of 3x3 matrices with E3x3>125 MeV (~1/2 of the average MIP deposit) around seeds, where seeds are made from all the channels exceeding 7 ADC counts with the time of the peak inside the interval 4-7.5 (clocks) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteelayout(dqmitems, "12-Timing",
  [{ 'path': "EcalEndcap/EESummaryClient/EETMT EE - timing quality summary", 'description': "Quality map showing the agreement of the expected peak of the pulse shape and its RMS around the expected values - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EESummaryClient/EETMT EE + timing quality summary", 'description': "Quality map showing the agreement of the expected peak of the pulse shape and its RMS around the expected values - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteelayout(dqmitems, "13-ClustersEnergy",
  [{ 'path': "EcalEndcap/EEClusterTask/EECLT BC energy map EE -", 'description': "2D map of the reconstructed Basic Clusters energy - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEClusterTask/EECLT BC energy projection R EE -", 'description': "R projection of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEClusterTask/EECLT BC energy projection phi EE -", 'description': "phi projection of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "14-ClustersEnergy",
  [{ 'path': "EcalEndcap/EEClusterTask/EECLT BC energy map EE +", 'description': "2D map of the reconstructed Basic Clusters energy - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEClusterTask/EECLT BC energy projection R EE +", 'description': "R projection of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEClusterTask/EECLT BC energy projection phi EE +", 'description': "phi projection of the 2D map - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>", 'draw': { 'withref': "yes" } }])

shifteelayout(dqmitems, "15-ClustersOccupancy",
  [{ 'path': "EcalEndcap/EEClusterTask/EECLT BC number map EE -", 'description': "2D map of basic cluster number (occupancy in terms of clusters) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEClusterTask/EECLT BC size map EE -", 'description': "2D map of basic clusters size (number of crystals composing each cluster) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

shifteelayout(dqmitems, "16-ClustersOccupancy",
  [{ 'path': "EcalEndcap/EEClusterTask/EECLT BC number map EE +", 'description': "2D map of basic cluster number (occupancy in terms of clusters) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
  [{ 'path': "EcalEndcap/EEClusterTask/EECLT BC size map EE +", 'description': "2D map of basic clusters size (number of crystals composing each cluster) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

#shifteelayout(dqmitems, "17-Laser",
#  [{ 'path': "EcalEndcap/EESummaryClient/EELT EE - laser quality summary L1", 'description': "Quality map for laser events: checks the mean amplitude and RMS of the light pulses - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
#  [{ 'path': "EcalEndcap/EESummaryClient/EELT EE + laser quality summary L1", 'description': "Quality map for laser events: checks the mean amplitude and RMS of the light pulses - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])
#
#shifteelayout(dqmitems, "18-Led",
#  [{ 'path': "EcalEndcap/EESummaryClient/EELT EE - laser quality summary L1", 'description': "Quality map for laser events: checks the mean amplitude and RMS of the light pulses - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
#  [{ 'path': "EcalEndcap/EESummaryClient/EELT EE + laser quality summary L1", 'description': "Quality map for laser events: checks the mean amplitude and RMS of the light pulses - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])
#
#shifteelayout(dqmitems, "19-Pedestal",
#  [{ 'path': "EcalEndcap/EESummaryClient/EEPT EE - pedestal quality summary", 'description': "Quality map for pedestal events: checks the mean and RMS of the pedestals - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
#  [{ 'path': "EcalEndcap/EESummaryClient/EEPT EE + pedestal quality summary", 'description': "Quality map for pedestal events: checks the mean and RMS of the pedestals - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])
#
#shifteelayout(dqmitems, "20-TestPulse",
#  [{ 'path': "EcalEndcap/EESummaryClient/EETPT EE - test pulse quality summary", 'description': "Quality map for test pulse events: checks the mean amplitude and RMS of the test pulses - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }],
#  [{ 'path': "EcalEndcap/EESummaryClient/EETPT EE + test pulse quality summary", 'description': "Quality map for test pulse events: checks the mean amplitude and RMS of the test pulses - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcal>DQMShiftEcal</a>" }])

