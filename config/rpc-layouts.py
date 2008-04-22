def rpclayout(i, p, *rows): i["Layouts/RPC Layouts/" + p] = DQMItem(layout=rows)



rpclayout(dqmitems, "RPC_Summary",

          ["RPC/RecHits/SumarryHistograms/WheelOccupancyXY_Wheel_0_0",
           "RPC/RecHits/SumarryHistograms/WheelOccupancyXY_Wheel_0_1",
           "RPC/RecHits/SumarryHistograms/WheelOccupancyXY_Wheel_0_2"],
          
          ["RPC/RecHits/SummaryHistograms/ClusterSize_for_Barrel",
           "RPC/RecHits/SumarryHistograms/ClusterSize_for_Wheel_0_2",
           "RPC/RecHits/SumarryHistograms/ClusterSize_for_Wheel_0_1",
           "RPC/RecHits/SumarryHistograms/ClusterSize_for_Wheel_0_0"])

rpclayout(dqmitems, "RPC_Barrel_Summary",

          ["RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_0_Sector_10",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_0_Sector_11",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_0_Sector_12",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_0_Sector_1",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_0_Sector_2",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_0_Sector_3"],
          
          ["RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_1_Sector_10",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_1_Sector_11",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_1_Sector_12",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_1_Sector_1",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_1_Sector_2",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_1_Sector_3"],
          
          
          ["RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_2_Sector_10",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_2_Sector_11",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_2_Sector_12",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_2_Sector_1",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_2_Sector_2",
           "RPC/RecHits/SumarryHistograms/SectorOccupancy_Wheel_2_Sector_3"])






rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_0/Sector_01",

          ["RPC/RecHits/Barrel/Wheel_0/station_1/sector_01/Occupancy_W+0_RB1in_S01_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_01/Occupancy_W+0_RB1in_S01_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_01/Occupancy_W+0_RBout_S01_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_01/Occupancy_W+0_RB1out_S01_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_0/station_2/sector_01/Occupancy_W+0_RB2in_S01_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_01/Occupancy_W+0_RB2in_S01_Middle",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_01/Occupancy_W+0_RB2in_S01_Backward",
           
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_01/Occupancy_W+0_RB2out_S01_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_01/Occupancy_W+0_RB2out_S01_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_0/station_3/sector_01/Occupancy_W+0_RB3_S01-_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_01/Occupancy_W+0_RB3_S01-_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_01/Occupancy_W+0_RB3_S01+_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_01/Occupancy_W+0_RB3_S01+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_0/station_4/sector_01/Occupancy_W+0_RB4_S01-_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_01/Occupancy_W+0_RB4_S01-_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_01/Occupancy_W+0_RB4_S01+_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_01/Occupancy_W+0_RB4_S01+_Backward"])
          
rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_0/Sector_02",

          ["RPC/RecHits/Barrel/Wheel_0/station_1/sector_02/Occupancy_W+0_RB1in_S02_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_02/Occupancy_W+0_RB1in_S02_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_02/Occupancy_W+0_RBout_S02_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_02/Occupancy_W+0_RB1out_S02_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_0/station_2/sector_02/Occupancy_W+0_RB2in_S02_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_02/Occupancy_W+0_RB2in_S02_Middle",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_02/Occupancy_W+0_RB2in_S02_Backward",
           
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_02/Occupancy_W+0_RB2out_S02_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_02/Occupancy_W+0_RB2out_S02_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_0/station_3/sector_02/Occupancy_W+0_RB3_S02-_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_02/Occupancy_W+0_RB3_S02-_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_02/Occupancy_W+0_RB3_S02+_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_02/Occupancy_W+0_RB3_S02+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_0/station_4/sector_02/Occupancy_W+0_RB4_S02-_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_02/Occupancy_W+0_RB4_S02-_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_02/Occupancy_W+0_RB4_S02+_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_02/Occupancy_W+0_RB4_S02+_Backward"])
                   
rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_0/Sector_03",

          ["RPC/RecHits/Barrel/Wheel_0/station_1/sector_03/Occupancy_W+0_RB1in_S03_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_03/Occupancy_W+0_RB1in_S03_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_03/Occupancy_W+0_RBout_S03_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_03/Occupancy_W+0_RB1out_S03_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_0/station_2/sector_03/Occupancy_W+0_RB2in_S03_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_03/Occupancy_W+0_RB2in_S03_Middle",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_03/Occupancy_W+0_RB2in_S03_Backward",
           
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_03/Occupancy_W+0_RB2out_S03_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_03/Occupancy_W+0_RB2out_S03_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_0/station_3/sector_03/Occupancy_W+0_RB3_S03-_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_03/Occupancy_W+0_RB3_S03-_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_03/Occupancy_W+0_RB3_S03+_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_03/Occupancy_W+0_RB3_S03+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_0/station_4/sector_03/Occupancy_W+0_RB4_S03-_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_03/Occupancy_W+0_RB4_S03-_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_03/Occupancy_W+0_RB4_S03+_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_03/Occupancy_W+0_RB4_S03+_Backward"])

rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_0/Sector_10",

          ["RPC/RecHits/Barrel/Wheel_0/station_1/sector_10/Occupancy_W+0_RB1in_S10_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_10/Occupancy_W+0_RB1in_S10_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_10/Occupancy_W+0_RBout_S10_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_10/Occupancy_W+0_RB1out_S10_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_0/station_2/sector_10/Occupancy_W+0_RB2in_S10_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_10/Occupancy_W+0_RB2in_S10_Backward",
           
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_10/Occupancy_W+0_RB2out_S10_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_10/Occupancy_W+0_RB2ou_S10_Middle",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_10/Occupancy_W+0_RB2out_S10_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_0/station_3/sector_10/Occupancy_W+0_RB3_S10-_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_10/Occupancy_W+0_RB3_S10-_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_10/Occupancy_W+0_RB3_S10+_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_10/Occupancy_W+0_RB3_S10+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_0/station_4/sector_10/Occupancy_W+0_RB4_S10-_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_10/Occupancy_W+0_RB4_S10-_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_10/Occupancy_W+0_RB4_S10+_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_10/Occupancy_W+0_RB4_S10+_Backward"])


rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_0/Sector_11",

          ["RPC/RecHits/Barrel/Wheel_0/station_1/sector_11/Occupancy_W+0_RB1in_S11_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_11/Occupancy_W+0_RB1in_S11_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_11/Occupancy_W+0_RBout_S11_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_11/Occupancy_W+0_RB1out_S11_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_0/station_2/sector_11/Occupancy_W+0_RB2in_S11_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_11/Occupancy_W+0_RB2in_S11_Middle",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_11/Occupancy_W+0_RB2in_S11_Backward",
           
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_11/Occupancy_W+0_RB2out_S11_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_11/Occupancy_W+0_RB2out_S11_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_0/station_3/sector_11/Occupancy_W+0_RB3_S11-_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_11/Occupancy_W+0_RB3_S11-_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_11/Occupancy_W+0_RB3_S11+_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_11/Occupancy_W+0_RB3_S11+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_0/station_4/sector_11/Occupancy_W+0_RB4_S11-_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_11/Occupancy_W+0_RB4_S11-_Backward"])
        

rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_0/Sector_12",

          ["RPC/RecHits/Barrel/Wheel_0/station_1/sector_12/Occupancy_W+0_RB1in_S12_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_12/Occupancy_W+0_RB1in_S12_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_12/Occupancy_W+0_RBout_S12_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_1/sector_12/Occupancy_W+0_RB1out_S12_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_0/station_2/sector_12/Occupancy_W+0_RB2in_S12_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_12/Occupancy_W+0_RB2in_S12_Backward",
           
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_12/Occupancy_W+0_RB2out_S12_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_12/Occupancy_W+0_RB2out_S12_Middle",
           "RPC/RecHits/Barrel/Wheel_0/station_2/sector_12/Occupancy_W+0_RB2out_S12_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_0/station_3/sector_12/Occupancy_W+0_RB3_S12-_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_12/Occupancy_W+0_RB3_S12-_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_12/Occupancy_W+0_RB3_S12+_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_3/sector_12/Occupancy_W+0_RB3_S12+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_0/station_4/sector_12/Occupancy_W+0_RB4_S12-_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_12/Occupancy_W+0_RB4_S12-_Backward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_12/Occupancy_W+0_RB4_S12+_Forward",
           "RPC/RecHits/Barrel/Wheel_0/station_4/sector_12/Occupancy_W+0_RB4_S12+_Backward"])





rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_1/Sector_01",

          ["RPC/RecHits/Barrel/Wheel_1/station_1/sector_01/Occupancy_W+1_RB1in_S01_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_01/Occupancy_W+1_RB1in_S01_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_01/Occupancy_W+1_RBout_S01_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_01/Occupancy_W+1_RB1out_S01_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_1/station_2/sector_01/Occupancy_W+1_RB2in_S01_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_01/Occupancy_W+1_RB2in_S01_Middle",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_01/Occupancy_W+1_RB2in_S01_Backward",
           
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_01/Occupancy_W+1_RB2out_S01_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_01/Occupancy_W+1_RB2out_S01_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_1/station_3/sector_01/Occupancy_W+1_RB3_S01-_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_01/Occupancy_W+1_RB3_S01-_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_01/Occupancy_W+1_RB3_S01+_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_01/Occupancy_W+1_RB3_S01+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_1/station_4/sector_01/Occupancy_W+1_RB4_S01-_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_01/Occupancy_W+1_RB4_S01-_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_01/Occupancy_W+1_RB4_S01+_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_01/Occupancy_W+1_RB4_S01+_Backward"])
          
rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_1/Sector_02",

          ["RPC/RecHits/Barrel/Wheel_1/station_1/sector_02/Occupancy_W+1_RB1in_S02_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_02/Occupancy_W+1_RB1in_S02_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_02/Occupancy_W+1_RBout_S02_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_02/Occupancy_W+1_RB1out_S02_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_1/station_2/sector_02/Occupancy_W+1_RB2in_S02_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_02/Occupancy_W+1_RB2in_S02_Middle",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_02/Occupancy_W+1_RB2in_S02_Backward",
           
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_02/Occupancy_W+1_RB2out_S02_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_02/Occupancy_W+1_RB2out_S02_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_1/station_3/sector_02/Occupancy_W+1_RB3_S02-_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_02/Occupancy_W+1_RB3_S02-_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_02/Occupancy_W+1_RB3_S02+_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_02/Occupancy_W+1_RB3_S02+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_1/station_4/sector_02/Occupancy_W+1_RB4_S02-_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_02/Occupancy_W+1_RB4_S02-_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_02/Occupancy_W+1_RB4_S02+_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_02/Occupancy_W+1_RB4_S02+_Backward"])
                   
rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_1/Sector_03",

          ["RPC/RecHits/Barrel/Wheel_1/station_1/sector_03/Occupancy_W+1_RB1in_S03_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_03/Occupancy_W+1_RB1in_S03_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_03/Occupancy_W+1_RBout_S03_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_03/Occupancy_W+1_RB1out_S03_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_1/station_2/sector_03/Occupancy_W+1_RB2in_S03_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_03/Occupancy_W+1_RB2in_S03_Middle",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_03/Occupancy_W+1_RB2in_S03_Backward",
           
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_03/Occupancy_W+1_RB2out_S03_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_03/Occupancy_W+1_RB2out_S03_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_1/station_3/sector_03/Occupancy_W+1_RB3_S03-_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_03/Occupancy_W+1_RB3_S03-_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_03/Occupancy_W+1_RB3_S03+_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_03/Occupancy_W+1_RB3_S03+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_1/station_4/sector_03/Occupancy_W+1_RB4_S03-_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_03/Occupancy_W+1_RB4_S03-_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_03/Occupancy_W+1_RB4_S03+_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_03/Occupancy_W+1_RB4_S03+_Backward"])

rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_1/Sector_10",

          ["RPC/RecHits/Barrel/Wheel_1/station_1/sector_10/Occupancy_W+1_RB1in_S10_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_10/Occupancy_W+1_RB1in_S10_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_10/Occupancy_W+1_RBout_S10_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_10/Occupancy_W+1_RB1out_S10_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_1/station_2/sector_10/Occupancy_W+1_RB2in_S10_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_10/Occupancy_W+1_RB2in_S10_Backward",
           
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_10/Occupancy_W+1_RB2out_S10_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_10/Occupancy_W+1_RB2ou_S10_Middle",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_10/Occupancy_W+1_RB2out_S10_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_1/station_3/sector_10/Occupancy_W+1_RB3_S10-_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_10/Occupancy_W+1_RB3_S10-_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_10/Occupancy_W+1_RB3_S10+_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_10/Occupancy_W+1_RB3_S10+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_1/station_4/sector_10/Occupancy_W+1_RB4_S10-_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_10/Occupancy_W+1_RB4_S10-_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_10/Occupancy_W+1_RB4_S10+_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_10/Occupancy_W+1_RB4_S10+_Backward"])


rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_1/Sector_11",

          ["RPC/RecHits/Barrel/Wheel_1/station_1/sector_11/Occupancy_W+1_RB1in_S11_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_11/Occupancy_W+1_RB1in_S11_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_11/Occupancy_W+1_RBout_S11_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_11/Occupancy_W+1_RB1out_S11_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_1/station_2/sector_11/Occupancy_W+1_RB2in_S11_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_11/Occupancy_W+1_RB2in_S11_Middle",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_11/Occupancy_W+1_RB2in_S11_Backward",
           
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_11/Occupancy_W+1_RB2out_S11_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_11/Occupancy_W+1_RB2out_S11_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_1/station_3/sector_11/Occupancy_W+1_RB3_S11-_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_11/Occupancy_W+1_RB3_S11-_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_11/Occupancy_W+1_RB3_S11+_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_11/Occupancy_W+1_RB3_S11+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_1/station_4/sector_11/Occupancy_W+1_RB4_S11-_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_11/Occupancy_W+1_RB4_S11-_Backward"])
        

rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_1/Sector_12",

          ["RPC/RecHits/Barrel/Wheel_1/station_1/sector_12/Occupancy_W+1_RB1in_S12_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_12/Occupancy_W+1_RB1in_S12_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_12/Occupancy_W+1_RBout_S12_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_1/sector_12/Occupancy_W+1_RB1out_S12_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_1/station_2/sector_12/Occupancy_W+1_RB2in_S12_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_12/Occupancy_W+1_RB2in_S12_Backward",
           
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_12/Occupancy_W+1_RB2out_S12_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_12/Occupancy_W+1_RB2out_S12_Middle",
           "RPC/RecHits/Barrel/Wheel_1/station_2/sector_12/Occupancy_W+1_RB2out_S12_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_1/station_3/sector_12/Occupancy_W+1_RB3_S12-_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_12/Occupancy_W+1_RB3_S12-_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_12/Occupancy_W+1_RB3_S12+_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_3/sector_12/Occupancy_W+1_RB3_S12+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_1/station_4/sector_12/Occupancy_W+1_RB4_S12-_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_12/Occupancy_W+1_RB4_S12-_Backward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_12/Occupancy_W+1_RB4_S12+_Forward",
           "RPC/RecHits/Barrel/Wheel_1/station_4/sector_12/Occupancy_W+1_RB4_S12+_Backward"])





rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_2/Sector_01",

          ["RPC/RecHits/Barrel/Wheel_2/station_1/sector_01/Occupancy_W+2_RB1in_S01_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_01/Occupancy_W+2_RB1in_S01_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_01/Occupancy_W+2_RBout_S01_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_01/Occupancy_W+2_RB1out_S01_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_2/station_2/sector_01/Occupancy_W+2_RB2in_S01_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_01/Occupancy_W+2_RB2in_S01_Middle",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_01/Occupancy_W+2_RB2in_S01_Backward",
           
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_01/Occupancy_W+2_RB2out_S01_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_01/Occupancy_W+2_RB2out_S01_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_2/station_3/sector_01/Occupancy_W+2_RB3_S01-_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_01/Occupancy_W+2_RB3_S01-_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_01/Occupancy_W+2_RB3_S01+_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_01/Occupancy_W+2_RB3_S01+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_2/station_4/sector_01/Occupancy_W+2_RB4_S01-_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_01/Occupancy_W+2_RB4_S01-_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_01/Occupancy_W+2_RB4_S01+_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_01/Occupancy_W+2_RB4_S01+_Backward"])
          
rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_2/Sector_02",

          ["RPC/RecHits/Barrel/Wheel_2/station_1/sector_02/Occupancy_W+2_RB1in_S02_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_02/Occupancy_W+2_RB1in_S02_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_02/Occupancy_W+2_RBout_S02_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_02/Occupancy_W+2_RB1out_S02_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_2/station_2/sector_02/Occupancy_W+2_RB2in_S02_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_02/Occupancy_W+2_RB2in_S02_Middle",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_02/Occupancy_W+2_RB2in_S02_Backward",
           
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_02/Occupancy_W+2_RB2out_S02_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_02/Occupancy_W+2_RB2out_S02_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_2/station_3/sector_02/Occupancy_W+2_RB3_S02-_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_02/Occupancy_W+2_RB3_S02-_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_02/Occupancy_W+2_RB3_S02+_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_02/Occupancy_W+2_RB3_S02+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_2/station_4/sector_02/Occupancy_W+2_RB4_S02-_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_02/Occupancy_W+2_RB4_S02-_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_02/Occupancy_W+2_RB4_S02+_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_02/Occupancy_W+2_RB4_S02+_Backward"])
                   
rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_2/Sector_03",

          ["RPC/RecHits/Barrel/Wheel_2/station_1/sector_03/Occupancy_W+2_RB1in_S03_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_03/Occupancy_W+2_RB1in_S03_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_03/Occupancy_W+2_RBout_S03_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_03/Occupancy_W+2_RB1out_S03_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_2/station_2/sector_03/Occupancy_W+2_RB2in_S03_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_03/Occupancy_W+2_RB2in_S03_Middle",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_03/Occupancy_W+2_RB2in_S03_Backward",
           
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_03/Occupancy_W+2_RB2out_S03_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_03/Occupancy_W+2_RB2out_S03_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_2/station_3/sector_03/Occupancy_W+2_RB3_S03-_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_03/Occupancy_W+2_RB3_S03-_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_03/Occupancy_W+2_RB3_S03+_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_03/Occupancy_W+2_RB3_S03+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_2/station_4/sector_03/Occupancy_W+2_RB4_S03-_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_03/Occupancy_W+2_RB4_S03-_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_03/Occupancy_W+2_RB4_S03+_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_03/Occupancy_W+2_RB4_S03+_Backward"])

rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_2/Sector_10",

          ["RPC/RecHits/Barrel/Wheel_2/station_1/sector_10/Occupancy_W+2_RB1in_S10_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_10/Occupancy_W+2_RB1in_S10_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_10/Occupancy_W+2_RBout_S10_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_10/Occupancy_W+2_RB1out_S10_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_2/station_2/sector_10/Occupancy_W+2_RB2in_S10_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_10/Occupancy_W+2_RB2in_S10_Backward",
           
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_10/Occupancy_W+2_RB2out_S10_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_10/Occupancy_W+2_RB2ou_S10_Middle",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_10/Occupancy_W+2_RB2out_S10_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_2/station_3/sector_10/Occupancy_W+2_RB3_S10-_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_10/Occupancy_W+2_RB3_S10-_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_10/Occupancy_W+2_RB3_S10+_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_10/Occupancy_W+2_RB3_S10+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_2/station_4/sector_10/Occupancy_W+2_RB4_S10-_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_10/Occupancy_W+2_RB4_S10-_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_10/Occupancy_W+2_RB4_S10+_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_10/Occupancy_W+2_RB4_S10+_Backward"])


rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_2/Sector_11",

          ["RPC/RecHits/Barrel/Wheel_2/station_1/sector_11/Occupancy_W+2_RB1in_S11_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_11/Occupancy_W+2_RB1in_S11_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_11/Occupancy_W+2_RBout_S11_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_11/Occupancy_W+2_RB1out_S11_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_2/station_2/sector_11/Occupancy_W+2_RB2in_S11_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_11/Occupancy_W+2_RB2in_S11_Middle",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_11/Occupancy_W+2_RB2in_S11_Backward",
           
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_11/Occupancy_W+2_RB2out_S11_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_11/Occupancy_W+2_RB2out_S11_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_2/station_3/sector_11/Occupancy_W+2_RB3_S11-_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_11/Occupancy_W+2_RB3_S11-_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_11/Occupancy_W+2_RB3_S11+_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_11/Occupancy_W+2_RB3_S11+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_2/station_4/sector_11/Occupancy_W+2_RB4_S11-_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_11/Occupancy_W+2_RB4_S11-_Backward"])
        

rpclayout(dqmitems, "RPC_Occupancy_RB1_RB2_RB3_RB4/Wheel_2/Sector_12",

          ["RPC/RecHits/Barrel/Wheel_2/station_1/sector_12/Occupancy_W+2_RB1in_S12_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_12/Occupancy_W+2_RB1in_S12_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_12/Occupancy_W+2_RBout_S12_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_1/sector_12/Occupancy_W+2_RB1out_S12_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_2/station_2/sector_12/Occupancy_W+2_RB2in_S12_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_12/Occupancy_W+2_RB2in_S12_Backward",
           
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_12/Occupancy_W+2_RB2out_S12_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_12/Occupancy_W+2_RB2out_S12_Middle",
           "RPC/RecHits/Barrel/Wheel_2/station_2/sector_12/Occupancy_W+2_RB2out_S12_Backcard"],

          ["RPC/RecHits/Barrel/Wheel_2/station_3/sector_12/Occupancy_W+2_RB3_S12-_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_12/Occupancy_W+2_RB3_S12-_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_12/Occupancy_W+2_RB3_S12+_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_3/sector_12/Occupancy_W+2_RB3_S12+_Backward"],

          ["RPC/RecHits/Barrel/Wheel_2/station_4/sector_12/Occupancy_W+2_RB4_S12-_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_12/Occupancy_W+2_RB4_S12-_Backward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_12/Occupancy_W+2_RB4_S12+_Forward",
           "RPC/RecHits/Barrel/Wheel_2/station_4/sector_12/Occupancy_W+2_RB4_S12+_Backward"])



