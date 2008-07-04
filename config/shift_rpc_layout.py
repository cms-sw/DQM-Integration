def shiftrpclayout(i, p, *rows): i["00 Shift/RPC/" + p] = DQMItem(layout=rows)

shiftrpclayout(dqmitems, "00-BarrelOccupancy",
  [{ 'path': "RPC/RecHits/SummaryHistograms/BarrelOccupancy", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>" }])

shiftrpclayout(dqmitems, "01-BarrelClusterSize",
  [{ 'path': "RPC/RECHits/SummaryHistograms/ClusterSize_for_Barrel" , 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>" }])

shiftrpclayout(dqmitems, "02-BarrelNumberOfDigis",
  [{ 'path': "RPC/RecHits/SummaryHistograms/NumberOfDigi_for_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>" }])

shiftrpclayout(dqmitems, "Wheel_+2_Occupancy",
  [{ 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>" }])

shiftrpclayout(dqmitems, "Wheel_+1_Occupancy",
  [{ 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>" }])

shiftrpclayout(dqmitems, "Wheel_0_Occupancy",
  [{ 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_0", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>" }])


shiftrpclayout(dqmitems, "Wheel_-1_Occupancy",
  [{ 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_-1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>" }])

shiftrpclayout(dqmitems, "Wheel_-2_Occupancy",
  [{ 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_-2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>" }])
