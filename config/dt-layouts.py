def dtlayout(i, p, *rows): i["Layouts/DT Layouts/" + p] = DQMItem(layout=rows)

dtlayout(dqmitems, "DTIntegrityCheck_Summary",
         ["DT/DataIntegrity/FED772/FED772_ROSSummary",
          "DT/DataIntegrity/FED772/FED772_TTSValues",
          "DT/DataIntegrity/FED772/FED772_EventLenght"],
         ["DT/DataIntegrity/FED772/FED772_ROSStatus",
          "DT/DataIntegrity/FED772/FED772_FIFOStatus",
          "DT/DataIntegrity/FED772/FED772_EventType"])

dtlayout(dqmitems, "DTLocalTrigger_W0_Phi",
         ["DT/Tests/DTLocalTrigger/Wheel0/TriggerAndSeg/TrigEff_Phi_W0",
          "DT/Tests/DTLocalTrigger/Wheel0/TriggerAndSeg/TrigEffHHHL_Phi_W0"],
         ["DT/Tests/DTLocalTrigger/Wheel0/LocalTriggerPhi/CorrectBX_Phi_W0",
          "DT/Tests/DTLocalTrigger/Wheel0/LocalTriggerPhi/CorrFraction_Phi_W0"])

dtlayout(dqmitems, "DTIntegrityCheck_W0_Sec1",
         ["DT/DataIntegrity/FED772/FED772_ROSSummary",
          "DT/DataIntegrity/FED772/FED772_EventLenght",
          "DT/DataIntegrity/FED772/SC1/FED772_SC1_SCTriggerBX"],
         ["DT/DataIntegrity/FED772/ROS1/FED772_ROS1_ROSError",
          "DT/DataIntegrity/FED772/ROS1/FED772_ROS1_ROSEventLenght",
          "DT/DataIntegrity/FED772/SC1/FED772_SC1_SCTriggerQuality"])

dtlayout(dqmitems, "DTIntegrityCheck_W0_Sec2",
         ["DT/DataIntegrity/FED772/FED772_ROSSummary",
          "DT/DataIntegrity/FED772/FED772_EventLenght",
          "DT/DataIntegrity/FED772/SC2/FED772_SC2_SCTriggerBX"],
         ["DT/DataIntegrity/FED772/ROS2/FED772_ROS2_ROSError",
          "DT/DataIntegrity/FED772/ROS2/FED772_ROS2_ROSEventLenght",
          "DT/DataIntegrity/FED772/SC2/FED772_SC2_SCTriggerQuality"])

dtlayout(dqmitems, "DTIntegrityCheck_W0_Sec3",
         ["DT/DataIntegrity/FED772/FED772_ROSSummary",
          "DT/DataIntegrity/FED772/FED772_EventLenght",
          "DT/DataIntegrity/FED772/SC3/FED772_SC3_SCTriggerBX"],
         ["DT/DataIntegrity/FED772/ROS3/FED772_ROS3_ROSError",
          "DT/DataIntegrity/FED772/ROS3/FED772_ROS3_ROSEventLenght",
          "DT/DataIntegrity/FED772/SC3/FED772_SC3_SCTriggerQuality"])

dtlayout(dqmitems, "DTIntegrityCheck_W0_Sec4",
         ["DT/DataIntegrity/FED772/FED772_ROSSummary",
          "DT/DataIntegrity/FED772/FED772_EventLenght",
          "DT/DataIntegrity/FED772/SC4/FED772_SC4_SCTriggerBX"],
         ["DT/DataIntegrity/FED772/ROS4/FED772_ROS4_ROSError",
          "DT/DataIntegrity/FED772/ROS4/FED772_ROS4_ROSEventLenght",
          "DT/DataIntegrity/FED772/SC4/FED772_SC4_SCTriggerQuality"])

dtlayout(dqmitems, "DTIntegrityCheck_W0_Sec5",
         ["DT/DataIntegrity/FED772/FED772_ROSSummary",
          "DT/DataIntegrity/FED772/FED772_EventLenght",
          "DT/DataIntegrity/FED772/SC5/FED772_SC5_SCTriggerBX"],
         ["DT/DataIntegrity/FED772/ROS5/FED772_ROS5_ROSError",
          "DT/DataIntegrity/FED772/ROS5/FED772_ROS5_ROSEventLenght",
          "DT/DataIntegrity/FED772/SC5/FED772_SC5_SCTriggerQuality"])

dtlayout(dqmitems, "DTIntegrityCheck_W0_Sec6",
         ["DT/DataIntegrity/FED772/FED772_ROSSummary",
          "DT/DataIntegrity/FED772/FED772_EventLenght",
          "DT/DataIntegrity/FED772/SC6/FED772_SC6_SCTriggerBX"],
         ["DT/DataIntegrity/FED772/ROS6/FED772_ROS6_ROSError",
          "DT/DataIntegrity/FED772/ROS6/FED772_ROS6_ROSEventLenght",
          "DT/DataIntegrity/FED772/SC6/FED772_SC6_SCTriggerQuality"])

dtlayout(dqmitems, "DTIntegrityCheck_W0_Sec7",
         ["DT/DataIntegrity/FED772/FED772_ROSSummary",
          "DT/DataIntegrity/FED772/FED772_EventLenght",
          "DT/DataIntegrity/FED772/SC7/FED772_SC7_SCTriggerBX"],
         ["DT/DataIntegrity/FED772/ROS7/FED772_ROS7_ROSError",
          "DT/DataIntegrity/FED772/ROS7/FED772_ROS7_ROSEventLenght",
          "DT/DataIntegrity/FED772/SC7/FED772_SC7_SCTriggerQuality"])

dtlayout(dqmitems, "DTIntegrityCheck_W0_Sec8",
         ["DT/DataIntegrity/FED772/FED772_ROSSummary",
          "DT/DataIntegrity/FED772/FED772_EventLenght",
          "DT/DataIntegrity/FED772/SC8/FED772_SC8_SCTriggerBX"],
         ["DT/DataIntegrity/FED772/ROS8/FED772_ROS8_ROSError",
          "DT/DataIntegrity/FED772/ROS8/FED772_ROS8_ROSEventLenght",
          "DT/DataIntegrity/FED772/SC8/FED772_SC8_SCTriggerQuality"])

dtlayout(dqmitems, "DTIntegrityCheck_W0_Sec9",
         ["DT/DataIntegrity/FED772/FED772_ROSSummary",
          "DT/DataIntegrity/FED772/FED772_EventLenght",
          "DT/DataIntegrity/FED772/SC9/FED772_SC9_SCTriggerBX"],
         ["DT/DataIntegrity/FED772/ROS9/FED772_ROS9_ROSError",
          "DT/DataIntegrity/FED772/ROS9/FED772_ROS9_ROSEventLenght",
          "DT/DataIntegrity/FED772/SC9/FED772_SC9_SCTriggerQuality"])

dtlayout(dqmitems, "DTIntegrityCheck_W0_Sec10",
         ["DT/DataIntegrity/FED772/FED772_ROSSummary",
          "DT/DataIntegrity/FED772/FED772_EventLenght",
          "DT/DataIntegrity/FED772/SC10/FED772_SC10_SCTriggerBX"],
         ["DT/DataIntegrity/FED772/ROS10/FED772_ROS10_ROSError",
          "DT/DataIntegrity/FED772/ROS10/FED772_ROS10_ROSEventLenght",
          "DT/DataIntegrity/FED772/SC10/FED772_SC10_SCTriggerQuality"])

dtlayout(dqmitems, "DTIntegrityCheck_W0_Sec11",
         ["DT/DataIntegrity/FED772/FED772_ROSSummary",
          "DT/DataIntegrity/FED772/FED772_EventLenght",
          "DT/DataIntegrity/FED772/SC11/FED772_SC11_SCTriggerBX"],
         ["DT/DataIntegrity/FED772/ROS11/FED772_ROS11_ROSError",
          "DT/DataIntegrity/FED772/ROS11/FED772_ROS11_ROSEventLenght",
          "DT/DataIntegrity/FED772/SC11/FED772_SC11_SCTriggerQuality"])

dtlayout(dqmitems, "DTIntegrityCheck_W0_Sec12",
         ["DT/DataIntegrity/FED772/FED772_ROSSummary",
          "DT/DataIntegrity/FED772/FED772_EventLenght",
          "DT/DataIntegrity/FED772/SC12/FED772_SC12_SCTriggerBX"],
         ["DT/DataIntegrity/FED772/ROS12/FED772_ROS12_ROSError",
          "DT/DataIntegrity/FED772/ROS12/FED772_ROS12_ROSEventLenght",
          "DT/DataIntegrity/FED772/SC12/FED772_SC12_SCTriggerQuality"])

