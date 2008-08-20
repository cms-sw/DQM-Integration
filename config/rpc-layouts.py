
def rpclayout(i, p, *rows): i["RPC/Layouts/" + p] = DQMItem(layout=rows)


rpclayout(dqmitems, "RPC_BarrelOccupancy",
          [{ 'path': "RPC/RecHits/SummaryHistograms/BarrelOccupancy", 'description': "BarrelOccupancy   >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>" }])


rpclayout(dqmitems, "RPC_Summary",
   [{ 'path': "RPC/RecHits/SummaryHistograms/NumberOfClusters_for_Barrel", 'description': "NumberOfClusters_for_Barrel >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    {'path': "RPC/RecHits/SummaryHistograms/NumberOfDigi_for_Barrel", 'description': "NumberOfDigi_for_Barrel >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
    [{'path': "RPC/RecHits/SummaryHistograms/SameBXDigis", 'description': "SameBXDigis >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/SummaryHistograms/ClusterSize_for_Barrel", 'description': "ClusterSize_for_Barrel >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}])

rpclayout(dqmitems, "RPC_Wheel_Occupancy",
    [{'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_2", 'description': "1DOccupancy_Wheel_2  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    {'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_1", 'description': "1DOccupancy_Wheel_1  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
          
 [{'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_0", 'description': "1DOccupancy_Wheel_0  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
  {'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_-1", 'description': "1DOccupancy_Wheel_-1  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
  {'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_-2", 'description': "1DOccupancy_Wheel_-2  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}])

rpclayout(dqmitems, "RPC_ClusterSize_by_Wheels",
  [ { 'path': "RPC/RecHits/SummaryHistograms/ClusterSize_Wheel_2", 'description': "ClusterSize_Wheel_2  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    { 'path': "RPC/RecHits/SummaryHistograms/ClusterSize_Wheel_1", 'description': "ClusterSize_Wheel_1  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
         
  [ { 'path': "RPC/RecHits/SummaryHistograms/ClusterSize_Wheel_0", 'description': "ClusterSize_Wheel_0  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    { 'path': "RPC/RecHits/SummaryHistograms/ClusterSize_Wheel_-1", 'description': " ClusterSize_Wheel_-1 >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    { 'path': "RPC/RecHits/SummaryHistograms/ClusterSize_Wheel_-2", 'description': "ClusterSize_Wheel_-2  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}])     
          
rpclayout(dqmitems, "SectorOccupancy_Wheel_2",
   [{'path': "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_1", 'description': "Occupancy_Wheel_2_Sector_1  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    {'path': "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_2", 'description': " Occupancy_Wheel_2_Sector_2 >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    {'path': "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_3", 'description': "Occupancy_Wheel_2_Sector_3  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
          
   [{'path': "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_4", 'description': "Occupancy_Wheel_2_Sector_4  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    {'path': "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_5", 'description': "Occupancy_Wheel_2_Sector_5  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    {'path': "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_6", 'description': "Occupancy_Wheel_2_Sector_6  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
          
   [{'path': "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_7", 'description': "Occupancy_Wheel_2_Sector_7  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    {'path': "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_8", 'description': "Occupancy_Wheel_2_Sector_8  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    {'path': "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_9", 'description': "Occupancy_Wheel_2_Sector_9  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
          
  [ {'path': "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_10", 'description': "Occupancy_Wheel_2_Sector_10  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    { 'path': "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_11", 'description': "Occupancy_Wheel_2_Sector_11  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    { 'path': "RPC/RecHits/Barrel/Wheel_2/SummaryBySectors/Occupancy_Wheel_2_Sector_12", 'description': " Occupancy_Wheel_2_Sector_12 >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}])

rpclayout(dqmitems, "SectorOccupancy_Wheel_1",
   [ { 'path': "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_1", 'description': "Occupancy_Wheel_1_Sector_1  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_2", 'description': "Occupancy_Wheel_1_Sector_2  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_3", 'description': "Occupancy_Wheel_1_Sector_3  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
   
   [ { 'path': "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_4", 'description': "Occupancy_Wheel_1_Sector_4  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    { 'path': "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_5", 'description': "Occupancy_Wheel_1_Sector_5  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_6", 'description': "Occupancy_Wheel_1_Sector_6  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
          
    [ { 'path': "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_7", 'description': "Occupancy_Wheel_1_Sector_7  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_8", 'description': "Occupancy_Wheel_1_Sector_8  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_9", 'description': "Occupancy_Wheel_1_Sector_9  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
          
   [ { 'path': "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_10", 'description': "Occupancy_Wheel_1_Sector_10  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
      { 'path': "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_11", 'description': "Occupancy_Wheel_1_Sector_11  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
      { 'path': "RPC/RecHits/Barrel/Wheel_1/SummaryBySectors/Occupancy_Wheel_1_Sector_12", 'description': "Occupancy_Wheel_1_Sector_12  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}])


rpclayout(dqmitems, "SectorOccupancy_Wheel_0",
   [ { 'path': "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_1", 'description': "SummaryBySectors/Occupancy_Wheel_0_Sector_1  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_2", 'description': "SummaryBySectors/Occupancy_Wheel_0_Sector_2  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_3", 'description': "SummaryBySectors/Occupancy_Wheel_0_Sector_3  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
          
   [ { 'path': "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_4", 'description': "SummaryBySectors/Occupancy_Wheel_0_Sector_4  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_5", 'description': "SummaryBySectors/Occupancy_Wheel_0_Sector_5  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_6", 'description': "SummaryBySectors/Occupancy_Wheel_0_Sector_6  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
          
   [ { 'path': "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_7", 'description': "SummaryBySectors/Occupancy_Wheel_0_Sector_7  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_8", 'description': "SummaryBySectors/Occupancy_Wheel_0_Sector_8  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_9", 'description': "SummaryBySectors/Occupancy_Wheel_0_Sector_9  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
          
   [ { 'path': "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_10", 'description': "SummaryBySectors/Occupancy_Wheel_0_Sector_10  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_11", 'description': "SummaryBySectors/Occupancy_Wheel_0_Sector_11  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_0/SummaryBySectors/Occupancy_Wheel_0_Sector_12", 'description': "SummaryBySectors/Occupancy_Wheel_0_Sector_12  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}])

rpclayout(dqmitems, "SectorOccupancy_Wheel_-1",
   [ { 'path': "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_1", 'description': "Occupancy_Wheel_-1_Sector_1  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_2", 'description': "Occupancy_Wheel_-1_Sector_2  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_3", 'description': "Occupancy_Wheel_-1_Sector_3  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],

   [ { 'path': "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_4", 'description': "Occupancy_Wheel_-1_Sector_4  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_5", 'description': "Occupancy_Wheel_-1_Sector_5  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_6", 'description': "Occupancy_Wheel_-1_Sector_6  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
          
   [ { 'path': "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_7", 'description': "Occupancy_Wheel_-1_Sector_7  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_8", 'description': "Occupancy_Wheel_-1_Sector_8  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_9", 'description': " Occupancy_Wheel_-1_Sector_9 >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
          
   [ { 'path': "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_10", 'description': "Occupancy_Wheel_-1_Sector_10  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_11", 'description': "Occupancy_Wheel_-1_Sector_11  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_-1/SummaryBySectors/Occupancy_Wheel_-1_Sector_12", 'description': "Occupancy_Wheel_-1_Sector_12  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}])

rpclayout(dqmitems, "SectorOccupancy_Wheel_-2",
  [ { 'path': "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_1", 'description': "Occupancy_Wheel_-2_Sector_1  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
   { 'path': "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_2", 'description': "Occupancy_Wheel_-2_Sector_2  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
    { 'path': "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_3", 'description': "Occupancy_Wheel_-2_Sector_3  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
          
   [ { 'path': "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_4", 'description': "Occupancy_Wheel_-2_Sector_4  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_5", 'description': "Occupancy_Wheel_-2_Sector_5  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_6", 'description': "Occupancy_Wheel_-2_Sector_6  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
          
   [ { 'path': "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_7", 'description': "Occupancy_Wheel_-2_Sector_7  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_8", 'description': "Occupancy_Wheel_-2_Sector_8  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_9", 'description': "Occupancy_Wheel_-2_Sector_9  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}],
          
   [ { 'path': "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_10", 'description': "Occupancy_Wheel_-2_Sector_10  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_11", 'description': "Occupancy_Wheel_-2_Sector_11  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"},
     { 'path': "RPC/RecHits/Barrel/Wheel_-2/SummaryBySectors/Occupancy_Wheel_-2_Sector_12", 'description': "Occupancy_Wheel_-2_Sector_12  >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Click here to see Description</a>"}])
