def rpclayout(i, p, *rows): i["RPC/Layouts/" + p] = DQMItem(layout=rows)

rpclayout(dqmitems, "RPC_Summary",
  ["RPC/RecHits/SumarryHistograms/NumberOfClusters_for_Barrel",
   "RPC/RecHits/SumarryHistograms/NumberOfDigi_for_Barrel",
   "RPC/RecHits/SumarryHistograms/SameBXDigis"],

  ["RPC/RecHits/SummaryHistograms/ClusterSize_for_Barrel",
   "RPC/RecHits/SumarryHistograms/ClusterSize_for_Wheel_0_2",
   "RPC/RecHits/SumarryHistograms/ClusterSize_for_Wheel_0_1",
   "RPC/RecHits/SumarryHistograms/ClusterSize_for_Wheel_0_0"])

rpclayout(dqmitems, "SectorOccubancy_W1_W0",
  ["RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_0_Sector_1",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_0_Sector_2",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_0_Sector_3",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_0_Sector_10",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_0_Sector_11",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_0_Sector_12"],

  ["RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_1_Sector_1",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_1_Sector_2",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_1_Sector_3",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_1_Sector_10",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_1_Sector_11",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_1_Sector_12"])

rpclayout(dqmitems, "SectorOccubancy_W2",
  ["RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_2_Sector_10",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_2_Sector_11",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_2_Sector_12",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_2_Sector_1",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_2_Sector_2",
   "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_2_Sector_3"])

