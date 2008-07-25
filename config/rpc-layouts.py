  def rpclayout(i, p, *rows): i["RPC/Layouts/" + p] = DQMItem(layout=rows)

rpclayout(dqmitems, "RPC_Summary",
  ["RPC/RecHits/SummaryHistograms/NumberOfClusters_for_Barrel",
  "RPC/RecHits/SummaryHistograms/NumberOfDigi_for_Barrel",
  "RPC/RecHits/SummaryHistograms/SameBXDigis"],

  ["RPC/RecHits/SummaryHistograms/ClusterSize_for_Barrel",
  "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_0",
  "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_1",
  "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_2"])

rpclayout(dqmitems, "RPC Cluster size by Wheels",
  ["RPC/RecHits/SummaryHistograms/ClusterSize_for_Wheel_0",
  "RPC/RecHits/SummaryHistograms/ClusterSize_for_Wheel_1",
  "RPC/RecHits/SummaryHistograms/ClusterSize_for_Wheel_2"])

rpclayout(dqmitems, "SectorOccupancy_WWheel_2",
  ["RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_1",
  "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_2",
  "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_3"],

  ["RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_4",
  "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_5",
  "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_6"],

  ["RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_7",
  "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_8",
  "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_9"],

  ["RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_10",
  "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_11",
  "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_12"])

rpclayout(dqmitems, "SectorOccupancy_WWheel_1",
  ["RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_1",
  "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_2",
  "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_3"],

  ["RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_4",
  "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_5",
  "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_6"],

  ["RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_7",
  "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_8",
  "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_9"],

  ["RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_10",
  "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_11",
  "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_12"])


rpclayout(dqmitems, "SectorOccupancy_WWheel_0",
  ["RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_1",
  "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_2",
  "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_3"],

  ["RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_4",
  "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_5",
  "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_6"],

  ["RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_7",
  "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_8",
  "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_9"],

  ["RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_10",
  "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_11",
  "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_12"])

rpclayout(dqmitems, "SectorOccupancy_WWheel_-1",
  ["RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_1",
  "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_2",
  "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_3"],

  ["RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_4",
  "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_5",
  "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_6"],

  ["RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_7",
  "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_8",
  "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_9"],

  ["RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_10",
  "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_11",
  "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_12"])

rpclayout(dqmitems, "SectorOccupancy_WWheel_-2",
  ["RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_1",
  "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_2",
  "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_3"],

  ["RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_4",
  "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_5",
  "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_6"],

  ["RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_7",
  "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_8",
  "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_9"],

  ["RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_10",
  "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_11",
  "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_12"])
