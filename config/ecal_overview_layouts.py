def ecaloverviewlayout(i, p, *rows): i["Collisions/EcalFeedBack/" + p] = DQMItem(layout=rows)

ecaloverviewlayout(dqmitems, "00 Occupancy EB",
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>" }],
  [{ 'path': "EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy projection eta", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy projection phi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } }])

ecaloverviewlayout(dqmitems, "01 Occupancy EE -",
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE -", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>" }],
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE - projection R", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE - projection phi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } }])

ecaloverviewlayout(dqmitems, "02 Occupancy EE +",
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE +", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>" }],
  [{ 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE + projection R", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE + projection phi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } }])

ecaloverviewlayout(dqmitems, "03 Timing RMS EB",
  [{ 'path': "EcalBarrel/EBSummaryClient/EBTMT timing rms 1D summary", 'description': "Average timing RMS along the run of all the channels in EB. Timing RMS is expected < 0.5 clocks. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } }],
  [{ 'path': "EcalBarrel/EBSummaryClient/EBTMT timing rms", 'description': "Average timing RMS along the run of all the channels in each DCC of EB. The error bar represents the spreads among the crystal of each DCC. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } }])

ecaloverviewlayout(dqmitems, "04 Timing Mean EB",
  [{ 'path': "EcalBarrel/EBSummaryClient/EBTMT timing mean 1D summary", 'description': "Mean timing of all the channels in EB along the run. Timing is expected within 5.5 - 6.5 clocks. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } }],
  [{ 'path': "EcalBarrel/EBSummaryClient/EBTMT timing mean", 'description': "Mean timing of all the channels in each DCC of EB along the run. Timing is expected within 5.5 - 6.5 clocks. The error bar represents the spreads among the crystal of each DCC. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } }])

ecaloverviewlayout(dqmitems, "05 Timing/02 Timing RMS EE",
  [{ 'path': "EcalEndcap/EESummaryClient/EETMT EE - timing rms 1D summary", 'description': "Timing RMS of all the channels in EE -. Timing RMS is expected < 0.5 clocks. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EESummaryClient/EETMT EE + timing rms 1D summary", 'description': "Timing RMS of all the channels in EE +. Timing RMS is expected < 0.5 clocks. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } }],
  [{ 'path': "EcalEndcap/EESummaryClient/EETMT timing rms", 'description': "Timing RMS of all the channels in each DCC of EE. The error bar represents the spreads among the crystal of each DCC. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } }])

ecaloverviewlayout(dqmitems, "06 Timing Mean EE",
  [{ 'path': "EcalEndcap/EESummaryClient/EETMT EE - timing mean 1D summary", 'description': "Mean timing of all the channels in EE -. Timing is expected within 5.5 - 6.5 clocks. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EESummaryClient/EETMT EE + timing mean 1D summary", 'description': "Mean timing of all the channels in EE +. Timing is expected within 5.5 - 6.5 clocks. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } }],
  [{ 'path': "EcalEndcap/EESummaryClient/EETMT timing mean", 'description': "Mean timing of all the channels in each DCC of EE. Timing is expected within 5.5 - 6.5 clocks. The error bar represents the spreads among the crystal of each DCC. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } }])

ecaloverviewlayout(dqmitems, "07 Single Event Timing EE",
  [{ 'path': "EcalEndcap/EETimingTask/EETMT timing 1D summary EE -", 'description': "Single event timing (in clock units) of the good rechits (good shape and amplitude > 500 MeV). Expected about 5.5 clocks. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } },
   { 'path': "EcalEndcap/EETimingTask/EETMT timing 1D summary EE +", 'description': "Single event timing (in clock units) of the good rechits (good shape and amplitude > 500 MeV). Expected about 5.5 clocks. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } }],
  [{ 'path': "EcalEndcap/EETimingTask/EETMT timing EE+ - EE-", 'description': "Event by event difference between the average timing in EE+ and EE- (in clock units) of the good rechits (good shape and amplitude > 500 MeV). Expected 0. <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftEcalExpert>DQMShiftEcalExpert</a>", 'draw': { 'withref': "yes" } }])

