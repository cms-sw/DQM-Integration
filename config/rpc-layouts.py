def rpclayout(i, p, *rows): i["RPC/Layouts/" + p] = DQMItem(layout=rows)

rpclayout(dqmitems, "RPC_Summary",
  ["RPC/RecHits/SumarryHistograms/NumberOfClusters_for_Barrel",
   "RPC/RecHits/SumarryHistograms/NumberOfDigi_for_Barrel",
   "RPC/RecHits/SumarryHistograms/SameBXDigis"],

  ["RPC/RecHits/SummaryHistograms/ClusterSize_for_Barrel",
   "RPC/RecHits/SumarryHistograms/ClusterSize_for_Wheel_0_2",
   "RPC/RecHits/SumarryHistograms/ClusterSize_for_Wheel_0_1",
   "RPC/RecHits/SumarryHistograms/ClusterSize_for_Wheel_0_0"])