dtlayout(dqmitems, "W0_Sec1_St1_Signal",
         ["DT/DTDigiTask/Wheel0/Station1/Sector1/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector1/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector1/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector1/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector1/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec1_St2_Signal",
         ["DT/DTDigiTask/Wheel0/Station2/Sector1/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector1/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector1/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector1/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector1/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec1_St3_Signal",
         ["DT/DTDigiTask/Wheel0/Station3/Sector1/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector1/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector1/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector1/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector1/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec1_St4_Signal",
         ["DT/DTDigiTask/Wheel0/Station4/Sector1/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector1/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector1/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector1/TimeBoxes/$2"])

dtlayout(dqmitems, "W0_Sec2_St1_Signal",
         ["DT/DTDigiTask/Wheel0/Station1/Sector2/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector2/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector2/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector2/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector2/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec2_St2_Signal",
         ["DT/DTDigiTask/Wheel0/Station2/Sector2/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector2/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector2/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector2/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector2/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec2_St3_Signal",
         ["DT/DTDigiTask/Wheel0/Station3/Sector2/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector2/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector2/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector2/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector2/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec2_St4_Signal",
         ["DT/DTDigiTask/Wheel0/Station4/Sector2/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector2/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector2/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector2/TimeBoxes/$2"])

dtlayout(dqmitems, "W0_Sec3_St1_Signal",
         ["DT/DTDigiTask/Wheel0/Station1/Sector3/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector3/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector3/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector3/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector3/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec3_St2_Signal",
         ["DT/DTDigiTask/Wheel0/Station2/Sector3/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector3/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector3/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector3/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector3/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec3_St3_Signal",
         ["DT/DTDigiTask/Wheel0/Station3/Sector3/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector3/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector3/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector3/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector3/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec3_St4_Signal",
         ["DT/DTDigiTask/Wheel0/Station4/Sector3/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector3/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector3/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector3/TimeBoxes/$2"])

dtlayout(dqmitems, "W0_Sec4_St1_Signal",
         ["DT/DTDigiTask/Wheel0/Station1/Sector4/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector4/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector4/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector4/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector4/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec4_St2_Signal",
         ["DT/DTDigiTask/Wheel0/Station2/Sector4/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector4/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector4/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector4/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector4/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec4_St3_Signal",
         ["DT/DTDigiTask/Wheel0/Station3/Sector4/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector4/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector4/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector4/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector4/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec4_St4_Signal",
         ["DT/DTDigiTask/Wheel0/Station4/Sector4/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector4/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector4/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector4/TimeBoxes/$2"])

dtlayout(dqmitems, "W0_Sec13_St4_Signal",
         ["DT/DTDigiTask/Wheel0/Station4/Sector13/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector13/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector13/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector13/TimeBoxes/$2"])

dtlayout(dqmitems, "W0_Sec5_St1_Signal",
         ["DT/DTDigiTask/Wheel0/Station1/Sector5/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector5/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector5/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector5/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector5/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec5_St2_Signal",
         ["DT/DTDigiTask/Wheel0/Station2/Sector5/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector5/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector5/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector5/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector5/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec5_St3_Signal",
         ["DT/DTDigiTask/Wheel0/Station3/Sector5/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector5/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector5/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector5/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector5/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec5_St4_Signal",
         ["DT/DTDigiTask/Wheel0/Station4/Sector5/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector5/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector5/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector5/TimeBoxes/$2"])

dtlayout(dqmitems, "W0_Sec6_St1_Signal",
         ["DT/DTDigiTask/Wheel0/Station1/Sector6/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector6/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector6/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector6/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector6/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec6_St2_Signal",
         ["DT/DTDigiTask/Wheel0/Station2/Sector6/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector6/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector6/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector6/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector6/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec6_St3_Signal",
         ["DT/DTDigiTask/Wheel0/Station3/Sector6/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector6/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector6/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector6/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector6/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec6_St4_Signal",
         ["DT/DTDigiTask/Wheel0/Station4/Sector6/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector6/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector6/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector6/TimeBoxes/$2"])

dtlayout(dqmitems, "W0_Sec7_St1_Signal",
         ["DT/DTDigiTask/Wheel0/Station1/Sector7/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector7/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector7/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector7/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector7/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec7_St2_Signal",
         ["DT/DTDigiTask/Wheel0/Station2/Sector7/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector7/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector7/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector7/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector7/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec7_St3_Signal",
         ["DT/DTDigiTask/Wheel0/Station3/Sector7/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector7/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector7/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector7/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector7/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec7_St4_Signal",
         ["DT/DTDigiTask/Wheel0/Station4/Sector7/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector7/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector7/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector7/TimeBoxes/$2"])

dtlayout(dqmitems, "W0_Sec8_St1_Signal",
         ["DT/DTDigiTask/Wheel0/Station1/Sector8/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector8/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector8/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector8/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector8/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec8_St2_Signal",
         ["DT/DTDigiTask/Wheel0/Station2/Sector8/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector8/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector8/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector8/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector8/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec8_St3_Signal",
         ["DT/DTDigiTask/Wheel0/Station3/Sector8/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector8/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector8/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector8/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector8/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec8_St4_Signal",
         ["DT/DTDigiTask/Wheel0/Station4/Sector8/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector8/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector8/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector8/TimeBoxes/$2"])

dtlayout(dqmitems, "W0_Sec9_St1_Signal",
         ["DT/DTDigiTask/Wheel0/Station1/Sector9/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector9/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector9/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector9/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector9/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec9_St2_Signal",
         ["DT/DTDigiTask/Wheel0/Station2/Sector9/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector9/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector9/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector9/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector9/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec9_St3_Signal",
         ["DT/DTDigiTask/Wheel0/Station3/Sector9/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector9/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector9/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector9/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector9/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec9_St4_Signal",
         ["DT/DTDigiTask/Wheel0/Station4/Sector9/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector9/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector9/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector9/TimeBoxes/$2"])

dtlayout(dqmitems, "W0_Sec10_St1_Signal",
         ["DT/DTDigiTask/Wheel0/Station1/Sector10/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector10/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector10/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector10/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector10/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec10_St2_Signal",
         ["DT/DTDigiTask/Wheel0/Station2/Sector10/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector10/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector10/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector10/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector10/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec10_St3_Signal",
         ["DT/DTDigiTask/Wheel0/Station3/Sector10/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector10/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector10/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector10/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector10/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec10_St4_Signal",
         ["DT/DTDigiTask/Wheel0/Station4/Sector10/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector10/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector10/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector10/TimeBoxes/$2"])

dtlayout(dqmitems, "W0_Sec14_St4_Signal",
         ["DT/DTDigiTask/Wheel0/Station4/Sector14/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector14/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector14/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector14/TimeBoxes/$2"])

dtlayout(dqmitems, "W0_Sec11_St1_Signal",
         ["DT/DTDigiTask/Wheel0/Station1/Sector11/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector11/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector11/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector11/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector11/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec11_St2_Signal",
         ["DT/DTDigiTask/Wheel0/Station2/Sector11/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector11/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector11/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector11/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector11/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec11_St3_Signal",
         ["DT/DTDigiTask/Wheel0/Station3/Sector11/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector11/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector11/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector11/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector11/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec11_St4_Signal",
         ["DT/DTDigiTask/Wheel0/Station4/Sector11/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector11/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector11/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector11/TimeBoxes/$2"])

dtlayout(dqmitems, "W0_Sec12_St1_Signal",
         ["DT/DTDigiTask/Wheel0/Station1/Sector12/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector12/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector12/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station1/Sector12/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector12/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec12_St2_Signal",
         ["DT/DTDigiTask/Wheel0/Station2/Sector12/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector12/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector12/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station2/Sector12/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector12/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec12_St3_Signal",
         ["DT/DTDigiTask/Wheel0/Station3/Sector12/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector12/Occupancies/$14"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector12/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station3/Sector12/TimeBoxes/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector12/TimeBoxes/$3"])

dtlayout(dqmitems, "W0_Sec12_St4_Signal",
         ["DT/DTDigiTask/Wheel0/Station4/Sector12/Occupancies/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector12/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector12/TimeBoxes/$1",
          "DT/DTDigiTask/Wheel0/Station4/Sector12/TimeBoxes/$2"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec1_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/LocalTriggerPhi/DCC_BXvsQual_W0_Sec1_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec1_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec1_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec1_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec1_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/LocalTriggerPhi/DCC_BestQual_W0_Sec1_St1"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec1_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/LocalTriggerPhi/DCC_BXvsQual_W0_Sec1_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec1_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec1_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec1_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec1_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/LocalTriggerPhi/DCC_BestQual_W0_Sec1_St2"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec1_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/LocalTriggerPhi/DCC_BXvsQual_W0_Sec1_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec1_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec1_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec1_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec1_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/LocalTriggerPhi/DCC_BestQual_W0_Sec1_St3"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec1_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/LocalTriggerPhi/DCC_BXvsQual_W0_Sec1_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec1_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec1_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec1_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec1_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/LocalTriggerPhi/DCC_BestQual_W0_Sec1_St4"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec2_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/LocalTriggerPhi/DCC_BXvsQual_W0_Sec2_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec2_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec2_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec2_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec2_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/LocalTriggerPhi/DCC_BestQual_W0_Sec2_St1"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec2_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/LocalTriggerPhi/DCC_BXvsQual_W0_Sec2_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec2_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec2_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec2_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec2_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/LocalTriggerPhi/DCC_BestQual_W0_Sec2_St2"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec2_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/LocalTriggerPhi/DCC_BXvsQual_W0_Sec2_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec2_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec2_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec2_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec2_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/LocalTriggerPhi/DCC_BestQual_W0_Sec2_St3"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec2_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/LocalTriggerPhi/DCC_BXvsQual_W0_Sec2_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec2_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec2_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec2_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec2_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/LocalTriggerPhi/DCC_BestQual_W0_Sec2_St4"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec3_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/LocalTriggerPhi/DCC_BXvsQual_W0_Sec3_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec3_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec3_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec3_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec3_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/LocalTriggerPhi/DCC_BestQual_W0_Sec3_St1"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec3_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/LocalTriggerPhi/DCC_BXvsQual_W0_Sec3_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec3_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec3_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec3_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec3_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/LocalTriggerPhi/DCC_BestQual_W0_Sec3_St2"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec3_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/LocalTriggerPhi/DCC_BXvsQual_W0_Sec3_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec3_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec3_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec3_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec3_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/LocalTriggerPhi/DCC_BestQual_W0_Sec3_St3"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec3_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/LocalTriggerPhi/DCC_BXvsQual_W0_Sec3_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec3_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec3_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec3_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec3_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/LocalTriggerPhi/DCC_BestQual_W0_Sec3_St4"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec4_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/LocalTriggerPhi/DCC_BXvsQual_W0_Sec4_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec4_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec4_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec4_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec4_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/LocalTriggerPhi/DCC_BestQual_W0_Sec4_St1"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec4_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/LocalTriggerPhi/DCC_BXvsQual_W0_Sec4_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec4_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec4_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec4_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec4_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/LocalTriggerPhi/DCC_BestQual_W0_Sec4_St2"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec4_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/LocalTriggerPhi/DCC_BXvsQual_W0_Sec4_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec4_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec4_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec4_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec4_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/LocalTriggerPhi/DCC_BestQual_W0_Sec4_St3"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec4_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/LocalTriggerPhi/DCC_BXvsQual_W0_Sec4_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec4_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec4_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec4_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec4_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/LocalTriggerPhi/DCC_BestQual_W0_Sec4_St4"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec5_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/LocalTriggerPhi/DCC_BXvsQual_W0_Sec5_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec5_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec5_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec5_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec5_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/LocalTriggerPhi/DCC_BestQual_W0_Sec5_St1"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec5_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/LocalTriggerPhi/DCC_BXvsQual_W0_Sec5_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec5_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec5_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec5_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec5_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/LocalTriggerPhi/DCC_BestQual_W0_Sec5_St2"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec5_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/LocalTriggerPhi/DCC_BXvsQual_W0_Sec5_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec5_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec5_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec5_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec5_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/LocalTriggerPhi/DCC_BestQual_W0_Sec5_St3"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec5_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/LocalTriggerPhi/DCC_BXvsQual_W0_Sec5_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec5_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec5_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec5_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec5_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/LocalTriggerPhi/DCC_BestQual_W0_Sec5_St4"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec6_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/LocalTriggerPhi/DCC_BXvsQual_W0_Sec6_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec6_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec6_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec6_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec6_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/LocalTriggerPhi/DCC_BestQual_W0_Sec6_St1"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec6_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/LocalTriggerPhi/DCC_BXvsQual_W0_Sec6_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec6_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec6_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec6_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec6_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/LocalTriggerPhi/DCC_BestQual_W0_Sec6_St2"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec6_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/LocalTriggerPhi/DCC_BXvsQual_W0_Sec6_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec6_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec6_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec6_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec6_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/LocalTriggerPhi/DCC_BestQual_W0_Sec6_St3"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec6_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/LocalTriggerPhi/DCC_BXvsQual_W0_Sec6_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec6_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec6_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec6_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec6_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/LocalTriggerPhi/DCC_BestQual_W0_Sec6_St4"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec7_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/LocalTriggerPhi/DCC_BXvsQual_W0_Sec7_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec7_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec7_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec7_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec7_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/LocalTriggerPhi/DCC_BestQual_W0_Sec7_St1"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec7_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/LocalTriggerPhi/DCC_BXvsQual_W0_Sec7_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec7_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec7_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec7_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec7_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/LocalTriggerPhi/DCC_BestQual_W0_Sec7_St2"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec7_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/LocalTriggerPhi/DCC_BXvsQual_W0_Sec7_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec7_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec7_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec7_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec7_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/LocalTriggerPhi/DCC_BestQual_W0_Sec7_St3"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec7_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/LocalTriggerPhi/DCC_BXvsQual_W0_Sec7_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec7_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec7_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec7_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec7_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/LocalTriggerPhi/DCC_BestQual_W0_Sec7_St4"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec8_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/LocalTriggerPhi/DCC_BXvsQual_W0_Sec8_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec8_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec8_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec8_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec8_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/LocalTriggerPhi/DCC_BestQual_W0_Sec8_St1"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec8_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/LocalTriggerPhi/DCC_BXvsQual_W0_Sec8_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec8_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec8_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec8_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec8_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/LocalTriggerPhi/DCC_BestQual_W0_Sec8_St2"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec8_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/LocalTriggerPhi/DCC_BXvsQual_W0_Sec8_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec8_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec8_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec8_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec8_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/LocalTriggerPhi/DCC_BestQual_W0_Sec8_St3"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec8_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/LocalTriggerPhi/DCC_BXvsQual_W0_Sec8_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec8_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec8_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec8_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec8_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/LocalTriggerPhi/DCC_BestQual_W0_Sec8_St4"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec9_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/LocalTriggerPhi/DCC_BXvsQual_W0_Sec9_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec9_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec9_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec9_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec9_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/LocalTriggerPhi/DCC_BestQual_W0_Sec9_St1"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec9_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/LocalTriggerPhi/DCC_BXvsQual_W0_Sec9_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec9_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec9_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec9_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec9_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/LocalTriggerPhi/DCC_BestQual_W0_Sec9_St2"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec9_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/LocalTriggerPhi/DCC_BXvsQual_W0_Sec9_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec9_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec9_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec9_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec9_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/LocalTriggerPhi/DCC_BestQual_W0_Sec9_St3"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec9_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/LocalTriggerPhi/DCC_BXvsQual_W0_Sec9_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec9_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec9_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec9_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec9_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/LocalTriggerPhi/DCC_BestQual_W0_Sec9_St4"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec10_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/LocalTriggerPhi/DCC_BXvsQual_W0_Sec10_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec10_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec10_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec10_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec10_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/LocalTriggerPhi/DCC_BestQual_W0_Sec10_St1"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec10_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/LocalTriggerPhi/DCC_BXvsQual_W0_Sec10_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec10_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec10_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec10_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec10_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/LocalTriggerPhi/DCC_BestQual_W0_Sec10_St2"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec10_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/LocalTriggerPhi/DCC_BXvsQual_W0_Sec10_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec10_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec10_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec10_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec10_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/LocalTriggerPhi/DCC_BestQual_W0_Sec10_St3"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec10_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/LocalTriggerPhi/DCC_BXvsQual_W0_Sec10_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec10_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec10_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec10_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec10_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/LocalTriggerPhi/DCC_BestQual_W0_Sec10_St4"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec11_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/LocalTriggerPhi/DCC_BXvsQual_W0_Sec11_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec11_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec11_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec11_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec11_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/LocalTriggerPhi/DCC_BestQual_W0_Sec11_St1"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec11_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/LocalTriggerPhi/DCC_BXvsQual_W0_Sec11_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec11_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec11_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec11_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec11_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/LocalTriggerPhi/DCC_BestQual_W0_Sec11_St2"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec11_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/LocalTriggerPhi/DCC_BXvsQual_W0_Sec11_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec11_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec11_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec11_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec11_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/LocalTriggerPhi/DCC_BestQual_W0_Sec11_St3"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec11_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/LocalTriggerPhi/DCC_BXvsQual_W0_Sec11_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec11_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec11_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec11_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec11_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/LocalTriggerPhi/DCC_BestQual_W0_Sec11_St4"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec12_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/LocalTriggerPhi/DCC_BXvsQual_W0_Sec12_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec12_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec12_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec12_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec12_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/LocalTriggerPhi/DCC_BestQual_W0_Sec12_St1"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec12_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/LocalTriggerPhi/DCC_BXvsQual_W0_Sec12_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec12_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec12_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec12_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec12_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/LocalTriggerPhi/DCC_BestQual_W0_Sec12_St2"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec12_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/LocalTriggerPhi/DCC_BXvsQual_W0_Sec12_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec12_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec12_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec12_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec12_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/LocalTriggerPhi/DCC_BestQual_W0_Sec12_St3"])

dtlayout(dqmitems, "DTLocalTrigger_producer_W0_Sec12_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/LocalTriggerPhi/DCC_BXvsQual_W0_Sec12_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/LocalTriggerPhi/DCC_Flag1stvsBX_W0_Sec12_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/LocalTriggerPhi/DCC_Flag1stvsQual_W0_Sec12_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/LocalTriggerPhi/DCC_QualvsPhirad_W0_Sec12_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/LocalTriggerPhi/DCC_QualvsPhibend_W0_Sec12_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/LocalTriggerPhi/DCC_BestQual_W0_Sec12_St4"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec1_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/Segment/DCC_TrackPosvsAngle_W0_Sec1_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec1_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec1_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/Segment/DCC_HitstkvsQualtrig_W0_Sec1_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/Segment/DCC_PhitkvsPhitrig_W0_Sec1_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/Segment/DCC_PhibtkvsPhibtrig_W0_Sec1_St1"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec1_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/Segment/DCC_TrackPosvsAngle_W0_Sec1_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec1_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec1_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/Segment/DCC_HitstkvsQualtrig_W0_Sec1_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/Segment/DCC_PhitkvsPhitrig_W0_Sec1_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/Segment/DCC_PhibtkvsPhibtrig_W0_Sec1_St2"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec1_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/Segment/DCC_TrackPosvsAngle_W0_Sec1_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec1_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec1_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/Segment/DCC_HitstkvsQualtrig_W0_Sec1_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/Segment/DCC_PhitkvsPhitrig_W0_Sec1_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/Segment/DCC_PhibtkvsPhibtrig_W0_Sec1_St3"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec1_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/Segment/DCC_TrackPosvsAngle_W0_Sec1_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec1_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec1_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/Segment/DCC_HitstkvsQualtrig_W0_Sec1_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/Segment/DCC_PhitkvsPhitrig_W0_Sec1_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/Segment/DCC_PhibtkvsPhibtrig_W0_Sec1_St4"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec2_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/Segment/DCC_TrackPosvsAngle_W0_Sec2_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec2_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec2_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/Segment/DCC_HitstkvsQualtrig_W0_Sec2_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/Segment/DCC_PhitkvsPhitrig_W0_Sec2_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/Segment/DCC_PhibtkvsPhibtrig_W0_Sec2_St1"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec2_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/Segment/DCC_TrackPosvsAngle_W0_Sec2_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec2_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec2_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/Segment/DCC_HitstkvsQualtrig_W0_Sec2_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/Segment/DCC_PhitkvsPhitrig_W0_Sec2_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/Segment/DCC_PhibtkvsPhibtrig_W0_Sec2_St2"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec2_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/Segment/DCC_TrackPosvsAngle_W0_Sec2_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec2_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec2_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/Segment/DCC_HitstkvsQualtrig_W0_Sec2_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/Segment/DCC_PhitkvsPhitrig_W0_Sec2_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/Segment/DCC_PhibtkvsPhibtrig_W0_Sec2_St3"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec2_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/Segment/DCC_TrackPosvsAngle_W0_Sec2_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec2_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec2_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/Segment/DCC_HitstkvsQualtrig_W0_Sec2_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/Segment/DCC_PhitkvsPhitrig_W0_Sec2_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/Segment/DCC_PhibtkvsPhibtrig_W0_Sec2_St4"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec3_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/Segment/DCC_TrackPosvsAngle_W0_Sec3_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec3_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec3_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/Segment/DCC_HitstkvsQualtrig_W0_Sec3_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/Segment/DCC_PhitkvsPhitrig_W0_Sec3_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/Segment/DCC_PhibtkvsPhibtrig_W0_Sec3_St1"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec3_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/Segment/DCC_TrackPosvsAngle_W0_Sec3_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec3_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec3_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/Segment/DCC_HitstkvsQualtrig_W0_Sec3_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/Segment/DCC_PhitkvsPhitrig_W0_Sec3_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/Segment/DCC_PhibtkvsPhibtrig_W0_Sec3_St2"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec3_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/Segment/DCC_TrackPosvsAngle_W0_Sec3_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec3_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec3_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/Segment/DCC_HitstkvsQualtrig_W0_Sec3_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/Segment/DCC_PhitkvsPhitrig_W0_Sec3_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/Segment/DCC_PhibtkvsPhibtrig_W0_Sec3_St3"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec3_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/Segment/DCC_TrackPosvsAngle_W0_Sec3_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec3_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec3_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/Segment/DCC_HitstkvsQualtrig_W0_Sec3_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/Segment/DCC_PhitkvsPhitrig_W0_Sec3_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/Segment/DCC_PhibtkvsPhibtrig_W0_Sec3_St4"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec4_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/Segment/DCC_TrackPosvsAngle_W0_Sec4_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec4_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec4_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/Segment/DCC_HitstkvsQualtrig_W0_Sec4_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/Segment/DCC_PhitkvsPhitrig_W0_Sec4_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/Segment/DCC_PhibtkvsPhibtrig_W0_Sec4_St1"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec4_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/Segment/DCC_TrackPosvsAngle_W0_Sec4_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec4_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec4_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/Segment/DCC_HitstkvsQualtrig_W0_Sec4_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/Segment/DCC_PhitkvsPhitrig_W0_Sec4_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/Segment/DCC_PhibtkvsPhibtrig_W0_Sec4_St2"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec4_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/Segment/DCC_TrackPosvsAngle_W0_Sec4_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec4_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec4_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/Segment/DCC_HitstkvsQualtrig_W0_Sec4_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/Segment/DCC_PhitkvsPhitrig_W0_Sec4_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/Segment/DCC_PhibtkvsPhibtrig_W0_Sec4_St3"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec4_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/Segment/DCC_TrackPosvsAngle_W0_Sec4_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec4_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec4_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/Segment/DCC_HitstkvsQualtrig_W0_Sec4_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/Segment/DCC_PhitkvsPhitrig_W0_Sec4_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/Segment/DCC_PhibtkvsPhibtrig_W0_Sec4_St4"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec5_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/Segment/DCC_TrackPosvsAngle_W0_Sec5_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec5_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec5_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/Segment/DCC_HitstkvsQualtrig_W0_Sec5_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/Segment/DCC_PhitkvsPhitrig_W0_Sec5_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/Segment/DCC_PhibtkvsPhibtrig_W0_Sec5_St1"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec5_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/Segment/DCC_TrackPosvsAngle_W0_Sec5_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec5_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec5_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/Segment/DCC_HitstkvsQualtrig_W0_Sec5_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/Segment/DCC_PhitkvsPhitrig_W0_Sec5_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/Segment/DCC_PhibtkvsPhibtrig_W0_Sec5_St2"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec5_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/Segment/DCC_TrackPosvsAngle_W0_Sec5_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec5_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec5_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/Segment/DCC_HitstkvsQualtrig_W0_Sec5_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/Segment/DCC_PhitkvsPhitrig_W0_Sec5_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/Segment/DCC_PhibtkvsPhibtrig_W0_Sec5_St3"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec5_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/Segment/DCC_TrackPosvsAngle_W0_Sec5_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec5_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec5_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/Segment/DCC_HitstkvsQualtrig_W0_Sec5_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/Segment/DCC_PhitkvsPhitrig_W0_Sec5_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/Segment/DCC_PhibtkvsPhibtrig_W0_Sec5_St4"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec6_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/Segment/DCC_TrackPosvsAngle_W0_Sec6_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec6_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec6_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/Segment/DCC_HitstkvsQualtrig_W0_Sec6_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/Segment/DCC_PhitkvsPhitrig_W0_Sec6_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/Segment/DCC_PhibtkvsPhibtrig_W0_Sec6_St1"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec6_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/Segment/DCC_TrackPosvsAngle_W0_Sec6_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec6_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec6_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/Segment/DCC_HitstkvsQualtrig_W0_Sec6_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/Segment/DCC_PhitkvsPhitrig_W0_Sec6_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/Segment/DCC_PhibtkvsPhibtrig_W0_Sec6_St2"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec6_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/Segment/DCC_TrackPosvsAngle_W0_Sec6_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec6_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec6_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/Segment/DCC_HitstkvsQualtrig_W0_Sec6_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/Segment/DCC_PhitkvsPhitrig_W0_Sec6_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/Segment/DCC_PhibtkvsPhibtrig_W0_Sec6_St3"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec6_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/Segment/DCC_TrackPosvsAngle_W0_Sec6_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec6_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec6_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/Segment/DCC_HitstkvsQualtrig_W0_Sec6_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/Segment/DCC_PhitkvsPhitrig_W0_Sec6_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/Segment/DCC_PhibtkvsPhibtrig_W0_Sec6_St4"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec7_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/Segment/DCC_TrackPosvsAngle_W0_Sec7_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec7_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec7_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/Segment/DCC_HitstkvsQualtrig_W0_Sec7_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/Segment/DCC_PhitkvsPhitrig_W0_Sec7_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/Segment/DCC_PhibtkvsPhibtrig_W0_Sec7_St1"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec7_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/Segment/DCC_TrackPosvsAngle_W0_Sec7_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec7_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec7_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/Segment/DCC_HitstkvsQualtrig_W0_Sec7_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/Segment/DCC_PhitkvsPhitrig_W0_Sec7_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/Segment/DCC_PhibtkvsPhibtrig_W0_Sec7_St2"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec7_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/Segment/DCC_TrackPosvsAngle_W0_Sec7_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec7_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec7_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/Segment/DCC_HitstkvsQualtrig_W0_Sec7_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/Segment/DCC_PhitkvsPhitrig_W0_Sec7_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/Segment/DCC_PhibtkvsPhibtrig_W0_Sec7_St3"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec7_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/Segment/DCC_TrackPosvsAngle_W0_Sec7_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec7_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec7_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/Segment/DCC_HitstkvsQualtrig_W0_Sec7_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/Segment/DCC_PhitkvsPhitrig_W0_Sec7_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/Segment/DCC_PhibtkvsPhibtrig_W0_Sec7_St4"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec8_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/Segment/DCC_TrackPosvsAngle_W0_Sec8_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec8_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec8_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/Segment/DCC_HitstkvsQualtrig_W0_Sec8_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/Segment/DCC_PhitkvsPhitrig_W0_Sec8_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/Segment/DCC_PhibtkvsPhibtrig_W0_Sec8_St1"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec8_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/Segment/DCC_TrackPosvsAngle_W0_Sec8_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec8_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec8_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/Segment/DCC_HitstkvsQualtrig_W0_Sec8_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/Segment/DCC_PhitkvsPhitrig_W0_Sec8_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/Segment/DCC_PhibtkvsPhibtrig_W0_Sec8_St2"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec8_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/Segment/DCC_TrackPosvsAngle_W0_Sec8_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec8_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec8_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/Segment/DCC_HitstkvsQualtrig_W0_Sec8_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/Segment/DCC_PhitkvsPhitrig_W0_Sec8_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/Segment/DCC_PhibtkvsPhibtrig_W0_Sec8_St3"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec8_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/Segment/DCC_TrackPosvsAngle_W0_Sec8_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec8_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec8_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/Segment/DCC_HitstkvsQualtrig_W0_Sec8_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/Segment/DCC_PhitkvsPhitrig_W0_Sec8_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/Segment/DCC_PhibtkvsPhibtrig_W0_Sec8_St4"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec9_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/Segment/DCC_TrackPosvsAngle_W0_Sec9_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec9_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec9_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/Segment/DCC_HitstkvsQualtrig_W0_Sec9_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/Segment/DCC_PhitkvsPhitrig_W0_Sec9_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/Segment/DCC_PhibtkvsPhibtrig_W0_Sec9_St1"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec9_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/Segment/DCC_TrackPosvsAngle_W0_Sec9_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec9_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec9_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/Segment/DCC_HitstkvsQualtrig_W0_Sec9_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/Segment/DCC_PhitkvsPhitrig_W0_Sec9_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/Segment/DCC_PhibtkvsPhibtrig_W0_Sec9_St2"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec9_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/Segment/DCC_TrackPosvsAngle_W0_Sec9_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec9_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec9_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/Segment/DCC_HitstkvsQualtrig_W0_Sec9_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/Segment/DCC_PhitkvsPhitrig_W0_Sec9_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/Segment/DCC_PhibtkvsPhibtrig_W0_Sec9_St3"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec9_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/Segment/DCC_TrackPosvsAngle_W0_Sec9_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec9_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec9_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/Segment/DCC_HitstkvsQualtrig_W0_Sec9_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/Segment/DCC_PhitkvsPhitrig_W0_Sec9_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/Segment/DCC_PhibtkvsPhibtrig_W0_Sec9_St4"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec10_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/Segment/DCC_TrackPosvsAngle_W0_Sec10_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec10_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec10_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/Segment/DCC_HitstkvsQualtrig_W0_Sec10_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/Segment/DCC_PhitkvsPhitrig_W0_Sec10_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/Segment/DCC_PhibtkvsPhibtrig_W0_Sec10_St1"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec10_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/Segment/DCC_TrackPosvsAngle_W0_Sec10_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec10_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec10_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/Segment/DCC_HitstkvsQualtrig_W0_Sec10_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/Segment/DCC_PhitkvsPhitrig_W0_Sec10_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/Segment/DCC_PhibtkvsPhibtrig_W0_Sec10_St2"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec10_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/Segment/DCC_TrackPosvsAngle_W0_Sec10_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec10_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec10_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/Segment/DCC_HitstkvsQualtrig_W0_Sec10_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/Segment/DCC_PhitkvsPhitrig_W0_Sec10_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/Segment/DCC_PhibtkvsPhibtrig_W0_Sec10_St3"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec10_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/Segment/DCC_TrackPosvsAngle_W0_Sec10_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec10_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec10_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/Segment/DCC_HitstkvsQualtrig_W0_Sec10_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/Segment/DCC_PhitkvsPhitrig_W0_Sec10_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/Segment/DCC_PhibtkvsPhibtrig_W0_Sec10_St4"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec11_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/Segment/DCC_TrackPosvsAngle_W0_Sec11_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec11_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec11_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/Segment/DCC_HitstkvsQualtrig_W0_Sec11_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/Segment/DCC_PhitkvsPhitrig_W0_Sec11_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/Segment/DCC_PhibtkvsPhibtrig_W0_Sec11_St1"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec11_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/Segment/DCC_TrackPosvsAngle_W0_Sec11_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec11_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec11_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/Segment/DCC_HitstkvsQualtrig_W0_Sec11_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/Segment/DCC_PhitkvsPhitrig_W0_Sec11_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/Segment/DCC_PhibtkvsPhibtrig_W0_Sec11_St2"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec11_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/Segment/DCC_TrackPosvsAngle_W0_Sec11_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec11_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec11_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/Segment/DCC_HitstkvsQualtrig_W0_Sec11_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/Segment/DCC_PhitkvsPhitrig_W0_Sec11_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/Segment/DCC_PhibtkvsPhibtrig_W0_Sec11_St3"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec11_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/Segment/DCC_TrackPosvsAngle_W0_Sec11_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec11_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec11_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/Segment/DCC_HitstkvsQualtrig_W0_Sec11_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/Segment/DCC_PhitkvsPhitrig_W0_Sec11_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/Segment/DCC_PhibtkvsPhibtrig_W0_Sec11_St4"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec12_Station1",
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/Segment/DCC_TrackPosvsAngle_W0_Sec12_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec12_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec12_St1"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/Segment/DCC_HitstkvsQualtrig_W0_Sec12_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/Segment/DCC_PhitkvsPhitrig_W0_Sec12_St1",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/Segment/DCC_PhibtkvsPhibtrig_W0_Sec12_St1"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec12_Station2",
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/Segment/DCC_TrackPosvsAngle_W0_Sec12_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec12_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec12_St2"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/Segment/DCC_HitstkvsQualtrig_W0_Sec12_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/Segment/DCC_PhitkvsPhitrig_W0_Sec12_St2",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/Segment/DCC_PhibtkvsPhibtrig_W0_Sec12_St2"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec12_Station3",
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/Segment/DCC_TrackPosvsAngle_W0_Sec12_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec12_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec12_St3"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/Segment/DCC_HitstkvsQualtrig_W0_Sec12_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/Segment/DCC_PhitkvsPhitrig_W0_Sec12_St3",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/Segment/DCC_PhibtkvsPhibtrig_W0_Sec12_St3"])

dtlayout(dqmitems, "DTLocalTrigger_segment_W0_Sec12_Station4",
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/Segment/DCC_TrackPosvsAngle_W0_Sec12_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/Segment/DCC_TrackPosvsAngleandTrig_W0_Sec12_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/Segment/DCC_TrackPosvsAngleandTrigHHHL_W0_Sec12_St4"],
         ["DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/Segment/DCC_HitstkvsQualtrig_W0_Sec12_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/Segment/DCC_PhitkvsPhitrig_W0_Sec12_St4",
          "DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/Segment/DCC_PhibtkvsPhibtrig_W0_Sec12_St4"])

dtlayout(dqmitems, "DTLocalTrigger_W0_Sec1_Station5_Client_Phi",
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector1/Station5/TrigEffPos_Phi_W0_Sec1_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector1/Station5/TrigEffAngle_Phi_W0_Sec1_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector1/Station5/TrigEffPosvsAngle_Phi_W0_Sec1_St5"],
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector1/Station5/TrigEffPosHHHL_Phi_W0_Sec1_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector1/Station5/TrigEffAngleHHHL_Phi_W0_Sec1_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector1/Station5/TrigEffPosvsAngleHHHL_Phi_W0_Sec1_St5"])

dtlayout(dqmitems, "DTLocalTrigger_W0_Sec2_Station5_Client_Phi",
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector2/Station5/TrigEffPos_Phi_W0_Sec2_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector2/Station5/TrigEffAngle_Phi_W0_Sec2_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector2/Station5/TrigEffPosvsAngle_Phi_W0_Sec2_St5"],
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector2/Station5/TrigEffPosHHHL_Phi_W0_Sec2_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector2/Station5/TrigEffAngleHHHL_Phi_W0_Sec2_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector2/Station5/TrigEffPosvsAngleHHHL_Phi_W0_Sec2_St5"])

dtlayout(dqmitems, "DTLocalTrigger_W0_Sec3_Station5_Client_Phi",
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector3/Station5/TrigEffPos_Phi_W0_Sec3_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector3/Station5/TrigEffAngle_Phi_W0_Sec3_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector3/Station5/TrigEffPosvsAngle_Phi_W0_Sec3_St5"],
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector3/Station5/TrigEffPosHHHL_Phi_W0_Sec3_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector3/Station5/TrigEffAngleHHHL_Phi_W0_Sec3_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector3/Station5/TrigEffPosvsAngleHHHL_Phi_W0_Sec3_St5"])

dtlayout(dqmitems, "DTLocalTrigger_W0_Sec4_Station5_Client_Phi",
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector4/Station5/TrigEffPos_Phi_W0_Sec4_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector4/Station5/TrigEffAngle_Phi_W0_Sec4_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector4/Station5/TrigEffPosvsAngle_Phi_W0_Sec4_St5"],
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector4/Station5/TrigEffPosHHHL_Phi_W0_Sec4_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector4/Station5/TrigEffAngleHHHL_Phi_W0_Sec4_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector4/Station5/TrigEffPosvsAngleHHHL_Phi_W0_Sec4_St5"])

dtlayout(dqmitems, "DTLocalTrigger_W0_Sec5_Station5_Client_Phi",
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector5/Station5/TrigEffPos_Phi_W0_Sec5_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector5/Station5/TrigEffAngle_Phi_W0_Sec5_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector5/Station5/TrigEffPosvsAngle_Phi_W0_Sec5_St5"],
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector5/Station5/TrigEffPosHHHL_Phi_W0_Sec5_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector5/Station5/TrigEffAngleHHHL_Phi_W0_Sec5_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector5/Station5/TrigEffPosvsAngleHHHL_Phi_W0_Sec5_St5"])

dtlayout(dqmitems, "DTLocalTrigger_W0_Sec6_Station5_Client_Phi",
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector6/Station5/TrigEffPos_Phi_W0_Sec6_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector6/Station5/TrigEffAngle_Phi_W0_Sec6_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector6/Station5/TrigEffPosvsAngle_Phi_W0_Sec6_St5"],
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector6/Station5/TrigEffPosHHHL_Phi_W0_Sec6_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector6/Station5/TrigEffAngleHHHL_Phi_W0_Sec6_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector6/Station5/TrigEffPosvsAngleHHHL_Phi_W0_Sec6_St5"])

dtlayout(dqmitems, "DTLocalTrigger_W0_Sec7_Station5_Client_Phi",
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector7/Station5/TrigEffPos_Phi_W0_Sec7_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector7/Station5/TrigEffAngle_Phi_W0_Sec7_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector7/Station5/TrigEffPosvsAngle_Phi_W0_Sec7_St5"],
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector7/Station5/TrigEffPosHHHL_Phi_W0_Sec7_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector7/Station5/TrigEffAngleHHHL_Phi_W0_Sec7_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector7/Station5/TrigEffPosvsAngleHHHL_Phi_W0_Sec7_St5"])

dtlayout(dqmitems, "DTLocalTrigger_W0_Sec8_Station5_Client_Phi",
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector8/Station5/TrigEffPos_Phi_W0_Sec8_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector8/Station5/TrigEffAngle_Phi_W0_Sec8_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector8/Station5/TrigEffPosvsAngle_Phi_W0_Sec8_St5"],
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector8/Station5/TrigEffPosHHHL_Phi_W0_Sec8_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector8/Station5/TrigEffAngleHHHL_Phi_W0_Sec8_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector8/Station5/TrigEffPosvsAngleHHHL_Phi_W0_Sec8_St5"])

dtlayout(dqmitems, "DTLocalTrigger_W0_Sec9_Station5_Client_Phi",
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector9/Station5/TrigEffPos_Phi_W0_Sec9_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector9/Station5/TrigEffAngle_Phi_W0_Sec9_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector9/Station5/TrigEffPosvsAngle_Phi_W0_Sec9_St5"],
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector9/Station5/TrigEffPosHHHL_Phi_W0_Sec9_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector9/Station5/TrigEffAngleHHHL_Phi_W0_Sec9_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector9/Station5/TrigEffPosvsAngleHHHL_Phi_W0_Sec9_St5"])

dtlayout(dqmitems, "DTLocalTrigger_W0_Sec10_Station5_Client_Phi",
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector10/Station5/TrigEffPos_Phi_W0_Sec10_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector10/Station5/TrigEffAngle_Phi_W0_Sec10_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector10/Station5/TrigEffPosvsAngle_Phi_W0_Sec10_St5"],
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector10/Station5/TrigEffPosHHHL_Phi_W0_Sec10_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector10/Station5/TrigEffAngleHHHL_Phi_W0_Sec10_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector10/Station5/TrigEffPosvsAngleHHHL_Phi_W0_Sec10_St5"])

dtlayout(dqmitems, "DTLocalTrigger_W0_Sec11_Station5_Client_Phi",
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector11/Station5/TrigEffPos_Phi_W0_Sec11_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector11/Station5/TrigEffAngle_Phi_W0_Sec11_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector11/Station5/TrigEffPosvsAngle_Phi_W0_Sec11_St5"],
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector11/Station5/TrigEffPosHHHL_Phi_W0_Sec11_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector11/Station5/TrigEffAngleHHHL_Phi_W0_Sec11_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector11/Station5/TrigEffPosvsAngleHHHL_Phi_W0_Sec11_St5"])

dtlayout(dqmitems, "DTLocalTrigger_W0_Sec12_Station5_Client_Phi",
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector12/Station5/TrigEffPos_Phi_W0_Sec12_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector12/Station5/TrigEffAngle_Phi_W0_Sec12_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector12/Station5/TrigEffPosvsAngle_Phi_W0_Sec12_St5"],
         ["DT/Tests/DTLocalTrigger/Wheel0/Sector12/Station5/TrigEffPosHHHL_Phi_W0_Sec12_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector12/Station5/TrigEffAngleHHHL_Phi_W0_Sec12_St5",
          "DT/Tests/DTLocalTrigger/Wheel0/Sector12/Station5/TrigEffPosvsAngleHHHL_Phi_W0_Sec12_St5"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec1_St1",
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector1/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector1/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector1/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector1/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector1/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector1/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector1/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector1/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector1/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector1/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector1/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector1/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec1_St2",
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector1/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector1/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector1/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector1/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector1/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector1/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector1/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector1/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector1/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector1/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector1/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector1/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec1_St3",
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector1/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector1/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector1/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector1/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector1/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector1/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector1/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector1/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector1/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector1/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector1/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector1/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec1_St4",
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector1/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector1/$5"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector1/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector1/$6"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector1/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector1/$7"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector1/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector1/$8"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec2_St1",
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector2/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector2/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector2/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector2/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector2/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector2/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector2/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector2/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector2/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector2/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector2/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector2/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec2_St2",
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector2/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector2/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector2/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector2/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector2/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector2/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector2/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector2/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector2/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector2/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector2/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector2/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec2_St3",
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector2/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector2/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector2/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector2/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector2/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector2/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector2/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector2/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector2/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector2/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector2/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector2/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec2_St4",
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector2/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector2/$5"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector2/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector2/$6"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector2/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector2/$7"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector2/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector2/$8"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec3_St1",
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector3/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector3/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector3/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector3/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector3/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector3/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector3/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector3/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector3/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector3/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector3/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector3/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec3_St2",
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector3/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector3/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector3/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector3/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector3/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector3/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector3/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector3/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector3/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector3/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector3/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector3/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec3_St3",
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector3/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector3/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector3/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector3/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector3/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector3/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector3/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector3/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector3/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector3/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector3/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector3/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec3_St4",
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector3/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector3/$5"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector3/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector3/$6"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector3/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector3/$7"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector3/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector3/$8"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec4_St1",
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector4/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector4/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector4/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector4/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector4/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector4/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector4/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector4/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector4/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector4/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector4/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector4/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec4_St2",
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector4/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector4/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector4/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector4/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector4/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector4/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector4/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector4/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector4/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector4/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector4/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector4/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec4_St3",
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector4/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector4/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector4/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector4/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector4/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector4/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector4/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector4/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector4/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector4/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector4/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector4/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec4_St4",
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector4/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector4/$5"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector4/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector4/$6"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector4/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector4/$7"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector4/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector4/$8"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec13_St4",
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector13/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector13/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector13/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector13/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector13/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector13/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector13/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector13/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector13/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector13/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector13/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector13/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec5_St1",
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector5/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector5/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector5/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector5/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector5/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector5/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector5/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector5/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector5/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector5/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector5/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector5/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec5_St2",
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector5/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector5/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector5/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector5/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector5/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector5/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector5/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector5/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector5/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector5/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector5/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector5/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec5_St3",
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector5/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector5/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector5/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector5/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector5/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector5/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector5/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector5/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector5/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector5/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector5/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector5/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec5_St4",
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector5/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector5/$5"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector5/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector5/$6"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector5/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector5/$7"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector5/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector5/$8"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec6_St1",
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector6/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector6/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector6/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector6/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector6/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector6/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector6/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector6/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector6/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector6/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector6/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector6/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec6_St2",
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector6/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector6/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector6/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector6/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector6/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector6/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector6/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector6/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector6/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector6/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector6/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector6/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec6_St3",
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector6/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector6/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector6/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector6/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector6/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector6/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector6/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector6/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector6/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector6/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector6/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector6/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec6_St4",
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector6/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector6/$5"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector6/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector6/$6"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector6/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector6/$7"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector6/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector6/$8"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec7_St1",
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector7/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector7/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector7/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector7/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector7/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector7/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector7/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector7/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector7/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector7/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector7/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector7/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec7_St2",
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector7/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector7/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector7/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector7/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector7/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector7/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector7/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector7/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector7/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector7/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector7/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector7/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec7_St3",
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector7/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector7/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector7/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector7/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector7/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector7/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector7/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector7/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector7/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector7/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector7/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector7/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec7_St4",
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector7/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector7/$5"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector7/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector7/$6"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector7/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector7/$7"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector7/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector7/$8"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec8_St1",
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector8/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector8/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector8/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector8/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector8/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector8/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector8/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector8/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector8/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector8/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector8/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector8/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec8_St2",
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector8/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector8/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector8/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector8/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector8/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector8/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector8/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector8/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector8/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector8/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector8/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector8/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec8_St3",
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector8/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector8/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector8/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector8/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector8/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector8/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector8/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector8/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector8/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector8/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector8/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector8/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec8_St4",
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector8/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector8/$5"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector8/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector8/$6"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector8/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector8/$7"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector8/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector8/$8"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec9_St1",
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector9/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector9/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector9/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector9/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector9/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector9/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector9/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector9/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector9/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector9/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector9/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector9/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec9_St2",
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector9/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector9/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector9/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector9/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector9/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector9/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector9/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector9/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector9/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector9/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector9/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector9/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec9_St3",
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector9/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector9/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector9/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector9/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector9/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector9/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector9/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector9/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector9/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector9/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector9/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector9/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec9_St4",
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector9/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector9/$5"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector9/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector9/$6"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector9/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector9/$7"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector9/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector9/$8"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec10_St1",
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector10/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector10/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector10/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector10/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector10/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector10/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector10/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector10/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector10/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector10/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector10/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector10/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec10_St2",
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector10/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector10/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector10/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector10/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector10/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector10/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector10/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector10/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector10/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector10/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector10/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector10/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec10_St3",
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector10/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector10/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector10/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector10/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector10/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector10/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector10/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector10/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector10/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector10/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector10/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector10/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec10_St4",
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector10/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector10/$5"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector10/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector10/$6"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector10/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector10/$7"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector10/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector10/$8"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec14_St4",
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector14/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector14/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector14/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector14/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector14/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector14/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector14/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector14/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector14/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector14/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector14/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector14/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec11_St1",
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector11/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector11/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector11/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector11/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector11/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector11/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector11/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector11/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector11/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector11/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector11/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector11/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec11_St2",
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector11/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector11/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector11/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector11/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector11/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector11/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector11/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector11/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector11/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector11/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector11/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector11/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec11_St3",
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector11/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector11/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector11/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector11/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector11/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector11/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector11/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector11/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector11/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector11/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector11/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector11/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec11_St4",
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector11/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector11/$5"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector11/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector11/$6"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector11/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector11/$7"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector11/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector11/$8"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec12_St1",
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector12/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector12/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector12/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector12/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector12/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector12/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector12/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector12/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector12/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station1/Sector12/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector12/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station1/Sector12/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec12_St2",
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector12/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector12/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector12/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector12/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector12/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector12/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector12/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector12/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector12/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station2/Sector12/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector12/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station2/Sector12/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec12_St3",
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector12/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector12/$5",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector12/$9"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector12/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector12/$6",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector12/$10"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector12/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector12/$7",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector12/$11"],
         ["DT/Tests/DTEfficiency/Wheel0/Station3/Sector12/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector12/$8",
          "DT/Tests/DTEfficiency/Wheel0/Station3/Sector12/$12"])

dtlayout(dqmitems, "Summary_Efficiency_W0_Sec12_St4",
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector12/$1",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector12/$5"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector12/$2",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector12/$6"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector12/$3",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector12/$7"],
         ["DT/Tests/DTEfficiency/Wheel0/Station4/Sector12/$4",
          "DT/Tests/DTEfficiency/Wheel0/Station4/Sector12/$8"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec1_St1",
         ["DT/DTDigiTask/Wheel0/Station1/Sector1/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector1/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station1/Sector1/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector1/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station1/Sector1/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station1/Sector1/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector1/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station1/Sector1/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station1/Sector1/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector1/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station1/Sector1/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station1/Sector1/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec1_St2",
         ["DT/DTDigiTask/Wheel0/Station2/Sector1/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector1/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station2/Sector1/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector1/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station2/Sector1/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station2/Sector1/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector1/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station2/Sector1/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station2/Sector1/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector1/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station2/Sector1/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station2/Sector1/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec1_St3",
         ["DT/DTDigiTask/Wheel0/Station3/Sector1/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector1/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station3/Sector1/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector1/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station3/Sector1/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station3/Sector1/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector1/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station3/Sector1/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station3/Sector1/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector1/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station3/Sector1/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station3/Sector1/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec1_St4",
         ["DT/DTDigiTask/Wheel0/Station4/Sector1/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station4/Sector1/Occupancies/$6"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector1/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station4/Sector1/Occupancies/$7"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector1/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station4/Sector1/Occupancies/$8"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector1/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station4/Sector1/Occupancies/$9"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec2_St1",
         ["DT/DTDigiTask/Wheel0/Station1/Sector2/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector2/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station1/Sector2/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector2/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station1/Sector2/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station1/Sector2/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector2/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station1/Sector2/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station1/Sector2/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector2/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station1/Sector2/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station1/Sector2/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec2_St2",
         ["DT/DTDigiTask/Wheel0/Station2/Sector2/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector2/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station2/Sector2/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector2/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station2/Sector2/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station2/Sector2/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector2/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station2/Sector2/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station2/Sector2/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector2/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station2/Sector2/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station2/Sector2/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec2_St3",
         ["DT/DTDigiTask/Wheel0/Station3/Sector2/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector2/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station3/Sector2/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector2/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station3/Sector2/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station3/Sector2/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector2/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station3/Sector2/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station3/Sector2/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector2/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station3/Sector2/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station3/Sector2/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec2_St4",
         ["DT/DTDigiTask/Wheel0/Station4/Sector2/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station4/Sector2/Occupancies/$6"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector2/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station4/Sector2/Occupancies/$7"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector2/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station4/Sector2/Occupancies/$8"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector2/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station4/Sector2/Occupancies/$9"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec3_St1",
         ["DT/DTDigiTask/Wheel0/Station1/Sector3/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector3/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station1/Sector3/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector3/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station1/Sector3/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station1/Sector3/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector3/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station1/Sector3/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station1/Sector3/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector3/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station1/Sector3/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station1/Sector3/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec3_St2",
         ["DT/DTDigiTask/Wheel0/Station2/Sector3/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector3/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station2/Sector3/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector3/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station2/Sector3/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station2/Sector3/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector3/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station2/Sector3/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station2/Sector3/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector3/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station2/Sector3/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station2/Sector3/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec3_St3",
         ["DT/DTDigiTask/Wheel0/Station3/Sector3/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector3/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station3/Sector3/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector3/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station3/Sector3/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station3/Sector3/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector3/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station3/Sector3/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station3/Sector3/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector3/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station3/Sector3/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station3/Sector3/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec3_St4",
         ["DT/DTDigiTask/Wheel0/Station4/Sector3/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station4/Sector3/Occupancies/$6"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector3/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station4/Sector3/Occupancies/$7"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector3/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station4/Sector3/Occupancies/$8"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector3/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station4/Sector3/Occupancies/$9"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec4_St1",
         ["DT/DTDigiTask/Wheel0/Station1/Sector4/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector4/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station1/Sector4/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector4/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station1/Sector4/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station1/Sector4/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector4/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station1/Sector4/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station1/Sector4/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector4/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station1/Sector4/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station1/Sector4/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec4_St2",
         ["DT/DTDigiTask/Wheel0/Station2/Sector4/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector4/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station2/Sector4/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector4/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station2/Sector4/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station2/Sector4/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector4/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station2/Sector4/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station2/Sector4/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector4/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station2/Sector4/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station2/Sector4/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec4_St3",
         ["DT/DTDigiTask/Wheel0/Station3/Sector4/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector4/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station3/Sector4/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector4/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station3/Sector4/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station3/Sector4/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector4/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station3/Sector4/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station3/Sector4/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector4/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station3/Sector4/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station3/Sector4/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec4_St4",
         ["DT/DTDigiTask/Wheel0/Station4/Sector4/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station4/Sector4/Occupancies/$6"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector4/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station4/Sector4/Occupancies/$7"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector4/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station4/Sector4/Occupancies/$8"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector4/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station4/Sector4/Occupancies/$9"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec13_St4",
         ["DT/DTDigiTask/Wheel0/Station4/Sector13/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station4/Sector13/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station4/Sector13/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector13/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station4/Sector13/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station4/Sector13/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector13/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station4/Sector13/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station4/Sector13/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector13/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station4/Sector13/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station4/Sector13/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec5_St1",
         ["DT/DTDigiTask/Wheel0/Station1/Sector5/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector5/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station1/Sector5/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector5/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station1/Sector5/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station1/Sector5/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector5/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station1/Sector5/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station1/Sector5/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector5/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station1/Sector5/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station1/Sector5/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec5_St2",
         ["DT/DTDigiTask/Wheel0/Station2/Sector5/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector5/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station2/Sector5/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector5/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station2/Sector5/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station2/Sector5/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector5/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station2/Sector5/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station2/Sector5/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector5/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station2/Sector5/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station2/Sector5/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec5_St3",
         ["DT/DTDigiTask/Wheel0/Station3/Sector5/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector5/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station3/Sector5/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector5/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station3/Sector5/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station3/Sector5/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector5/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station3/Sector5/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station3/Sector5/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector5/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station3/Sector5/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station3/Sector5/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec5_St4",
         ["DT/DTDigiTask/Wheel0/Station4/Sector5/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station4/Sector5/Occupancies/$6"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector5/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station4/Sector5/Occupancies/$7"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector5/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station4/Sector5/Occupancies/$8"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector5/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station4/Sector5/Occupancies/$9"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec6_St1",
         ["DT/DTDigiTask/Wheel0/Station1/Sector6/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector6/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station1/Sector6/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector6/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station1/Sector6/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station1/Sector6/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector6/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station1/Sector6/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station1/Sector6/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector6/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station1/Sector6/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station1/Sector6/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec6_St2",
         ["DT/DTDigiTask/Wheel0/Station2/Sector6/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector6/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station2/Sector6/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector6/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station2/Sector6/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station2/Sector6/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector6/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station2/Sector6/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station2/Sector6/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector6/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station2/Sector6/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station2/Sector6/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec6_St3",
         ["DT/DTDigiTask/Wheel0/Station3/Sector6/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector6/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station3/Sector6/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector6/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station3/Sector6/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station3/Sector6/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector6/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station3/Sector6/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station3/Sector6/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector6/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station3/Sector6/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station3/Sector6/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec6_St4",
         ["DT/DTDigiTask/Wheel0/Station4/Sector6/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station4/Sector6/Occupancies/$6"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector6/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station4/Sector6/Occupancies/$7"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector6/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station4/Sector6/Occupancies/$8"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector6/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station4/Sector6/Occupancies/$9"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec7_St1",
         ["DT/DTDigiTask/Wheel0/Station1/Sector7/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector7/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station1/Sector7/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector7/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station1/Sector7/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station1/Sector7/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector7/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station1/Sector7/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station1/Sector7/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector7/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station1/Sector7/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station1/Sector7/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec7_St2",
         ["DT/DTDigiTask/Wheel0/Station2/Sector7/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector7/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station2/Sector7/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector7/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station2/Sector7/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station2/Sector7/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector7/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station2/Sector7/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station2/Sector7/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector7/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station2/Sector7/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station2/Sector7/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec7_St3",
         ["DT/DTDigiTask/Wheel0/Station3/Sector7/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector7/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station3/Sector7/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector7/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station3/Sector7/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station3/Sector7/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector7/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station3/Sector7/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station3/Sector7/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector7/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station3/Sector7/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station3/Sector7/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec7_St4",
         ["DT/DTDigiTask/Wheel0/Station4/Sector7/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station4/Sector7/Occupancies/$6"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector7/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station4/Sector7/Occupancies/$7"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector7/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station4/Sector7/Occupancies/$8"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector7/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station4/Sector7/Occupancies/$9"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec8_St1",
         ["DT/DTDigiTask/Wheel0/Station1/Sector8/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector8/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station1/Sector8/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector8/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station1/Sector8/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station1/Sector8/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector8/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station1/Sector8/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station1/Sector8/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector8/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station1/Sector8/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station1/Sector8/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec8_St2",
         ["DT/DTDigiTask/Wheel0/Station2/Sector8/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector8/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station2/Sector8/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector8/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station2/Sector8/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station2/Sector8/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector8/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station2/Sector8/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station2/Sector8/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector8/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station2/Sector8/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station2/Sector8/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec8_St3",
         ["DT/DTDigiTask/Wheel0/Station3/Sector8/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector8/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station3/Sector8/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector8/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station3/Sector8/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station3/Sector8/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector8/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station3/Sector8/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station3/Sector8/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector8/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station3/Sector8/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station3/Sector8/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec8_St4",
         ["DT/DTDigiTask/Wheel0/Station4/Sector8/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station4/Sector8/Occupancies/$6"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector8/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station4/Sector8/Occupancies/$7"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector8/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station4/Sector8/Occupancies/$8"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector8/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station4/Sector8/Occupancies/$9"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec9_St1",
         ["DT/DTDigiTask/Wheel0/Station1/Sector9/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector9/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station1/Sector9/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector9/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station1/Sector9/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station1/Sector9/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector9/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station1/Sector9/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station1/Sector9/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector9/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station1/Sector9/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station1/Sector9/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec9_St2",
         ["DT/DTDigiTask/Wheel0/Station2/Sector9/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector9/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station2/Sector9/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector9/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station2/Sector9/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station2/Sector9/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector9/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station2/Sector9/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station2/Sector9/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector9/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station2/Sector9/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station2/Sector9/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec9_St3",
         ["DT/DTDigiTask/Wheel0/Station3/Sector9/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector9/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station3/Sector9/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector9/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station3/Sector9/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station3/Sector9/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector9/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station3/Sector9/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station3/Sector9/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector9/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station3/Sector9/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station3/Sector9/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec9_St4",
         ["DT/DTDigiTask/Wheel0/Station4/Sector9/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station4/Sector9/Occupancies/$6"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector9/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station4/Sector9/Occupancies/$7"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector9/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station4/Sector9/Occupancies/$8"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector9/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station4/Sector9/Occupancies/$9"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec10_St1",
         ["DT/DTDigiTask/Wheel0/Station1/Sector10/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector10/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station1/Sector10/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector10/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station1/Sector10/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station1/Sector10/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector10/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station1/Sector10/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station1/Sector10/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector10/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station1/Sector10/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station1/Sector10/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec10_St2",
         ["DT/DTDigiTask/Wheel0/Station2/Sector10/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector10/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station2/Sector10/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector10/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station2/Sector10/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station2/Sector10/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector10/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station2/Sector10/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station2/Sector10/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector10/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station2/Sector10/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station2/Sector10/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec10_St3",
         ["DT/DTDigiTask/Wheel0/Station3/Sector10/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector10/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station3/Sector10/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector10/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station3/Sector10/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station3/Sector10/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector10/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station3/Sector10/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station3/Sector10/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector10/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station3/Sector10/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station3/Sector10/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec10_St4",
         ["DT/DTDigiTask/Wheel0/Station4/Sector10/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station4/Sector10/Occupancies/$6"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector10/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station4/Sector10/Occupancies/$7"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector10/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station4/Sector10/Occupancies/$8"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector10/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station4/Sector10/Occupancies/$9"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec14_St4",
         ["DT/DTDigiTask/Wheel0/Station4/Sector14/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station4/Sector14/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station4/Sector14/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector14/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station4/Sector14/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station4/Sector14/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector14/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station4/Sector14/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station4/Sector14/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector14/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station4/Sector14/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station4/Sector14/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec11_St1",
         ["DT/DTDigiTask/Wheel0/Station1/Sector11/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector11/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station1/Sector11/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector11/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station1/Sector11/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station1/Sector11/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector11/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station1/Sector11/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station1/Sector11/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector11/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station1/Sector11/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station1/Sector11/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec11_St2",
         ["DT/DTDigiTask/Wheel0/Station2/Sector11/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector11/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station2/Sector11/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector11/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station2/Sector11/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station2/Sector11/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector11/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station2/Sector11/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station2/Sector11/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector11/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station2/Sector11/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station2/Sector11/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec11_St3",
         ["DT/DTDigiTask/Wheel0/Station3/Sector11/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector11/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station3/Sector11/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector11/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station3/Sector11/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station3/Sector11/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector11/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station3/Sector11/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station3/Sector11/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector11/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station3/Sector11/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station3/Sector11/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec11_St4",
         ["DT/DTDigiTask/Wheel0/Station4/Sector11/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station4/Sector11/Occupancies/$6"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector11/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station4/Sector11/Occupancies/$7"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector11/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station4/Sector11/Occupancies/$8"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector11/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station4/Sector11/Occupancies/$9"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec12_St1",
         ["DT/DTDigiTask/Wheel0/Station1/Sector12/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station1/Sector12/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station1/Sector12/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector12/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station1/Sector12/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station1/Sector12/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector12/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station1/Sector12/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station1/Sector12/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station1/Sector12/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station1/Sector12/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station1/Sector12/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec12_St2",
         ["DT/DTDigiTask/Wheel0/Station2/Sector12/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station2/Sector12/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station2/Sector12/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector12/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station2/Sector12/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station2/Sector12/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector12/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station2/Sector12/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station2/Sector12/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station2/Sector12/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station2/Sector12/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station2/Sector12/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec12_St3",
         ["DT/DTDigiTask/Wheel0/Station3/Sector12/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station3/Sector12/Occupancies/$6",
          "DT/DTDigiTask/Wheel0/Station3/Sector12/Occupancies/$10"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector12/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station3/Sector12/Occupancies/$7",
          "DT/DTDigiTask/Wheel0/Station3/Sector12/Occupancies/$11"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector12/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station3/Sector12/Occupancies/$8",
          "DT/DTDigiTask/Wheel0/Station3/Sector12/Occupancies/$12"],
         ["DT/DTDigiTask/Wheel0/Station3/Sector12/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station3/Sector12/Occupancies/$9",
          "DT/DTDigiTask/Wheel0/Station3/Sector12/Occupancies/$13"])

dtlayout(dqmitems, "OccupancyPerLayer_W0_Sec12_St4",
         ["DT/DTDigiTask/Wheel0/Station4/Sector12/Occupancies/$2",
          "DT/DTDigiTask/Wheel0/Station4/Sector12/Occupancies/$6"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector12/Occupancies/$3",
          "DT/DTDigiTask/Wheel0/Station4/Sector12/Occupancies/$7"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector12/Occupancies/$4",
          "DT/DTDigiTask/Wheel0/Station4/Sector12/Occupancies/$8"],
         ["DT/DTDigiTask/Wheel0/Station4/Sector12/Occupancies/$5",
          "DT/DTDigiTask/Wheel0/Station4/Sector12/Occupancies/$9"])

