def rpclayout(i, p, *rows): i["RPC/Layouts/" + p] = DQMItem(layout=rows)

rpclayout(dqmitems, "RPC_Summary",
  ["RPC/RecHits/SummaryHistograms/NumberOfClusters_for_Barrel",
   "RPC/RecHits/SummaryHistograms/NumberOfDigi_for_Barrel",
   "RPC/RecHits/SummaryHistograms/SameBXDigis"],

  ["RPC/RecHits/SummaryHistograms/ClusterSize_for_Barrel",
   "RPC/REcHits/SummaryHistograms/Wheel1DOccupancy_Wheel_0_0",
   "RPC/REcHits/SummaryHistograms/Wheel1DOccupancy_Wheel_0_1",
   "RPC/REcHits/SummaryHistograms/Wheel1DOccupancy_Wheel_0_2"])

rpclayout(dqmitems, "RPC Cluster size by Wheels")   
   "RPC/RecHits/SummaryHistograms/ClusterSize_for_Wheel_0_0",
   "RPC/RecHits/SummaryHistograms/ClusterSize_for_Wheel_0_1",
   "RPC/RecHits/SummaryHistograms/ClusterSize_for_Wheel_0_2"])

rpclayout(dqmitems, "SectorOccupancy_W1_W0",
  ["RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_0_Sector_1",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_0_Sector_2",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_0_Sector_3",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_0_Sector_10",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_0_Sector_11",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_0_Sector_12"],

  ["RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_1_Sector_1",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_1_Sector_2",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_1_Sector_3",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_1_Sector_10",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_1_Sector_11",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_1_Sector_12"])

rpclayout(dqmitems, "SectorOccupancy_W2",
  ["RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_2_Sector_10",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_2_Sector_11",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_2_Sector_12",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_2_Sector_1",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_2_Sector_2",
   "RPC/RecHits/SummaryHistograms/SectorOccupancy_Wheel_2_Sector_3"])

