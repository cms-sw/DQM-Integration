def dtlayout(i, p, *rows): i["DT/Layouts/" + p] = DQMItem(layout=rows)

dtlayout(dqmitems, "00-Summary/00-DataIntegritySummary",
  [{ 'path': "DT/DataIntegrity/DataIntegritySummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description</a>" }])

dtlayout(dqmitems, "00-Summary/01-OccupancySummary",
  [{ 'path': "DT/Digi/OccupancySummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description</a>" }])

dtlayout(dqmitems, "00-Summary/02-SegmentSummary",
  [{ 'path': "DT/Segments/segmentSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description</a>" }])

dtlayout(dqmitems, "00-Summary/03-LocalTriggerSummary",
  [{ 'path': "DT/LocalTrigger/DDU_CorrFractionSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description</a>" }])



dtlayout(dqmitems, "Wheel0/Sector1/Station1/Trigger(DDU)_W0_St1_Sec1",
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/LocalTriggerPhi/DDU_BestQual_W0_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec1_St1"])

dtlayout(dqmitems, "Wheel0/Sector1/Station1/Signal_W0_St1_Sec1",
	["DT/Digi/Wheel0/Station1/Sector1/Occupancies/OccupancyAllHits_perCh_W0_St1_Sec1",
	 "DT/Digi/Wheel0/Station1/Sector1/TimeBoxes/TimeBox_W0_St1_Sec1_SL1"],
	["DT/Digi/Wheel0/Station1/Sector1/TimeBoxes/TimeBox_W0_St1_Sec1_SL2",
	 "DT/Digi/Wheel0/Station1/Sector1/TimeBoxes/TimeBox_W0_St1_Sec1_SL3"])


dtlayout(dqmitems, "Wheel0/Sector1/Station2/Trigger(DDU)_W0_St2_Sec1",
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/LocalTriggerPhi/DDU_BestQual_W0_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec1_St2"])

dtlayout(dqmitems, "Wheel0/Sector1/Station2/Signal_W0_St2_Sec1",
	["DT/Digi/Wheel0/Station2/Sector1/Occupancies/OccupancyAllHits_perCh_W0_St2_Sec1",
	 "DT/Digi/Wheel0/Station2/Sector1/TimeBoxes/TimeBox_W0_St2_Sec1_SL1"],
	["DT/Digi/Wheel0/Station2/Sector1/TimeBoxes/TimeBox_W0_St2_Sec1_SL2",
	 "DT/Digi/Wheel0/Station2/Sector1/TimeBoxes/TimeBox_W0_St2_Sec1_SL3"])


dtlayout(dqmitems, "Wheel0/Sector1/Station3/Trigger(DDU)_W0_St3_Sec1",
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/LocalTriggerPhi/DDU_BestQual_W0_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec1_St3"])

dtlayout(dqmitems, "Wheel0/Sector1/Station3/Signal_W0_St3_Sec1",
	["DT/Digi/Wheel0/Station3/Sector1/Occupancies/OccupancyAllHits_perCh_W0_St3_Sec1",
	 "DT/Digi/Wheel0/Station3/Sector1/TimeBoxes/TimeBox_W0_St3_Sec1_SL1"],
	["DT/Digi/Wheel0/Station3/Sector1/TimeBoxes/TimeBox_W0_St3_Sec1_SL2",
	 "DT/Digi/Wheel0/Station3/Sector1/TimeBoxes/TimeBox_W0_St3_Sec1_SL3"])


dtlayout(dqmitems, "Wheel0/Sector1/Station4/Trigger(DDU)_W0_St4_Sec1",
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec1_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec1_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/LocalTriggerPhi/DDU_BestQual_W0_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec1_St4"])

dtlayout(dqmitems, "Wheel0/Sector1/Station4/Signal_W0_St4_Sec1",
	["DT/Digi/Wheel0/Station4/Sector1/Occupancies/OccupancyAllHits_perCh_W0_St4_Sec1",
	 "DT/Digi/Wheel0/Station4/Sector1/TimeBoxes/TimeBox_W0_St4_Sec1_SL1"],
	["DT/Digi/Wheel0/Station4/Sector1/TimeBoxes/TimeBox_W0_St4_Sec1_SL3"])


dtlayout(dqmitems, "Wheel0/Sector2/Station1/Trigger(DDU)_W0_St1_Sec2",
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/LocalTriggerPhi/DDU_BestQual_W0_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec2_St1"])

dtlayout(dqmitems, "Wheel0/Sector2/Station1/Signal_W0_St1_Sec2",
	["DT/Digi/Wheel0/Station1/Sector2/Occupancies/OccupancyAllHits_perCh_W0_St1_Sec2",
	 "DT/Digi/Wheel0/Station1/Sector2/TimeBoxes/TimeBox_W0_St1_Sec2_SL1"],
	["DT/Digi/Wheel0/Station1/Sector2/TimeBoxes/TimeBox_W0_St1_Sec2_SL2",
	 "DT/Digi/Wheel0/Station1/Sector2/TimeBoxes/TimeBox_W0_St1_Sec2_SL3"])


dtlayout(dqmitems, "Wheel0/Sector2/Station2/Trigger(DDU)_W0_St2_Sec2",
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/LocalTriggerPhi/DDU_BestQual_W0_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec2_St2"])

dtlayout(dqmitems, "Wheel0/Sector2/Station2/Signal_W0_St2_Sec2",
	["DT/Digi/Wheel0/Station2/Sector2/Occupancies/OccupancyAllHits_perCh_W0_St2_Sec2",
	 "DT/Digi/Wheel0/Station2/Sector2/TimeBoxes/TimeBox_W0_St2_Sec2_SL1"],
	["DT/Digi/Wheel0/Station2/Sector2/TimeBoxes/TimeBox_W0_St2_Sec2_SL2",
	 "DT/Digi/Wheel0/Station2/Sector2/TimeBoxes/TimeBox_W0_St2_Sec2_SL3"])


dtlayout(dqmitems, "Wheel0/Sector2/Station3/Trigger(DDU)_W0_St3_Sec2",
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/LocalTriggerPhi/DDU_BestQual_W0_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec2_St3"])

dtlayout(dqmitems, "Wheel0/Sector2/Station3/Signal_W0_St3_Sec2",
	["DT/Digi/Wheel0/Station3/Sector2/Occupancies/OccupancyAllHits_perCh_W0_St3_Sec2",
	 "DT/Digi/Wheel0/Station3/Sector2/TimeBoxes/TimeBox_W0_St3_Sec2_SL1"],
	["DT/Digi/Wheel0/Station3/Sector2/TimeBoxes/TimeBox_W0_St3_Sec2_SL2",
	 "DT/Digi/Wheel0/Station3/Sector2/TimeBoxes/TimeBox_W0_St3_Sec2_SL3"])


dtlayout(dqmitems, "Wheel0/Sector2/Station4/Trigger(DDU)_W0_St4_Sec2",
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec2_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec2_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/LocalTriggerPhi/DDU_BestQual_W0_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec2_St4"])

dtlayout(dqmitems, "Wheel0/Sector2/Station4/Signal_W0_St4_Sec2",
	["DT/Digi/Wheel0/Station4/Sector2/Occupancies/OccupancyAllHits_perCh_W0_St4_Sec2",
	 "DT/Digi/Wheel0/Station4/Sector2/TimeBoxes/TimeBox_W0_St4_Sec2_SL1"],
	["DT/Digi/Wheel0/Station4/Sector2/TimeBoxes/TimeBox_W0_St4_Sec2_SL3"])


dtlayout(dqmitems, "Wheel0/Sector3/Station1/Trigger(DDU)_W0_St1_Sec3",
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/LocalTriggerPhi/DDU_BestQual_W0_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec3_St1"])

dtlayout(dqmitems, "Wheel0/Sector3/Station1/Signal_W0_St1_Sec3",
	["DT/Digi/Wheel0/Station1/Sector3/Occupancies/OccupancyAllHits_perCh_W0_St1_Sec3",
	 "DT/Digi/Wheel0/Station1/Sector3/TimeBoxes/TimeBox_W0_St1_Sec3_SL1"],
	["DT/Digi/Wheel0/Station1/Sector3/TimeBoxes/TimeBox_W0_St1_Sec3_SL2",
	 "DT/Digi/Wheel0/Station1/Sector3/TimeBoxes/TimeBox_W0_St1_Sec3_SL3"])


dtlayout(dqmitems, "Wheel0/Sector3/Station2/Trigger(DDU)_W0_St2_Sec3",
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/LocalTriggerPhi/DDU_BestQual_W0_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec3_St2"])

dtlayout(dqmitems, "Wheel0/Sector3/Station2/Signal_W0_St2_Sec3",
	["DT/Digi/Wheel0/Station2/Sector3/Occupancies/OccupancyAllHits_perCh_W0_St2_Sec3",
	 "DT/Digi/Wheel0/Station2/Sector3/TimeBoxes/TimeBox_W0_St2_Sec3_SL1"],
	["DT/Digi/Wheel0/Station2/Sector3/TimeBoxes/TimeBox_W0_St2_Sec3_SL2",
	 "DT/Digi/Wheel0/Station2/Sector3/TimeBoxes/TimeBox_W0_St2_Sec3_SL3"])


dtlayout(dqmitems, "Wheel0/Sector3/Station3/Trigger(DDU)_W0_St3_Sec3",
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/LocalTriggerPhi/DDU_BestQual_W0_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec3_St3"])

dtlayout(dqmitems, "Wheel0/Sector3/Station3/Signal_W0_St3_Sec3",
	["DT/Digi/Wheel0/Station3/Sector3/Occupancies/OccupancyAllHits_perCh_W0_St3_Sec3",
	 "DT/Digi/Wheel0/Station3/Sector3/TimeBoxes/TimeBox_W0_St3_Sec3_SL1"],
	["DT/Digi/Wheel0/Station3/Sector3/TimeBoxes/TimeBox_W0_St3_Sec3_SL2",
	 "DT/Digi/Wheel0/Station3/Sector3/TimeBoxes/TimeBox_W0_St3_Sec3_SL3"])


dtlayout(dqmitems, "Wheel0/Sector3/Station4/Trigger(DDU)_W0_St4_Sec3",
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec3_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec3_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/LocalTriggerPhi/DDU_BestQual_W0_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec3_St4"])

dtlayout(dqmitems, "Wheel0/Sector3/Station4/Signal_W0_St4_Sec3",
	["DT/Digi/Wheel0/Station4/Sector3/Occupancies/OccupancyAllHits_perCh_W0_St4_Sec3",
	 "DT/Digi/Wheel0/Station4/Sector3/TimeBoxes/TimeBox_W0_St4_Sec3_SL1"],
	["DT/Digi/Wheel0/Station4/Sector3/TimeBoxes/TimeBox_W0_St4_Sec3_SL3"])


dtlayout(dqmitems, "Wheel0/Sector4/Station1/Trigger(DDU)_W0_St1_Sec4",
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/LocalTriggerPhi/DDU_BestQual_W0_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec4_St1"])

dtlayout(dqmitems, "Wheel0/Sector4/Station1/Signal_W0_St1_Sec4",
	["DT/Digi/Wheel0/Station1/Sector4/Occupancies/OccupancyAllHits_perCh_W0_St1_Sec4",
	 "DT/Digi/Wheel0/Station1/Sector4/TimeBoxes/TimeBox_W0_St1_Sec4_SL1"],
	["DT/Digi/Wheel0/Station1/Sector4/TimeBoxes/TimeBox_W0_St1_Sec4_SL2",
	 "DT/Digi/Wheel0/Station1/Sector4/TimeBoxes/TimeBox_W0_St1_Sec4_SL3"])


dtlayout(dqmitems, "Wheel0/Sector4/Station2/Trigger(DDU)_W0_St2_Sec4",
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/LocalTriggerPhi/DDU_BestQual_W0_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec4_St2"])

dtlayout(dqmitems, "Wheel0/Sector4/Station2/Signal_W0_St2_Sec4",
	["DT/Digi/Wheel0/Station2/Sector4/Occupancies/OccupancyAllHits_perCh_W0_St2_Sec4",
	 "DT/Digi/Wheel0/Station2/Sector4/TimeBoxes/TimeBox_W0_St2_Sec4_SL1"],
	["DT/Digi/Wheel0/Station2/Sector4/TimeBoxes/TimeBox_W0_St2_Sec4_SL2",
	 "DT/Digi/Wheel0/Station2/Sector4/TimeBoxes/TimeBox_W0_St2_Sec4_SL3"])


dtlayout(dqmitems, "Wheel0/Sector4/Station3/Trigger(DDU)_W0_St3_Sec4",
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/LocalTriggerPhi/DDU_BestQual_W0_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec4_St3"])

dtlayout(dqmitems, "Wheel0/Sector4/Station3/Signal_W0_St3_Sec4",
	["DT/Digi/Wheel0/Station3/Sector4/Occupancies/OccupancyAllHits_perCh_W0_St3_Sec4",
	 "DT/Digi/Wheel0/Station3/Sector4/TimeBoxes/TimeBox_W0_St3_Sec4_SL1"],
	["DT/Digi/Wheel0/Station3/Sector4/TimeBoxes/TimeBox_W0_St3_Sec4_SL2",
	 "DT/Digi/Wheel0/Station3/Sector4/TimeBoxes/TimeBox_W0_St3_Sec4_SL3"])


dtlayout(dqmitems, "Wheel0/Sector4/Station4/Trigger(DDU)_W0_St4_Sec4",
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec4_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec4_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/LocalTriggerPhi/DDU_BestQual_W0_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec4_St4"])

dtlayout(dqmitems, "Wheel0/Sector4/Station4/Signal_W0_St4_Sec4",
	["DT/Digi/Wheel0/Station4/Sector4/Occupancies/OccupancyAllHits_perCh_W0_St4_Sec4",
	 "DT/Digi/Wheel0/Station4/Sector4/TimeBoxes/TimeBox_W0_St4_Sec4_SL1"],
	["DT/Digi/Wheel0/Station4/Sector4/TimeBoxes/TimeBox_W0_St4_Sec4_SL3"])


dtlayout(dqmitems, "Wheel0/Sector5/Station1/Trigger(DDU)_W0_St1_Sec5",
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/LocalTriggerPhi/DDU_BestQual_W0_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec5_St1"])

dtlayout(dqmitems, "Wheel0/Sector5/Station1/Signal_W0_St1_Sec5",
	["DT/Digi/Wheel0/Station1/Sector5/Occupancies/OccupancyAllHits_perCh_W0_St1_Sec5",
	 "DT/Digi/Wheel0/Station1/Sector5/TimeBoxes/TimeBox_W0_St1_Sec5_SL1"],
	["DT/Digi/Wheel0/Station1/Sector5/TimeBoxes/TimeBox_W0_St1_Sec5_SL2",
	 "DT/Digi/Wheel0/Station1/Sector5/TimeBoxes/TimeBox_W0_St1_Sec5_SL3"])


dtlayout(dqmitems, "Wheel0/Sector5/Station2/Trigger(DDU)_W0_St2_Sec5",
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/LocalTriggerPhi/DDU_BestQual_W0_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec5_St2"])

dtlayout(dqmitems, "Wheel0/Sector5/Station2/Signal_W0_St2_Sec5",
	["DT/Digi/Wheel0/Station2/Sector5/Occupancies/OccupancyAllHits_perCh_W0_St2_Sec5",
	 "DT/Digi/Wheel0/Station2/Sector5/TimeBoxes/TimeBox_W0_St2_Sec5_SL1"],
	["DT/Digi/Wheel0/Station2/Sector5/TimeBoxes/TimeBox_W0_St2_Sec5_SL2",
	 "DT/Digi/Wheel0/Station2/Sector5/TimeBoxes/TimeBox_W0_St2_Sec5_SL3"])


dtlayout(dqmitems, "Wheel0/Sector5/Station3/Trigger(DDU)_W0_St3_Sec5",
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/LocalTriggerPhi/DDU_BestQual_W0_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec5_St3"])

dtlayout(dqmitems, "Wheel0/Sector5/Station3/Signal_W0_St3_Sec5",
	["DT/Digi/Wheel0/Station3/Sector5/Occupancies/OccupancyAllHits_perCh_W0_St3_Sec5",
	 "DT/Digi/Wheel0/Station3/Sector5/TimeBoxes/TimeBox_W0_St3_Sec5_SL1"],
	["DT/Digi/Wheel0/Station3/Sector5/TimeBoxes/TimeBox_W0_St3_Sec5_SL2",
	 "DT/Digi/Wheel0/Station3/Sector5/TimeBoxes/TimeBox_W0_St3_Sec5_SL3"])


dtlayout(dqmitems, "Wheel0/Sector5/Station4/Trigger(DDU)_W0_St4_Sec5",
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec5_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec5_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/LocalTriggerPhi/DDU_BestQual_W0_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec5_St4"])

dtlayout(dqmitems, "Wheel0/Sector5/Station4/Signal_W0_St4_Sec5",
	["DT/Digi/Wheel0/Station4/Sector5/Occupancies/OccupancyAllHits_perCh_W0_St4_Sec5",
	 "DT/Digi/Wheel0/Station4/Sector5/TimeBoxes/TimeBox_W0_St4_Sec5_SL1"],
	["DT/Digi/Wheel0/Station4/Sector5/TimeBoxes/TimeBox_W0_St4_Sec5_SL3"])


dtlayout(dqmitems, "Wheel0/Sector6/Station1/Trigger(DDU)_W0_St1_Sec6",
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/LocalTriggerPhi/DDU_BestQual_W0_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec6_St1"])

dtlayout(dqmitems, "Wheel0/Sector6/Station1/Signal_W0_St1_Sec6",
	["DT/Digi/Wheel0/Station1/Sector6/Occupancies/OccupancyAllHits_perCh_W0_St1_Sec6",
	 "DT/Digi/Wheel0/Station1/Sector6/TimeBoxes/TimeBox_W0_St1_Sec6_SL1"],
	["DT/Digi/Wheel0/Station1/Sector6/TimeBoxes/TimeBox_W0_St1_Sec6_SL2",
	 "DT/Digi/Wheel0/Station1/Sector6/TimeBoxes/TimeBox_W0_St1_Sec6_SL3"])


dtlayout(dqmitems, "Wheel0/Sector6/Station2/Trigger(DDU)_W0_St2_Sec6",
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/LocalTriggerPhi/DDU_BestQual_W0_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec6_St2"])

dtlayout(dqmitems, "Wheel0/Sector6/Station2/Signal_W0_St2_Sec6",
	["DT/Digi/Wheel0/Station2/Sector6/Occupancies/OccupancyAllHits_perCh_W0_St2_Sec6",
	 "DT/Digi/Wheel0/Station2/Sector6/TimeBoxes/TimeBox_W0_St2_Sec6_SL1"],
	["DT/Digi/Wheel0/Station2/Sector6/TimeBoxes/TimeBox_W0_St2_Sec6_SL2",
	 "DT/Digi/Wheel0/Station2/Sector6/TimeBoxes/TimeBox_W0_St2_Sec6_SL3"])


dtlayout(dqmitems, "Wheel0/Sector6/Station3/Trigger(DDU)_W0_St3_Sec6",
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/LocalTriggerPhi/DDU_BestQual_W0_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec6_St3"])

dtlayout(dqmitems, "Wheel0/Sector6/Station3/Signal_W0_St3_Sec6",
	["DT/Digi/Wheel0/Station3/Sector6/Occupancies/OccupancyAllHits_perCh_W0_St3_Sec6",
	 "DT/Digi/Wheel0/Station3/Sector6/TimeBoxes/TimeBox_W0_St3_Sec6_SL1"],
	["DT/Digi/Wheel0/Station3/Sector6/TimeBoxes/TimeBox_W0_St3_Sec6_SL2",
	 "DT/Digi/Wheel0/Station3/Sector6/TimeBoxes/TimeBox_W0_St3_Sec6_SL3"])


dtlayout(dqmitems, "Wheel0/Sector6/Station4/Trigger(DDU)_W0_St4_Sec6",
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec6_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec6_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/LocalTriggerPhi/DDU_BestQual_W0_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec6_St4"])

dtlayout(dqmitems, "Wheel0/Sector6/Station4/Signal_W0_St4_Sec6",
	["DT/Digi/Wheel0/Station4/Sector6/Occupancies/OccupancyAllHits_perCh_W0_St4_Sec6",
	 "DT/Digi/Wheel0/Station4/Sector6/TimeBoxes/TimeBox_W0_St4_Sec6_SL1"],
	["DT/Digi/Wheel0/Station4/Sector6/TimeBoxes/TimeBox_W0_St4_Sec6_SL3"])


dtlayout(dqmitems, "Wheel0/Sector7/Station1/Trigger(DDU)_W0_St1_Sec7",
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/LocalTriggerPhi/DDU_BestQual_W0_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec7_St1"])

dtlayout(dqmitems, "Wheel0/Sector7/Station1/Signal_W0_St1_Sec7",
	["DT/Digi/Wheel0/Station1/Sector7/Occupancies/OccupancyAllHits_perCh_W0_St1_Sec7",
	 "DT/Digi/Wheel0/Station1/Sector7/TimeBoxes/TimeBox_W0_St1_Sec7_SL1"],
	["DT/Digi/Wheel0/Station1/Sector7/TimeBoxes/TimeBox_W0_St1_Sec7_SL2",
	 "DT/Digi/Wheel0/Station1/Sector7/TimeBoxes/TimeBox_W0_St1_Sec7_SL3"])


dtlayout(dqmitems, "Wheel0/Sector7/Station2/Trigger(DDU)_W0_St2_Sec7",
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/LocalTriggerPhi/DDU_BestQual_W0_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec7_St2"])

dtlayout(dqmitems, "Wheel0/Sector7/Station2/Signal_W0_St2_Sec7",
	["DT/Digi/Wheel0/Station2/Sector7/Occupancies/OccupancyAllHits_perCh_W0_St2_Sec7",
	 "DT/Digi/Wheel0/Station2/Sector7/TimeBoxes/TimeBox_W0_St2_Sec7_SL1"],
	["DT/Digi/Wheel0/Station2/Sector7/TimeBoxes/TimeBox_W0_St2_Sec7_SL2",
	 "DT/Digi/Wheel0/Station2/Sector7/TimeBoxes/TimeBox_W0_St2_Sec7_SL3"])


dtlayout(dqmitems, "Wheel0/Sector7/Station3/Trigger(DDU)_W0_St3_Sec7",
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/LocalTriggerPhi/DDU_BestQual_W0_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec7_St3"])

dtlayout(dqmitems, "Wheel0/Sector7/Station3/Signal_W0_St3_Sec7",
	["DT/Digi/Wheel0/Station3/Sector7/Occupancies/OccupancyAllHits_perCh_W0_St3_Sec7",
	 "DT/Digi/Wheel0/Station3/Sector7/TimeBoxes/TimeBox_W0_St3_Sec7_SL1"],
	["DT/Digi/Wheel0/Station3/Sector7/TimeBoxes/TimeBox_W0_St3_Sec7_SL2",
	 "DT/Digi/Wheel0/Station3/Sector7/TimeBoxes/TimeBox_W0_St3_Sec7_SL3"])


dtlayout(dqmitems, "Wheel0/Sector7/Station4/Trigger(DDU)_W0_St4_Sec7",
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec7_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec7_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/LocalTriggerPhi/DDU_BestQual_W0_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec7_St4"])

dtlayout(dqmitems, "Wheel0/Sector7/Station4/Signal_W0_St4_Sec7",
	["DT/Digi/Wheel0/Station4/Sector7/Occupancies/OccupancyAllHits_perCh_W0_St4_Sec7",
	 "DT/Digi/Wheel0/Station4/Sector7/TimeBoxes/TimeBox_W0_St4_Sec7_SL1"],
	["DT/Digi/Wheel0/Station4/Sector7/TimeBoxes/TimeBox_W0_St4_Sec7_SL3"])


dtlayout(dqmitems, "Wheel0/Sector8/Station1/Trigger(DDU)_W0_St1_Sec8",
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/LocalTriggerPhi/DDU_BestQual_W0_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec8_St1"])

dtlayout(dqmitems, "Wheel0/Sector8/Station1/Signal_W0_St1_Sec8",
	["DT/Digi/Wheel0/Station1/Sector8/Occupancies/OccupancyAllHits_perCh_W0_St1_Sec8",
	 "DT/Digi/Wheel0/Station1/Sector8/TimeBoxes/TimeBox_W0_St1_Sec8_SL1"],
	["DT/Digi/Wheel0/Station1/Sector8/TimeBoxes/TimeBox_W0_St1_Sec8_SL2",
	 "DT/Digi/Wheel0/Station1/Sector8/TimeBoxes/TimeBox_W0_St1_Sec8_SL3"])


dtlayout(dqmitems, "Wheel0/Sector8/Station2/Trigger(DDU)_W0_St2_Sec8",
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/LocalTriggerPhi/DDU_BestQual_W0_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec8_St2"])

dtlayout(dqmitems, "Wheel0/Sector8/Station2/Signal_W0_St2_Sec8",
	["DT/Digi/Wheel0/Station2/Sector8/Occupancies/OccupancyAllHits_perCh_W0_St2_Sec8",
	 "DT/Digi/Wheel0/Station2/Sector8/TimeBoxes/TimeBox_W0_St2_Sec8_SL1"],
	["DT/Digi/Wheel0/Station2/Sector8/TimeBoxes/TimeBox_W0_St2_Sec8_SL2",
	 "DT/Digi/Wheel0/Station2/Sector8/TimeBoxes/TimeBox_W0_St2_Sec8_SL3"])


dtlayout(dqmitems, "Wheel0/Sector8/Station3/Trigger(DDU)_W0_St3_Sec8",
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/LocalTriggerPhi/DDU_BestQual_W0_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec8_St3"])

dtlayout(dqmitems, "Wheel0/Sector8/Station3/Signal_W0_St3_Sec8",
	["DT/Digi/Wheel0/Station3/Sector8/Occupancies/OccupancyAllHits_perCh_W0_St3_Sec8",
	 "DT/Digi/Wheel0/Station3/Sector8/TimeBoxes/TimeBox_W0_St3_Sec8_SL1"],
	["DT/Digi/Wheel0/Station3/Sector8/TimeBoxes/TimeBox_W0_St3_Sec8_SL2",
	 "DT/Digi/Wheel0/Station3/Sector8/TimeBoxes/TimeBox_W0_St3_Sec8_SL3"])


dtlayout(dqmitems, "Wheel0/Sector8/Station4/Trigger(DDU)_W0_St4_Sec8",
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec8_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec8_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/LocalTriggerPhi/DDU_BestQual_W0_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec8_St4"])

dtlayout(dqmitems, "Wheel0/Sector8/Station4/Signal_W0_St4_Sec8",
	["DT/Digi/Wheel0/Station4/Sector8/Occupancies/OccupancyAllHits_perCh_W0_St4_Sec8",
	 "DT/Digi/Wheel0/Station4/Sector8/TimeBoxes/TimeBox_W0_St4_Sec8_SL1"],
	["DT/Digi/Wheel0/Station4/Sector8/TimeBoxes/TimeBox_W0_St4_Sec8_SL3"])


dtlayout(dqmitems, "Wheel0/Sector9/Station1/Trigger(DDU)_W0_St1_Sec9",
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/LocalTriggerPhi/DDU_BestQual_W0_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec9_St1"])

dtlayout(dqmitems, "Wheel0/Sector9/Station1/Signal_W0_St1_Sec9",
	["DT/Digi/Wheel0/Station1/Sector9/Occupancies/OccupancyAllHits_perCh_W0_St1_Sec9",
	 "DT/Digi/Wheel0/Station1/Sector9/TimeBoxes/TimeBox_W0_St1_Sec9_SL1"],
	["DT/Digi/Wheel0/Station1/Sector9/TimeBoxes/TimeBox_W0_St1_Sec9_SL2",
	 "DT/Digi/Wheel0/Station1/Sector9/TimeBoxes/TimeBox_W0_St1_Sec9_SL3"])


dtlayout(dqmitems, "Wheel0/Sector9/Station2/Trigger(DDU)_W0_St2_Sec9",
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/LocalTriggerPhi/DDU_BestQual_W0_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec9_St2"])

dtlayout(dqmitems, "Wheel0/Sector9/Station2/Signal_W0_St2_Sec9",
	["DT/Digi/Wheel0/Station2/Sector9/Occupancies/OccupancyAllHits_perCh_W0_St2_Sec9",
	 "DT/Digi/Wheel0/Station2/Sector9/TimeBoxes/TimeBox_W0_St2_Sec9_SL1"],
	["DT/Digi/Wheel0/Station2/Sector9/TimeBoxes/TimeBox_W0_St2_Sec9_SL2",
	 "DT/Digi/Wheel0/Station2/Sector9/TimeBoxes/TimeBox_W0_St2_Sec9_SL3"])


dtlayout(dqmitems, "Wheel0/Sector9/Station3/Trigger(DDU)_W0_St3_Sec9",
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/LocalTriggerPhi/DDU_BestQual_W0_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec9_St3"])

dtlayout(dqmitems, "Wheel0/Sector9/Station3/Signal_W0_St3_Sec9",
	["DT/Digi/Wheel0/Station3/Sector9/Occupancies/OccupancyAllHits_perCh_W0_St3_Sec9",
	 "DT/Digi/Wheel0/Station3/Sector9/TimeBoxes/TimeBox_W0_St3_Sec9_SL1"],
	["DT/Digi/Wheel0/Station3/Sector9/TimeBoxes/TimeBox_W0_St3_Sec9_SL2",
	 "DT/Digi/Wheel0/Station3/Sector9/TimeBoxes/TimeBox_W0_St3_Sec9_SL3"])


dtlayout(dqmitems, "Wheel0/Sector9/Station4/Trigger(DDU)_W0_St4_Sec9",
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec9_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec9_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/LocalTriggerPhi/DDU_BestQual_W0_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec9_St4"])

dtlayout(dqmitems, "Wheel0/Sector9/Station4/Signal_W0_St4_Sec9",
	["DT/Digi/Wheel0/Station4/Sector9/Occupancies/OccupancyAllHits_perCh_W0_St4_Sec9",
	 "DT/Digi/Wheel0/Station4/Sector9/TimeBoxes/TimeBox_W0_St4_Sec9_SL1"],
	["DT/Digi/Wheel0/Station4/Sector9/TimeBoxes/TimeBox_W0_St4_Sec9_SL3"])


dtlayout(dqmitems, "Wheel0/Sector10/Station1/Trigger(DDU)_W0_St1_Sec10",
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/LocalTriggerPhi/DDU_BestQual_W0_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec10_St1"])

dtlayout(dqmitems, "Wheel0/Sector10/Station1/Signal_W0_St1_Sec10",
	["DT/Digi/Wheel0/Station1/Sector10/Occupancies/OccupancyAllHits_perCh_W0_St1_Sec10",
	 "DT/Digi/Wheel0/Station1/Sector10/TimeBoxes/TimeBox_W0_St1_Sec10_SL1"],
	["DT/Digi/Wheel0/Station1/Sector10/TimeBoxes/TimeBox_W0_St1_Sec10_SL2",
	 "DT/Digi/Wheel0/Station1/Sector10/TimeBoxes/TimeBox_W0_St1_Sec10_SL3"])


dtlayout(dqmitems, "Wheel0/Sector10/Station2/Trigger(DDU)_W0_St2_Sec10",
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/LocalTriggerPhi/DDU_BestQual_W0_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec10_St2"])

dtlayout(dqmitems, "Wheel0/Sector10/Station2/Signal_W0_St2_Sec10",
	["DT/Digi/Wheel0/Station2/Sector10/Occupancies/OccupancyAllHits_perCh_W0_St2_Sec10",
	 "DT/Digi/Wheel0/Station2/Sector10/TimeBoxes/TimeBox_W0_St2_Sec10_SL1"],
	["DT/Digi/Wheel0/Station2/Sector10/TimeBoxes/TimeBox_W0_St2_Sec10_SL2",
	 "DT/Digi/Wheel0/Station2/Sector10/TimeBoxes/TimeBox_W0_St2_Sec10_SL3"])


dtlayout(dqmitems, "Wheel0/Sector10/Station3/Trigger(DDU)_W0_St3_Sec10",
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/LocalTriggerPhi/DDU_BestQual_W0_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec10_St3"])

dtlayout(dqmitems, "Wheel0/Sector10/Station3/Signal_W0_St3_Sec10",
	["DT/Digi/Wheel0/Station3/Sector10/Occupancies/OccupancyAllHits_perCh_W0_St3_Sec10",
	 "DT/Digi/Wheel0/Station3/Sector10/TimeBoxes/TimeBox_W0_St3_Sec10_SL1"],
	["DT/Digi/Wheel0/Station3/Sector10/TimeBoxes/TimeBox_W0_St3_Sec10_SL2",
	 "DT/Digi/Wheel0/Station3/Sector10/TimeBoxes/TimeBox_W0_St3_Sec10_SL3"])


dtlayout(dqmitems, "Wheel0/Sector10/Station4/Trigger(DDU)_W0_St4_Sec10",
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec10_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec10_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/LocalTriggerPhi/DDU_BestQual_W0_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec10_St4"])

dtlayout(dqmitems, "Wheel0/Sector10/Station4/Signal_W0_St4_Sec10",
	["DT/Digi/Wheel0/Station4/Sector10/Occupancies/OccupancyAllHits_perCh_W0_St4_Sec10",
	 "DT/Digi/Wheel0/Station4/Sector10/TimeBoxes/TimeBox_W0_St4_Sec10_SL1"],
	["DT/Digi/Wheel0/Station4/Sector10/TimeBoxes/TimeBox_W0_St4_Sec10_SL3"])


dtlayout(dqmitems, "Wheel0/Sector11/Station1/Trigger(DDU)_W0_St1_Sec11",
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/LocalTriggerPhi/DDU_BestQual_W0_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec11_St1"])

dtlayout(dqmitems, "Wheel0/Sector11/Station1/Signal_W0_St1_Sec11",
	["DT/Digi/Wheel0/Station1/Sector11/Occupancies/OccupancyAllHits_perCh_W0_St1_Sec11",
	 "DT/Digi/Wheel0/Station1/Sector11/TimeBoxes/TimeBox_W0_St1_Sec11_SL1"],
	["DT/Digi/Wheel0/Station1/Sector11/TimeBoxes/TimeBox_W0_St1_Sec11_SL2",
	 "DT/Digi/Wheel0/Station1/Sector11/TimeBoxes/TimeBox_W0_St1_Sec11_SL3"])


dtlayout(dqmitems, "Wheel0/Sector11/Station2/Trigger(DDU)_W0_St2_Sec11",
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/LocalTriggerPhi/DDU_BestQual_W0_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec11_St2"])

dtlayout(dqmitems, "Wheel0/Sector11/Station2/Signal_W0_St2_Sec11",
	["DT/Digi/Wheel0/Station2/Sector11/Occupancies/OccupancyAllHits_perCh_W0_St2_Sec11",
	 "DT/Digi/Wheel0/Station2/Sector11/TimeBoxes/TimeBox_W0_St2_Sec11_SL1"],
	["DT/Digi/Wheel0/Station2/Sector11/TimeBoxes/TimeBox_W0_St2_Sec11_SL2",
	 "DT/Digi/Wheel0/Station2/Sector11/TimeBoxes/TimeBox_W0_St2_Sec11_SL3"])


dtlayout(dqmitems, "Wheel0/Sector11/Station3/Trigger(DDU)_W0_St3_Sec11",
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/LocalTriggerPhi/DDU_BestQual_W0_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec11_St3"])

dtlayout(dqmitems, "Wheel0/Sector11/Station3/Signal_W0_St3_Sec11",
	["DT/Digi/Wheel0/Station3/Sector11/Occupancies/OccupancyAllHits_perCh_W0_St3_Sec11",
	 "DT/Digi/Wheel0/Station3/Sector11/TimeBoxes/TimeBox_W0_St3_Sec11_SL1"],
	["DT/Digi/Wheel0/Station3/Sector11/TimeBoxes/TimeBox_W0_St3_Sec11_SL2",
	 "DT/Digi/Wheel0/Station3/Sector11/TimeBoxes/TimeBox_W0_St3_Sec11_SL3"])


dtlayout(dqmitems, "Wheel0/Sector11/Station4/Trigger(DDU)_W0_St4_Sec11",
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec11_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec11_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/LocalTriggerPhi/DDU_BestQual_W0_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec11_St4"])

dtlayout(dqmitems, "Wheel0/Sector11/Station4/Signal_W0_St4_Sec11",
	["DT/Digi/Wheel0/Station4/Sector11/Occupancies/OccupancyAllHits_perCh_W0_St4_Sec11",
	 "DT/Digi/Wheel0/Station4/Sector11/TimeBoxes/TimeBox_W0_St4_Sec11_SL1"],
	["DT/Digi/Wheel0/Station4/Sector11/TimeBoxes/TimeBox_W0_St4_Sec11_SL3"])


dtlayout(dqmitems, "Wheel0/Sector12/Station1/Trigger(DDU)_W0_St1_Sec12",
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/LocalTriggerPhi/DDU_BestQual_W0_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec12_St1"])

dtlayout(dqmitems, "Wheel0/Sector12/Station1/Signal_W0_St1_Sec12",
	["DT/Digi/Wheel0/Station1/Sector12/Occupancies/OccupancyAllHits_perCh_W0_St1_Sec12",
	 "DT/Digi/Wheel0/Station1/Sector12/TimeBoxes/TimeBox_W0_St1_Sec12_SL1"],
	["DT/Digi/Wheel0/Station1/Sector12/TimeBoxes/TimeBox_W0_St1_Sec12_SL2",
	 "DT/Digi/Wheel0/Station1/Sector12/TimeBoxes/TimeBox_W0_St1_Sec12_SL3"])


dtlayout(dqmitems, "Wheel0/Sector12/Station2/Trigger(DDU)_W0_St2_Sec12",
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/LocalTriggerPhi/DDU_BestQual_W0_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec12_St2"])

dtlayout(dqmitems, "Wheel0/Sector12/Station2/Signal_W0_St2_Sec12",
	["DT/Digi/Wheel0/Station2/Sector12/Occupancies/OccupancyAllHits_perCh_W0_St2_Sec12",
	 "DT/Digi/Wheel0/Station2/Sector12/TimeBoxes/TimeBox_W0_St2_Sec12_SL1"],
	["DT/Digi/Wheel0/Station2/Sector12/TimeBoxes/TimeBox_W0_St2_Sec12_SL2",
	 "DT/Digi/Wheel0/Station2/Sector12/TimeBoxes/TimeBox_W0_St2_Sec12_SL3"])


dtlayout(dqmitems, "Wheel0/Sector12/Station3/Trigger(DDU)_W0_St3_Sec12",
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/LocalTriggerPhi/DDU_BestQual_W0_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec12_St3"])

dtlayout(dqmitems, "Wheel0/Sector12/Station3/Signal_W0_St3_Sec12",
	["DT/Digi/Wheel0/Station3/Sector12/Occupancies/OccupancyAllHits_perCh_W0_St3_Sec12",
	 "DT/Digi/Wheel0/Station3/Sector12/TimeBoxes/TimeBox_W0_St3_Sec12_SL1"],
	["DT/Digi/Wheel0/Station3/Sector12/TimeBoxes/TimeBox_W0_St3_Sec12_SL2",
	 "DT/Digi/Wheel0/Station3/Sector12/TimeBoxes/TimeBox_W0_St3_Sec12_SL3"])


dtlayout(dqmitems, "Wheel0/Sector12/Station4/Trigger(DDU)_W0_St4_Sec12",
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec12_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W0_Sec12_St4"],
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/LocalTriggerPhi/DDU_BestQual_W0_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W0_Sec12_St4"])

dtlayout(dqmitems, "Wheel0/Sector12/Station4/Signal_W0_St4_Sec12",
	["DT/Digi/Wheel0/Station4/Sector12/Occupancies/OccupancyAllHits_perCh_W0_St4_Sec12",
	 "DT/Digi/Wheel0/Station4/Sector12/TimeBoxes/TimeBox_W0_St4_Sec12_SL1"],
	["DT/Digi/Wheel0/Station4/Sector12/TimeBoxes/TimeBox_W0_St4_Sec12_SL3"])


dtlayout(dqmitems, "Wheel1/Sector1/Station1/Trigger(DDU)_W1_St1_Sec1",
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station1/LocalTriggerPhi/DDU_BestQual_W1_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec1_St1"])

dtlayout(dqmitems, "Wheel1/Sector1/Station1/Signal_W1_St1_Sec1",
	["DT/Digi/Wheel1/Station1/Sector1/Occupancies/OccupancyAllHits_perCh_W1_St1_Sec1",
	 "DT/Digi/Wheel1/Station1/Sector1/TimeBoxes/TimeBox_W1_St1_Sec1_SL1"],
	["DT/Digi/Wheel1/Station1/Sector1/TimeBoxes/TimeBox_W1_St1_Sec1_SL2",
	 "DT/Digi/Wheel1/Station1/Sector1/TimeBoxes/TimeBox_W1_St1_Sec1_SL3"])


dtlayout(dqmitems, "Wheel1/Sector1/Station2/Trigger(DDU)_W1_St2_Sec1",
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station2/LocalTriggerPhi/DDU_BestQual_W1_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec1_St2"])

dtlayout(dqmitems, "Wheel1/Sector1/Station2/Signal_W1_St2_Sec1",
	["DT/Digi/Wheel1/Station2/Sector1/Occupancies/OccupancyAllHits_perCh_W1_St2_Sec1",
	 "DT/Digi/Wheel1/Station2/Sector1/TimeBoxes/TimeBox_W1_St2_Sec1_SL1"],
	["DT/Digi/Wheel1/Station2/Sector1/TimeBoxes/TimeBox_W1_St2_Sec1_SL2",
	 "DT/Digi/Wheel1/Station2/Sector1/TimeBoxes/TimeBox_W1_St2_Sec1_SL3"])


dtlayout(dqmitems, "Wheel1/Sector1/Station3/Trigger(DDU)_W1_St3_Sec1",
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station3/LocalTriggerPhi/DDU_BestQual_W1_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec1_St3"])

dtlayout(dqmitems, "Wheel1/Sector1/Station3/Signal_W1_St3_Sec1",
	["DT/Digi/Wheel1/Station3/Sector1/Occupancies/OccupancyAllHits_perCh_W1_St3_Sec1",
	 "DT/Digi/Wheel1/Station3/Sector1/TimeBoxes/TimeBox_W1_St3_Sec1_SL1"],
	["DT/Digi/Wheel1/Station3/Sector1/TimeBoxes/TimeBox_W1_St3_Sec1_SL2",
	 "DT/Digi/Wheel1/Station3/Sector1/TimeBoxes/TimeBox_W1_St3_Sec1_SL3"])


dtlayout(dqmitems, "Wheel1/Sector1/Station4/Trigger(DDU)_W1_St4_Sec1",
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec1_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec1_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station4/LocalTriggerPhi/DDU_BestQual_W1_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec1_St4"])

dtlayout(dqmitems, "Wheel1/Sector1/Station4/Signal_W1_St4_Sec1",
	["DT/Digi/Wheel1/Station4/Sector1/Occupancies/OccupancyAllHits_perCh_W1_St4_Sec1",
	 "DT/Digi/Wheel1/Station4/Sector1/TimeBoxes/TimeBox_W1_St4_Sec1_SL1"],
	["DT/Digi/Wheel1/Station4/Sector1/TimeBoxes/TimeBox_W1_St4_Sec1_SL3"])


dtlayout(dqmitems, "Wheel1/Sector2/Station1/Trigger(DDU)_W1_St1_Sec2",
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station1/LocalTriggerPhi/DDU_BestQual_W1_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec2_St1"])

dtlayout(dqmitems, "Wheel1/Sector2/Station1/Signal_W1_St1_Sec2",
	["DT/Digi/Wheel1/Station1/Sector2/Occupancies/OccupancyAllHits_perCh_W1_St1_Sec2",
	 "DT/Digi/Wheel1/Station1/Sector2/TimeBoxes/TimeBox_W1_St1_Sec2_SL1"],
	["DT/Digi/Wheel1/Station1/Sector2/TimeBoxes/TimeBox_W1_St1_Sec2_SL2",
	 "DT/Digi/Wheel1/Station1/Sector2/TimeBoxes/TimeBox_W1_St1_Sec2_SL3"])


dtlayout(dqmitems, "Wheel1/Sector2/Station2/Trigger(DDU)_W1_St2_Sec2",
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station2/LocalTriggerPhi/DDU_BestQual_W1_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec2_St2"])

dtlayout(dqmitems, "Wheel1/Sector2/Station2/Signal_W1_St2_Sec2",
	["DT/Digi/Wheel1/Station2/Sector2/Occupancies/OccupancyAllHits_perCh_W1_St2_Sec2",
	 "DT/Digi/Wheel1/Station2/Sector2/TimeBoxes/TimeBox_W1_St2_Sec2_SL1"],
	["DT/Digi/Wheel1/Station2/Sector2/TimeBoxes/TimeBox_W1_St2_Sec2_SL2",
	 "DT/Digi/Wheel1/Station2/Sector2/TimeBoxes/TimeBox_W1_St2_Sec2_SL3"])


dtlayout(dqmitems, "Wheel1/Sector2/Station3/Trigger(DDU)_W1_St3_Sec2",
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station3/LocalTriggerPhi/DDU_BestQual_W1_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec2_St3"])

dtlayout(dqmitems, "Wheel1/Sector2/Station3/Signal_W1_St3_Sec2",
	["DT/Digi/Wheel1/Station3/Sector2/Occupancies/OccupancyAllHits_perCh_W1_St3_Sec2",
	 "DT/Digi/Wheel1/Station3/Sector2/TimeBoxes/TimeBox_W1_St3_Sec2_SL1"],
	["DT/Digi/Wheel1/Station3/Sector2/TimeBoxes/TimeBox_W1_St3_Sec2_SL2",
	 "DT/Digi/Wheel1/Station3/Sector2/TimeBoxes/TimeBox_W1_St3_Sec2_SL3"])


dtlayout(dqmitems, "Wheel1/Sector2/Station4/Trigger(DDU)_W1_St4_Sec2",
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec2_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec2_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station4/LocalTriggerPhi/DDU_BestQual_W1_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec2_St4"])

dtlayout(dqmitems, "Wheel1/Sector2/Station4/Signal_W1_St4_Sec2",
	["DT/Digi/Wheel1/Station4/Sector2/Occupancies/OccupancyAllHits_perCh_W1_St4_Sec2",
	 "DT/Digi/Wheel1/Station4/Sector2/TimeBoxes/TimeBox_W1_St4_Sec2_SL1"],
	["DT/Digi/Wheel1/Station4/Sector2/TimeBoxes/TimeBox_W1_St4_Sec2_SL3"])


dtlayout(dqmitems, "Wheel1/Sector3/Station1/Trigger(DDU)_W1_St1_Sec3",
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station1/LocalTriggerPhi/DDU_BestQual_W1_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec3_St1"])

dtlayout(dqmitems, "Wheel1/Sector3/Station1/Signal_W1_St1_Sec3",
	["DT/Digi/Wheel1/Station1/Sector3/Occupancies/OccupancyAllHits_perCh_W1_St1_Sec3",
	 "DT/Digi/Wheel1/Station1/Sector3/TimeBoxes/TimeBox_W1_St1_Sec3_SL1"],
	["DT/Digi/Wheel1/Station1/Sector3/TimeBoxes/TimeBox_W1_St1_Sec3_SL2",
	 "DT/Digi/Wheel1/Station1/Sector3/TimeBoxes/TimeBox_W1_St1_Sec3_SL3"])


dtlayout(dqmitems, "Wheel1/Sector3/Station2/Trigger(DDU)_W1_St2_Sec3",
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station2/LocalTriggerPhi/DDU_BestQual_W1_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec3_St2"])

dtlayout(dqmitems, "Wheel1/Sector3/Station2/Signal_W1_St2_Sec3",
	["DT/Digi/Wheel1/Station2/Sector3/Occupancies/OccupancyAllHits_perCh_W1_St2_Sec3",
	 "DT/Digi/Wheel1/Station2/Sector3/TimeBoxes/TimeBox_W1_St2_Sec3_SL1"],
	["DT/Digi/Wheel1/Station2/Sector3/TimeBoxes/TimeBox_W1_St2_Sec3_SL2",
	 "DT/Digi/Wheel1/Station2/Sector3/TimeBoxes/TimeBox_W1_St2_Sec3_SL3"])


dtlayout(dqmitems, "Wheel1/Sector3/Station3/Trigger(DDU)_W1_St3_Sec3",
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station3/LocalTriggerPhi/DDU_BestQual_W1_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec3_St3"])

dtlayout(dqmitems, "Wheel1/Sector3/Station3/Signal_W1_St3_Sec3",
	["DT/Digi/Wheel1/Station3/Sector3/Occupancies/OccupancyAllHits_perCh_W1_St3_Sec3",
	 "DT/Digi/Wheel1/Station3/Sector3/TimeBoxes/TimeBox_W1_St3_Sec3_SL1"],
	["DT/Digi/Wheel1/Station3/Sector3/TimeBoxes/TimeBox_W1_St3_Sec3_SL2",
	 "DT/Digi/Wheel1/Station3/Sector3/TimeBoxes/TimeBox_W1_St3_Sec3_SL3"])


dtlayout(dqmitems, "Wheel1/Sector3/Station4/Trigger(DDU)_W1_St4_Sec3",
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec3_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec3_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station4/LocalTriggerPhi/DDU_BestQual_W1_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec3_St4"])

dtlayout(dqmitems, "Wheel1/Sector3/Station4/Signal_W1_St4_Sec3",
	["DT/Digi/Wheel1/Station4/Sector3/Occupancies/OccupancyAllHits_perCh_W1_St4_Sec3",
	 "DT/Digi/Wheel1/Station4/Sector3/TimeBoxes/TimeBox_W1_St4_Sec3_SL1"],
	["DT/Digi/Wheel1/Station4/Sector3/TimeBoxes/TimeBox_W1_St4_Sec3_SL3"])


dtlayout(dqmitems, "Wheel1/Sector4/Station1/Trigger(DDU)_W1_St1_Sec4",
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station1/LocalTriggerPhi/DDU_BestQual_W1_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec4_St1"])

dtlayout(dqmitems, "Wheel1/Sector4/Station1/Signal_W1_St1_Sec4",
	["DT/Digi/Wheel1/Station1/Sector4/Occupancies/OccupancyAllHits_perCh_W1_St1_Sec4",
	 "DT/Digi/Wheel1/Station1/Sector4/TimeBoxes/TimeBox_W1_St1_Sec4_SL1"],
	["DT/Digi/Wheel1/Station1/Sector4/TimeBoxes/TimeBox_W1_St1_Sec4_SL2",
	 "DT/Digi/Wheel1/Station1/Sector4/TimeBoxes/TimeBox_W1_St1_Sec4_SL3"])


dtlayout(dqmitems, "Wheel1/Sector4/Station2/Trigger(DDU)_W1_St2_Sec4",
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station2/LocalTriggerPhi/DDU_BestQual_W1_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec4_St2"])

dtlayout(dqmitems, "Wheel1/Sector4/Station2/Signal_W1_St2_Sec4",
	["DT/Digi/Wheel1/Station2/Sector4/Occupancies/OccupancyAllHits_perCh_W1_St2_Sec4",
	 "DT/Digi/Wheel1/Station2/Sector4/TimeBoxes/TimeBox_W1_St2_Sec4_SL1"],
	["DT/Digi/Wheel1/Station2/Sector4/TimeBoxes/TimeBox_W1_St2_Sec4_SL2",
	 "DT/Digi/Wheel1/Station2/Sector4/TimeBoxes/TimeBox_W1_St2_Sec4_SL3"])


dtlayout(dqmitems, "Wheel1/Sector4/Station3/Trigger(DDU)_W1_St3_Sec4",
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station3/LocalTriggerPhi/DDU_BestQual_W1_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec4_St3"])

dtlayout(dqmitems, "Wheel1/Sector4/Station3/Signal_W1_St3_Sec4",
	["DT/Digi/Wheel1/Station3/Sector4/Occupancies/OccupancyAllHits_perCh_W1_St3_Sec4",
	 "DT/Digi/Wheel1/Station3/Sector4/TimeBoxes/TimeBox_W1_St3_Sec4_SL1"],
	["DT/Digi/Wheel1/Station3/Sector4/TimeBoxes/TimeBox_W1_St3_Sec4_SL2",
	 "DT/Digi/Wheel1/Station3/Sector4/TimeBoxes/TimeBox_W1_St3_Sec4_SL3"])


dtlayout(dqmitems, "Wheel1/Sector4/Station4/Trigger(DDU)_W1_St4_Sec4",
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec4_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec4_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station4/LocalTriggerPhi/DDU_BestQual_W1_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec4_St4"])

dtlayout(dqmitems, "Wheel1/Sector4/Station4/Signal_W1_St4_Sec4",
	["DT/Digi/Wheel1/Station4/Sector4/Occupancies/OccupancyAllHits_perCh_W1_St4_Sec4",
	 "DT/Digi/Wheel1/Station4/Sector4/TimeBoxes/TimeBox_W1_St4_Sec4_SL1"],
	["DT/Digi/Wheel1/Station4/Sector4/TimeBoxes/TimeBox_W1_St4_Sec4_SL3"])


dtlayout(dqmitems, "Wheel1/Sector5/Station1/Trigger(DDU)_W1_St1_Sec5",
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station1/LocalTriggerPhi/DDU_BestQual_W1_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec5_St1"])

dtlayout(dqmitems, "Wheel1/Sector5/Station1/Signal_W1_St1_Sec5",
	["DT/Digi/Wheel1/Station1/Sector5/Occupancies/OccupancyAllHits_perCh_W1_St1_Sec5",
	 "DT/Digi/Wheel1/Station1/Sector5/TimeBoxes/TimeBox_W1_St1_Sec5_SL1"],
	["DT/Digi/Wheel1/Station1/Sector5/TimeBoxes/TimeBox_W1_St1_Sec5_SL2",
	 "DT/Digi/Wheel1/Station1/Sector5/TimeBoxes/TimeBox_W1_St1_Sec5_SL3"])


dtlayout(dqmitems, "Wheel1/Sector5/Station2/Trigger(DDU)_W1_St2_Sec5",
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station2/LocalTriggerPhi/DDU_BestQual_W1_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec5_St2"])

dtlayout(dqmitems, "Wheel1/Sector5/Station2/Signal_W1_St2_Sec5",
	["DT/Digi/Wheel1/Station2/Sector5/Occupancies/OccupancyAllHits_perCh_W1_St2_Sec5",
	 "DT/Digi/Wheel1/Station2/Sector5/TimeBoxes/TimeBox_W1_St2_Sec5_SL1"],
	["DT/Digi/Wheel1/Station2/Sector5/TimeBoxes/TimeBox_W1_St2_Sec5_SL2",
	 "DT/Digi/Wheel1/Station2/Sector5/TimeBoxes/TimeBox_W1_St2_Sec5_SL3"])


dtlayout(dqmitems, "Wheel1/Sector5/Station3/Trigger(DDU)_W1_St3_Sec5",
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station3/LocalTriggerPhi/DDU_BestQual_W1_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec5_St3"])

dtlayout(dqmitems, "Wheel1/Sector5/Station3/Signal_W1_St3_Sec5",
	["DT/Digi/Wheel1/Station3/Sector5/Occupancies/OccupancyAllHits_perCh_W1_St3_Sec5",
	 "DT/Digi/Wheel1/Station3/Sector5/TimeBoxes/TimeBox_W1_St3_Sec5_SL1"],
	["DT/Digi/Wheel1/Station3/Sector5/TimeBoxes/TimeBox_W1_St3_Sec5_SL2",
	 "DT/Digi/Wheel1/Station3/Sector5/TimeBoxes/TimeBox_W1_St3_Sec5_SL3"])


dtlayout(dqmitems, "Wheel1/Sector5/Station4/Trigger(DDU)_W1_St4_Sec5",
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec5_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec5_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station4/LocalTriggerPhi/DDU_BestQual_W1_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec5_St4"])

dtlayout(dqmitems, "Wheel1/Sector5/Station4/Signal_W1_St4_Sec5",
	["DT/Digi/Wheel1/Station4/Sector5/Occupancies/OccupancyAllHits_perCh_W1_St4_Sec5",
	 "DT/Digi/Wheel1/Station4/Sector5/TimeBoxes/TimeBox_W1_St4_Sec5_SL1"],
	["DT/Digi/Wheel1/Station4/Sector5/TimeBoxes/TimeBox_W1_St4_Sec5_SL3"])


dtlayout(dqmitems, "Wheel1/Sector6/Station1/Trigger(DDU)_W1_St1_Sec6",
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station1/LocalTriggerPhi/DDU_BestQual_W1_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec6_St1"])

dtlayout(dqmitems, "Wheel1/Sector6/Station1/Signal_W1_St1_Sec6",
	["DT/Digi/Wheel1/Station1/Sector6/Occupancies/OccupancyAllHits_perCh_W1_St1_Sec6",
	 "DT/Digi/Wheel1/Station1/Sector6/TimeBoxes/TimeBox_W1_St1_Sec6_SL1"],
	["DT/Digi/Wheel1/Station1/Sector6/TimeBoxes/TimeBox_W1_St1_Sec6_SL2",
	 "DT/Digi/Wheel1/Station1/Sector6/TimeBoxes/TimeBox_W1_St1_Sec6_SL3"])


dtlayout(dqmitems, "Wheel1/Sector6/Station2/Trigger(DDU)_W1_St2_Sec6",
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station2/LocalTriggerPhi/DDU_BestQual_W1_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec6_St2"])

dtlayout(dqmitems, "Wheel1/Sector6/Station2/Signal_W1_St2_Sec6",
	["DT/Digi/Wheel1/Station2/Sector6/Occupancies/OccupancyAllHits_perCh_W1_St2_Sec6",
	 "DT/Digi/Wheel1/Station2/Sector6/TimeBoxes/TimeBox_W1_St2_Sec6_SL1"],
	["DT/Digi/Wheel1/Station2/Sector6/TimeBoxes/TimeBox_W1_St2_Sec6_SL2",
	 "DT/Digi/Wheel1/Station2/Sector6/TimeBoxes/TimeBox_W1_St2_Sec6_SL3"])


dtlayout(dqmitems, "Wheel1/Sector6/Station3/Trigger(DDU)_W1_St3_Sec6",
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station3/LocalTriggerPhi/DDU_BestQual_W1_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec6_St3"])

dtlayout(dqmitems, "Wheel1/Sector6/Station3/Signal_W1_St3_Sec6",
	["DT/Digi/Wheel1/Station3/Sector6/Occupancies/OccupancyAllHits_perCh_W1_St3_Sec6",
	 "DT/Digi/Wheel1/Station3/Sector6/TimeBoxes/TimeBox_W1_St3_Sec6_SL1"],
	["DT/Digi/Wheel1/Station3/Sector6/TimeBoxes/TimeBox_W1_St3_Sec6_SL2",
	 "DT/Digi/Wheel1/Station3/Sector6/TimeBoxes/TimeBox_W1_St3_Sec6_SL3"])


dtlayout(dqmitems, "Wheel1/Sector6/Station4/Trigger(DDU)_W1_St4_Sec6",
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec6_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec6_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station4/LocalTriggerPhi/DDU_BestQual_W1_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec6_St4"])

dtlayout(dqmitems, "Wheel1/Sector6/Station4/Signal_W1_St4_Sec6",
	["DT/Digi/Wheel1/Station4/Sector6/Occupancies/OccupancyAllHits_perCh_W1_St4_Sec6",
	 "DT/Digi/Wheel1/Station4/Sector6/TimeBoxes/TimeBox_W1_St4_Sec6_SL1"],
	["DT/Digi/Wheel1/Station4/Sector6/TimeBoxes/TimeBox_W1_St4_Sec6_SL3"])


dtlayout(dqmitems, "Wheel1/Sector7/Station1/Trigger(DDU)_W1_St1_Sec7",
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station1/LocalTriggerPhi/DDU_BestQual_W1_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec7_St1"])

dtlayout(dqmitems, "Wheel1/Sector7/Station1/Signal_W1_St1_Sec7",
	["DT/Digi/Wheel1/Station1/Sector7/Occupancies/OccupancyAllHits_perCh_W1_St1_Sec7",
	 "DT/Digi/Wheel1/Station1/Sector7/TimeBoxes/TimeBox_W1_St1_Sec7_SL1"],
	["DT/Digi/Wheel1/Station1/Sector7/TimeBoxes/TimeBox_W1_St1_Sec7_SL2",
	 "DT/Digi/Wheel1/Station1/Sector7/TimeBoxes/TimeBox_W1_St1_Sec7_SL3"])


dtlayout(dqmitems, "Wheel1/Sector7/Station2/Trigger(DDU)_W1_St2_Sec7",
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station2/LocalTriggerPhi/DDU_BestQual_W1_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec7_St2"])

dtlayout(dqmitems, "Wheel1/Sector7/Station2/Signal_W1_St2_Sec7",
	["DT/Digi/Wheel1/Station2/Sector7/Occupancies/OccupancyAllHits_perCh_W1_St2_Sec7",
	 "DT/Digi/Wheel1/Station2/Sector7/TimeBoxes/TimeBox_W1_St2_Sec7_SL1"],
	["DT/Digi/Wheel1/Station2/Sector7/TimeBoxes/TimeBox_W1_St2_Sec7_SL2",
	 "DT/Digi/Wheel1/Station2/Sector7/TimeBoxes/TimeBox_W1_St2_Sec7_SL3"])


dtlayout(dqmitems, "Wheel1/Sector7/Station3/Trigger(DDU)_W1_St3_Sec7",
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station3/LocalTriggerPhi/DDU_BestQual_W1_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec7_St3"])

dtlayout(dqmitems, "Wheel1/Sector7/Station3/Signal_W1_St3_Sec7",
	["DT/Digi/Wheel1/Station3/Sector7/Occupancies/OccupancyAllHits_perCh_W1_St3_Sec7",
	 "DT/Digi/Wheel1/Station3/Sector7/TimeBoxes/TimeBox_W1_St3_Sec7_SL1"],
	["DT/Digi/Wheel1/Station3/Sector7/TimeBoxes/TimeBox_W1_St3_Sec7_SL2",
	 "DT/Digi/Wheel1/Station3/Sector7/TimeBoxes/TimeBox_W1_St3_Sec7_SL3"])


dtlayout(dqmitems, "Wheel1/Sector7/Station4/Trigger(DDU)_W1_St4_Sec7",
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec7_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec7_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station4/LocalTriggerPhi/DDU_BestQual_W1_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec7_St4"])

dtlayout(dqmitems, "Wheel1/Sector7/Station4/Signal_W1_St4_Sec7",
	["DT/Digi/Wheel1/Station4/Sector7/Occupancies/OccupancyAllHits_perCh_W1_St4_Sec7",
	 "DT/Digi/Wheel1/Station4/Sector7/TimeBoxes/TimeBox_W1_St4_Sec7_SL1"],
	["DT/Digi/Wheel1/Station4/Sector7/TimeBoxes/TimeBox_W1_St4_Sec7_SL3"])


dtlayout(dqmitems, "Wheel1/Sector8/Station1/Trigger(DDU)_W1_St1_Sec8",
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station1/LocalTriggerPhi/DDU_BestQual_W1_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec8_St1"])

dtlayout(dqmitems, "Wheel1/Sector8/Station1/Signal_W1_St1_Sec8",
	["DT/Digi/Wheel1/Station1/Sector8/Occupancies/OccupancyAllHits_perCh_W1_St1_Sec8",
	 "DT/Digi/Wheel1/Station1/Sector8/TimeBoxes/TimeBox_W1_St1_Sec8_SL1"],
	["DT/Digi/Wheel1/Station1/Sector8/TimeBoxes/TimeBox_W1_St1_Sec8_SL2",
	 "DT/Digi/Wheel1/Station1/Sector8/TimeBoxes/TimeBox_W1_St1_Sec8_SL3"])


dtlayout(dqmitems, "Wheel1/Sector8/Station2/Trigger(DDU)_W1_St2_Sec8",
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station2/LocalTriggerPhi/DDU_BestQual_W1_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec8_St2"])

dtlayout(dqmitems, "Wheel1/Sector8/Station2/Signal_W1_St2_Sec8",
	["DT/Digi/Wheel1/Station2/Sector8/Occupancies/OccupancyAllHits_perCh_W1_St2_Sec8",
	 "DT/Digi/Wheel1/Station2/Sector8/TimeBoxes/TimeBox_W1_St2_Sec8_SL1"],
	["DT/Digi/Wheel1/Station2/Sector8/TimeBoxes/TimeBox_W1_St2_Sec8_SL2",
	 "DT/Digi/Wheel1/Station2/Sector8/TimeBoxes/TimeBox_W1_St2_Sec8_SL3"])


dtlayout(dqmitems, "Wheel1/Sector8/Station3/Trigger(DDU)_W1_St3_Sec8",
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station3/LocalTriggerPhi/DDU_BestQual_W1_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec8_St3"])

dtlayout(dqmitems, "Wheel1/Sector8/Station3/Signal_W1_St3_Sec8",
	["DT/Digi/Wheel1/Station3/Sector8/Occupancies/OccupancyAllHits_perCh_W1_St3_Sec8",
	 "DT/Digi/Wheel1/Station3/Sector8/TimeBoxes/TimeBox_W1_St3_Sec8_SL1"],
	["DT/Digi/Wheel1/Station3/Sector8/TimeBoxes/TimeBox_W1_St3_Sec8_SL2",
	 "DT/Digi/Wheel1/Station3/Sector8/TimeBoxes/TimeBox_W1_St3_Sec8_SL3"])


dtlayout(dqmitems, "Wheel1/Sector8/Station4/Trigger(DDU)_W1_St4_Sec8",
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec8_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec8_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station4/LocalTriggerPhi/DDU_BestQual_W1_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec8_St4"])

dtlayout(dqmitems, "Wheel1/Sector8/Station4/Signal_W1_St4_Sec8",
	["DT/Digi/Wheel1/Station4/Sector8/Occupancies/OccupancyAllHits_perCh_W1_St4_Sec8",
	 "DT/Digi/Wheel1/Station4/Sector8/TimeBoxes/TimeBox_W1_St4_Sec8_SL1"],
	["DT/Digi/Wheel1/Station4/Sector8/TimeBoxes/TimeBox_W1_St4_Sec8_SL3"])


dtlayout(dqmitems, "Wheel1/Sector9/Station1/Trigger(DDU)_W1_St1_Sec9",
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station1/LocalTriggerPhi/DDU_BestQual_W1_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec9_St1"])

dtlayout(dqmitems, "Wheel1/Sector9/Station1/Signal_W1_St1_Sec9",
	["DT/Digi/Wheel1/Station1/Sector9/Occupancies/OccupancyAllHits_perCh_W1_St1_Sec9",
	 "DT/Digi/Wheel1/Station1/Sector9/TimeBoxes/TimeBox_W1_St1_Sec9_SL1"],
	["DT/Digi/Wheel1/Station1/Sector9/TimeBoxes/TimeBox_W1_St1_Sec9_SL2",
	 "DT/Digi/Wheel1/Station1/Sector9/TimeBoxes/TimeBox_W1_St1_Sec9_SL3"])


dtlayout(dqmitems, "Wheel1/Sector9/Station2/Trigger(DDU)_W1_St2_Sec9",
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station2/LocalTriggerPhi/DDU_BestQual_W1_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec9_St2"])

dtlayout(dqmitems, "Wheel1/Sector9/Station2/Signal_W1_St2_Sec9",
	["DT/Digi/Wheel1/Station2/Sector9/Occupancies/OccupancyAllHits_perCh_W1_St2_Sec9",
	 "DT/Digi/Wheel1/Station2/Sector9/TimeBoxes/TimeBox_W1_St2_Sec9_SL1"],
	["DT/Digi/Wheel1/Station2/Sector9/TimeBoxes/TimeBox_W1_St2_Sec9_SL2",
	 "DT/Digi/Wheel1/Station2/Sector9/TimeBoxes/TimeBox_W1_St2_Sec9_SL3"])


dtlayout(dqmitems, "Wheel1/Sector9/Station3/Trigger(DDU)_W1_St3_Sec9",
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station3/LocalTriggerPhi/DDU_BestQual_W1_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec9_St3"])

dtlayout(dqmitems, "Wheel1/Sector9/Station3/Signal_W1_St3_Sec9",
	["DT/Digi/Wheel1/Station3/Sector9/Occupancies/OccupancyAllHits_perCh_W1_St3_Sec9",
	 "DT/Digi/Wheel1/Station3/Sector9/TimeBoxes/TimeBox_W1_St3_Sec9_SL1"],
	["DT/Digi/Wheel1/Station3/Sector9/TimeBoxes/TimeBox_W1_St3_Sec9_SL2",
	 "DT/Digi/Wheel1/Station3/Sector9/TimeBoxes/TimeBox_W1_St3_Sec9_SL3"])


dtlayout(dqmitems, "Wheel1/Sector9/Station4/Trigger(DDU)_W1_St4_Sec9",
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec9_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec9_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station4/LocalTriggerPhi/DDU_BestQual_W1_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec9_St4"])

dtlayout(dqmitems, "Wheel1/Sector9/Station4/Signal_W1_St4_Sec9",
	["DT/Digi/Wheel1/Station4/Sector9/Occupancies/OccupancyAllHits_perCh_W1_St4_Sec9",
	 "DT/Digi/Wheel1/Station4/Sector9/TimeBoxes/TimeBox_W1_St4_Sec9_SL1"],
	["DT/Digi/Wheel1/Station4/Sector9/TimeBoxes/TimeBox_W1_St4_Sec9_SL3"])


dtlayout(dqmitems, "Wheel1/Sector10/Station1/Trigger(DDU)_W1_St1_Sec10",
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station1/LocalTriggerPhi/DDU_BestQual_W1_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec10_St1"])

dtlayout(dqmitems, "Wheel1/Sector10/Station1/Signal_W1_St1_Sec10",
	["DT/Digi/Wheel1/Station1/Sector10/Occupancies/OccupancyAllHits_perCh_W1_St1_Sec10",
	 "DT/Digi/Wheel1/Station1/Sector10/TimeBoxes/TimeBox_W1_St1_Sec10_SL1"],
	["DT/Digi/Wheel1/Station1/Sector10/TimeBoxes/TimeBox_W1_St1_Sec10_SL2",
	 "DT/Digi/Wheel1/Station1/Sector10/TimeBoxes/TimeBox_W1_St1_Sec10_SL3"])


dtlayout(dqmitems, "Wheel1/Sector10/Station2/Trigger(DDU)_W1_St2_Sec10",
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station2/LocalTriggerPhi/DDU_BestQual_W1_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec10_St2"])

dtlayout(dqmitems, "Wheel1/Sector10/Station2/Signal_W1_St2_Sec10",
	["DT/Digi/Wheel1/Station2/Sector10/Occupancies/OccupancyAllHits_perCh_W1_St2_Sec10",
	 "DT/Digi/Wheel1/Station2/Sector10/TimeBoxes/TimeBox_W1_St2_Sec10_SL1"],
	["DT/Digi/Wheel1/Station2/Sector10/TimeBoxes/TimeBox_W1_St2_Sec10_SL2",
	 "DT/Digi/Wheel1/Station2/Sector10/TimeBoxes/TimeBox_W1_St2_Sec10_SL3"])


dtlayout(dqmitems, "Wheel1/Sector10/Station3/Trigger(DDU)_W1_St3_Sec10",
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station3/LocalTriggerPhi/DDU_BestQual_W1_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec10_St3"])

dtlayout(dqmitems, "Wheel1/Sector10/Station3/Signal_W1_St3_Sec10",
	["DT/Digi/Wheel1/Station3/Sector10/Occupancies/OccupancyAllHits_perCh_W1_St3_Sec10",
	 "DT/Digi/Wheel1/Station3/Sector10/TimeBoxes/TimeBox_W1_St3_Sec10_SL1"],
	["DT/Digi/Wheel1/Station3/Sector10/TimeBoxes/TimeBox_W1_St3_Sec10_SL2",
	 "DT/Digi/Wheel1/Station3/Sector10/TimeBoxes/TimeBox_W1_St3_Sec10_SL3"])


dtlayout(dqmitems, "Wheel1/Sector10/Station4/Trigger(DDU)_W1_St4_Sec10",
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec10_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec10_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station4/LocalTriggerPhi/DDU_BestQual_W1_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec10_St4"])

dtlayout(dqmitems, "Wheel1/Sector10/Station4/Signal_W1_St4_Sec10",
	["DT/Digi/Wheel1/Station4/Sector10/Occupancies/OccupancyAllHits_perCh_W1_St4_Sec10",
	 "DT/Digi/Wheel1/Station4/Sector10/TimeBoxes/TimeBox_W1_St4_Sec10_SL1"],
	["DT/Digi/Wheel1/Station4/Sector10/TimeBoxes/TimeBox_W1_St4_Sec10_SL3"])


dtlayout(dqmitems, "Wheel1/Sector11/Station1/Trigger(DDU)_W1_St1_Sec11",
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station1/LocalTriggerPhi/DDU_BestQual_W1_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec11_St1"])

dtlayout(dqmitems, "Wheel1/Sector11/Station1/Signal_W1_St1_Sec11",
	["DT/Digi/Wheel1/Station1/Sector11/Occupancies/OccupancyAllHits_perCh_W1_St1_Sec11",
	 "DT/Digi/Wheel1/Station1/Sector11/TimeBoxes/TimeBox_W1_St1_Sec11_SL1"],
	["DT/Digi/Wheel1/Station1/Sector11/TimeBoxes/TimeBox_W1_St1_Sec11_SL2",
	 "DT/Digi/Wheel1/Station1/Sector11/TimeBoxes/TimeBox_W1_St1_Sec11_SL3"])


dtlayout(dqmitems, "Wheel1/Sector11/Station2/Trigger(DDU)_W1_St2_Sec11",
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station2/LocalTriggerPhi/DDU_BestQual_W1_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec11_St2"])

dtlayout(dqmitems, "Wheel1/Sector11/Station2/Signal_W1_St2_Sec11",
	["DT/Digi/Wheel1/Station2/Sector11/Occupancies/OccupancyAllHits_perCh_W1_St2_Sec11",
	 "DT/Digi/Wheel1/Station2/Sector11/TimeBoxes/TimeBox_W1_St2_Sec11_SL1"],
	["DT/Digi/Wheel1/Station2/Sector11/TimeBoxes/TimeBox_W1_St2_Sec11_SL2",
	 "DT/Digi/Wheel1/Station2/Sector11/TimeBoxes/TimeBox_W1_St2_Sec11_SL3"])


dtlayout(dqmitems, "Wheel1/Sector11/Station3/Trigger(DDU)_W1_St3_Sec11",
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station3/LocalTriggerPhi/DDU_BestQual_W1_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec11_St3"])

dtlayout(dqmitems, "Wheel1/Sector11/Station3/Signal_W1_St3_Sec11",
	["DT/Digi/Wheel1/Station3/Sector11/Occupancies/OccupancyAllHits_perCh_W1_St3_Sec11",
	 "DT/Digi/Wheel1/Station3/Sector11/TimeBoxes/TimeBox_W1_St3_Sec11_SL1"],
	["DT/Digi/Wheel1/Station3/Sector11/TimeBoxes/TimeBox_W1_St3_Sec11_SL2",
	 "DT/Digi/Wheel1/Station3/Sector11/TimeBoxes/TimeBox_W1_St3_Sec11_SL3"])


dtlayout(dqmitems, "Wheel1/Sector11/Station4/Trigger(DDU)_W1_St4_Sec11",
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec11_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec11_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station4/LocalTriggerPhi/DDU_BestQual_W1_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec11_St4"])

dtlayout(dqmitems, "Wheel1/Sector11/Station4/Signal_W1_St4_Sec11",
	["DT/Digi/Wheel1/Station4/Sector11/Occupancies/OccupancyAllHits_perCh_W1_St4_Sec11",
	 "DT/Digi/Wheel1/Station4/Sector11/TimeBoxes/TimeBox_W1_St4_Sec11_SL1"],
	["DT/Digi/Wheel1/Station4/Sector11/TimeBoxes/TimeBox_W1_St4_Sec11_SL3"])


dtlayout(dqmitems, "Wheel1/Sector12/Station1/Trigger(DDU)_W1_St1_Sec12",
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station1/LocalTriggerPhi/DDU_BestQual_W1_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec12_St1"])

dtlayout(dqmitems, "Wheel1/Sector12/Station1/Signal_W1_St1_Sec12",
	["DT/Digi/Wheel1/Station1/Sector12/Occupancies/OccupancyAllHits_perCh_W1_St1_Sec12",
	 "DT/Digi/Wheel1/Station1/Sector12/TimeBoxes/TimeBox_W1_St1_Sec12_SL1"],
	["DT/Digi/Wheel1/Station1/Sector12/TimeBoxes/TimeBox_W1_St1_Sec12_SL2",
	 "DT/Digi/Wheel1/Station1/Sector12/TimeBoxes/TimeBox_W1_St1_Sec12_SL3"])


dtlayout(dqmitems, "Wheel1/Sector12/Station2/Trigger(DDU)_W1_St2_Sec12",
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station2/LocalTriggerPhi/DDU_BestQual_W1_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec12_St2"])

dtlayout(dqmitems, "Wheel1/Sector12/Station2/Signal_W1_St2_Sec12",
	["DT/Digi/Wheel1/Station2/Sector12/Occupancies/OccupancyAllHits_perCh_W1_St2_Sec12",
	 "DT/Digi/Wheel1/Station2/Sector12/TimeBoxes/TimeBox_W1_St2_Sec12_SL1"],
	["DT/Digi/Wheel1/Station2/Sector12/TimeBoxes/TimeBox_W1_St2_Sec12_SL2",
	 "DT/Digi/Wheel1/Station2/Sector12/TimeBoxes/TimeBox_W1_St2_Sec12_SL3"])


dtlayout(dqmitems, "Wheel1/Sector12/Station3/Trigger(DDU)_W1_St3_Sec12",
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station3/LocalTriggerPhi/DDU_BestQual_W1_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec12_St3"])

dtlayout(dqmitems, "Wheel1/Sector12/Station3/Signal_W1_St3_Sec12",
	["DT/Digi/Wheel1/Station3/Sector12/Occupancies/OccupancyAllHits_perCh_W1_St3_Sec12",
	 "DT/Digi/Wheel1/Station3/Sector12/TimeBoxes/TimeBox_W1_St3_Sec12_SL1"],
	["DT/Digi/Wheel1/Station3/Sector12/TimeBoxes/TimeBox_W1_St3_Sec12_SL2",
	 "DT/Digi/Wheel1/Station3/Sector12/TimeBoxes/TimeBox_W1_St3_Sec12_SL3"])


dtlayout(dqmitems, "Wheel1/Sector12/Station4/Trigger(DDU)_W1_St4_Sec12",
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec12_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W1_Sec12_St4"],
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station4/LocalTriggerPhi/DDU_BestQual_W1_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W1_Sec12_St4"])

dtlayout(dqmitems, "Wheel1/Sector12/Station4/Signal_W1_St4_Sec12",
	["DT/Digi/Wheel1/Station4/Sector12/Occupancies/OccupancyAllHits_perCh_W1_St4_Sec12",
	 "DT/Digi/Wheel1/Station4/Sector12/TimeBoxes/TimeBox_W1_St4_Sec12_SL1"],
	["DT/Digi/Wheel1/Station4/Sector12/TimeBoxes/TimeBox_W1_St4_Sec12_SL3"])


dtlayout(dqmitems, "Wheel2/Sector1/Station1/Trigger(DDU)_W2_St1_Sec1",
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station1/LocalTriggerPhi/DDU_BestQual_W2_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec1_St1"])

dtlayout(dqmitems, "Wheel2/Sector1/Station1/Signal_W2_St1_Sec1",
	["DT/Digi/Wheel2/Station1/Sector1/Occupancies/OccupancyAllHits_perCh_W2_St1_Sec1",
	 "DT/Digi/Wheel2/Station1/Sector1/TimeBoxes/TimeBox_W2_St1_Sec1_SL1"],
	["DT/Digi/Wheel2/Station1/Sector1/TimeBoxes/TimeBox_W2_St1_Sec1_SL2",
	 "DT/Digi/Wheel2/Station1/Sector1/TimeBoxes/TimeBox_W2_St1_Sec1_SL3"])


dtlayout(dqmitems, "Wheel2/Sector1/Station2/Trigger(DDU)_W2_St2_Sec1",
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station2/LocalTriggerPhi/DDU_BestQual_W2_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec1_St2"])

dtlayout(dqmitems, "Wheel2/Sector1/Station2/Signal_W2_St2_Sec1",
	["DT/Digi/Wheel2/Station2/Sector1/Occupancies/OccupancyAllHits_perCh_W2_St2_Sec1",
	 "DT/Digi/Wheel2/Station2/Sector1/TimeBoxes/TimeBox_W2_St2_Sec1_SL1"],
	["DT/Digi/Wheel2/Station2/Sector1/TimeBoxes/TimeBox_W2_St2_Sec1_SL2",
	 "DT/Digi/Wheel2/Station2/Sector1/TimeBoxes/TimeBox_W2_St2_Sec1_SL3"])


dtlayout(dqmitems, "Wheel2/Sector1/Station3/Trigger(DDU)_W2_St3_Sec1",
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station3/LocalTriggerPhi/DDU_BestQual_W2_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec1_St3"])

dtlayout(dqmitems, "Wheel2/Sector1/Station3/Signal_W2_St3_Sec1",
	["DT/Digi/Wheel2/Station3/Sector1/Occupancies/OccupancyAllHits_perCh_W2_St3_Sec1",
	 "DT/Digi/Wheel2/Station3/Sector1/TimeBoxes/TimeBox_W2_St3_Sec1_SL1"],
	["DT/Digi/Wheel2/Station3/Sector1/TimeBoxes/TimeBox_W2_St3_Sec1_SL2",
	 "DT/Digi/Wheel2/Station3/Sector1/TimeBoxes/TimeBox_W2_St3_Sec1_SL3"])


dtlayout(dqmitems, "Wheel2/Sector1/Station4/Trigger(DDU)_W2_St4_Sec1",
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec1_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec1_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station4/LocalTriggerPhi/DDU_BestQual_W2_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec1_St4"])

dtlayout(dqmitems, "Wheel2/Sector1/Station4/Signal_W2_St4_Sec1",
	["DT/Digi/Wheel2/Station4/Sector1/Occupancies/OccupancyAllHits_perCh_W2_St4_Sec1",
	 "DT/Digi/Wheel2/Station4/Sector1/TimeBoxes/TimeBox_W2_St4_Sec1_SL1"],
	["DT/Digi/Wheel2/Station4/Sector1/TimeBoxes/TimeBox_W2_St4_Sec1_SL3"])


dtlayout(dqmitems, "Wheel2/Sector2/Station1/Trigger(DDU)_W2_St1_Sec2",
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station1/LocalTriggerPhi/DDU_BestQual_W2_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec2_St1"])

dtlayout(dqmitems, "Wheel2/Sector2/Station1/Signal_W2_St1_Sec2",
	["DT/Digi/Wheel2/Station1/Sector2/Occupancies/OccupancyAllHits_perCh_W2_St1_Sec2",
	 "DT/Digi/Wheel2/Station1/Sector2/TimeBoxes/TimeBox_W2_St1_Sec2_SL1"],
	["DT/Digi/Wheel2/Station1/Sector2/TimeBoxes/TimeBox_W2_St1_Sec2_SL2",
	 "DT/Digi/Wheel2/Station1/Sector2/TimeBoxes/TimeBox_W2_St1_Sec2_SL3"])


dtlayout(dqmitems, "Wheel2/Sector2/Station2/Trigger(DDU)_W2_St2_Sec2",
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station2/LocalTriggerPhi/DDU_BestQual_W2_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec2_St2"])

dtlayout(dqmitems, "Wheel2/Sector2/Station2/Signal_W2_St2_Sec2",
	["DT/Digi/Wheel2/Station2/Sector2/Occupancies/OccupancyAllHits_perCh_W2_St2_Sec2",
	 "DT/Digi/Wheel2/Station2/Sector2/TimeBoxes/TimeBox_W2_St2_Sec2_SL1"],
	["DT/Digi/Wheel2/Station2/Sector2/TimeBoxes/TimeBox_W2_St2_Sec2_SL2",
	 "DT/Digi/Wheel2/Station2/Sector2/TimeBoxes/TimeBox_W2_St2_Sec2_SL3"])


dtlayout(dqmitems, "Wheel2/Sector2/Station3/Trigger(DDU)_W2_St3_Sec2",
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station3/LocalTriggerPhi/DDU_BestQual_W2_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec2_St3"])

dtlayout(dqmitems, "Wheel2/Sector2/Station3/Signal_W2_St3_Sec2",
	["DT/Digi/Wheel2/Station3/Sector2/Occupancies/OccupancyAllHits_perCh_W2_St3_Sec2",
	 "DT/Digi/Wheel2/Station3/Sector2/TimeBoxes/TimeBox_W2_St3_Sec2_SL1"],
	["DT/Digi/Wheel2/Station3/Sector2/TimeBoxes/TimeBox_W2_St3_Sec2_SL2",
	 "DT/Digi/Wheel2/Station3/Sector2/TimeBoxes/TimeBox_W2_St3_Sec2_SL3"])


dtlayout(dqmitems, "Wheel2/Sector2/Station4/Trigger(DDU)_W2_St4_Sec2",
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec2_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec2_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station4/LocalTriggerPhi/DDU_BestQual_W2_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec2_St4"])

dtlayout(dqmitems, "Wheel2/Sector2/Station4/Signal_W2_St4_Sec2",
	["DT/Digi/Wheel2/Station4/Sector2/Occupancies/OccupancyAllHits_perCh_W2_St4_Sec2",
	 "DT/Digi/Wheel2/Station4/Sector2/TimeBoxes/TimeBox_W2_St4_Sec2_SL1"],
	["DT/Digi/Wheel2/Station4/Sector2/TimeBoxes/TimeBox_W2_St4_Sec2_SL3"])


dtlayout(dqmitems, "Wheel2/Sector3/Station1/Trigger(DDU)_W2_St1_Sec3",
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station1/LocalTriggerPhi/DDU_BestQual_W2_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec3_St1"])

dtlayout(dqmitems, "Wheel2/Sector3/Station1/Signal_W2_St1_Sec3",
	["DT/Digi/Wheel2/Station1/Sector3/Occupancies/OccupancyAllHits_perCh_W2_St1_Sec3",
	 "DT/Digi/Wheel2/Station1/Sector3/TimeBoxes/TimeBox_W2_St1_Sec3_SL1"],
	["DT/Digi/Wheel2/Station1/Sector3/TimeBoxes/TimeBox_W2_St1_Sec3_SL2",
	 "DT/Digi/Wheel2/Station1/Sector3/TimeBoxes/TimeBox_W2_St1_Sec3_SL3"])


dtlayout(dqmitems, "Wheel2/Sector3/Station2/Trigger(DDU)_W2_St2_Sec3",
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station2/LocalTriggerPhi/DDU_BestQual_W2_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec3_St2"])

dtlayout(dqmitems, "Wheel2/Sector3/Station2/Signal_W2_St2_Sec3",
	["DT/Digi/Wheel2/Station2/Sector3/Occupancies/OccupancyAllHits_perCh_W2_St2_Sec3",
	 "DT/Digi/Wheel2/Station2/Sector3/TimeBoxes/TimeBox_W2_St2_Sec3_SL1"],
	["DT/Digi/Wheel2/Station2/Sector3/TimeBoxes/TimeBox_W2_St2_Sec3_SL2",
	 "DT/Digi/Wheel2/Station2/Sector3/TimeBoxes/TimeBox_W2_St2_Sec3_SL3"])


dtlayout(dqmitems, "Wheel2/Sector3/Station3/Trigger(DDU)_W2_St3_Sec3",
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station3/LocalTriggerPhi/DDU_BestQual_W2_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec3_St3"])

dtlayout(dqmitems, "Wheel2/Sector3/Station3/Signal_W2_St3_Sec3",
	["DT/Digi/Wheel2/Station3/Sector3/Occupancies/OccupancyAllHits_perCh_W2_St3_Sec3",
	 "DT/Digi/Wheel2/Station3/Sector3/TimeBoxes/TimeBox_W2_St3_Sec3_SL1"],
	["DT/Digi/Wheel2/Station3/Sector3/TimeBoxes/TimeBox_W2_St3_Sec3_SL2",
	 "DT/Digi/Wheel2/Station3/Sector3/TimeBoxes/TimeBox_W2_St3_Sec3_SL3"])


dtlayout(dqmitems, "Wheel2/Sector3/Station4/Trigger(DDU)_W2_St4_Sec3",
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec3_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec3_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station4/LocalTriggerPhi/DDU_BestQual_W2_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec3_St4"])

dtlayout(dqmitems, "Wheel2/Sector3/Station4/Signal_W2_St4_Sec3",
	["DT/Digi/Wheel2/Station4/Sector3/Occupancies/OccupancyAllHits_perCh_W2_St4_Sec3",
	 "DT/Digi/Wheel2/Station4/Sector3/TimeBoxes/TimeBox_W2_St4_Sec3_SL1"],
	["DT/Digi/Wheel2/Station4/Sector3/TimeBoxes/TimeBox_W2_St4_Sec3_SL3"])


dtlayout(dqmitems, "Wheel2/Sector4/Station1/Trigger(DDU)_W2_St1_Sec4",
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station1/LocalTriggerPhi/DDU_BestQual_W2_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec4_St1"])

dtlayout(dqmitems, "Wheel2/Sector4/Station1/Signal_W2_St1_Sec4",
	["DT/Digi/Wheel2/Station1/Sector4/Occupancies/OccupancyAllHits_perCh_W2_St1_Sec4",
	 "DT/Digi/Wheel2/Station1/Sector4/TimeBoxes/TimeBox_W2_St1_Sec4_SL1"],
	["DT/Digi/Wheel2/Station1/Sector4/TimeBoxes/TimeBox_W2_St1_Sec4_SL2",
	 "DT/Digi/Wheel2/Station1/Sector4/TimeBoxes/TimeBox_W2_St1_Sec4_SL3"])


dtlayout(dqmitems, "Wheel2/Sector4/Station2/Trigger(DDU)_W2_St2_Sec4",
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station2/LocalTriggerPhi/DDU_BestQual_W2_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec4_St2"])

dtlayout(dqmitems, "Wheel2/Sector4/Station2/Signal_W2_St2_Sec4",
	["DT/Digi/Wheel2/Station2/Sector4/Occupancies/OccupancyAllHits_perCh_W2_St2_Sec4",
	 "DT/Digi/Wheel2/Station2/Sector4/TimeBoxes/TimeBox_W2_St2_Sec4_SL1"],
	["DT/Digi/Wheel2/Station2/Sector4/TimeBoxes/TimeBox_W2_St2_Sec4_SL2",
	 "DT/Digi/Wheel2/Station2/Sector4/TimeBoxes/TimeBox_W2_St2_Sec4_SL3"])


dtlayout(dqmitems, "Wheel2/Sector4/Station3/Trigger(DDU)_W2_St3_Sec4",
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station3/LocalTriggerPhi/DDU_BestQual_W2_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec4_St3"])

dtlayout(dqmitems, "Wheel2/Sector4/Station3/Signal_W2_St3_Sec4",
	["DT/Digi/Wheel2/Station3/Sector4/Occupancies/OccupancyAllHits_perCh_W2_St3_Sec4",
	 "DT/Digi/Wheel2/Station3/Sector4/TimeBoxes/TimeBox_W2_St3_Sec4_SL1"],
	["DT/Digi/Wheel2/Station3/Sector4/TimeBoxes/TimeBox_W2_St3_Sec4_SL2",
	 "DT/Digi/Wheel2/Station3/Sector4/TimeBoxes/TimeBox_W2_St3_Sec4_SL3"])


dtlayout(dqmitems, "Wheel2/Sector4/Station4/Trigger(DDU)_W2_St4_Sec4",
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec4_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec4_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station4/LocalTriggerPhi/DDU_BestQual_W2_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec4_St4"])

dtlayout(dqmitems, "Wheel2/Sector4/Station4/Signal_W2_St4_Sec4",
	["DT/Digi/Wheel2/Station4/Sector4/Occupancies/OccupancyAllHits_perCh_W2_St4_Sec4",
	 "DT/Digi/Wheel2/Station4/Sector4/TimeBoxes/TimeBox_W2_St4_Sec4_SL1"],
	["DT/Digi/Wheel2/Station4/Sector4/TimeBoxes/TimeBox_W2_St4_Sec4_SL3"])


dtlayout(dqmitems, "Wheel2/Sector5/Station1/Trigger(DDU)_W2_St1_Sec5",
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station1/LocalTriggerPhi/DDU_BestQual_W2_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec5_St1"])

dtlayout(dqmitems, "Wheel2/Sector5/Station1/Signal_W2_St1_Sec5",
	["DT/Digi/Wheel2/Station1/Sector5/Occupancies/OccupancyAllHits_perCh_W2_St1_Sec5",
	 "DT/Digi/Wheel2/Station1/Sector5/TimeBoxes/TimeBox_W2_St1_Sec5_SL1"],
	["DT/Digi/Wheel2/Station1/Sector5/TimeBoxes/TimeBox_W2_St1_Sec5_SL2",
	 "DT/Digi/Wheel2/Station1/Sector5/TimeBoxes/TimeBox_W2_St1_Sec5_SL3"])


dtlayout(dqmitems, "Wheel2/Sector5/Station2/Trigger(DDU)_W2_St2_Sec5",
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station2/LocalTriggerPhi/DDU_BestQual_W2_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec5_St2"])

dtlayout(dqmitems, "Wheel2/Sector5/Station2/Signal_W2_St2_Sec5",
	["DT/Digi/Wheel2/Station2/Sector5/Occupancies/OccupancyAllHits_perCh_W2_St2_Sec5",
	 "DT/Digi/Wheel2/Station2/Sector5/TimeBoxes/TimeBox_W2_St2_Sec5_SL1"],
	["DT/Digi/Wheel2/Station2/Sector5/TimeBoxes/TimeBox_W2_St2_Sec5_SL2",
	 "DT/Digi/Wheel2/Station2/Sector5/TimeBoxes/TimeBox_W2_St2_Sec5_SL3"])


dtlayout(dqmitems, "Wheel2/Sector5/Station3/Trigger(DDU)_W2_St3_Sec5",
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station3/LocalTriggerPhi/DDU_BestQual_W2_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec5_St3"])

dtlayout(dqmitems, "Wheel2/Sector5/Station3/Signal_W2_St3_Sec5",
	["DT/Digi/Wheel2/Station3/Sector5/Occupancies/OccupancyAllHits_perCh_W2_St3_Sec5",
	 "DT/Digi/Wheel2/Station3/Sector5/TimeBoxes/TimeBox_W2_St3_Sec5_SL1"],
	["DT/Digi/Wheel2/Station3/Sector5/TimeBoxes/TimeBox_W2_St3_Sec5_SL2",
	 "DT/Digi/Wheel2/Station3/Sector5/TimeBoxes/TimeBox_W2_St3_Sec5_SL3"])


dtlayout(dqmitems, "Wheel2/Sector5/Station4/Trigger(DDU)_W2_St4_Sec5",
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec5_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec5_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station4/LocalTriggerPhi/DDU_BestQual_W2_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec5_St4"])

dtlayout(dqmitems, "Wheel2/Sector5/Station4/Signal_W2_St4_Sec5",
	["DT/Digi/Wheel2/Station4/Sector5/Occupancies/OccupancyAllHits_perCh_W2_St4_Sec5",
	 "DT/Digi/Wheel2/Station4/Sector5/TimeBoxes/TimeBox_W2_St4_Sec5_SL1"],
	["DT/Digi/Wheel2/Station4/Sector5/TimeBoxes/TimeBox_W2_St4_Sec5_SL3"])


dtlayout(dqmitems, "Wheel2/Sector6/Station1/Trigger(DDU)_W2_St1_Sec6",
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station1/LocalTriggerPhi/DDU_BestQual_W2_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec6_St1"])

dtlayout(dqmitems, "Wheel2/Sector6/Station1/Signal_W2_St1_Sec6",
	["DT/Digi/Wheel2/Station1/Sector6/Occupancies/OccupancyAllHits_perCh_W2_St1_Sec6",
	 "DT/Digi/Wheel2/Station1/Sector6/TimeBoxes/TimeBox_W2_St1_Sec6_SL1"],
	["DT/Digi/Wheel2/Station1/Sector6/TimeBoxes/TimeBox_W2_St1_Sec6_SL2",
	 "DT/Digi/Wheel2/Station1/Sector6/TimeBoxes/TimeBox_W2_St1_Sec6_SL3"])


dtlayout(dqmitems, "Wheel2/Sector6/Station2/Trigger(DDU)_W2_St2_Sec6",
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station2/LocalTriggerPhi/DDU_BestQual_W2_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec6_St2"])

dtlayout(dqmitems, "Wheel2/Sector6/Station2/Signal_W2_St2_Sec6",
	["DT/Digi/Wheel2/Station2/Sector6/Occupancies/OccupancyAllHits_perCh_W2_St2_Sec6",
	 "DT/Digi/Wheel2/Station2/Sector6/TimeBoxes/TimeBox_W2_St2_Sec6_SL1"],
	["DT/Digi/Wheel2/Station2/Sector6/TimeBoxes/TimeBox_W2_St2_Sec6_SL2",
	 "DT/Digi/Wheel2/Station2/Sector6/TimeBoxes/TimeBox_W2_St2_Sec6_SL3"])


dtlayout(dqmitems, "Wheel2/Sector6/Station3/Trigger(DDU)_W2_St3_Sec6",
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station3/LocalTriggerPhi/DDU_BestQual_W2_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec6_St3"])

dtlayout(dqmitems, "Wheel2/Sector6/Station3/Signal_W2_St3_Sec6",
	["DT/Digi/Wheel2/Station3/Sector6/Occupancies/OccupancyAllHits_perCh_W2_St3_Sec6",
	 "DT/Digi/Wheel2/Station3/Sector6/TimeBoxes/TimeBox_W2_St3_Sec6_SL1"],
	["DT/Digi/Wheel2/Station3/Sector6/TimeBoxes/TimeBox_W2_St3_Sec6_SL2",
	 "DT/Digi/Wheel2/Station3/Sector6/TimeBoxes/TimeBox_W2_St3_Sec6_SL3"])


dtlayout(dqmitems, "Wheel2/Sector6/Station4/Trigger(DDU)_W2_St4_Sec6",
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec6_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec6_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station4/LocalTriggerPhi/DDU_BestQual_W2_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec6_St4"])

dtlayout(dqmitems, "Wheel2/Sector6/Station4/Signal_W2_St4_Sec6",
	["DT/Digi/Wheel2/Station4/Sector6/Occupancies/OccupancyAllHits_perCh_W2_St4_Sec6",
	 "DT/Digi/Wheel2/Station4/Sector6/TimeBoxes/TimeBox_W2_St4_Sec6_SL1"],
	["DT/Digi/Wheel2/Station4/Sector6/TimeBoxes/TimeBox_W2_St4_Sec6_SL3"])


dtlayout(dqmitems, "Wheel2/Sector7/Station1/Trigger(DDU)_W2_St1_Sec7",
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station1/LocalTriggerPhi/DDU_BestQual_W2_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec7_St1"])

dtlayout(dqmitems, "Wheel2/Sector7/Station1/Signal_W2_St1_Sec7",
	["DT/Digi/Wheel2/Station1/Sector7/Occupancies/OccupancyAllHits_perCh_W2_St1_Sec7",
	 "DT/Digi/Wheel2/Station1/Sector7/TimeBoxes/TimeBox_W2_St1_Sec7_SL1"],
	["DT/Digi/Wheel2/Station1/Sector7/TimeBoxes/TimeBox_W2_St1_Sec7_SL2",
	 "DT/Digi/Wheel2/Station1/Sector7/TimeBoxes/TimeBox_W2_St1_Sec7_SL3"])


dtlayout(dqmitems, "Wheel2/Sector7/Station2/Trigger(DDU)_W2_St2_Sec7",
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station2/LocalTriggerPhi/DDU_BestQual_W2_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec7_St2"])

dtlayout(dqmitems, "Wheel2/Sector7/Station2/Signal_W2_St2_Sec7",
	["DT/Digi/Wheel2/Station2/Sector7/Occupancies/OccupancyAllHits_perCh_W2_St2_Sec7",
	 "DT/Digi/Wheel2/Station2/Sector7/TimeBoxes/TimeBox_W2_St2_Sec7_SL1"],
	["DT/Digi/Wheel2/Station2/Sector7/TimeBoxes/TimeBox_W2_St2_Sec7_SL2",
	 "DT/Digi/Wheel2/Station2/Sector7/TimeBoxes/TimeBox_W2_St2_Sec7_SL3"])


dtlayout(dqmitems, "Wheel2/Sector7/Station3/Trigger(DDU)_W2_St3_Sec7",
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station3/LocalTriggerPhi/DDU_BestQual_W2_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec7_St3"])

dtlayout(dqmitems, "Wheel2/Sector7/Station3/Signal_W2_St3_Sec7",
	["DT/Digi/Wheel2/Station3/Sector7/Occupancies/OccupancyAllHits_perCh_W2_St3_Sec7",
	 "DT/Digi/Wheel2/Station3/Sector7/TimeBoxes/TimeBox_W2_St3_Sec7_SL1"],
	["DT/Digi/Wheel2/Station3/Sector7/TimeBoxes/TimeBox_W2_St3_Sec7_SL2",
	 "DT/Digi/Wheel2/Station3/Sector7/TimeBoxes/TimeBox_W2_St3_Sec7_SL3"])


dtlayout(dqmitems, "Wheel2/Sector7/Station4/Trigger(DDU)_W2_St4_Sec7",
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec7_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec7_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station4/LocalTriggerPhi/DDU_BestQual_W2_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec7_St4"])

dtlayout(dqmitems, "Wheel2/Sector7/Station4/Signal_W2_St4_Sec7",
	["DT/Digi/Wheel2/Station4/Sector7/Occupancies/OccupancyAllHits_perCh_W2_St4_Sec7",
	 "DT/Digi/Wheel2/Station4/Sector7/TimeBoxes/TimeBox_W2_St4_Sec7_SL1"],
	["DT/Digi/Wheel2/Station4/Sector7/TimeBoxes/TimeBox_W2_St4_Sec7_SL3"])


dtlayout(dqmitems, "Wheel2/Sector8/Station1/Trigger(DDU)_W2_St1_Sec8",
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station1/LocalTriggerPhi/DDU_BestQual_W2_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec8_St1"])

dtlayout(dqmitems, "Wheel2/Sector8/Station1/Signal_W2_St1_Sec8",
	["DT/Digi/Wheel2/Station1/Sector8/Occupancies/OccupancyAllHits_perCh_W2_St1_Sec8",
	 "DT/Digi/Wheel2/Station1/Sector8/TimeBoxes/TimeBox_W2_St1_Sec8_SL1"],
	["DT/Digi/Wheel2/Station1/Sector8/TimeBoxes/TimeBox_W2_St1_Sec8_SL2",
	 "DT/Digi/Wheel2/Station1/Sector8/TimeBoxes/TimeBox_W2_St1_Sec8_SL3"])


dtlayout(dqmitems, "Wheel2/Sector8/Station2/Trigger(DDU)_W2_St2_Sec8",
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station2/LocalTriggerPhi/DDU_BestQual_W2_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec8_St2"])

dtlayout(dqmitems, "Wheel2/Sector8/Station2/Signal_W2_St2_Sec8",
	["DT/Digi/Wheel2/Station2/Sector8/Occupancies/OccupancyAllHits_perCh_W2_St2_Sec8",
	 "DT/Digi/Wheel2/Station2/Sector8/TimeBoxes/TimeBox_W2_St2_Sec8_SL1"],
	["DT/Digi/Wheel2/Station2/Sector8/TimeBoxes/TimeBox_W2_St2_Sec8_SL2",
	 "DT/Digi/Wheel2/Station2/Sector8/TimeBoxes/TimeBox_W2_St2_Sec8_SL3"])


dtlayout(dqmitems, "Wheel2/Sector8/Station3/Trigger(DDU)_W2_St3_Sec8",
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station3/LocalTriggerPhi/DDU_BestQual_W2_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec8_St3"])

dtlayout(dqmitems, "Wheel2/Sector8/Station3/Signal_W2_St3_Sec8",
	["DT/Digi/Wheel2/Station3/Sector8/Occupancies/OccupancyAllHits_perCh_W2_St3_Sec8",
	 "DT/Digi/Wheel2/Station3/Sector8/TimeBoxes/TimeBox_W2_St3_Sec8_SL1"],
	["DT/Digi/Wheel2/Station3/Sector8/TimeBoxes/TimeBox_W2_St3_Sec8_SL2",
	 "DT/Digi/Wheel2/Station3/Sector8/TimeBoxes/TimeBox_W2_St3_Sec8_SL3"])


dtlayout(dqmitems, "Wheel2/Sector8/Station4/Trigger(DDU)_W2_St4_Sec8",
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec8_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec8_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station4/LocalTriggerPhi/DDU_BestQual_W2_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec8_St4"])

dtlayout(dqmitems, "Wheel2/Sector8/Station4/Signal_W2_St4_Sec8",
	["DT/Digi/Wheel2/Station4/Sector8/Occupancies/OccupancyAllHits_perCh_W2_St4_Sec8",
	 "DT/Digi/Wheel2/Station4/Sector8/TimeBoxes/TimeBox_W2_St4_Sec8_SL1"],
	["DT/Digi/Wheel2/Station4/Sector8/TimeBoxes/TimeBox_W2_St4_Sec8_SL3"])


dtlayout(dqmitems, "Wheel2/Sector9/Station1/Trigger(DDU)_W2_St1_Sec9",
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station1/LocalTriggerPhi/DDU_BestQual_W2_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec9_St1"])

dtlayout(dqmitems, "Wheel2/Sector9/Station1/Signal_W2_St1_Sec9",
	["DT/Digi/Wheel2/Station1/Sector9/Occupancies/OccupancyAllHits_perCh_W2_St1_Sec9",
	 "DT/Digi/Wheel2/Station1/Sector9/TimeBoxes/TimeBox_W2_St1_Sec9_SL1"],
	["DT/Digi/Wheel2/Station1/Sector9/TimeBoxes/TimeBox_W2_St1_Sec9_SL2",
	 "DT/Digi/Wheel2/Station1/Sector9/TimeBoxes/TimeBox_W2_St1_Sec9_SL3"])


dtlayout(dqmitems, "Wheel2/Sector9/Station2/Trigger(DDU)_W2_St2_Sec9",
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station2/LocalTriggerPhi/DDU_BestQual_W2_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec9_St2"])

dtlayout(dqmitems, "Wheel2/Sector9/Station2/Signal_W2_St2_Sec9",
	["DT/Digi/Wheel2/Station2/Sector9/Occupancies/OccupancyAllHits_perCh_W2_St2_Sec9",
	 "DT/Digi/Wheel2/Station2/Sector9/TimeBoxes/TimeBox_W2_St2_Sec9_SL1"],
	["DT/Digi/Wheel2/Station2/Sector9/TimeBoxes/TimeBox_W2_St2_Sec9_SL2",
	 "DT/Digi/Wheel2/Station2/Sector9/TimeBoxes/TimeBox_W2_St2_Sec9_SL3"])


dtlayout(dqmitems, "Wheel2/Sector9/Station3/Trigger(DDU)_W2_St3_Sec9",
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station3/LocalTriggerPhi/DDU_BestQual_W2_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec9_St3"])

dtlayout(dqmitems, "Wheel2/Sector9/Station3/Signal_W2_St3_Sec9",
	["DT/Digi/Wheel2/Station3/Sector9/Occupancies/OccupancyAllHits_perCh_W2_St3_Sec9",
	 "DT/Digi/Wheel2/Station3/Sector9/TimeBoxes/TimeBox_W2_St3_Sec9_SL1"],
	["DT/Digi/Wheel2/Station3/Sector9/TimeBoxes/TimeBox_W2_St3_Sec9_SL2",
	 "DT/Digi/Wheel2/Station3/Sector9/TimeBoxes/TimeBox_W2_St3_Sec9_SL3"])


dtlayout(dqmitems, "Wheel2/Sector9/Station4/Trigger(DDU)_W2_St4_Sec9",
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec9_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec9_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station4/LocalTriggerPhi/DDU_BestQual_W2_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec9_St4"])

dtlayout(dqmitems, "Wheel2/Sector9/Station4/Signal_W2_St4_Sec9",
	["DT/Digi/Wheel2/Station4/Sector9/Occupancies/OccupancyAllHits_perCh_W2_St4_Sec9",
	 "DT/Digi/Wheel2/Station4/Sector9/TimeBoxes/TimeBox_W2_St4_Sec9_SL1"],
	["DT/Digi/Wheel2/Station4/Sector9/TimeBoxes/TimeBox_W2_St4_Sec9_SL3"])


dtlayout(dqmitems, "Wheel2/Sector10/Station1/Trigger(DDU)_W2_St1_Sec10",
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station1/LocalTriggerPhi/DDU_BestQual_W2_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec10_St1"])

dtlayout(dqmitems, "Wheel2/Sector10/Station1/Signal_W2_St1_Sec10",
	["DT/Digi/Wheel2/Station1/Sector10/Occupancies/OccupancyAllHits_perCh_W2_St1_Sec10",
	 "DT/Digi/Wheel2/Station1/Sector10/TimeBoxes/TimeBox_W2_St1_Sec10_SL1"],
	["DT/Digi/Wheel2/Station1/Sector10/TimeBoxes/TimeBox_W2_St1_Sec10_SL2",
	 "DT/Digi/Wheel2/Station1/Sector10/TimeBoxes/TimeBox_W2_St1_Sec10_SL3"])


dtlayout(dqmitems, "Wheel2/Sector10/Station2/Trigger(DDU)_W2_St2_Sec10",
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station2/LocalTriggerPhi/DDU_BestQual_W2_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec10_St2"])

dtlayout(dqmitems, "Wheel2/Sector10/Station2/Signal_W2_St2_Sec10",
	["DT/Digi/Wheel2/Station2/Sector10/Occupancies/OccupancyAllHits_perCh_W2_St2_Sec10",
	 "DT/Digi/Wheel2/Station2/Sector10/TimeBoxes/TimeBox_W2_St2_Sec10_SL1"],
	["DT/Digi/Wheel2/Station2/Sector10/TimeBoxes/TimeBox_W2_St2_Sec10_SL2",
	 "DT/Digi/Wheel2/Station2/Sector10/TimeBoxes/TimeBox_W2_St2_Sec10_SL3"])


dtlayout(dqmitems, "Wheel2/Sector10/Station3/Trigger(DDU)_W2_St3_Sec10",
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station3/LocalTriggerPhi/DDU_BestQual_W2_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec10_St3"])

dtlayout(dqmitems, "Wheel2/Sector10/Station3/Signal_W2_St3_Sec10",
	["DT/Digi/Wheel2/Station3/Sector10/Occupancies/OccupancyAllHits_perCh_W2_St3_Sec10",
	 "DT/Digi/Wheel2/Station3/Sector10/TimeBoxes/TimeBox_W2_St3_Sec10_SL1"],
	["DT/Digi/Wheel2/Station3/Sector10/TimeBoxes/TimeBox_W2_St3_Sec10_SL2",
	 "DT/Digi/Wheel2/Station3/Sector10/TimeBoxes/TimeBox_W2_St3_Sec10_SL3"])


dtlayout(dqmitems, "Wheel2/Sector10/Station4/Trigger(DDU)_W2_St4_Sec10",
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec10_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec10_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station4/LocalTriggerPhi/DDU_BestQual_W2_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec10_St4"])

dtlayout(dqmitems, "Wheel2/Sector10/Station4/Signal_W2_St4_Sec10",
	["DT/Digi/Wheel2/Station4/Sector10/Occupancies/OccupancyAllHits_perCh_W2_St4_Sec10",
	 "DT/Digi/Wheel2/Station4/Sector10/TimeBoxes/TimeBox_W2_St4_Sec10_SL1"],
	["DT/Digi/Wheel2/Station4/Sector10/TimeBoxes/TimeBox_W2_St4_Sec10_SL3"])


dtlayout(dqmitems, "Wheel2/Sector11/Station1/Trigger(DDU)_W2_St1_Sec11",
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station1/LocalTriggerPhi/DDU_BestQual_W2_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec11_St1"])

dtlayout(dqmitems, "Wheel2/Sector11/Station1/Signal_W2_St1_Sec11",
	["DT/Digi/Wheel2/Station1/Sector11/Occupancies/OccupancyAllHits_perCh_W2_St1_Sec11",
	 "DT/Digi/Wheel2/Station1/Sector11/TimeBoxes/TimeBox_W2_St1_Sec11_SL1"],
	["DT/Digi/Wheel2/Station1/Sector11/TimeBoxes/TimeBox_W2_St1_Sec11_SL2",
	 "DT/Digi/Wheel2/Station1/Sector11/TimeBoxes/TimeBox_W2_St1_Sec11_SL3"])


dtlayout(dqmitems, "Wheel2/Sector11/Station2/Trigger(DDU)_W2_St2_Sec11",
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station2/LocalTriggerPhi/DDU_BestQual_W2_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec11_St2"])

dtlayout(dqmitems, "Wheel2/Sector11/Station2/Signal_W2_St2_Sec11",
	["DT/Digi/Wheel2/Station2/Sector11/Occupancies/OccupancyAllHits_perCh_W2_St2_Sec11",
	 "DT/Digi/Wheel2/Station2/Sector11/TimeBoxes/TimeBox_W2_St2_Sec11_SL1"],
	["DT/Digi/Wheel2/Station2/Sector11/TimeBoxes/TimeBox_W2_St2_Sec11_SL2",
	 "DT/Digi/Wheel2/Station2/Sector11/TimeBoxes/TimeBox_W2_St2_Sec11_SL3"])


dtlayout(dqmitems, "Wheel2/Sector11/Station3/Trigger(DDU)_W2_St3_Sec11",
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station3/LocalTriggerPhi/DDU_BestQual_W2_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec11_St3"])

dtlayout(dqmitems, "Wheel2/Sector11/Station3/Signal_W2_St3_Sec11",
	["DT/Digi/Wheel2/Station3/Sector11/Occupancies/OccupancyAllHits_perCh_W2_St3_Sec11",
	 "DT/Digi/Wheel2/Station3/Sector11/TimeBoxes/TimeBox_W2_St3_Sec11_SL1"],
	["DT/Digi/Wheel2/Station3/Sector11/TimeBoxes/TimeBox_W2_St3_Sec11_SL2",
	 "DT/Digi/Wheel2/Station3/Sector11/TimeBoxes/TimeBox_W2_St3_Sec11_SL3"])


dtlayout(dqmitems, "Wheel2/Sector11/Station4/Trigger(DDU)_W2_St4_Sec11",
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec11_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec11_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station4/LocalTriggerPhi/DDU_BestQual_W2_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec11_St4"])

dtlayout(dqmitems, "Wheel2/Sector11/Station4/Signal_W2_St4_Sec11",
	["DT/Digi/Wheel2/Station4/Sector11/Occupancies/OccupancyAllHits_perCh_W2_St4_Sec11",
	 "DT/Digi/Wheel2/Station4/Sector11/TimeBoxes/TimeBox_W2_St4_Sec11_SL1"],
	["DT/Digi/Wheel2/Station4/Sector11/TimeBoxes/TimeBox_W2_St4_Sec11_SL3"])


dtlayout(dqmitems, "Wheel2/Sector12/Station1/Trigger(DDU)_W2_St1_Sec12",
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station1/LocalTriggerPhi/DDU_BestQual_W2_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec12_St1"])

dtlayout(dqmitems, "Wheel2/Sector12/Station1/Signal_W2_St1_Sec12",
	["DT/Digi/Wheel2/Station1/Sector12/Occupancies/OccupancyAllHits_perCh_W2_St1_Sec12",
	 "DT/Digi/Wheel2/Station1/Sector12/TimeBoxes/TimeBox_W2_St1_Sec12_SL1"],
	["DT/Digi/Wheel2/Station1/Sector12/TimeBoxes/TimeBox_W2_St1_Sec12_SL2",
	 "DT/Digi/Wheel2/Station1/Sector12/TimeBoxes/TimeBox_W2_St1_Sec12_SL3"])


dtlayout(dqmitems, "Wheel2/Sector12/Station2/Trigger(DDU)_W2_St2_Sec12",
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station2/LocalTriggerPhi/DDU_BestQual_W2_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec12_St2"])

dtlayout(dqmitems, "Wheel2/Sector12/Station2/Signal_W2_St2_Sec12",
	["DT/Digi/Wheel2/Station2/Sector12/Occupancies/OccupancyAllHits_perCh_W2_St2_Sec12",
	 "DT/Digi/Wheel2/Station2/Sector12/TimeBoxes/TimeBox_W2_St2_Sec12_SL1"],
	["DT/Digi/Wheel2/Station2/Sector12/TimeBoxes/TimeBox_W2_St2_Sec12_SL2",
	 "DT/Digi/Wheel2/Station2/Sector12/TimeBoxes/TimeBox_W2_St2_Sec12_SL3"])


dtlayout(dqmitems, "Wheel2/Sector12/Station3/Trigger(DDU)_W2_St3_Sec12",
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station3/LocalTriggerPhi/DDU_BestQual_W2_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec12_St3"])

dtlayout(dqmitems, "Wheel2/Sector12/Station3/Signal_W2_St3_Sec12",
	["DT/Digi/Wheel2/Station3/Sector12/Occupancies/OccupancyAllHits_perCh_W2_St3_Sec12",
	 "DT/Digi/Wheel2/Station3/Sector12/TimeBoxes/TimeBox_W2_St3_Sec12_SL1"],
	["DT/Digi/Wheel2/Station3/Sector12/TimeBoxes/TimeBox_W2_St3_Sec12_SL2",
	 "DT/Digi/Wheel2/Station3/Sector12/TimeBoxes/TimeBox_W2_St3_Sec12_SL3"])


dtlayout(dqmitems, "Wheel2/Sector12/Station4/Trigger(DDU)_W2_St4_Sec12",
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec12_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W2_Sec12_St4"],
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station4/LocalTriggerPhi/DDU_BestQual_W2_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W2_Sec12_St4"])

dtlayout(dqmitems, "Wheel2/Sector12/Station4/Signal_W2_St4_Sec12",
	["DT/Digi/Wheel2/Station4/Sector12/Occupancies/OccupancyAllHits_perCh_W2_St4_Sec12",
	 "DT/Digi/Wheel2/Station4/Sector12/TimeBoxes/TimeBox_W2_St4_Sec12_SL1"],
	["DT/Digi/Wheel2/Station4/Sector12/TimeBoxes/TimeBox_W2_St4_Sec12_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector1/Station1/Trigger(DDU)_W-1_St1_Sec1",
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station1/LocalTriggerPhi/DDU_BestQual_W-1_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec1_St1"])

dtlayout(dqmitems, "Wheel-1/Sector1/Station1/Signal_W-1_St1_Sec1",
	["DT/Digi/Wheel-1/Station1/Sector1/Occupancies/OccupancyAllHits_perCh_W-1_St1_Sec1",
	 "DT/Digi/Wheel-1/Station1/Sector1/TimeBoxes/TimeBox_W-1_St1_Sec1_SL1"],
	["DT/Digi/Wheel-1/Station1/Sector1/TimeBoxes/TimeBox_W-1_St1_Sec1_SL2",
	 "DT/Digi/Wheel-1/Station1/Sector1/TimeBoxes/TimeBox_W-1_St1_Sec1_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector1/Station2/Trigger(DDU)_W-1_St2_Sec1",
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station2/LocalTriggerPhi/DDU_BestQual_W-1_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec1_St2"])

dtlayout(dqmitems, "Wheel-1/Sector1/Station2/Signal_W-1_St2_Sec1",
	["DT/Digi/Wheel-1/Station2/Sector1/Occupancies/OccupancyAllHits_perCh_W-1_St2_Sec1",
	 "DT/Digi/Wheel-1/Station2/Sector1/TimeBoxes/TimeBox_W-1_St2_Sec1_SL1"],
	["DT/Digi/Wheel-1/Station2/Sector1/TimeBoxes/TimeBox_W-1_St2_Sec1_SL2",
	 "DT/Digi/Wheel-1/Station2/Sector1/TimeBoxes/TimeBox_W-1_St2_Sec1_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector1/Station3/Trigger(DDU)_W-1_St3_Sec1",
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station3/LocalTriggerPhi/DDU_BestQual_W-1_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec1_St3"])

dtlayout(dqmitems, "Wheel-1/Sector1/Station3/Signal_W-1_St3_Sec1",
	["DT/Digi/Wheel-1/Station3/Sector1/Occupancies/OccupancyAllHits_perCh_W-1_St3_Sec1",
	 "DT/Digi/Wheel-1/Station3/Sector1/TimeBoxes/TimeBox_W-1_St3_Sec1_SL1"],
	["DT/Digi/Wheel-1/Station3/Sector1/TimeBoxes/TimeBox_W-1_St3_Sec1_SL2",
	 "DT/Digi/Wheel-1/Station3/Sector1/TimeBoxes/TimeBox_W-1_St3_Sec1_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector1/Station4/Trigger(DDU)_W-1_St4_Sec1",
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec1_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec1_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station4/LocalTriggerPhi/DDU_BestQual_W-1_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec1_St4"])

dtlayout(dqmitems, "Wheel-1/Sector1/Station4/Signal_W-1_St4_Sec1",
	["DT/Digi/Wheel-1/Station4/Sector1/Occupancies/OccupancyAllHits_perCh_W-1_St4_Sec1",
	 "DT/Digi/Wheel-1/Station4/Sector1/TimeBoxes/TimeBox_W-1_St4_Sec1_SL1"],
	["DT/Digi/Wheel-1/Station4/Sector1/TimeBoxes/TimeBox_W-1_St4_Sec1_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector2/Station1/Trigger(DDU)_W-1_St1_Sec2",
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station1/LocalTriggerPhi/DDU_BestQual_W-1_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec2_St1"])

dtlayout(dqmitems, "Wheel-1/Sector2/Station1/Signal_W-1_St1_Sec2",
	["DT/Digi/Wheel-1/Station1/Sector2/Occupancies/OccupancyAllHits_perCh_W-1_St1_Sec2",
	 "DT/Digi/Wheel-1/Station1/Sector2/TimeBoxes/TimeBox_W-1_St1_Sec2_SL1"],
	["DT/Digi/Wheel-1/Station1/Sector2/TimeBoxes/TimeBox_W-1_St1_Sec2_SL2",
	 "DT/Digi/Wheel-1/Station1/Sector2/TimeBoxes/TimeBox_W-1_St1_Sec2_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector2/Station2/Trigger(DDU)_W-1_St2_Sec2",
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station2/LocalTriggerPhi/DDU_BestQual_W-1_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec2_St2"])

dtlayout(dqmitems, "Wheel-1/Sector2/Station2/Signal_W-1_St2_Sec2",
	["DT/Digi/Wheel-1/Station2/Sector2/Occupancies/OccupancyAllHits_perCh_W-1_St2_Sec2",
	 "DT/Digi/Wheel-1/Station2/Sector2/TimeBoxes/TimeBox_W-1_St2_Sec2_SL1"],
	["DT/Digi/Wheel-1/Station2/Sector2/TimeBoxes/TimeBox_W-1_St2_Sec2_SL2",
	 "DT/Digi/Wheel-1/Station2/Sector2/TimeBoxes/TimeBox_W-1_St2_Sec2_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector2/Station3/Trigger(DDU)_W-1_St3_Sec2",
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station3/LocalTriggerPhi/DDU_BestQual_W-1_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec2_St3"])

dtlayout(dqmitems, "Wheel-1/Sector2/Station3/Signal_W-1_St3_Sec2",
	["DT/Digi/Wheel-1/Station3/Sector2/Occupancies/OccupancyAllHits_perCh_W-1_St3_Sec2",
	 "DT/Digi/Wheel-1/Station3/Sector2/TimeBoxes/TimeBox_W-1_St3_Sec2_SL1"],
	["DT/Digi/Wheel-1/Station3/Sector2/TimeBoxes/TimeBox_W-1_St3_Sec2_SL2",
	 "DT/Digi/Wheel-1/Station3/Sector2/TimeBoxes/TimeBox_W-1_St3_Sec2_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector2/Station4/Trigger(DDU)_W-1_St4_Sec2",
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec2_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec2_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station4/LocalTriggerPhi/DDU_BestQual_W-1_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec2_St4"])

dtlayout(dqmitems, "Wheel-1/Sector2/Station4/Signal_W-1_St4_Sec2",
	["DT/Digi/Wheel-1/Station4/Sector2/Occupancies/OccupancyAllHits_perCh_W-1_St4_Sec2",
	 "DT/Digi/Wheel-1/Station4/Sector2/TimeBoxes/TimeBox_W-1_St4_Sec2_SL1"],
	["DT/Digi/Wheel-1/Station4/Sector2/TimeBoxes/TimeBox_W-1_St4_Sec2_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector3/Station1/Trigger(DDU)_W-1_St1_Sec3",
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station1/LocalTriggerPhi/DDU_BestQual_W-1_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec3_St1"])

dtlayout(dqmitems, "Wheel-1/Sector3/Station1/Signal_W-1_St1_Sec3",
	["DT/Digi/Wheel-1/Station1/Sector3/Occupancies/OccupancyAllHits_perCh_W-1_St1_Sec3",
	 "DT/Digi/Wheel-1/Station1/Sector3/TimeBoxes/TimeBox_W-1_St1_Sec3_SL1"],
	["DT/Digi/Wheel-1/Station1/Sector3/TimeBoxes/TimeBox_W-1_St1_Sec3_SL2",
	 "DT/Digi/Wheel-1/Station1/Sector3/TimeBoxes/TimeBox_W-1_St1_Sec3_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector3/Station2/Trigger(DDU)_W-1_St2_Sec3",
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station2/LocalTriggerPhi/DDU_BestQual_W-1_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec3_St2"])

dtlayout(dqmitems, "Wheel-1/Sector3/Station2/Signal_W-1_St2_Sec3",
	["DT/Digi/Wheel-1/Station2/Sector3/Occupancies/OccupancyAllHits_perCh_W-1_St2_Sec3",
	 "DT/Digi/Wheel-1/Station2/Sector3/TimeBoxes/TimeBox_W-1_St2_Sec3_SL1"],
	["DT/Digi/Wheel-1/Station2/Sector3/TimeBoxes/TimeBox_W-1_St2_Sec3_SL2",
	 "DT/Digi/Wheel-1/Station2/Sector3/TimeBoxes/TimeBox_W-1_St2_Sec3_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector3/Station3/Trigger(DDU)_W-1_St3_Sec3",
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station3/LocalTriggerPhi/DDU_BestQual_W-1_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec3_St3"])

dtlayout(dqmitems, "Wheel-1/Sector3/Station3/Signal_W-1_St3_Sec3",
	["DT/Digi/Wheel-1/Station3/Sector3/Occupancies/OccupancyAllHits_perCh_W-1_St3_Sec3",
	 "DT/Digi/Wheel-1/Station3/Sector3/TimeBoxes/TimeBox_W-1_St3_Sec3_SL1"],
	["DT/Digi/Wheel-1/Station3/Sector3/TimeBoxes/TimeBox_W-1_St3_Sec3_SL2",
	 "DT/Digi/Wheel-1/Station3/Sector3/TimeBoxes/TimeBox_W-1_St3_Sec3_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector3/Station4/Trigger(DDU)_W-1_St4_Sec3",
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec3_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec3_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station4/LocalTriggerPhi/DDU_BestQual_W-1_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec3_St4"])

dtlayout(dqmitems, "Wheel-1/Sector3/Station4/Signal_W-1_St4_Sec3",
	["DT/Digi/Wheel-1/Station4/Sector3/Occupancies/OccupancyAllHits_perCh_W-1_St4_Sec3",
	 "DT/Digi/Wheel-1/Station4/Sector3/TimeBoxes/TimeBox_W-1_St4_Sec3_SL1"],
	["DT/Digi/Wheel-1/Station4/Sector3/TimeBoxes/TimeBox_W-1_St4_Sec3_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector4/Station1/Trigger(DDU)_W-1_St1_Sec4",
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station1/LocalTriggerPhi/DDU_BestQual_W-1_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec4_St1"])

dtlayout(dqmitems, "Wheel-1/Sector4/Station1/Signal_W-1_St1_Sec4",
	["DT/Digi/Wheel-1/Station1/Sector4/Occupancies/OccupancyAllHits_perCh_W-1_St1_Sec4",
	 "DT/Digi/Wheel-1/Station1/Sector4/TimeBoxes/TimeBox_W-1_St1_Sec4_SL1"],
	["DT/Digi/Wheel-1/Station1/Sector4/TimeBoxes/TimeBox_W-1_St1_Sec4_SL2",
	 "DT/Digi/Wheel-1/Station1/Sector4/TimeBoxes/TimeBox_W-1_St1_Sec4_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector4/Station2/Trigger(DDU)_W-1_St2_Sec4",
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station2/LocalTriggerPhi/DDU_BestQual_W-1_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec4_St2"])

dtlayout(dqmitems, "Wheel-1/Sector4/Station2/Signal_W-1_St2_Sec4",
	["DT/Digi/Wheel-1/Station2/Sector4/Occupancies/OccupancyAllHits_perCh_W-1_St2_Sec4",
	 "DT/Digi/Wheel-1/Station2/Sector4/TimeBoxes/TimeBox_W-1_St2_Sec4_SL1"],
	["DT/Digi/Wheel-1/Station2/Sector4/TimeBoxes/TimeBox_W-1_St2_Sec4_SL2",
	 "DT/Digi/Wheel-1/Station2/Sector4/TimeBoxes/TimeBox_W-1_St2_Sec4_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector4/Station3/Trigger(DDU)_W-1_St3_Sec4",
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station3/LocalTriggerPhi/DDU_BestQual_W-1_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec4_St3"])

dtlayout(dqmitems, "Wheel-1/Sector4/Station3/Signal_W-1_St3_Sec4",
	["DT/Digi/Wheel-1/Station3/Sector4/Occupancies/OccupancyAllHits_perCh_W-1_St3_Sec4",
	 "DT/Digi/Wheel-1/Station3/Sector4/TimeBoxes/TimeBox_W-1_St3_Sec4_SL1"],
	["DT/Digi/Wheel-1/Station3/Sector4/TimeBoxes/TimeBox_W-1_St3_Sec4_SL2",
	 "DT/Digi/Wheel-1/Station3/Sector4/TimeBoxes/TimeBox_W-1_St3_Sec4_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector4/Station4/Trigger(DDU)_W-1_St4_Sec4",
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec4_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec4_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station4/LocalTriggerPhi/DDU_BestQual_W-1_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec4_St4"])

dtlayout(dqmitems, "Wheel-1/Sector4/Station4/Signal_W-1_St4_Sec4",
	["DT/Digi/Wheel-1/Station4/Sector4/Occupancies/OccupancyAllHits_perCh_W-1_St4_Sec4",
	 "DT/Digi/Wheel-1/Station4/Sector4/TimeBoxes/TimeBox_W-1_St4_Sec4_SL1"],
	["DT/Digi/Wheel-1/Station4/Sector4/TimeBoxes/TimeBox_W-1_St4_Sec4_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector5/Station1/Trigger(DDU)_W-1_St1_Sec5",
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station1/LocalTriggerPhi/DDU_BestQual_W-1_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec5_St1"])

dtlayout(dqmitems, "Wheel-1/Sector5/Station1/Signal_W-1_St1_Sec5",
	["DT/Digi/Wheel-1/Station1/Sector5/Occupancies/OccupancyAllHits_perCh_W-1_St1_Sec5",
	 "DT/Digi/Wheel-1/Station1/Sector5/TimeBoxes/TimeBox_W-1_St1_Sec5_SL1"],
	["DT/Digi/Wheel-1/Station1/Sector5/TimeBoxes/TimeBox_W-1_St1_Sec5_SL2",
	 "DT/Digi/Wheel-1/Station1/Sector5/TimeBoxes/TimeBox_W-1_St1_Sec5_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector5/Station2/Trigger(DDU)_W-1_St2_Sec5",
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station2/LocalTriggerPhi/DDU_BestQual_W-1_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec5_St2"])

dtlayout(dqmitems, "Wheel-1/Sector5/Station2/Signal_W-1_St2_Sec5",
	["DT/Digi/Wheel-1/Station2/Sector5/Occupancies/OccupancyAllHits_perCh_W-1_St2_Sec5",
	 "DT/Digi/Wheel-1/Station2/Sector5/TimeBoxes/TimeBox_W-1_St2_Sec5_SL1"],
	["DT/Digi/Wheel-1/Station2/Sector5/TimeBoxes/TimeBox_W-1_St2_Sec5_SL2",
	 "DT/Digi/Wheel-1/Station2/Sector5/TimeBoxes/TimeBox_W-1_St2_Sec5_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector5/Station3/Trigger(DDU)_W-1_St3_Sec5",
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station3/LocalTriggerPhi/DDU_BestQual_W-1_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec5_St3"])

dtlayout(dqmitems, "Wheel-1/Sector5/Station3/Signal_W-1_St3_Sec5",
	["DT/Digi/Wheel-1/Station3/Sector5/Occupancies/OccupancyAllHits_perCh_W-1_St3_Sec5",
	 "DT/Digi/Wheel-1/Station3/Sector5/TimeBoxes/TimeBox_W-1_St3_Sec5_SL1"],
	["DT/Digi/Wheel-1/Station3/Sector5/TimeBoxes/TimeBox_W-1_St3_Sec5_SL2",
	 "DT/Digi/Wheel-1/Station3/Sector5/TimeBoxes/TimeBox_W-1_St3_Sec5_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector5/Station4/Trigger(DDU)_W-1_St4_Sec5",
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec5_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec5_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station4/LocalTriggerPhi/DDU_BestQual_W-1_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec5_St4"])

dtlayout(dqmitems, "Wheel-1/Sector5/Station4/Signal_W-1_St4_Sec5",
	["DT/Digi/Wheel-1/Station4/Sector5/Occupancies/OccupancyAllHits_perCh_W-1_St4_Sec5",
	 "DT/Digi/Wheel-1/Station4/Sector5/TimeBoxes/TimeBox_W-1_St4_Sec5_SL1"],
	["DT/Digi/Wheel-1/Station4/Sector5/TimeBoxes/TimeBox_W-1_St4_Sec5_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector6/Station1/Trigger(DDU)_W-1_St1_Sec6",
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station1/LocalTriggerPhi/DDU_BestQual_W-1_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec6_St1"])

dtlayout(dqmitems, "Wheel-1/Sector6/Station1/Signal_W-1_St1_Sec6",
	["DT/Digi/Wheel-1/Station1/Sector6/Occupancies/OccupancyAllHits_perCh_W-1_St1_Sec6",
	 "DT/Digi/Wheel-1/Station1/Sector6/TimeBoxes/TimeBox_W-1_St1_Sec6_SL1"],
	["DT/Digi/Wheel-1/Station1/Sector6/TimeBoxes/TimeBox_W-1_St1_Sec6_SL2",
	 "DT/Digi/Wheel-1/Station1/Sector6/TimeBoxes/TimeBox_W-1_St1_Sec6_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector6/Station2/Trigger(DDU)_W-1_St2_Sec6",
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station2/LocalTriggerPhi/DDU_BestQual_W-1_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec6_St2"])

dtlayout(dqmitems, "Wheel-1/Sector6/Station2/Signal_W-1_St2_Sec6",
	["DT/Digi/Wheel-1/Station2/Sector6/Occupancies/OccupancyAllHits_perCh_W-1_St2_Sec6",
	 "DT/Digi/Wheel-1/Station2/Sector6/TimeBoxes/TimeBox_W-1_St2_Sec6_SL1"],
	["DT/Digi/Wheel-1/Station2/Sector6/TimeBoxes/TimeBox_W-1_St2_Sec6_SL2",
	 "DT/Digi/Wheel-1/Station2/Sector6/TimeBoxes/TimeBox_W-1_St2_Sec6_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector6/Station3/Trigger(DDU)_W-1_St3_Sec6",
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station3/LocalTriggerPhi/DDU_BestQual_W-1_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec6_St3"])

dtlayout(dqmitems, "Wheel-1/Sector6/Station3/Signal_W-1_St3_Sec6",
	["DT/Digi/Wheel-1/Station3/Sector6/Occupancies/OccupancyAllHits_perCh_W-1_St3_Sec6",
	 "DT/Digi/Wheel-1/Station3/Sector6/TimeBoxes/TimeBox_W-1_St3_Sec6_SL1"],
	["DT/Digi/Wheel-1/Station3/Sector6/TimeBoxes/TimeBox_W-1_St3_Sec6_SL2",
	 "DT/Digi/Wheel-1/Station3/Sector6/TimeBoxes/TimeBox_W-1_St3_Sec6_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector6/Station4/Trigger(DDU)_W-1_St4_Sec6",
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec6_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec6_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station4/LocalTriggerPhi/DDU_BestQual_W-1_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec6_St4"])

dtlayout(dqmitems, "Wheel-1/Sector6/Station4/Signal_W-1_St4_Sec6",
	["DT/Digi/Wheel-1/Station4/Sector6/Occupancies/OccupancyAllHits_perCh_W-1_St4_Sec6",
	 "DT/Digi/Wheel-1/Station4/Sector6/TimeBoxes/TimeBox_W-1_St4_Sec6_SL1"],
	["DT/Digi/Wheel-1/Station4/Sector6/TimeBoxes/TimeBox_W-1_St4_Sec6_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector7/Station1/Trigger(DDU)_W-1_St1_Sec7",
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station1/LocalTriggerPhi/DDU_BestQual_W-1_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec7_St1"])

dtlayout(dqmitems, "Wheel-1/Sector7/Station1/Signal_W-1_St1_Sec7",
	["DT/Digi/Wheel-1/Station1/Sector7/Occupancies/OccupancyAllHits_perCh_W-1_St1_Sec7",
	 "DT/Digi/Wheel-1/Station1/Sector7/TimeBoxes/TimeBox_W-1_St1_Sec7_SL1"],
	["DT/Digi/Wheel-1/Station1/Sector7/TimeBoxes/TimeBox_W-1_St1_Sec7_SL2",
	 "DT/Digi/Wheel-1/Station1/Sector7/TimeBoxes/TimeBox_W-1_St1_Sec7_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector7/Station2/Trigger(DDU)_W-1_St2_Sec7",
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station2/LocalTriggerPhi/DDU_BestQual_W-1_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec7_St2"])

dtlayout(dqmitems, "Wheel-1/Sector7/Station2/Signal_W-1_St2_Sec7",
	["DT/Digi/Wheel-1/Station2/Sector7/Occupancies/OccupancyAllHits_perCh_W-1_St2_Sec7",
	 "DT/Digi/Wheel-1/Station2/Sector7/TimeBoxes/TimeBox_W-1_St2_Sec7_SL1"],
	["DT/Digi/Wheel-1/Station2/Sector7/TimeBoxes/TimeBox_W-1_St2_Sec7_SL2",
	 "DT/Digi/Wheel-1/Station2/Sector7/TimeBoxes/TimeBox_W-1_St2_Sec7_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector7/Station3/Trigger(DDU)_W-1_St3_Sec7",
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station3/LocalTriggerPhi/DDU_BestQual_W-1_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec7_St3"])

dtlayout(dqmitems, "Wheel-1/Sector7/Station3/Signal_W-1_St3_Sec7",
	["DT/Digi/Wheel-1/Station3/Sector7/Occupancies/OccupancyAllHits_perCh_W-1_St3_Sec7",
	 "DT/Digi/Wheel-1/Station3/Sector7/TimeBoxes/TimeBox_W-1_St3_Sec7_SL1"],
	["DT/Digi/Wheel-1/Station3/Sector7/TimeBoxes/TimeBox_W-1_St3_Sec7_SL2",
	 "DT/Digi/Wheel-1/Station3/Sector7/TimeBoxes/TimeBox_W-1_St3_Sec7_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector7/Station4/Trigger(DDU)_W-1_St4_Sec7",
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec7_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec7_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station4/LocalTriggerPhi/DDU_BestQual_W-1_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec7_St4"])

dtlayout(dqmitems, "Wheel-1/Sector7/Station4/Signal_W-1_St4_Sec7",
	["DT/Digi/Wheel-1/Station4/Sector7/Occupancies/OccupancyAllHits_perCh_W-1_St4_Sec7",
	 "DT/Digi/Wheel-1/Station4/Sector7/TimeBoxes/TimeBox_W-1_St4_Sec7_SL1"],
	["DT/Digi/Wheel-1/Station4/Sector7/TimeBoxes/TimeBox_W-1_St4_Sec7_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector8/Station1/Trigger(DDU)_W-1_St1_Sec8",
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station1/LocalTriggerPhi/DDU_BestQual_W-1_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec8_St1"])

dtlayout(dqmitems, "Wheel-1/Sector8/Station1/Signal_W-1_St1_Sec8",
	["DT/Digi/Wheel-1/Station1/Sector8/Occupancies/OccupancyAllHits_perCh_W-1_St1_Sec8",
	 "DT/Digi/Wheel-1/Station1/Sector8/TimeBoxes/TimeBox_W-1_St1_Sec8_SL1"],
	["DT/Digi/Wheel-1/Station1/Sector8/TimeBoxes/TimeBox_W-1_St1_Sec8_SL2",
	 "DT/Digi/Wheel-1/Station1/Sector8/TimeBoxes/TimeBox_W-1_St1_Sec8_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector8/Station2/Trigger(DDU)_W-1_St2_Sec8",
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station2/LocalTriggerPhi/DDU_BestQual_W-1_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec8_St2"])

dtlayout(dqmitems, "Wheel-1/Sector8/Station2/Signal_W-1_St2_Sec8",
	["DT/Digi/Wheel-1/Station2/Sector8/Occupancies/OccupancyAllHits_perCh_W-1_St2_Sec8",
	 "DT/Digi/Wheel-1/Station2/Sector8/TimeBoxes/TimeBox_W-1_St2_Sec8_SL1"],
	["DT/Digi/Wheel-1/Station2/Sector8/TimeBoxes/TimeBox_W-1_St2_Sec8_SL2",
	 "DT/Digi/Wheel-1/Station2/Sector8/TimeBoxes/TimeBox_W-1_St2_Sec8_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector8/Station3/Trigger(DDU)_W-1_St3_Sec8",
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station3/LocalTriggerPhi/DDU_BestQual_W-1_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec8_St3"])

dtlayout(dqmitems, "Wheel-1/Sector8/Station3/Signal_W-1_St3_Sec8",
	["DT/Digi/Wheel-1/Station3/Sector8/Occupancies/OccupancyAllHits_perCh_W-1_St3_Sec8",
	 "DT/Digi/Wheel-1/Station3/Sector8/TimeBoxes/TimeBox_W-1_St3_Sec8_SL1"],
	["DT/Digi/Wheel-1/Station3/Sector8/TimeBoxes/TimeBox_W-1_St3_Sec8_SL2",
	 "DT/Digi/Wheel-1/Station3/Sector8/TimeBoxes/TimeBox_W-1_St3_Sec8_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector8/Station4/Trigger(DDU)_W-1_St4_Sec8",
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec8_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec8_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station4/LocalTriggerPhi/DDU_BestQual_W-1_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec8_St4"])

dtlayout(dqmitems, "Wheel-1/Sector8/Station4/Signal_W-1_St4_Sec8",
	["DT/Digi/Wheel-1/Station4/Sector8/Occupancies/OccupancyAllHits_perCh_W-1_St4_Sec8",
	 "DT/Digi/Wheel-1/Station4/Sector8/TimeBoxes/TimeBox_W-1_St4_Sec8_SL1"],
	["DT/Digi/Wheel-1/Station4/Sector8/TimeBoxes/TimeBox_W-1_St4_Sec8_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector9/Station1/Trigger(DDU)_W-1_St1_Sec9",
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station1/LocalTriggerPhi/DDU_BestQual_W-1_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec9_St1"])

dtlayout(dqmitems, "Wheel-1/Sector9/Station1/Signal_W-1_St1_Sec9",
	["DT/Digi/Wheel-1/Station1/Sector9/Occupancies/OccupancyAllHits_perCh_W-1_St1_Sec9",
	 "DT/Digi/Wheel-1/Station1/Sector9/TimeBoxes/TimeBox_W-1_St1_Sec9_SL1"],
	["DT/Digi/Wheel-1/Station1/Sector9/TimeBoxes/TimeBox_W-1_St1_Sec9_SL2",
	 "DT/Digi/Wheel-1/Station1/Sector9/TimeBoxes/TimeBox_W-1_St1_Sec9_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector9/Station2/Trigger(DDU)_W-1_St2_Sec9",
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station2/LocalTriggerPhi/DDU_BestQual_W-1_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec9_St2"])

dtlayout(dqmitems, "Wheel-1/Sector9/Station2/Signal_W-1_St2_Sec9",
	["DT/Digi/Wheel-1/Station2/Sector9/Occupancies/OccupancyAllHits_perCh_W-1_St2_Sec9",
	 "DT/Digi/Wheel-1/Station2/Sector9/TimeBoxes/TimeBox_W-1_St2_Sec9_SL1"],
	["DT/Digi/Wheel-1/Station2/Sector9/TimeBoxes/TimeBox_W-1_St2_Sec9_SL2",
	 "DT/Digi/Wheel-1/Station2/Sector9/TimeBoxes/TimeBox_W-1_St2_Sec9_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector9/Station3/Trigger(DDU)_W-1_St3_Sec9",
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station3/LocalTriggerPhi/DDU_BestQual_W-1_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec9_St3"])

dtlayout(dqmitems, "Wheel-1/Sector9/Station3/Signal_W-1_St3_Sec9",
	["DT/Digi/Wheel-1/Station3/Sector9/Occupancies/OccupancyAllHits_perCh_W-1_St3_Sec9",
	 "DT/Digi/Wheel-1/Station3/Sector9/TimeBoxes/TimeBox_W-1_St3_Sec9_SL1"],
	["DT/Digi/Wheel-1/Station3/Sector9/TimeBoxes/TimeBox_W-1_St3_Sec9_SL2",
	 "DT/Digi/Wheel-1/Station3/Sector9/TimeBoxes/TimeBox_W-1_St3_Sec9_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector9/Station4/Trigger(DDU)_W-1_St4_Sec9",
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec9_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec9_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station4/LocalTriggerPhi/DDU_BestQual_W-1_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec9_St4"])

dtlayout(dqmitems, "Wheel-1/Sector9/Station4/Signal_W-1_St4_Sec9",
	["DT/Digi/Wheel-1/Station4/Sector9/Occupancies/OccupancyAllHits_perCh_W-1_St4_Sec9",
	 "DT/Digi/Wheel-1/Station4/Sector9/TimeBoxes/TimeBox_W-1_St4_Sec9_SL1"],
	["DT/Digi/Wheel-1/Station4/Sector9/TimeBoxes/TimeBox_W-1_St4_Sec9_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector10/Station1/Trigger(DDU)_W-1_St1_Sec10",
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station1/LocalTriggerPhi/DDU_BestQual_W-1_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec10_St1"])

dtlayout(dqmitems, "Wheel-1/Sector10/Station1/Signal_W-1_St1_Sec10",
	["DT/Digi/Wheel-1/Station1/Sector10/Occupancies/OccupancyAllHits_perCh_W-1_St1_Sec10",
	 "DT/Digi/Wheel-1/Station1/Sector10/TimeBoxes/TimeBox_W-1_St1_Sec10_SL1"],
	["DT/Digi/Wheel-1/Station1/Sector10/TimeBoxes/TimeBox_W-1_St1_Sec10_SL2",
	 "DT/Digi/Wheel-1/Station1/Sector10/TimeBoxes/TimeBox_W-1_St1_Sec10_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector10/Station2/Trigger(DDU)_W-1_St2_Sec10",
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station2/LocalTriggerPhi/DDU_BestQual_W-1_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec10_St2"])

dtlayout(dqmitems, "Wheel-1/Sector10/Station2/Signal_W-1_St2_Sec10",
	["DT/Digi/Wheel-1/Station2/Sector10/Occupancies/OccupancyAllHits_perCh_W-1_St2_Sec10",
	 "DT/Digi/Wheel-1/Station2/Sector10/TimeBoxes/TimeBox_W-1_St2_Sec10_SL1"],
	["DT/Digi/Wheel-1/Station2/Sector10/TimeBoxes/TimeBox_W-1_St2_Sec10_SL2",
	 "DT/Digi/Wheel-1/Station2/Sector10/TimeBoxes/TimeBox_W-1_St2_Sec10_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector10/Station3/Trigger(DDU)_W-1_St3_Sec10",
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station3/LocalTriggerPhi/DDU_BestQual_W-1_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec10_St3"])

dtlayout(dqmitems, "Wheel-1/Sector10/Station3/Signal_W-1_St3_Sec10",
	["DT/Digi/Wheel-1/Station3/Sector10/Occupancies/OccupancyAllHits_perCh_W-1_St3_Sec10",
	 "DT/Digi/Wheel-1/Station3/Sector10/TimeBoxes/TimeBox_W-1_St3_Sec10_SL1"],
	["DT/Digi/Wheel-1/Station3/Sector10/TimeBoxes/TimeBox_W-1_St3_Sec10_SL2",
	 "DT/Digi/Wheel-1/Station3/Sector10/TimeBoxes/TimeBox_W-1_St3_Sec10_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector10/Station4/Trigger(DDU)_W-1_St4_Sec10",
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec10_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec10_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station4/LocalTriggerPhi/DDU_BestQual_W-1_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec10_St4"])

dtlayout(dqmitems, "Wheel-1/Sector10/Station4/Signal_W-1_St4_Sec10",
	["DT/Digi/Wheel-1/Station4/Sector10/Occupancies/OccupancyAllHits_perCh_W-1_St4_Sec10",
	 "DT/Digi/Wheel-1/Station4/Sector10/TimeBoxes/TimeBox_W-1_St4_Sec10_SL1"],
	["DT/Digi/Wheel-1/Station4/Sector10/TimeBoxes/TimeBox_W-1_St4_Sec10_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector11/Station1/Trigger(DDU)_W-1_St1_Sec11",
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station1/LocalTriggerPhi/DDU_BestQual_W-1_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec11_St1"])

dtlayout(dqmitems, "Wheel-1/Sector11/Station1/Signal_W-1_St1_Sec11",
	["DT/Digi/Wheel-1/Station1/Sector11/Occupancies/OccupancyAllHits_perCh_W-1_St1_Sec11",
	 "DT/Digi/Wheel-1/Station1/Sector11/TimeBoxes/TimeBox_W-1_St1_Sec11_SL1"],
	["DT/Digi/Wheel-1/Station1/Sector11/TimeBoxes/TimeBox_W-1_St1_Sec11_SL2",
	 "DT/Digi/Wheel-1/Station1/Sector11/TimeBoxes/TimeBox_W-1_St1_Sec11_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector11/Station2/Trigger(DDU)_W-1_St2_Sec11",
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station2/LocalTriggerPhi/DDU_BestQual_W-1_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec11_St2"])

dtlayout(dqmitems, "Wheel-1/Sector11/Station2/Signal_W-1_St2_Sec11",
	["DT/Digi/Wheel-1/Station2/Sector11/Occupancies/OccupancyAllHits_perCh_W-1_St2_Sec11",
	 "DT/Digi/Wheel-1/Station2/Sector11/TimeBoxes/TimeBox_W-1_St2_Sec11_SL1"],
	["DT/Digi/Wheel-1/Station2/Sector11/TimeBoxes/TimeBox_W-1_St2_Sec11_SL2",
	 "DT/Digi/Wheel-1/Station2/Sector11/TimeBoxes/TimeBox_W-1_St2_Sec11_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector11/Station3/Trigger(DDU)_W-1_St3_Sec11",
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station3/LocalTriggerPhi/DDU_BestQual_W-1_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec11_St3"])

dtlayout(dqmitems, "Wheel-1/Sector11/Station3/Signal_W-1_St3_Sec11",
	["DT/Digi/Wheel-1/Station3/Sector11/Occupancies/OccupancyAllHits_perCh_W-1_St3_Sec11",
	 "DT/Digi/Wheel-1/Station3/Sector11/TimeBoxes/TimeBox_W-1_St3_Sec11_SL1"],
	["DT/Digi/Wheel-1/Station3/Sector11/TimeBoxes/TimeBox_W-1_St3_Sec11_SL2",
	 "DT/Digi/Wheel-1/Station3/Sector11/TimeBoxes/TimeBox_W-1_St3_Sec11_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector11/Station4/Trigger(DDU)_W-1_St4_Sec11",
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec11_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec11_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station4/LocalTriggerPhi/DDU_BestQual_W-1_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec11_St4"])

dtlayout(dqmitems, "Wheel-1/Sector11/Station4/Signal_W-1_St4_Sec11",
	["DT/Digi/Wheel-1/Station4/Sector11/Occupancies/OccupancyAllHits_perCh_W-1_St4_Sec11",
	 "DT/Digi/Wheel-1/Station4/Sector11/TimeBoxes/TimeBox_W-1_St4_Sec11_SL1"],
	["DT/Digi/Wheel-1/Station4/Sector11/TimeBoxes/TimeBox_W-1_St4_Sec11_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector12/Station1/Trigger(DDU)_W-1_St1_Sec12",
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station1/LocalTriggerPhi/DDU_BestQual_W-1_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec12_St1"])

dtlayout(dqmitems, "Wheel-1/Sector12/Station1/Signal_W-1_St1_Sec12",
	["DT/Digi/Wheel-1/Station1/Sector12/Occupancies/OccupancyAllHits_perCh_W-1_St1_Sec12",
	 "DT/Digi/Wheel-1/Station1/Sector12/TimeBoxes/TimeBox_W-1_St1_Sec12_SL1"],
	["DT/Digi/Wheel-1/Station1/Sector12/TimeBoxes/TimeBox_W-1_St1_Sec12_SL2",
	 "DT/Digi/Wheel-1/Station1/Sector12/TimeBoxes/TimeBox_W-1_St1_Sec12_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector12/Station2/Trigger(DDU)_W-1_St2_Sec12",
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station2/LocalTriggerPhi/DDU_BestQual_W-1_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec12_St2"])

dtlayout(dqmitems, "Wheel-1/Sector12/Station2/Signal_W-1_St2_Sec12",
	["DT/Digi/Wheel-1/Station2/Sector12/Occupancies/OccupancyAllHits_perCh_W-1_St2_Sec12",
	 "DT/Digi/Wheel-1/Station2/Sector12/TimeBoxes/TimeBox_W-1_St2_Sec12_SL1"],
	["DT/Digi/Wheel-1/Station2/Sector12/TimeBoxes/TimeBox_W-1_St2_Sec12_SL2",
	 "DT/Digi/Wheel-1/Station2/Sector12/TimeBoxes/TimeBox_W-1_St2_Sec12_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector12/Station3/Trigger(DDU)_W-1_St3_Sec12",
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station3/LocalTriggerPhi/DDU_BestQual_W-1_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec12_St3"])

dtlayout(dqmitems, "Wheel-1/Sector12/Station3/Signal_W-1_St3_Sec12",
	["DT/Digi/Wheel-1/Station3/Sector12/Occupancies/OccupancyAllHits_perCh_W-1_St3_Sec12",
	 "DT/Digi/Wheel-1/Station3/Sector12/TimeBoxes/TimeBox_W-1_St3_Sec12_SL1"],
	["DT/Digi/Wheel-1/Station3/Sector12/TimeBoxes/TimeBox_W-1_St3_Sec12_SL2",
	 "DT/Digi/Wheel-1/Station3/Sector12/TimeBoxes/TimeBox_W-1_St3_Sec12_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector12/Station4/Trigger(DDU)_W-1_St4_Sec12",
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec12_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-1_Sec12_St4"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station4/LocalTriggerPhi/DDU_BestQual_W-1_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-1_Sec12_St4"])

dtlayout(dqmitems, "Wheel-1/Sector12/Station4/Signal_W-1_St4_Sec12",
	["DT/Digi/Wheel-1/Station4/Sector12/Occupancies/OccupancyAllHits_perCh_W-1_St4_Sec12",
	 "DT/Digi/Wheel-1/Station4/Sector12/TimeBoxes/TimeBox_W-1_St4_Sec12_SL1"],
	["DT/Digi/Wheel-1/Station4/Sector12/TimeBoxes/TimeBox_W-1_St4_Sec12_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector1/Station1/Trigger(DDU)_W-2_St1_Sec1",
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station1/LocalTriggerPhi/DDU_BestQual_W-2_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec1_St1"])

dtlayout(dqmitems, "Wheel-2/Sector1/Station1/Signal_W-2_St1_Sec1",
	["DT/Digi/Wheel-2/Station1/Sector1/Occupancies/OccupancyAllHits_perCh_W-2_St1_Sec1",
	 "DT/Digi/Wheel-2/Station1/Sector1/TimeBoxes/TimeBox_W-2_St1_Sec1_SL1"],
	["DT/Digi/Wheel-2/Station1/Sector1/TimeBoxes/TimeBox_W-2_St1_Sec1_SL2",
	 "DT/Digi/Wheel-2/Station1/Sector1/TimeBoxes/TimeBox_W-2_St1_Sec1_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector1/Station2/Trigger(DDU)_W-2_St2_Sec1",
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station2/LocalTriggerPhi/DDU_BestQual_W-2_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec1_St2"])

dtlayout(dqmitems, "Wheel-2/Sector1/Station2/Signal_W-2_St2_Sec1",
	["DT/Digi/Wheel-2/Station2/Sector1/Occupancies/OccupancyAllHits_perCh_W-2_St2_Sec1",
	 "DT/Digi/Wheel-2/Station2/Sector1/TimeBoxes/TimeBox_W-2_St2_Sec1_SL1"],
	["DT/Digi/Wheel-2/Station2/Sector1/TimeBoxes/TimeBox_W-2_St2_Sec1_SL2",
	 "DT/Digi/Wheel-2/Station2/Sector1/TimeBoxes/TimeBox_W-2_St2_Sec1_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector1/Station3/Trigger(DDU)_W-2_St3_Sec1",
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station3/LocalTriggerPhi/DDU_BestQual_W-2_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec1_St3"])

dtlayout(dqmitems, "Wheel-2/Sector1/Station3/Signal_W-2_St3_Sec1",
	["DT/Digi/Wheel-2/Station3/Sector1/Occupancies/OccupancyAllHits_perCh_W-2_St3_Sec1",
	 "DT/Digi/Wheel-2/Station3/Sector1/TimeBoxes/TimeBox_W-2_St3_Sec1_SL1"],
	["DT/Digi/Wheel-2/Station3/Sector1/TimeBoxes/TimeBox_W-2_St3_Sec1_SL2",
	 "DT/Digi/Wheel-2/Station3/Sector1/TimeBoxes/TimeBox_W-2_St3_Sec1_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector1/Station4/Trigger(DDU)_W-2_St4_Sec1",
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec1_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec1_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station4/LocalTriggerPhi/DDU_BestQual_W-2_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec1_St4"])

dtlayout(dqmitems, "Wheel-2/Sector1/Station4/Signal_W-2_St4_Sec1",
	["DT/Digi/Wheel-2/Station4/Sector1/Occupancies/OccupancyAllHits_perCh_W-2_St4_Sec1",
	 "DT/Digi/Wheel-2/Station4/Sector1/TimeBoxes/TimeBox_W-2_St4_Sec1_SL1"],
	["DT/Digi/Wheel-2/Station4/Sector1/TimeBoxes/TimeBox_W-2_St4_Sec1_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector2/Station1/Trigger(DDU)_W-2_St1_Sec2",
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station1/LocalTriggerPhi/DDU_BestQual_W-2_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec2_St1"])

dtlayout(dqmitems, "Wheel-2/Sector2/Station1/Signal_W-2_St1_Sec2",
	["DT/Digi/Wheel-2/Station1/Sector2/Occupancies/OccupancyAllHits_perCh_W-2_St1_Sec2",
	 "DT/Digi/Wheel-2/Station1/Sector2/TimeBoxes/TimeBox_W-2_St1_Sec2_SL1"],
	["DT/Digi/Wheel-2/Station1/Sector2/TimeBoxes/TimeBox_W-2_St1_Sec2_SL2",
	 "DT/Digi/Wheel-2/Station1/Sector2/TimeBoxes/TimeBox_W-2_St1_Sec2_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector2/Station2/Trigger(DDU)_W-2_St2_Sec2",
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station2/LocalTriggerPhi/DDU_BestQual_W-2_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec2_St2"])

dtlayout(dqmitems, "Wheel-2/Sector2/Station2/Signal_W-2_St2_Sec2",
	["DT/Digi/Wheel-2/Station2/Sector2/Occupancies/OccupancyAllHits_perCh_W-2_St2_Sec2",
	 "DT/Digi/Wheel-2/Station2/Sector2/TimeBoxes/TimeBox_W-2_St2_Sec2_SL1"],
	["DT/Digi/Wheel-2/Station2/Sector2/TimeBoxes/TimeBox_W-2_St2_Sec2_SL2",
	 "DT/Digi/Wheel-2/Station2/Sector2/TimeBoxes/TimeBox_W-2_St2_Sec2_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector2/Station3/Trigger(DDU)_W-2_St3_Sec2",
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station3/LocalTriggerPhi/DDU_BestQual_W-2_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec2_St3"])

dtlayout(dqmitems, "Wheel-2/Sector2/Station3/Signal_W-2_St3_Sec2",
	["DT/Digi/Wheel-2/Station3/Sector2/Occupancies/OccupancyAllHits_perCh_W-2_St3_Sec2",
	 "DT/Digi/Wheel-2/Station3/Sector2/TimeBoxes/TimeBox_W-2_St3_Sec2_SL1"],
	["DT/Digi/Wheel-2/Station3/Sector2/TimeBoxes/TimeBox_W-2_St3_Sec2_SL2",
	 "DT/Digi/Wheel-2/Station3/Sector2/TimeBoxes/TimeBox_W-2_St3_Sec2_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector2/Station4/Trigger(DDU)_W-2_St4_Sec2",
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec2_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec2_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station4/LocalTriggerPhi/DDU_BestQual_W-2_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec2_St4"])

dtlayout(dqmitems, "Wheel-2/Sector2/Station4/Signal_W-2_St4_Sec2",
	["DT/Digi/Wheel-2/Station4/Sector2/Occupancies/OccupancyAllHits_perCh_W-2_St4_Sec2",
	 "DT/Digi/Wheel-2/Station4/Sector2/TimeBoxes/TimeBox_W-2_St4_Sec2_SL1"],
	["DT/Digi/Wheel-2/Station4/Sector2/TimeBoxes/TimeBox_W-2_St4_Sec2_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector3/Station1/Trigger(DDU)_W-2_St1_Sec3",
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station1/LocalTriggerPhi/DDU_BestQual_W-2_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec3_St1"])

dtlayout(dqmitems, "Wheel-2/Sector3/Station1/Signal_W-2_St1_Sec3",
	["DT/Digi/Wheel-2/Station1/Sector3/Occupancies/OccupancyAllHits_perCh_W-2_St1_Sec3",
	 "DT/Digi/Wheel-2/Station1/Sector3/TimeBoxes/TimeBox_W-2_St1_Sec3_SL1"],
	["DT/Digi/Wheel-2/Station1/Sector3/TimeBoxes/TimeBox_W-2_St1_Sec3_SL2",
	 "DT/Digi/Wheel-2/Station1/Sector3/TimeBoxes/TimeBox_W-2_St1_Sec3_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector3/Station2/Trigger(DDU)_W-2_St2_Sec3",
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station2/LocalTriggerPhi/DDU_BestQual_W-2_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec3_St2"])

dtlayout(dqmitems, "Wheel-2/Sector3/Station2/Signal_W-2_St2_Sec3",
	["DT/Digi/Wheel-2/Station2/Sector3/Occupancies/OccupancyAllHits_perCh_W-2_St2_Sec3",
	 "DT/Digi/Wheel-2/Station2/Sector3/TimeBoxes/TimeBox_W-2_St2_Sec3_SL1"],
	["DT/Digi/Wheel-2/Station2/Sector3/TimeBoxes/TimeBox_W-2_St2_Sec3_SL2",
	 "DT/Digi/Wheel-2/Station2/Sector3/TimeBoxes/TimeBox_W-2_St2_Sec3_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector3/Station3/Trigger(DDU)_W-2_St3_Sec3",
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station3/LocalTriggerPhi/DDU_BestQual_W-2_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec3_St3"])

dtlayout(dqmitems, "Wheel-2/Sector3/Station3/Signal_W-2_St3_Sec3",
	["DT/Digi/Wheel-2/Station3/Sector3/Occupancies/OccupancyAllHits_perCh_W-2_St3_Sec3",
	 "DT/Digi/Wheel-2/Station3/Sector3/TimeBoxes/TimeBox_W-2_St3_Sec3_SL1"],
	["DT/Digi/Wheel-2/Station3/Sector3/TimeBoxes/TimeBox_W-2_St3_Sec3_SL2",
	 "DT/Digi/Wheel-2/Station3/Sector3/TimeBoxes/TimeBox_W-2_St3_Sec3_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector3/Station4/Trigger(DDU)_W-2_St4_Sec3",
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec3_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec3_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station4/LocalTriggerPhi/DDU_BestQual_W-2_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec3_St4"])

dtlayout(dqmitems, "Wheel-2/Sector3/Station4/Signal_W-2_St4_Sec3",
	["DT/Digi/Wheel-2/Station4/Sector3/Occupancies/OccupancyAllHits_perCh_W-2_St4_Sec3",
	 "DT/Digi/Wheel-2/Station4/Sector3/TimeBoxes/TimeBox_W-2_St4_Sec3_SL1"],
	["DT/Digi/Wheel-2/Station4/Sector3/TimeBoxes/TimeBox_W-2_St4_Sec3_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector4/Station1/Trigger(DDU)_W-2_St1_Sec4",
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station1/LocalTriggerPhi/DDU_BestQual_W-2_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec4_St1"])

dtlayout(dqmitems, "Wheel-2/Sector4/Station1/Signal_W-2_St1_Sec4",
	["DT/Digi/Wheel-2/Station1/Sector4/Occupancies/OccupancyAllHits_perCh_W-2_St1_Sec4",
	 "DT/Digi/Wheel-2/Station1/Sector4/TimeBoxes/TimeBox_W-2_St1_Sec4_SL1"],
	["DT/Digi/Wheel-2/Station1/Sector4/TimeBoxes/TimeBox_W-2_St1_Sec4_SL2",
	 "DT/Digi/Wheel-2/Station1/Sector4/TimeBoxes/TimeBox_W-2_St1_Sec4_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector4/Station2/Trigger(DDU)_W-2_St2_Sec4",
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station2/LocalTriggerPhi/DDU_BestQual_W-2_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec4_St2"])

dtlayout(dqmitems, "Wheel-2/Sector4/Station2/Signal_W-2_St2_Sec4",
	["DT/Digi/Wheel-2/Station2/Sector4/Occupancies/OccupancyAllHits_perCh_W-2_St2_Sec4",
	 "DT/Digi/Wheel-2/Station2/Sector4/TimeBoxes/TimeBox_W-2_St2_Sec4_SL1"],
	["DT/Digi/Wheel-2/Station2/Sector4/TimeBoxes/TimeBox_W-2_St2_Sec4_SL2",
	 "DT/Digi/Wheel-2/Station2/Sector4/TimeBoxes/TimeBox_W-2_St2_Sec4_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector4/Station3/Trigger(DDU)_W-2_St3_Sec4",
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station3/LocalTriggerPhi/DDU_BestQual_W-2_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec4_St3"])

dtlayout(dqmitems, "Wheel-2/Sector4/Station3/Signal_W-2_St3_Sec4",
	["DT/Digi/Wheel-2/Station3/Sector4/Occupancies/OccupancyAllHits_perCh_W-2_St3_Sec4",
	 "DT/Digi/Wheel-2/Station3/Sector4/TimeBoxes/TimeBox_W-2_St3_Sec4_SL1"],
	["DT/Digi/Wheel-2/Station3/Sector4/TimeBoxes/TimeBox_W-2_St3_Sec4_SL2",
	 "DT/Digi/Wheel-2/Station3/Sector4/TimeBoxes/TimeBox_W-2_St3_Sec4_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector4/Station4/Trigger(DDU)_W-2_St4_Sec4",
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec4_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec4_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station4/LocalTriggerPhi/DDU_BestQual_W-2_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec4_St4"])

dtlayout(dqmitems, "Wheel-2/Sector4/Station4/Signal_W-2_St4_Sec4",
	["DT/Digi/Wheel-2/Station4/Sector4/Occupancies/OccupancyAllHits_perCh_W-2_St4_Sec4",
	 "DT/Digi/Wheel-2/Station4/Sector4/TimeBoxes/TimeBox_W-2_St4_Sec4_SL1"],
	["DT/Digi/Wheel-2/Station4/Sector4/TimeBoxes/TimeBox_W-2_St4_Sec4_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector5/Station1/Trigger(DDU)_W-2_St1_Sec5",
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station1/LocalTriggerPhi/DDU_BestQual_W-2_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec5_St1"])

dtlayout(dqmitems, "Wheel-2/Sector5/Station1/Signal_W-2_St1_Sec5",
	["DT/Digi/Wheel-2/Station1/Sector5/Occupancies/OccupancyAllHits_perCh_W-2_St1_Sec5",
	 "DT/Digi/Wheel-2/Station1/Sector5/TimeBoxes/TimeBox_W-2_St1_Sec5_SL1"],
	["DT/Digi/Wheel-2/Station1/Sector5/TimeBoxes/TimeBox_W-2_St1_Sec5_SL2",
	 "DT/Digi/Wheel-2/Station1/Sector5/TimeBoxes/TimeBox_W-2_St1_Sec5_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector5/Station2/Trigger(DDU)_W-2_St2_Sec5",
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station2/LocalTriggerPhi/DDU_BestQual_W-2_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec5_St2"])

dtlayout(dqmitems, "Wheel-2/Sector5/Station2/Signal_W-2_St2_Sec5",
	["DT/Digi/Wheel-2/Station2/Sector5/Occupancies/OccupancyAllHits_perCh_W-2_St2_Sec5",
	 "DT/Digi/Wheel-2/Station2/Sector5/TimeBoxes/TimeBox_W-2_St2_Sec5_SL1"],
	["DT/Digi/Wheel-2/Station2/Sector5/TimeBoxes/TimeBox_W-2_St2_Sec5_SL2",
	 "DT/Digi/Wheel-2/Station2/Sector5/TimeBoxes/TimeBox_W-2_St2_Sec5_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector5/Station3/Trigger(DDU)_W-2_St3_Sec5",
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station3/LocalTriggerPhi/DDU_BestQual_W-2_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec5_St3"])

dtlayout(dqmitems, "Wheel-2/Sector5/Station3/Signal_W-2_St3_Sec5",
	["DT/Digi/Wheel-2/Station3/Sector5/Occupancies/OccupancyAllHits_perCh_W-2_St3_Sec5",
	 "DT/Digi/Wheel-2/Station3/Sector5/TimeBoxes/TimeBox_W-2_St3_Sec5_SL1"],
	["DT/Digi/Wheel-2/Station3/Sector5/TimeBoxes/TimeBox_W-2_St3_Sec5_SL2",
	 "DT/Digi/Wheel-2/Station3/Sector5/TimeBoxes/TimeBox_W-2_St3_Sec5_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector5/Station4/Trigger(DDU)_W-2_St4_Sec5",
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec5_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec5_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station4/LocalTriggerPhi/DDU_BestQual_W-2_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec5_St4"])

dtlayout(dqmitems, "Wheel-2/Sector5/Station4/Signal_W-2_St4_Sec5",
	["DT/Digi/Wheel-2/Station4/Sector5/Occupancies/OccupancyAllHits_perCh_W-2_St4_Sec5",
	 "DT/Digi/Wheel-2/Station4/Sector5/TimeBoxes/TimeBox_W-2_St4_Sec5_SL1"],
	["DT/Digi/Wheel-2/Station4/Sector5/TimeBoxes/TimeBox_W-2_St4_Sec5_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector6/Station1/Trigger(DDU)_W-2_St1_Sec6",
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station1/LocalTriggerPhi/DDU_BestQual_W-2_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec6_St1"])

dtlayout(dqmitems, "Wheel-2/Sector6/Station1/Signal_W-2_St1_Sec6",
	["DT/Digi/Wheel-2/Station1/Sector6/Occupancies/OccupancyAllHits_perCh_W-2_St1_Sec6",
	 "DT/Digi/Wheel-2/Station1/Sector6/TimeBoxes/TimeBox_W-2_St1_Sec6_SL1"],
	["DT/Digi/Wheel-2/Station1/Sector6/TimeBoxes/TimeBox_W-2_St1_Sec6_SL2",
	 "DT/Digi/Wheel-2/Station1/Sector6/TimeBoxes/TimeBox_W-2_St1_Sec6_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector6/Station2/Trigger(DDU)_W-2_St2_Sec6",
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station2/LocalTriggerPhi/DDU_BestQual_W-2_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec6_St2"])

dtlayout(dqmitems, "Wheel-2/Sector6/Station2/Signal_W-2_St2_Sec6",
	["DT/Digi/Wheel-2/Station2/Sector6/Occupancies/OccupancyAllHits_perCh_W-2_St2_Sec6",
	 "DT/Digi/Wheel-2/Station2/Sector6/TimeBoxes/TimeBox_W-2_St2_Sec6_SL1"],
	["DT/Digi/Wheel-2/Station2/Sector6/TimeBoxes/TimeBox_W-2_St2_Sec6_SL2",
	 "DT/Digi/Wheel-2/Station2/Sector6/TimeBoxes/TimeBox_W-2_St2_Sec6_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector6/Station3/Trigger(DDU)_W-2_St3_Sec6",
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station3/LocalTriggerPhi/DDU_BestQual_W-2_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec6_St3"])

dtlayout(dqmitems, "Wheel-2/Sector6/Station3/Signal_W-2_St3_Sec6",
	["DT/Digi/Wheel-2/Station3/Sector6/Occupancies/OccupancyAllHits_perCh_W-2_St3_Sec6",
	 "DT/Digi/Wheel-2/Station3/Sector6/TimeBoxes/TimeBox_W-2_St3_Sec6_SL1"],
	["DT/Digi/Wheel-2/Station3/Sector6/TimeBoxes/TimeBox_W-2_St3_Sec6_SL2",
	 "DT/Digi/Wheel-2/Station3/Sector6/TimeBoxes/TimeBox_W-2_St3_Sec6_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector6/Station4/Trigger(DDU)_W-2_St4_Sec6",
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec6_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec6_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station4/LocalTriggerPhi/DDU_BestQual_W-2_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec6_St4"])

dtlayout(dqmitems, "Wheel-2/Sector6/Station4/Signal_W-2_St4_Sec6",
	["DT/Digi/Wheel-2/Station4/Sector6/Occupancies/OccupancyAllHits_perCh_W-2_St4_Sec6",
	 "DT/Digi/Wheel-2/Station4/Sector6/TimeBoxes/TimeBox_W-2_St4_Sec6_SL1"],
	["DT/Digi/Wheel-2/Station4/Sector6/TimeBoxes/TimeBox_W-2_St4_Sec6_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector7/Station1/Trigger(DDU)_W-2_St1_Sec7",
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station1/LocalTriggerPhi/DDU_BestQual_W-2_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec7_St1"])

dtlayout(dqmitems, "Wheel-2/Sector7/Station1/Signal_W-2_St1_Sec7",
	["DT/Digi/Wheel-2/Station1/Sector7/Occupancies/OccupancyAllHits_perCh_W-2_St1_Sec7",
	 "DT/Digi/Wheel-2/Station1/Sector7/TimeBoxes/TimeBox_W-2_St1_Sec7_SL1"],
	["DT/Digi/Wheel-2/Station1/Sector7/TimeBoxes/TimeBox_W-2_St1_Sec7_SL2",
	 "DT/Digi/Wheel-2/Station1/Sector7/TimeBoxes/TimeBox_W-2_St1_Sec7_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector7/Station2/Trigger(DDU)_W-2_St2_Sec7",
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station2/LocalTriggerPhi/DDU_BestQual_W-2_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec7_St2"])

dtlayout(dqmitems, "Wheel-2/Sector7/Station2/Signal_W-2_St2_Sec7",
	["DT/Digi/Wheel-2/Station2/Sector7/Occupancies/OccupancyAllHits_perCh_W-2_St2_Sec7",
	 "DT/Digi/Wheel-2/Station2/Sector7/TimeBoxes/TimeBox_W-2_St2_Sec7_SL1"],
	["DT/Digi/Wheel-2/Station2/Sector7/TimeBoxes/TimeBox_W-2_St2_Sec7_SL2",
	 "DT/Digi/Wheel-2/Station2/Sector7/TimeBoxes/TimeBox_W-2_St2_Sec7_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector7/Station3/Trigger(DDU)_W-2_St3_Sec7",
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station3/LocalTriggerPhi/DDU_BestQual_W-2_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec7_St3"])

dtlayout(dqmitems, "Wheel-2/Sector7/Station3/Signal_W-2_St3_Sec7",
	["DT/Digi/Wheel-2/Station3/Sector7/Occupancies/OccupancyAllHits_perCh_W-2_St3_Sec7",
	 "DT/Digi/Wheel-2/Station3/Sector7/TimeBoxes/TimeBox_W-2_St3_Sec7_SL1"],
	["DT/Digi/Wheel-2/Station3/Sector7/TimeBoxes/TimeBox_W-2_St3_Sec7_SL2",
	 "DT/Digi/Wheel-2/Station3/Sector7/TimeBoxes/TimeBox_W-2_St3_Sec7_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector7/Station4/Trigger(DDU)_W-2_St4_Sec7",
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec7_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec7_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station4/LocalTriggerPhi/DDU_BestQual_W-2_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec7_St4"])

dtlayout(dqmitems, "Wheel-2/Sector7/Station4/Signal_W-2_St4_Sec7",
	["DT/Digi/Wheel-2/Station4/Sector7/Occupancies/OccupancyAllHits_perCh_W-2_St4_Sec7",
	 "DT/Digi/Wheel-2/Station4/Sector7/TimeBoxes/TimeBox_W-2_St4_Sec7_SL1"],
	["DT/Digi/Wheel-2/Station4/Sector7/TimeBoxes/TimeBox_W-2_St4_Sec7_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector8/Station1/Trigger(DDU)_W-2_St1_Sec8",
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station1/LocalTriggerPhi/DDU_BestQual_W-2_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec8_St1"])

dtlayout(dqmitems, "Wheel-2/Sector8/Station1/Signal_W-2_St1_Sec8",
	["DT/Digi/Wheel-2/Station1/Sector8/Occupancies/OccupancyAllHits_perCh_W-2_St1_Sec8",
	 "DT/Digi/Wheel-2/Station1/Sector8/TimeBoxes/TimeBox_W-2_St1_Sec8_SL1"],
	["DT/Digi/Wheel-2/Station1/Sector8/TimeBoxes/TimeBox_W-2_St1_Sec8_SL2",
	 "DT/Digi/Wheel-2/Station1/Sector8/TimeBoxes/TimeBox_W-2_St1_Sec8_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector8/Station2/Trigger(DDU)_W-2_St2_Sec8",
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station2/LocalTriggerPhi/DDU_BestQual_W-2_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec8_St2"])

dtlayout(dqmitems, "Wheel-2/Sector8/Station2/Signal_W-2_St2_Sec8",
	["DT/Digi/Wheel-2/Station2/Sector8/Occupancies/OccupancyAllHits_perCh_W-2_St2_Sec8",
	 "DT/Digi/Wheel-2/Station2/Sector8/TimeBoxes/TimeBox_W-2_St2_Sec8_SL1"],
	["DT/Digi/Wheel-2/Station2/Sector8/TimeBoxes/TimeBox_W-2_St2_Sec8_SL2",
	 "DT/Digi/Wheel-2/Station2/Sector8/TimeBoxes/TimeBox_W-2_St2_Sec8_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector8/Station3/Trigger(DDU)_W-2_St3_Sec8",
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station3/LocalTriggerPhi/DDU_BestQual_W-2_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec8_St3"])

dtlayout(dqmitems, "Wheel-2/Sector8/Station3/Signal_W-2_St3_Sec8",
	["DT/Digi/Wheel-2/Station3/Sector8/Occupancies/OccupancyAllHits_perCh_W-2_St3_Sec8",
	 "DT/Digi/Wheel-2/Station3/Sector8/TimeBoxes/TimeBox_W-2_St3_Sec8_SL1"],
	["DT/Digi/Wheel-2/Station3/Sector8/TimeBoxes/TimeBox_W-2_St3_Sec8_SL2",
	 "DT/Digi/Wheel-2/Station3/Sector8/TimeBoxes/TimeBox_W-2_St3_Sec8_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector8/Station4/Trigger(DDU)_W-2_St4_Sec8",
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec8_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec8_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station4/LocalTriggerPhi/DDU_BestQual_W-2_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec8_St4"])

dtlayout(dqmitems, "Wheel-2/Sector8/Station4/Signal_W-2_St4_Sec8",
	["DT/Digi/Wheel-2/Station4/Sector8/Occupancies/OccupancyAllHits_perCh_W-2_St4_Sec8",
	 "DT/Digi/Wheel-2/Station4/Sector8/TimeBoxes/TimeBox_W-2_St4_Sec8_SL1"],
	["DT/Digi/Wheel-2/Station4/Sector8/TimeBoxes/TimeBox_W-2_St4_Sec8_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector9/Station1/Trigger(DDU)_W-2_St1_Sec9",
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station1/LocalTriggerPhi/DDU_BestQual_W-2_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec9_St1"])

dtlayout(dqmitems, "Wheel-2/Sector9/Station1/Signal_W-2_St1_Sec9",
	["DT/Digi/Wheel-2/Station1/Sector9/Occupancies/OccupancyAllHits_perCh_W-2_St1_Sec9",
	 "DT/Digi/Wheel-2/Station1/Sector9/TimeBoxes/TimeBox_W-2_St1_Sec9_SL1"],
	["DT/Digi/Wheel-2/Station1/Sector9/TimeBoxes/TimeBox_W-2_St1_Sec9_SL2",
	 "DT/Digi/Wheel-2/Station1/Sector9/TimeBoxes/TimeBox_W-2_St1_Sec9_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector9/Station2/Trigger(DDU)_W-2_St2_Sec9",
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station2/LocalTriggerPhi/DDU_BestQual_W-2_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec9_St2"])

dtlayout(dqmitems, "Wheel-2/Sector9/Station2/Signal_W-2_St2_Sec9",
	["DT/Digi/Wheel-2/Station2/Sector9/Occupancies/OccupancyAllHits_perCh_W-2_St2_Sec9",
	 "DT/Digi/Wheel-2/Station2/Sector9/TimeBoxes/TimeBox_W-2_St2_Sec9_SL1"],
	["DT/Digi/Wheel-2/Station2/Sector9/TimeBoxes/TimeBox_W-2_St2_Sec9_SL2",
	 "DT/Digi/Wheel-2/Station2/Sector9/TimeBoxes/TimeBox_W-2_St2_Sec9_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector9/Station3/Trigger(DDU)_W-2_St3_Sec9",
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station3/LocalTriggerPhi/DDU_BestQual_W-2_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec9_St3"])

dtlayout(dqmitems, "Wheel-2/Sector9/Station3/Signal_W-2_St3_Sec9",
	["DT/Digi/Wheel-2/Station3/Sector9/Occupancies/OccupancyAllHits_perCh_W-2_St3_Sec9",
	 "DT/Digi/Wheel-2/Station3/Sector9/TimeBoxes/TimeBox_W-2_St3_Sec9_SL1"],
	["DT/Digi/Wheel-2/Station3/Sector9/TimeBoxes/TimeBox_W-2_St3_Sec9_SL2",
	 "DT/Digi/Wheel-2/Station3/Sector9/TimeBoxes/TimeBox_W-2_St3_Sec9_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector9/Station4/Trigger(DDU)_W-2_St4_Sec9",
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec9_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec9_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station4/LocalTriggerPhi/DDU_BestQual_W-2_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec9_St4"])

dtlayout(dqmitems, "Wheel-2/Sector9/Station4/Signal_W-2_St4_Sec9",
	["DT/Digi/Wheel-2/Station4/Sector9/Occupancies/OccupancyAllHits_perCh_W-2_St4_Sec9",
	 "DT/Digi/Wheel-2/Station4/Sector9/TimeBoxes/TimeBox_W-2_St4_Sec9_SL1"],
	["DT/Digi/Wheel-2/Station4/Sector9/TimeBoxes/TimeBox_W-2_St4_Sec9_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector10/Station1/Trigger(DDU)_W-2_St1_Sec10",
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station1/LocalTriggerPhi/DDU_BestQual_W-2_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec10_St1"])

dtlayout(dqmitems, "Wheel-2/Sector10/Station1/Signal_W-2_St1_Sec10",
	["DT/Digi/Wheel-2/Station1/Sector10/Occupancies/OccupancyAllHits_perCh_W-2_St1_Sec10",
	 "DT/Digi/Wheel-2/Station1/Sector10/TimeBoxes/TimeBox_W-2_St1_Sec10_SL1"],
	["DT/Digi/Wheel-2/Station1/Sector10/TimeBoxes/TimeBox_W-2_St1_Sec10_SL2",
	 "DT/Digi/Wheel-2/Station1/Sector10/TimeBoxes/TimeBox_W-2_St1_Sec10_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector10/Station2/Trigger(DDU)_W-2_St2_Sec10",
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station2/LocalTriggerPhi/DDU_BestQual_W-2_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec10_St2"])

dtlayout(dqmitems, "Wheel-2/Sector10/Station2/Signal_W-2_St2_Sec10",
	["DT/Digi/Wheel-2/Station2/Sector10/Occupancies/OccupancyAllHits_perCh_W-2_St2_Sec10",
	 "DT/Digi/Wheel-2/Station2/Sector10/TimeBoxes/TimeBox_W-2_St2_Sec10_SL1"],
	["DT/Digi/Wheel-2/Station2/Sector10/TimeBoxes/TimeBox_W-2_St2_Sec10_SL2",
	 "DT/Digi/Wheel-2/Station2/Sector10/TimeBoxes/TimeBox_W-2_St2_Sec10_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector10/Station3/Trigger(DDU)_W-2_St3_Sec10",
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station3/LocalTriggerPhi/DDU_BestQual_W-2_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec10_St3"])

dtlayout(dqmitems, "Wheel-2/Sector10/Station3/Signal_W-2_St3_Sec10",
	["DT/Digi/Wheel-2/Station3/Sector10/Occupancies/OccupancyAllHits_perCh_W-2_St3_Sec10",
	 "DT/Digi/Wheel-2/Station3/Sector10/TimeBoxes/TimeBox_W-2_St3_Sec10_SL1"],
	["DT/Digi/Wheel-2/Station3/Sector10/TimeBoxes/TimeBox_W-2_St3_Sec10_SL2",
	 "DT/Digi/Wheel-2/Station3/Sector10/TimeBoxes/TimeBox_W-2_St3_Sec10_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector10/Station4/Trigger(DDU)_W-2_St4_Sec10",
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec10_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec10_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station4/LocalTriggerPhi/DDU_BestQual_W-2_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec10_St4"])

dtlayout(dqmitems, "Wheel-2/Sector10/Station4/Signal_W-2_St4_Sec10",
	["DT/Digi/Wheel-2/Station4/Sector10/Occupancies/OccupancyAllHits_perCh_W-2_St4_Sec10",
	 "DT/Digi/Wheel-2/Station4/Sector10/TimeBoxes/TimeBox_W-2_St4_Sec10_SL1"],
	["DT/Digi/Wheel-2/Station4/Sector10/TimeBoxes/TimeBox_W-2_St4_Sec10_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector11/Station1/Trigger(DDU)_W-2_St1_Sec11",
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station1/LocalTriggerPhi/DDU_BestQual_W-2_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec11_St1"])

dtlayout(dqmitems, "Wheel-2/Sector11/Station1/Signal_W-2_St1_Sec11",
	["DT/Digi/Wheel-2/Station1/Sector11/Occupancies/OccupancyAllHits_perCh_W-2_St1_Sec11",
	 "DT/Digi/Wheel-2/Station1/Sector11/TimeBoxes/TimeBox_W-2_St1_Sec11_SL1"],
	["DT/Digi/Wheel-2/Station1/Sector11/TimeBoxes/TimeBox_W-2_St1_Sec11_SL2",
	 "DT/Digi/Wheel-2/Station1/Sector11/TimeBoxes/TimeBox_W-2_St1_Sec11_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector11/Station2/Trigger(DDU)_W-2_St2_Sec11",
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station2/LocalTriggerPhi/DDU_BestQual_W-2_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec11_St2"])

dtlayout(dqmitems, "Wheel-2/Sector11/Station2/Signal_W-2_St2_Sec11",
	["DT/Digi/Wheel-2/Station2/Sector11/Occupancies/OccupancyAllHits_perCh_W-2_St2_Sec11",
	 "DT/Digi/Wheel-2/Station2/Sector11/TimeBoxes/TimeBox_W-2_St2_Sec11_SL1"],
	["DT/Digi/Wheel-2/Station2/Sector11/TimeBoxes/TimeBox_W-2_St2_Sec11_SL2",
	 "DT/Digi/Wheel-2/Station2/Sector11/TimeBoxes/TimeBox_W-2_St2_Sec11_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector11/Station3/Trigger(DDU)_W-2_St3_Sec11",
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station3/LocalTriggerPhi/DDU_BestQual_W-2_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec11_St3"])

dtlayout(dqmitems, "Wheel-2/Sector11/Station3/Signal_W-2_St3_Sec11",
	["DT/Digi/Wheel-2/Station3/Sector11/Occupancies/OccupancyAllHits_perCh_W-2_St3_Sec11",
	 "DT/Digi/Wheel-2/Station3/Sector11/TimeBoxes/TimeBox_W-2_St3_Sec11_SL1"],
	["DT/Digi/Wheel-2/Station3/Sector11/TimeBoxes/TimeBox_W-2_St3_Sec11_SL2",
	 "DT/Digi/Wheel-2/Station3/Sector11/TimeBoxes/TimeBox_W-2_St3_Sec11_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector11/Station4/Trigger(DDU)_W-2_St4_Sec11",
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec11_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec11_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station4/LocalTriggerPhi/DDU_BestQual_W-2_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec11_St4"])

dtlayout(dqmitems, "Wheel-2/Sector11/Station4/Signal_W-2_St4_Sec11",
	["DT/Digi/Wheel-2/Station4/Sector11/Occupancies/OccupancyAllHits_perCh_W-2_St4_Sec11",
	 "DT/Digi/Wheel-2/Station4/Sector11/TimeBoxes/TimeBox_W-2_St4_Sec11_SL1"],
	["DT/Digi/Wheel-2/Station4/Sector11/TimeBoxes/TimeBox_W-2_St4_Sec11_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector12/Station1/Trigger(DDU)_W-2_St1_Sec12",
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station1/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station1/LocalTriggerPhi/DDU_BestQual_W-2_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec12_St1"])

dtlayout(dqmitems, "Wheel-2/Sector12/Station1/Signal_W-2_St1_Sec12",
	["DT/Digi/Wheel-2/Station1/Sector12/Occupancies/OccupancyAllHits_perCh_W-2_St1_Sec12",
	 "DT/Digi/Wheel-2/Station1/Sector12/TimeBoxes/TimeBox_W-2_St1_Sec12_SL1"],
	["DT/Digi/Wheel-2/Station1/Sector12/TimeBoxes/TimeBox_W-2_St1_Sec12_SL2",
	 "DT/Digi/Wheel-2/Station1/Sector12/TimeBoxes/TimeBox_W-2_St1_Sec12_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector12/Station2/Trigger(DDU)_W-2_St2_Sec12",
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station2/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station2/LocalTriggerPhi/DDU_BestQual_W-2_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec12_St2"])

dtlayout(dqmitems, "Wheel-2/Sector12/Station2/Signal_W-2_St2_Sec12",
	["DT/Digi/Wheel-2/Station2/Sector12/Occupancies/OccupancyAllHits_perCh_W-2_St2_Sec12",
	 "DT/Digi/Wheel-2/Station2/Sector12/TimeBoxes/TimeBox_W-2_St2_Sec12_SL1"],
	["DT/Digi/Wheel-2/Station2/Sector12/TimeBoxes/TimeBox_W-2_St2_Sec12_SL2",
	 "DT/Digi/Wheel-2/Station2/Sector12/TimeBoxes/TimeBox_W-2_St2_Sec12_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector12/Station3/Trigger(DDU)_W-2_St3_Sec12",
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station3/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station3/LocalTriggerPhi/DDU_BestQual_W-2_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec12_St3"])

dtlayout(dqmitems, "Wheel-2/Sector12/Station3/Signal_W-2_St3_Sec12",
	["DT/Digi/Wheel-2/Station3/Sector12/Occupancies/OccupancyAllHits_perCh_W-2_St3_Sec12",
	 "DT/Digi/Wheel-2/Station3/Sector12/TimeBoxes/TimeBox_W-2_St3_Sec12_SL1"],
	["DT/Digi/Wheel-2/Station3/Sector12/TimeBoxes/TimeBox_W-2_St3_Sec12_SL2",
	 "DT/Digi/Wheel-2/Station3/Sector12/TimeBoxes/TimeBox_W-2_St3_Sec12_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector12/Station4/Trigger(DDU)_W-2_St4_Sec12",
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec12_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station4/LocalTriggerPhi/DDU_Flag1stvsQual_W-2_Sec12_St4"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station4/LocalTriggerPhi/DDU_BestQual_W-2_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBestQual_W-2_Sec12_St4"])

dtlayout(dqmitems, "Wheel-2/Sector12/Station4/Signal_W-2_St4_Sec12",
	["DT/Digi/Wheel-2/Station4/Sector12/Occupancies/OccupancyAllHits_perCh_W-2_St4_Sec12",
	 "DT/Digi/Wheel-2/Station4/Sector12/TimeBoxes/TimeBox_W-2_St4_Sec12_SL1"],
	["DT/Digi/Wheel-2/Station4/Sector12/TimeBoxes/TimeBox_W-2_St4_Sec12_SL3"])


dtlayout(dqmitems, "Wheel0/Sector4/Station4(Sector13)/Signal_W0_St4(Sector13)_Sec4",
	["DT/Digi/Wheel0/Station4/Sector13/Occupancies/OccupancyAllHits_perCh_W0_St4_Sec13",
	 "DT/Digi/Wheel0/Station4/Sector13/TimeBoxes/TimeBox_W0_St4_Sec13_SL1"],
	["DT/Digi/Wheel0/Station4/Sector13/TimeBoxes/TimeBox_W0_St4_Sec13_SL3"])


dtlayout(dqmitems, "Wheel0/Sector10/Station4(Sector14)/Signal_W0_St4(Sector14)_Sec10",
	["DT/Digi/Wheel0/Station4/Sector14/Occupancies/OccupancyAllHits_perCh_W0_St4_Sec14",
	 "DT/Digi/Wheel0/Station4/Sector14/TimeBoxes/TimeBox_W0_St4_Sec14_SL1"],
	["DT/Digi/Wheel0/Station4/Sector14/TimeBoxes/TimeBox_W0_St4_Sec14_SL3"])


dtlayout(dqmitems, "Wheel1/Sector4/Station4(Sector13)/Signal_W1_St4(Sector13)_Sec4",
	["DT/Digi/Wheel1/Station4/Sector13/Occupancies/OccupancyAllHits_perCh_W1_St4_Sec13",
	 "DT/Digi/Wheel1/Station4/Sector13/TimeBoxes/TimeBox_W1_St4_Sec13_SL1"],
	["DT/Digi/Wheel1/Station4/Sector13/TimeBoxes/TimeBox_W1_St4_Sec13_SL3"])


dtlayout(dqmitems, "Wheel1/Sector10/Station4(Sector14)/Signal_W1_St4(Sector14)_Sec10",
	["DT/Digi/Wheel1/Station4/Sector14/Occupancies/OccupancyAllHits_perCh_W1_St4_Sec14",
	 "DT/Digi/Wheel1/Station4/Sector14/TimeBoxes/TimeBox_W1_St4_Sec14_SL1"],
	["DT/Digi/Wheel1/Station4/Sector14/TimeBoxes/TimeBox_W1_St4_Sec14_SL3"])


dtlayout(dqmitems, "Wheel2/Sector4/Station4(Sector13)/Signal_W2_St4(Sector13)_Sec4",
	["DT/Digi/Wheel2/Station4/Sector13/Occupancies/OccupancyAllHits_perCh_W2_St4_Sec13",
	 "DT/Digi/Wheel2/Station4/Sector13/TimeBoxes/TimeBox_W2_St4_Sec13_SL1"],
	["DT/Digi/Wheel2/Station4/Sector13/TimeBoxes/TimeBox_W2_St4_Sec13_SL3"])


dtlayout(dqmitems, "Wheel2/Sector10/Station4(Sector14)/Signal_W2_St4(Sector14)_Sec10",
	["DT/Digi/Wheel2/Station4/Sector14/Occupancies/OccupancyAllHits_perCh_W2_St4_Sec14",
	 "DT/Digi/Wheel2/Station4/Sector14/TimeBoxes/TimeBox_W2_St4_Sec14_SL1"],
	["DT/Digi/Wheel2/Station4/Sector14/TimeBoxes/TimeBox_W2_St4_Sec14_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector4/Station4(Sector13)/Signal_W-1_St4(Sector13)_Sec4",
	["DT/Digi/Wheel-1/Station4/Sector13/Occupancies/OccupancyAllHits_perCh_W-1_St4_Sec13",
	 "DT/Digi/Wheel-1/Station4/Sector13/TimeBoxes/TimeBox_W-1_St4_Sec13_SL1"],
	["DT/Digi/Wheel-1/Station4/Sector13/TimeBoxes/TimeBox_W-1_St4_Sec13_SL3"])


dtlayout(dqmitems, "Wheel-1/Sector10/Station4(Sector14)/Signal_W-1_St4(Sector14)_Sec10",
	["DT/Digi/Wheel-1/Station4/Sector14/Occupancies/OccupancyAllHits_perCh_W-1_St4_Sec14",
	 "DT/Digi/Wheel-1/Station4/Sector14/TimeBoxes/TimeBox_W-1_St4_Sec14_SL1"],
	["DT/Digi/Wheel-1/Station4/Sector14/TimeBoxes/TimeBox_W-1_St4_Sec14_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector4/Station4(Sector13)/Signal_W-2_St4(Sector13)_Sec4",
	["DT/Digi/Wheel-2/Station4/Sector13/Occupancies/OccupancyAllHits_perCh_W-2_St4_Sec13",
	 "DT/Digi/Wheel-2/Station4/Sector13/TimeBoxes/TimeBox_W-2_St4_Sec13_SL1"],
	["DT/Digi/Wheel-2/Station4/Sector13/TimeBoxes/TimeBox_W-2_St4_Sec13_SL3"])


dtlayout(dqmitems, "Wheel-2/Sector10/Station4(Sector14)/Signal_W-2_St4(Sector14)_Sec10",
	["DT/Digi/Wheel-2/Station4/Sector14/Occupancies/OccupancyAllHits_perCh_W-2_St4_Sec14",
	 "DT/Digi/Wheel-2/Station4/Sector14/TimeBoxes/TimeBox_W-2_St4_Sec14_SL1"],
	["DT/Digi/Wheel-2/Station4/Sector14/TimeBoxes/TimeBox_W-2_St4_Sec14_SL3"])



dtlayout(dqmitems, "Wheel0/Sector1/Summary/TriggerQuality_W0_Sec1",
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec1_St4"])

dtlayout(dqmitems, "DataIntegrity/FED772/FED772_ROS1_Summary",
	["DT/DataIntegrity/FED772/FED772_EventLenght",
	 "DT/DataIntegrity/FED772/SC1/FED772_SC1_SCTriggerBX",
	 "DT/DataIntegrity/FED772/ROS1/FED772_ROS1_Event_word_vs_time"],
	["DT/DataIntegrity/FED772/ROS1/FED772_ROS1_ROSError",
	 "DT/DataIntegrity/FED772/ROS1/FED772_ROS1_ROSEventLenght",
	 "DT/DataIntegrity/FED772/SC1/FED772_SC1_SCTriggerQuality",
	 "DT/DataIntegrity/FED772/ROS1/FED772_ROS1_ROB_mean"])


dtlayout(dqmitems, "Wheel0/Sector2/Summary/TriggerQuality_W0_Sec2",
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec2_St4"])

dtlayout(dqmitems, "DataIntegrity/FED772/FED772_ROS2_Summary",
	["DT/DataIntegrity/FED772/FED772_EventLenght",
	 "DT/DataIntegrity/FED772/SC2/FED772_SC2_SCTriggerBX",
	 "DT/DataIntegrity/FED772/ROS2/FED772_ROS2_Event_word_vs_time"],
	["DT/DataIntegrity/FED772/ROS2/FED772_ROS2_ROSError",
	 "DT/DataIntegrity/FED772/ROS2/FED772_ROS2_ROSEventLenght",
	 "DT/DataIntegrity/FED772/SC2/FED772_SC2_SCTriggerQuality",
	 "DT/DataIntegrity/FED772/ROS2/FED772_ROS2_ROB_mean"])


dtlayout(dqmitems, "Wheel0/Sector3/Summary/TriggerQuality_W0_Sec3",
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec3_St4"])

dtlayout(dqmitems, "DataIntegrity/FED772/FED772_ROS3_Summary",
	["DT/DataIntegrity/FED772/FED772_EventLenght",
	 "DT/DataIntegrity/FED772/SC3/FED772_SC3_SCTriggerBX",
	 "DT/DataIntegrity/FED772/ROS3/FED772_ROS3_Event_word_vs_time"],
	["DT/DataIntegrity/FED772/ROS3/FED772_ROS3_ROSError",
	 "DT/DataIntegrity/FED772/ROS3/FED772_ROS3_ROSEventLenght",
	 "DT/DataIntegrity/FED772/SC3/FED772_SC3_SCTriggerQuality",
	 "DT/DataIntegrity/FED772/ROS3/FED772_ROS3_ROB_mean"])


dtlayout(dqmitems, "Wheel0/Sector4/Summary/TriggerQuality_W0_Sec4",
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec4_St4"])

dtlayout(dqmitems, "DataIntegrity/FED772/FED772_ROS4_Summary",
	["DT/DataIntegrity/FED772/FED772_EventLenght",
	 "DT/DataIntegrity/FED772/SC4/FED772_SC4_SCTriggerBX",
	 "DT/DataIntegrity/FED772/ROS4/FED772_ROS4_Event_word_vs_time"],
	["DT/DataIntegrity/FED772/ROS4/FED772_ROS4_ROSError",
	 "DT/DataIntegrity/FED772/ROS4/FED772_ROS4_ROSEventLenght",
	 "DT/DataIntegrity/FED772/SC4/FED772_SC4_SCTriggerQuality",
	 "DT/DataIntegrity/FED772/ROS4/FED772_ROS4_ROB_mean"])


dtlayout(dqmitems, "Wheel0/Sector5/Summary/TriggerQuality_W0_Sec5",
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec5_St4"])

dtlayout(dqmitems, "DataIntegrity/FED772/FED772_ROS5_Summary",
	["DT/DataIntegrity/FED772/FED772_EventLenght",
	 "DT/DataIntegrity/FED772/SC5/FED772_SC5_SCTriggerBX",
	 "DT/DataIntegrity/FED772/ROS5/FED772_ROS5_Event_word_vs_time"],
	["DT/DataIntegrity/FED772/ROS5/FED772_ROS5_ROSError",
	 "DT/DataIntegrity/FED772/ROS5/FED772_ROS5_ROSEventLenght",
	 "DT/DataIntegrity/FED772/SC5/FED772_SC5_SCTriggerQuality",
	 "DT/DataIntegrity/FED772/ROS5/FED772_ROS5_ROB_mean"])


dtlayout(dqmitems, "Wheel0/Sector6/Summary/TriggerQuality_W0_Sec6",
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec6_St4"])

dtlayout(dqmitems, "DataIntegrity/FED772/FED772_ROS6_Summary",
	["DT/DataIntegrity/FED772/FED772_EventLenght",
	 "DT/DataIntegrity/FED772/SC6/FED772_SC6_SCTriggerBX",
	 "DT/DataIntegrity/FED772/ROS6/FED772_ROS6_Event_word_vs_time"],
	["DT/DataIntegrity/FED772/ROS6/FED772_ROS6_ROSError",
	 "DT/DataIntegrity/FED772/ROS6/FED772_ROS6_ROSEventLenght",
	 "DT/DataIntegrity/FED772/SC6/FED772_SC6_SCTriggerQuality",
	 "DT/DataIntegrity/FED772/ROS6/FED772_ROS6_ROB_mean"])


dtlayout(dqmitems, "Wheel0/Sector7/Summary/TriggerQuality_W0_Sec7",
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec7_St4"])

dtlayout(dqmitems, "DataIntegrity/FED772/FED772_ROS7_Summary",
	["DT/DataIntegrity/FED772/FED772_EventLenght",
	 "DT/DataIntegrity/FED772/SC7/FED772_SC7_SCTriggerBX",
	 "DT/DataIntegrity/FED772/ROS7/FED772_ROS7_Event_word_vs_time"],
	["DT/DataIntegrity/FED772/ROS7/FED772_ROS7_ROSError",
	 "DT/DataIntegrity/FED772/ROS7/FED772_ROS7_ROSEventLenght",
	 "DT/DataIntegrity/FED772/SC7/FED772_SC7_SCTriggerQuality",
	 "DT/DataIntegrity/FED772/ROS7/FED772_ROS7_ROB_mean"])


dtlayout(dqmitems, "Wheel0/Sector8/Summary/TriggerQuality_W0_Sec8",
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec8_St4"])

dtlayout(dqmitems, "DataIntegrity/FED772/FED772_ROS8_Summary",
	["DT/DataIntegrity/FED772/FED772_EventLenght",
	 "DT/DataIntegrity/FED772/SC8/FED772_SC8_SCTriggerBX",
	 "DT/DataIntegrity/FED772/ROS8/FED772_ROS8_Event_word_vs_time"],
	["DT/DataIntegrity/FED772/ROS8/FED772_ROS8_ROSError",
	 "DT/DataIntegrity/FED772/ROS8/FED772_ROS8_ROSEventLenght",
	 "DT/DataIntegrity/FED772/SC8/FED772_SC8_SCTriggerQuality",
	 "DT/DataIntegrity/FED772/ROS8/FED772_ROS8_ROB_mean"])


dtlayout(dqmitems, "Wheel0/Sector9/Summary/TriggerQuality_W0_Sec9",
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec9_St4"])

dtlayout(dqmitems, "DataIntegrity/FED772/FED772_ROS9_Summary",
	["DT/DataIntegrity/FED772/FED772_EventLenght",
	 "DT/DataIntegrity/FED772/SC9/FED772_SC9_SCTriggerBX",
	 "DT/DataIntegrity/FED772/ROS9/FED772_ROS9_Event_word_vs_time"],
	["DT/DataIntegrity/FED772/ROS9/FED772_ROS9_ROSError",
	 "DT/DataIntegrity/FED772/ROS9/FED772_ROS9_ROSEventLenght",
	 "DT/DataIntegrity/FED772/SC9/FED772_SC9_SCTriggerQuality",
	 "DT/DataIntegrity/FED772/ROS9/FED772_ROS9_ROB_mean"])


dtlayout(dqmitems, "Wheel0/Sector10/Summary/TriggerQuality_W0_Sec10",
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec10_St4"])

dtlayout(dqmitems, "DataIntegrity/FED772/FED772_ROS10_Summary",
	["DT/DataIntegrity/FED772/FED772_EventLenght",
	 "DT/DataIntegrity/FED772/SC10/FED772_SC10_SCTriggerBX",
	 "DT/DataIntegrity/FED772/ROS10/FED772_ROS10_Event_word_vs_time"],
	["DT/DataIntegrity/FED772/ROS10/FED772_ROS10_ROSError",
	 "DT/DataIntegrity/FED772/ROS10/FED772_ROS10_ROSEventLenght",
	 "DT/DataIntegrity/FED772/SC10/FED772_SC10_SCTriggerQuality",
	 "DT/DataIntegrity/FED772/ROS10/FED772_ROS10_ROB_mean"])


dtlayout(dqmitems, "Wheel0/Sector11/Summary/TriggerQuality_W0_Sec11",
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec11_St4"])

dtlayout(dqmitems, "DataIntegrity/FED772/FED772_ROS11_Summary",
	["DT/DataIntegrity/FED772/FED772_EventLenght",
	 "DT/DataIntegrity/FED772/SC11/FED772_SC11_SCTriggerBX",
	 "DT/DataIntegrity/FED772/ROS11/FED772_ROS11_Event_word_vs_time"],
	["DT/DataIntegrity/FED772/ROS11/FED772_ROS11_ROSError",
	 "DT/DataIntegrity/FED772/ROS11/FED772_ROS11_ROSEventLenght",
	 "DT/DataIntegrity/FED772/SC11/FED772_SC11_SCTriggerQuality",
	 "DT/DataIntegrity/FED772/ROS11/FED772_ROS11_ROB_mean"])


dtlayout(dqmitems, "Wheel0/Sector12/Summary/TriggerQuality_W0_Sec12",
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/LocalTriggerPhi/DDU_BXvsQual_W0_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel0/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/LocalTriggerPhi/DDU_BXvsQual_W0_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel0/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/LocalTriggerPhi/DDU_BXvsQual_W0_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel0/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/LocalTriggerPhi/DDU_BXvsQual_W0_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel0/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W0_Sec12_St4"])

dtlayout(dqmitems, "DataIntegrity/FED772/FED772_ROS12_Summary",
	["DT/DataIntegrity/FED772/FED772_EventLenght",
	 "DT/DataIntegrity/FED772/SC12/FED772_SC12_SCTriggerBX",
	 "DT/DataIntegrity/FED772/ROS12/FED772_ROS12_Event_word_vs_time"],
	["DT/DataIntegrity/FED772/ROS12/FED772_ROS12_ROSError",
	 "DT/DataIntegrity/FED772/ROS12/FED772_ROS12_ROSEventLenght",
	 "DT/DataIntegrity/FED772/SC12/FED772_SC12_SCTriggerQuality",
	 "DT/DataIntegrity/FED772/ROS12/FED772_ROS12_ROB_mean"])


dtlayout(dqmitems, "Wheel1/Sector1/Summary/TriggerQuality_W1_Sec1",
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector1/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec1_St4"])

dtlayout(dqmitems, "DataIntegrity/FED773/FED773_ROS1_Summary",
	["DT/DataIntegrity/FED773/FED773_EventLenght",
	 "DT/DataIntegrity/FED773/SC1/FED773_SC1_SCTriggerBX",
	 "DT/DataIntegrity/FED773/ROS1/FED773_ROS1_Event_word_vs_time"],
	["DT/DataIntegrity/FED773/ROS1/FED773_ROS1_ROSError",
	 "DT/DataIntegrity/FED773/ROS1/FED773_ROS1_ROSEventLenght",
	 "DT/DataIntegrity/FED773/SC1/FED773_SC1_SCTriggerQuality",
	 "DT/DataIntegrity/FED773/ROS1/FED773_ROS1_ROB_mean"])


dtlayout(dqmitems, "Wheel1/Sector2/Summary/TriggerQuality_W1_Sec2",
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector2/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec2_St4"])

dtlayout(dqmitems, "DataIntegrity/FED773/FED773_ROS2_Summary",
	["DT/DataIntegrity/FED773/FED773_EventLenght",
	 "DT/DataIntegrity/FED773/SC2/FED773_SC2_SCTriggerBX",
	 "DT/DataIntegrity/FED773/ROS2/FED773_ROS2_Event_word_vs_time"],
	["DT/DataIntegrity/FED773/ROS2/FED773_ROS2_ROSError",
	 "DT/DataIntegrity/FED773/ROS2/FED773_ROS2_ROSEventLenght",
	 "DT/DataIntegrity/FED773/SC2/FED773_SC2_SCTriggerQuality",
	 "DT/DataIntegrity/FED773/ROS2/FED773_ROS2_ROB_mean"])


dtlayout(dqmitems, "Wheel1/Sector3/Summary/TriggerQuality_W1_Sec3",
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector3/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec3_St4"])

dtlayout(dqmitems, "DataIntegrity/FED773/FED773_ROS3_Summary",
	["DT/DataIntegrity/FED773/FED773_EventLenght",
	 "DT/DataIntegrity/FED773/SC3/FED773_SC3_SCTriggerBX",
	 "DT/DataIntegrity/FED773/ROS3/FED773_ROS3_Event_word_vs_time"],
	["DT/DataIntegrity/FED773/ROS3/FED773_ROS3_ROSError",
	 "DT/DataIntegrity/FED773/ROS3/FED773_ROS3_ROSEventLenght",
	 "DT/DataIntegrity/FED773/SC3/FED773_SC3_SCTriggerQuality",
	 "DT/DataIntegrity/FED773/ROS3/FED773_ROS3_ROB_mean"])


dtlayout(dqmitems, "Wheel1/Sector4/Summary/TriggerQuality_W1_Sec4",
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector4/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec4_St4"])

dtlayout(dqmitems, "DataIntegrity/FED773/FED773_ROS4_Summary",
	["DT/DataIntegrity/FED773/FED773_EventLenght",
	 "DT/DataIntegrity/FED773/SC4/FED773_SC4_SCTriggerBX",
	 "DT/DataIntegrity/FED773/ROS4/FED773_ROS4_Event_word_vs_time"],
	["DT/DataIntegrity/FED773/ROS4/FED773_ROS4_ROSError",
	 "DT/DataIntegrity/FED773/ROS4/FED773_ROS4_ROSEventLenght",
	 "DT/DataIntegrity/FED773/SC4/FED773_SC4_SCTriggerQuality",
	 "DT/DataIntegrity/FED773/ROS4/FED773_ROS4_ROB_mean"])


dtlayout(dqmitems, "Wheel1/Sector5/Summary/TriggerQuality_W1_Sec5",
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector5/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec5_St4"])

dtlayout(dqmitems, "DataIntegrity/FED773/FED773_ROS5_Summary",
	["DT/DataIntegrity/FED773/FED773_EventLenght",
	 "DT/DataIntegrity/FED773/SC5/FED773_SC5_SCTriggerBX",
	 "DT/DataIntegrity/FED773/ROS5/FED773_ROS5_Event_word_vs_time"],
	["DT/DataIntegrity/FED773/ROS5/FED773_ROS5_ROSError",
	 "DT/DataIntegrity/FED773/ROS5/FED773_ROS5_ROSEventLenght",
	 "DT/DataIntegrity/FED773/SC5/FED773_SC5_SCTriggerQuality",
	 "DT/DataIntegrity/FED773/ROS5/FED773_ROS5_ROB_mean"])


dtlayout(dqmitems, "Wheel1/Sector6/Summary/TriggerQuality_W1_Sec6",
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector6/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec6_St4"])

dtlayout(dqmitems, "DataIntegrity/FED773/FED773_ROS6_Summary",
	["DT/DataIntegrity/FED773/FED773_EventLenght",
	 "DT/DataIntegrity/FED773/SC6/FED773_SC6_SCTriggerBX",
	 "DT/DataIntegrity/FED773/ROS6/FED773_ROS6_Event_word_vs_time"],
	["DT/DataIntegrity/FED773/ROS6/FED773_ROS6_ROSError",
	 "DT/DataIntegrity/FED773/ROS6/FED773_ROS6_ROSEventLenght",
	 "DT/DataIntegrity/FED773/SC6/FED773_SC6_SCTriggerQuality",
	 "DT/DataIntegrity/FED773/ROS6/FED773_ROS6_ROB_mean"])


dtlayout(dqmitems, "Wheel1/Sector7/Summary/TriggerQuality_W1_Sec7",
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector7/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec7_St4"])

dtlayout(dqmitems, "DataIntegrity/FED773/FED773_ROS7_Summary",
	["DT/DataIntegrity/FED773/FED773_EventLenght",
	 "DT/DataIntegrity/FED773/SC7/FED773_SC7_SCTriggerBX",
	 "DT/DataIntegrity/FED773/ROS7/FED773_ROS7_Event_word_vs_time"],
	["DT/DataIntegrity/FED773/ROS7/FED773_ROS7_ROSError",
	 "DT/DataIntegrity/FED773/ROS7/FED773_ROS7_ROSEventLenght",
	 "DT/DataIntegrity/FED773/SC7/FED773_SC7_SCTriggerQuality",
	 "DT/DataIntegrity/FED773/ROS7/FED773_ROS7_ROB_mean"])


dtlayout(dqmitems, "Wheel1/Sector8/Summary/TriggerQuality_W1_Sec8",
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector8/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec8_St4"])

dtlayout(dqmitems, "DataIntegrity/FED773/FED773_ROS8_Summary",
	["DT/DataIntegrity/FED773/FED773_EventLenght",
	 "DT/DataIntegrity/FED773/SC8/FED773_SC8_SCTriggerBX",
	 "DT/DataIntegrity/FED773/ROS8/FED773_ROS8_Event_word_vs_time"],
	["DT/DataIntegrity/FED773/ROS8/FED773_ROS8_ROSError",
	 "DT/DataIntegrity/FED773/ROS8/FED773_ROS8_ROSEventLenght",
	 "DT/DataIntegrity/FED773/SC8/FED773_SC8_SCTriggerQuality",
	 "DT/DataIntegrity/FED773/ROS8/FED773_ROS8_ROB_mean"])


dtlayout(dqmitems, "Wheel1/Sector9/Summary/TriggerQuality_W1_Sec9",
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector9/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec9_St4"])

dtlayout(dqmitems, "DataIntegrity/FED773/FED773_ROS9_Summary",
	["DT/DataIntegrity/FED773/FED773_EventLenght",
	 "DT/DataIntegrity/FED773/SC9/FED773_SC9_SCTriggerBX",
	 "DT/DataIntegrity/FED773/ROS9/FED773_ROS9_Event_word_vs_time"],
	["DT/DataIntegrity/FED773/ROS9/FED773_ROS9_ROSError",
	 "DT/DataIntegrity/FED773/ROS9/FED773_ROS9_ROSEventLenght",
	 "DT/DataIntegrity/FED773/SC9/FED773_SC9_SCTriggerQuality",
	 "DT/DataIntegrity/FED773/ROS9/FED773_ROS9_ROB_mean"])


dtlayout(dqmitems, "Wheel1/Sector10/Summary/TriggerQuality_W1_Sec10",
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector10/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec10_St4"])

dtlayout(dqmitems, "DataIntegrity/FED773/FED773_ROS10_Summary",
	["DT/DataIntegrity/FED773/FED773_EventLenght",
	 "DT/DataIntegrity/FED773/SC10/FED773_SC10_SCTriggerBX",
	 "DT/DataIntegrity/FED773/ROS10/FED773_ROS10_Event_word_vs_time"],
	["DT/DataIntegrity/FED773/ROS10/FED773_ROS10_ROSError",
	 "DT/DataIntegrity/FED773/ROS10/FED773_ROS10_ROSEventLenght",
	 "DT/DataIntegrity/FED773/SC10/FED773_SC10_SCTriggerQuality",
	 "DT/DataIntegrity/FED773/ROS10/FED773_ROS10_ROB_mean"])


dtlayout(dqmitems, "Wheel1/Sector11/Summary/TriggerQuality_W1_Sec11",
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector11/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec11_St4"])

dtlayout(dqmitems, "DataIntegrity/FED773/FED773_ROS11_Summary",
	["DT/DataIntegrity/FED773/FED773_EventLenght",
	 "DT/DataIntegrity/FED773/SC11/FED773_SC11_SCTriggerBX",
	 "DT/DataIntegrity/FED773/ROS11/FED773_ROS11_Event_word_vs_time"],
	["DT/DataIntegrity/FED773/ROS11/FED773_ROS11_ROSError",
	 "DT/DataIntegrity/FED773/ROS11/FED773_ROS11_ROSEventLenght",
	 "DT/DataIntegrity/FED773/SC11/FED773_SC11_SCTriggerQuality",
	 "DT/DataIntegrity/FED773/ROS11/FED773_ROS11_ROB_mean"])


dtlayout(dqmitems, "Wheel1/Sector12/Summary/TriggerQuality_W1_Sec12",
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station1/LocalTriggerPhi/DDU_BXvsQual_W1_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel1/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station2/LocalTriggerPhi/DDU_BXvsQual_W1_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel1/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station3/LocalTriggerPhi/DDU_BXvsQual_W1_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel1/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel1/Sector12/Station4/LocalTriggerPhi/DDU_BXvsQual_W1_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel1/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W1_Sec12_St4"])

dtlayout(dqmitems, "DataIntegrity/FED773/FED773_ROS12_Summary",
	["DT/DataIntegrity/FED773/FED773_EventLenght",
	 "DT/DataIntegrity/FED773/SC12/FED773_SC12_SCTriggerBX",
	 "DT/DataIntegrity/FED773/ROS12/FED773_ROS12_Event_word_vs_time"],
	["DT/DataIntegrity/FED773/ROS12/FED773_ROS12_ROSError",
	 "DT/DataIntegrity/FED773/ROS12/FED773_ROS12_ROSEventLenght",
	 "DT/DataIntegrity/FED773/SC12/FED773_SC12_SCTriggerQuality",
	 "DT/DataIntegrity/FED773/ROS12/FED773_ROS12_ROB_mean"])


dtlayout(dqmitems, "Wheel2/Sector1/Summary/TriggerQuality_W2_Sec1",
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector1/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec1_St4"])

dtlayout(dqmitems, "DataIntegrity/FED774/FED774_ROS1_Summary",
	["DT/DataIntegrity/FED774/FED774_EventLenght",
	 "DT/DataIntegrity/FED774/SC1/FED774_SC1_SCTriggerBX",
	 "DT/DataIntegrity/FED774/ROS1/FED774_ROS1_Event_word_vs_time"],
	["DT/DataIntegrity/FED774/ROS1/FED774_ROS1_ROSError",
	 "DT/DataIntegrity/FED774/ROS1/FED774_ROS1_ROSEventLenght",
	 "DT/DataIntegrity/FED774/SC1/FED774_SC1_SCTriggerQuality",
	 "DT/DataIntegrity/FED774/ROS1/FED774_ROS1_ROB_mean"])


dtlayout(dqmitems, "Wheel2/Sector2/Summary/TriggerQuality_W2_Sec2",
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector2/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec2_St4"])

dtlayout(dqmitems, "DataIntegrity/FED774/FED774_ROS2_Summary",
	["DT/DataIntegrity/FED774/FED774_EventLenght",
	 "DT/DataIntegrity/FED774/SC2/FED774_SC2_SCTriggerBX",
	 "DT/DataIntegrity/FED774/ROS2/FED774_ROS2_Event_word_vs_time"],
	["DT/DataIntegrity/FED774/ROS2/FED774_ROS2_ROSError",
	 "DT/DataIntegrity/FED774/ROS2/FED774_ROS2_ROSEventLenght",
	 "DT/DataIntegrity/FED774/SC2/FED774_SC2_SCTriggerQuality",
	 "DT/DataIntegrity/FED774/ROS2/FED774_ROS2_ROB_mean"])


dtlayout(dqmitems, "Wheel2/Sector3/Summary/TriggerQuality_W2_Sec3",
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector3/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec3_St4"])

dtlayout(dqmitems, "DataIntegrity/FED774/FED774_ROS3_Summary",
	["DT/DataIntegrity/FED774/FED774_EventLenght",
	 "DT/DataIntegrity/FED774/SC3/FED774_SC3_SCTriggerBX",
	 "DT/DataIntegrity/FED774/ROS3/FED774_ROS3_Event_word_vs_time"],
	["DT/DataIntegrity/FED774/ROS3/FED774_ROS3_ROSError",
	 "DT/DataIntegrity/FED774/ROS3/FED774_ROS3_ROSEventLenght",
	 "DT/DataIntegrity/FED774/SC3/FED774_SC3_SCTriggerQuality",
	 "DT/DataIntegrity/FED774/ROS3/FED774_ROS3_ROB_mean"])


dtlayout(dqmitems, "Wheel2/Sector4/Summary/TriggerQuality_W2_Sec4",
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector4/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec4_St4"])

dtlayout(dqmitems, "DataIntegrity/FED774/FED774_ROS4_Summary",
	["DT/DataIntegrity/FED774/FED774_EventLenght",
	 "DT/DataIntegrity/FED774/SC4/FED774_SC4_SCTriggerBX",
	 "DT/DataIntegrity/FED774/ROS4/FED774_ROS4_Event_word_vs_time"],
	["DT/DataIntegrity/FED774/ROS4/FED774_ROS4_ROSError",
	 "DT/DataIntegrity/FED774/ROS4/FED774_ROS4_ROSEventLenght",
	 "DT/DataIntegrity/FED774/SC4/FED774_SC4_SCTriggerQuality",
	 "DT/DataIntegrity/FED774/ROS4/FED774_ROS4_ROB_mean"])


dtlayout(dqmitems, "Wheel2/Sector5/Summary/TriggerQuality_W2_Sec5",
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector5/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec5_St4"])

dtlayout(dqmitems, "DataIntegrity/FED774/FED774_ROS5_Summary",
	["DT/DataIntegrity/FED774/FED774_EventLenght",
	 "DT/DataIntegrity/FED774/SC5/FED774_SC5_SCTriggerBX",
	 "DT/DataIntegrity/FED774/ROS5/FED774_ROS5_Event_word_vs_time"],
	["DT/DataIntegrity/FED774/ROS5/FED774_ROS5_ROSError",
	 "DT/DataIntegrity/FED774/ROS5/FED774_ROS5_ROSEventLenght",
	 "DT/DataIntegrity/FED774/SC5/FED774_SC5_SCTriggerQuality",
	 "DT/DataIntegrity/FED774/ROS5/FED774_ROS5_ROB_mean"])


dtlayout(dqmitems, "Wheel2/Sector6/Summary/TriggerQuality_W2_Sec6",
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector6/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec6_St4"])

dtlayout(dqmitems, "DataIntegrity/FED774/FED774_ROS6_Summary",
	["DT/DataIntegrity/FED774/FED774_EventLenght",
	 "DT/DataIntegrity/FED774/SC6/FED774_SC6_SCTriggerBX",
	 "DT/DataIntegrity/FED774/ROS6/FED774_ROS6_Event_word_vs_time"],
	["DT/DataIntegrity/FED774/ROS6/FED774_ROS6_ROSError",
	 "DT/DataIntegrity/FED774/ROS6/FED774_ROS6_ROSEventLenght",
	 "DT/DataIntegrity/FED774/SC6/FED774_SC6_SCTriggerQuality",
	 "DT/DataIntegrity/FED774/ROS6/FED774_ROS6_ROB_mean"])


dtlayout(dqmitems, "Wheel2/Sector7/Summary/TriggerQuality_W2_Sec7",
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector7/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec7_St4"])

dtlayout(dqmitems, "DataIntegrity/FED774/FED774_ROS7_Summary",
	["DT/DataIntegrity/FED774/FED774_EventLenght",
	 "DT/DataIntegrity/FED774/SC7/FED774_SC7_SCTriggerBX",
	 "DT/DataIntegrity/FED774/ROS7/FED774_ROS7_Event_word_vs_time"],
	["DT/DataIntegrity/FED774/ROS7/FED774_ROS7_ROSError",
	 "DT/DataIntegrity/FED774/ROS7/FED774_ROS7_ROSEventLenght",
	 "DT/DataIntegrity/FED774/SC7/FED774_SC7_SCTriggerQuality",
	 "DT/DataIntegrity/FED774/ROS7/FED774_ROS7_ROB_mean"])


dtlayout(dqmitems, "Wheel2/Sector8/Summary/TriggerQuality_W2_Sec8",
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector8/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec8_St4"])

dtlayout(dqmitems, "DataIntegrity/FED774/FED774_ROS8_Summary",
	["DT/DataIntegrity/FED774/FED774_EventLenght",
	 "DT/DataIntegrity/FED774/SC8/FED774_SC8_SCTriggerBX",
	 "DT/DataIntegrity/FED774/ROS8/FED774_ROS8_Event_word_vs_time"],
	["DT/DataIntegrity/FED774/ROS8/FED774_ROS8_ROSError",
	 "DT/DataIntegrity/FED774/ROS8/FED774_ROS8_ROSEventLenght",
	 "DT/DataIntegrity/FED774/SC8/FED774_SC8_SCTriggerQuality",
	 "DT/DataIntegrity/FED774/ROS8/FED774_ROS8_ROB_mean"])


dtlayout(dqmitems, "Wheel2/Sector9/Summary/TriggerQuality_W2_Sec9",
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector9/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec9_St4"])

dtlayout(dqmitems, "DataIntegrity/FED774/FED774_ROS9_Summary",
	["DT/DataIntegrity/FED774/FED774_EventLenght",
	 "DT/DataIntegrity/FED774/SC9/FED774_SC9_SCTriggerBX",
	 "DT/DataIntegrity/FED774/ROS9/FED774_ROS9_Event_word_vs_time"],
	["DT/DataIntegrity/FED774/ROS9/FED774_ROS9_ROSError",
	 "DT/DataIntegrity/FED774/ROS9/FED774_ROS9_ROSEventLenght",
	 "DT/DataIntegrity/FED774/SC9/FED774_SC9_SCTriggerQuality",
	 "DT/DataIntegrity/FED774/ROS9/FED774_ROS9_ROB_mean"])


dtlayout(dqmitems, "Wheel2/Sector10/Summary/TriggerQuality_W2_Sec10",
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector10/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec10_St4"])

dtlayout(dqmitems, "DataIntegrity/FED774/FED774_ROS10_Summary",
	["DT/DataIntegrity/FED774/FED774_EventLenght",
	 "DT/DataIntegrity/FED774/SC10/FED774_SC10_SCTriggerBX",
	 "DT/DataIntegrity/FED774/ROS10/FED774_ROS10_Event_word_vs_time"],
	["DT/DataIntegrity/FED774/ROS10/FED774_ROS10_ROSError",
	 "DT/DataIntegrity/FED774/ROS10/FED774_ROS10_ROSEventLenght",
	 "DT/DataIntegrity/FED774/SC10/FED774_SC10_SCTriggerQuality",
	 "DT/DataIntegrity/FED774/ROS10/FED774_ROS10_ROB_mean"])


dtlayout(dqmitems, "Wheel2/Sector11/Summary/TriggerQuality_W2_Sec11",
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector11/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec11_St4"])

dtlayout(dqmitems, "DataIntegrity/FED774/FED774_ROS11_Summary",
	["DT/DataIntegrity/FED774/FED774_EventLenght",
	 "DT/DataIntegrity/FED774/SC11/FED774_SC11_SCTriggerBX",
	 "DT/DataIntegrity/FED774/ROS11/FED774_ROS11_Event_word_vs_time"],
	["DT/DataIntegrity/FED774/ROS11/FED774_ROS11_ROSError",
	 "DT/DataIntegrity/FED774/ROS11/FED774_ROS11_ROSEventLenght",
	 "DT/DataIntegrity/FED774/SC11/FED774_SC11_SCTriggerQuality",
	 "DT/DataIntegrity/FED774/ROS11/FED774_ROS11_ROB_mean"])


dtlayout(dqmitems, "Wheel2/Sector12/Summary/TriggerQuality_W2_Sec12",
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station1/LocalTriggerPhi/DDU_BXvsQual_W2_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel2/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station2/LocalTriggerPhi/DDU_BXvsQual_W2_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel2/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station3/LocalTriggerPhi/DDU_BXvsQual_W2_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel2/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel2/Sector12/Station4/LocalTriggerPhi/DDU_BXvsQual_W2_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel2/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W2_Sec12_St4"])

dtlayout(dqmitems, "DataIntegrity/FED774/FED774_ROS12_Summary",
	["DT/DataIntegrity/FED774/FED774_EventLenght",
	 "DT/DataIntegrity/FED774/SC12/FED774_SC12_SCTriggerBX",
	 "DT/DataIntegrity/FED774/ROS12/FED774_ROS12_Event_word_vs_time"],
	["DT/DataIntegrity/FED774/ROS12/FED774_ROS12_ROSError",
	 "DT/DataIntegrity/FED774/ROS12/FED774_ROS12_ROSEventLenght",
	 "DT/DataIntegrity/FED774/SC12/FED774_SC12_SCTriggerQuality",
	 "DT/DataIntegrity/FED774/ROS12/FED774_ROS12_ROB_mean"])


dtlayout(dqmitems, "Wheel-1/Sector1/Summary/TriggerQuality_W-1_Sec1",
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector1/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec1_St4"])

dtlayout(dqmitems, "DataIntegrity/FED771/FED771_ROS1_Summary",
	["DT/DataIntegrity/FED771/FED771_EventLenght",
	 "DT/DataIntegrity/FED771/SC1/FED771_SC1_SCTriggerBX",
	 "DT/DataIntegrity/FED771/ROS1/FED771_ROS1_Event_word_vs_time"],
	["DT/DataIntegrity/FED771/ROS1/FED771_ROS1_ROSError",
	 "DT/DataIntegrity/FED771/ROS1/FED771_ROS1_ROSEventLenght",
	 "DT/DataIntegrity/FED771/SC1/FED771_SC1_SCTriggerQuality",
	 "DT/DataIntegrity/FED771/ROS1/FED771_ROS1_ROB_mean"])


dtlayout(dqmitems, "Wheel-1/Sector2/Summary/TriggerQuality_W-1_Sec2",
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector2/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec2_St4"])

dtlayout(dqmitems, "DataIntegrity/FED771/FED771_ROS2_Summary",
	["DT/DataIntegrity/FED771/FED771_EventLenght",
	 "DT/DataIntegrity/FED771/SC2/FED771_SC2_SCTriggerBX",
	 "DT/DataIntegrity/FED771/ROS2/FED771_ROS2_Event_word_vs_time"],
	["DT/DataIntegrity/FED771/ROS2/FED771_ROS2_ROSError",
	 "DT/DataIntegrity/FED771/ROS2/FED771_ROS2_ROSEventLenght",
	 "DT/DataIntegrity/FED771/SC2/FED771_SC2_SCTriggerQuality",
	 "DT/DataIntegrity/FED771/ROS2/FED771_ROS2_ROB_mean"])


dtlayout(dqmitems, "Wheel-1/Sector3/Summary/TriggerQuality_W-1_Sec3",
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector3/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec3_St4"])

dtlayout(dqmitems, "DataIntegrity/FED771/FED771_ROS3_Summary",
	["DT/DataIntegrity/FED771/FED771_EventLenght",
	 "DT/DataIntegrity/FED771/SC3/FED771_SC3_SCTriggerBX",
	 "DT/DataIntegrity/FED771/ROS3/FED771_ROS3_Event_word_vs_time"],
	["DT/DataIntegrity/FED771/ROS3/FED771_ROS3_ROSError",
	 "DT/DataIntegrity/FED771/ROS3/FED771_ROS3_ROSEventLenght",
	 "DT/DataIntegrity/FED771/SC3/FED771_SC3_SCTriggerQuality",
	 "DT/DataIntegrity/FED771/ROS3/FED771_ROS3_ROB_mean"])


dtlayout(dqmitems, "Wheel-1/Sector4/Summary/TriggerQuality_W-1_Sec4",
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector4/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec4_St4"])

dtlayout(dqmitems, "DataIntegrity/FED771/FED771_ROS4_Summary",
	["DT/DataIntegrity/FED771/FED771_EventLenght",
	 "DT/DataIntegrity/FED771/SC4/FED771_SC4_SCTriggerBX",
	 "DT/DataIntegrity/FED771/ROS4/FED771_ROS4_Event_word_vs_time"],
	["DT/DataIntegrity/FED771/ROS4/FED771_ROS4_ROSError",
	 "DT/DataIntegrity/FED771/ROS4/FED771_ROS4_ROSEventLenght",
	 "DT/DataIntegrity/FED771/SC4/FED771_SC4_SCTriggerQuality",
	 "DT/DataIntegrity/FED771/ROS4/FED771_ROS4_ROB_mean"])


dtlayout(dqmitems, "Wheel-1/Sector5/Summary/TriggerQuality_W-1_Sec5",
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector5/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec5_St4"])

dtlayout(dqmitems, "DataIntegrity/FED771/FED771_ROS5_Summary",
	["DT/DataIntegrity/FED771/FED771_EventLenght",
	 "DT/DataIntegrity/FED771/SC5/FED771_SC5_SCTriggerBX",
	 "DT/DataIntegrity/FED771/ROS5/FED771_ROS5_Event_word_vs_time"],
	["DT/DataIntegrity/FED771/ROS5/FED771_ROS5_ROSError",
	 "DT/DataIntegrity/FED771/ROS5/FED771_ROS5_ROSEventLenght",
	 "DT/DataIntegrity/FED771/SC5/FED771_SC5_SCTriggerQuality",
	 "DT/DataIntegrity/FED771/ROS5/FED771_ROS5_ROB_mean"])


dtlayout(dqmitems, "Wheel-1/Sector6/Summary/TriggerQuality_W-1_Sec6",
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector6/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec6_St4"])

dtlayout(dqmitems, "DataIntegrity/FED771/FED771_ROS6_Summary",
	["DT/DataIntegrity/FED771/FED771_EventLenght",
	 "DT/DataIntegrity/FED771/SC6/FED771_SC6_SCTriggerBX",
	 "DT/DataIntegrity/FED771/ROS6/FED771_ROS6_Event_word_vs_time"],
	["DT/DataIntegrity/FED771/ROS6/FED771_ROS6_ROSError",
	 "DT/DataIntegrity/FED771/ROS6/FED771_ROS6_ROSEventLenght",
	 "DT/DataIntegrity/FED771/SC6/FED771_SC6_SCTriggerQuality",
	 "DT/DataIntegrity/FED771/ROS6/FED771_ROS6_ROB_mean"])


dtlayout(dqmitems, "Wheel-1/Sector7/Summary/TriggerQuality_W-1_Sec7",
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector7/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec7_St4"])

dtlayout(dqmitems, "DataIntegrity/FED771/FED771_ROS7_Summary",
	["DT/DataIntegrity/FED771/FED771_EventLenght",
	 "DT/DataIntegrity/FED771/SC7/FED771_SC7_SCTriggerBX",
	 "DT/DataIntegrity/FED771/ROS7/FED771_ROS7_Event_word_vs_time"],
	["DT/DataIntegrity/FED771/ROS7/FED771_ROS7_ROSError",
	 "DT/DataIntegrity/FED771/ROS7/FED771_ROS7_ROSEventLenght",
	 "DT/DataIntegrity/FED771/SC7/FED771_SC7_SCTriggerQuality",
	 "DT/DataIntegrity/FED771/ROS7/FED771_ROS7_ROB_mean"])


dtlayout(dqmitems, "Wheel-1/Sector8/Summary/TriggerQuality_W-1_Sec8",
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector8/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec8_St4"])

dtlayout(dqmitems, "DataIntegrity/FED771/FED771_ROS8_Summary",
	["DT/DataIntegrity/FED771/FED771_EventLenght",
	 "DT/DataIntegrity/FED771/SC8/FED771_SC8_SCTriggerBX",
	 "DT/DataIntegrity/FED771/ROS8/FED771_ROS8_Event_word_vs_time"],
	["DT/DataIntegrity/FED771/ROS8/FED771_ROS8_ROSError",
	 "DT/DataIntegrity/FED771/ROS8/FED771_ROS8_ROSEventLenght",
	 "DT/DataIntegrity/FED771/SC8/FED771_SC8_SCTriggerQuality",
	 "DT/DataIntegrity/FED771/ROS8/FED771_ROS8_ROB_mean"])


dtlayout(dqmitems, "Wheel-1/Sector9/Summary/TriggerQuality_W-1_Sec9",
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector9/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec9_St4"])

dtlayout(dqmitems, "DataIntegrity/FED771/FED771_ROS9_Summary",
	["DT/DataIntegrity/FED771/FED771_EventLenght",
	 "DT/DataIntegrity/FED771/SC9/FED771_SC9_SCTriggerBX",
	 "DT/DataIntegrity/FED771/ROS9/FED771_ROS9_Event_word_vs_time"],
	["DT/DataIntegrity/FED771/ROS9/FED771_ROS9_ROSError",
	 "DT/DataIntegrity/FED771/ROS9/FED771_ROS9_ROSEventLenght",
	 "DT/DataIntegrity/FED771/SC9/FED771_SC9_SCTriggerQuality",
	 "DT/DataIntegrity/FED771/ROS9/FED771_ROS9_ROB_mean"])


dtlayout(dqmitems, "Wheel-1/Sector10/Summary/TriggerQuality_W-1_Sec10",
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector10/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec10_St4"])

dtlayout(dqmitems, "DataIntegrity/FED771/FED771_ROS10_Summary",
	["DT/DataIntegrity/FED771/FED771_EventLenght",
	 "DT/DataIntegrity/FED771/SC10/FED771_SC10_SCTriggerBX",
	 "DT/DataIntegrity/FED771/ROS10/FED771_ROS10_Event_word_vs_time"],
	["DT/DataIntegrity/FED771/ROS10/FED771_ROS10_ROSError",
	 "DT/DataIntegrity/FED771/ROS10/FED771_ROS10_ROSEventLenght",
	 "DT/DataIntegrity/FED771/SC10/FED771_SC10_SCTriggerQuality",
	 "DT/DataIntegrity/FED771/ROS10/FED771_ROS10_ROB_mean"])


dtlayout(dqmitems, "Wheel-1/Sector11/Summary/TriggerQuality_W-1_Sec11",
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector11/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec11_St4"])

dtlayout(dqmitems, "DataIntegrity/FED771/FED771_ROS11_Summary",
	["DT/DataIntegrity/FED771/FED771_EventLenght",
	 "DT/DataIntegrity/FED771/SC11/FED771_SC11_SCTriggerBX",
	 "DT/DataIntegrity/FED771/ROS11/FED771_ROS11_Event_word_vs_time"],
	["DT/DataIntegrity/FED771/ROS11/FED771_ROS11_ROSError",
	 "DT/DataIntegrity/FED771/ROS11/FED771_ROS11_ROSEventLenght",
	 "DT/DataIntegrity/FED771/SC11/FED771_SC11_SCTriggerQuality",
	 "DT/DataIntegrity/FED771/ROS11/FED771_ROS11_ROB_mean"])


dtlayout(dqmitems, "Wheel-1/Sector12/Summary/TriggerQuality_W-1_Sec12",
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station1/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station2/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station3/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel-1/Sector12/Station4/LocalTriggerPhi/DDU_BXvsQual_W-1_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel-1/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-1_Sec12_St4"])

dtlayout(dqmitems, "DataIntegrity/FED771/FED771_ROS12_Summary",
	["DT/DataIntegrity/FED771/FED771_EventLenght",
	 "DT/DataIntegrity/FED771/SC12/FED771_SC12_SCTriggerBX",
	 "DT/DataIntegrity/FED771/ROS12/FED771_ROS12_Event_word_vs_time"],
	["DT/DataIntegrity/FED771/ROS12/FED771_ROS12_ROSError",
	 "DT/DataIntegrity/FED771/ROS12/FED771_ROS12_ROSEventLenght",
	 "DT/DataIntegrity/FED771/SC12/FED771_SC12_SCTriggerQuality",
	 "DT/DataIntegrity/FED771/ROS12/FED771_ROS12_ROB_mean"])


dtlayout(dqmitems, "Wheel-2/Sector1/Summary/TriggerQuality_W-2_Sec1",
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec1_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector1/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec1_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec1_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector1/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec1_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec1_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector1/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec1_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector1/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec1_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector1/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec1_St4"])

dtlayout(dqmitems, "DataIntegrity/FED770/FED770_ROS1_Summary",
	["DT/DataIntegrity/FED770/FED770_EventLenght",
	 "DT/DataIntegrity/FED770/SC1/FED770_SC1_SCTriggerBX",
	 "DT/DataIntegrity/FED770/ROS1/FED770_ROS1_Event_word_vs_time"],
	["DT/DataIntegrity/FED770/ROS1/FED770_ROS1_ROSError",
	 "DT/DataIntegrity/FED770/ROS1/FED770_ROS1_ROSEventLenght",
	 "DT/DataIntegrity/FED770/SC1/FED770_SC1_SCTriggerQuality",
	 "DT/DataIntegrity/FED770/ROS1/FED770_ROS1_ROB_mean"])


dtlayout(dqmitems, "Wheel-2/Sector2/Summary/TriggerQuality_W-2_Sec2",
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec2_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector2/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec2_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec2_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector2/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec2_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec2_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector2/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec2_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector2/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec2_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector2/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec2_St4"])

dtlayout(dqmitems, "DataIntegrity/FED770/FED770_ROS2_Summary",
	["DT/DataIntegrity/FED770/FED770_EventLenght",
	 "DT/DataIntegrity/FED770/SC2/FED770_SC2_SCTriggerBX",
	 "DT/DataIntegrity/FED770/ROS2/FED770_ROS2_Event_word_vs_time"],
	["DT/DataIntegrity/FED770/ROS2/FED770_ROS2_ROSError",
	 "DT/DataIntegrity/FED770/ROS2/FED770_ROS2_ROSEventLenght",
	 "DT/DataIntegrity/FED770/SC2/FED770_SC2_SCTriggerQuality",
	 "DT/DataIntegrity/FED770/ROS2/FED770_ROS2_ROB_mean"])


dtlayout(dqmitems, "Wheel-2/Sector3/Summary/TriggerQuality_W-2_Sec3",
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec3_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector3/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec3_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec3_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector3/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec3_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec3_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector3/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec3_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector3/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec3_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector3/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec3_St4"])

dtlayout(dqmitems, "DataIntegrity/FED770/FED770_ROS3_Summary",
	["DT/DataIntegrity/FED770/FED770_EventLenght",
	 "DT/DataIntegrity/FED770/SC3/FED770_SC3_SCTriggerBX",
	 "DT/DataIntegrity/FED770/ROS3/FED770_ROS3_Event_word_vs_time"],
	["DT/DataIntegrity/FED770/ROS3/FED770_ROS3_ROSError",
	 "DT/DataIntegrity/FED770/ROS3/FED770_ROS3_ROSEventLenght",
	 "DT/DataIntegrity/FED770/SC3/FED770_SC3_SCTriggerQuality",
	 "DT/DataIntegrity/FED770/ROS3/FED770_ROS3_ROB_mean"])


dtlayout(dqmitems, "Wheel-2/Sector4/Summary/TriggerQuality_W-2_Sec4",
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec4_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector4/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec4_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec4_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector4/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec4_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec4_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector4/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec4_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector4/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec4_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector4/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec4_St4"])

dtlayout(dqmitems, "DataIntegrity/FED770/FED770_ROS4_Summary",
	["DT/DataIntegrity/FED770/FED770_EventLenght",
	 "DT/DataIntegrity/FED770/SC4/FED770_SC4_SCTriggerBX",
	 "DT/DataIntegrity/FED770/ROS4/FED770_ROS4_Event_word_vs_time"],
	["DT/DataIntegrity/FED770/ROS4/FED770_ROS4_ROSError",
	 "DT/DataIntegrity/FED770/ROS4/FED770_ROS4_ROSEventLenght",
	 "DT/DataIntegrity/FED770/SC4/FED770_SC4_SCTriggerQuality",
	 "DT/DataIntegrity/FED770/ROS4/FED770_ROS4_ROB_mean"])


dtlayout(dqmitems, "Wheel-2/Sector5/Summary/TriggerQuality_W-2_Sec5",
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec5_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector5/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec5_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec5_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector5/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec5_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec5_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector5/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec5_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector5/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec5_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector5/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec5_St4"])

dtlayout(dqmitems, "DataIntegrity/FED770/FED770_ROS5_Summary",
	["DT/DataIntegrity/FED770/FED770_EventLenght",
	 "DT/DataIntegrity/FED770/SC5/FED770_SC5_SCTriggerBX",
	 "DT/DataIntegrity/FED770/ROS5/FED770_ROS5_Event_word_vs_time"],
	["DT/DataIntegrity/FED770/ROS5/FED770_ROS5_ROSError",
	 "DT/DataIntegrity/FED770/ROS5/FED770_ROS5_ROSEventLenght",
	 "DT/DataIntegrity/FED770/SC5/FED770_SC5_SCTriggerQuality",
	 "DT/DataIntegrity/FED770/ROS5/FED770_ROS5_ROB_mean"])


dtlayout(dqmitems, "Wheel-2/Sector6/Summary/TriggerQuality_W-2_Sec6",
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec6_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector6/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec6_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec6_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector6/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec6_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec6_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector6/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec6_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector6/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec6_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector6/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec6_St4"])

dtlayout(dqmitems, "DataIntegrity/FED770/FED770_ROS6_Summary",
	["DT/DataIntegrity/FED770/FED770_EventLenght",
	 "DT/DataIntegrity/FED770/SC6/FED770_SC6_SCTriggerBX",
	 "DT/DataIntegrity/FED770/ROS6/FED770_ROS6_Event_word_vs_time"],
	["DT/DataIntegrity/FED770/ROS6/FED770_ROS6_ROSError",
	 "DT/DataIntegrity/FED770/ROS6/FED770_ROS6_ROSEventLenght",
	 "DT/DataIntegrity/FED770/SC6/FED770_SC6_SCTriggerQuality",
	 "DT/DataIntegrity/FED770/ROS6/FED770_ROS6_ROB_mean"])


dtlayout(dqmitems, "Wheel-2/Sector7/Summary/TriggerQuality_W-2_Sec7",
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec7_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector7/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec7_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec7_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector7/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec7_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec7_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector7/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec7_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector7/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec7_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector7/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec7_St4"])

dtlayout(dqmitems, "DataIntegrity/FED770/FED770_ROS7_Summary",
	["DT/DataIntegrity/FED770/FED770_EventLenght",
	 "DT/DataIntegrity/FED770/SC7/FED770_SC7_SCTriggerBX",
	 "DT/DataIntegrity/FED770/ROS7/FED770_ROS7_Event_word_vs_time"],
	["DT/DataIntegrity/FED770/ROS7/FED770_ROS7_ROSError",
	 "DT/DataIntegrity/FED770/ROS7/FED770_ROS7_ROSEventLenght",
	 "DT/DataIntegrity/FED770/SC7/FED770_SC7_SCTriggerQuality",
	 "DT/DataIntegrity/FED770/ROS7/FED770_ROS7_ROB_mean"])


dtlayout(dqmitems, "Wheel-2/Sector8/Summary/TriggerQuality_W-2_Sec8",
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec8_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector8/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec8_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec8_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector8/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec8_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec8_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector8/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec8_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector8/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec8_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector8/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec8_St4"])

dtlayout(dqmitems, "DataIntegrity/FED770/FED770_ROS8_Summary",
	["DT/DataIntegrity/FED770/FED770_EventLenght",
	 "DT/DataIntegrity/FED770/SC8/FED770_SC8_SCTriggerBX",
	 "DT/DataIntegrity/FED770/ROS8/FED770_ROS8_Event_word_vs_time"],
	["DT/DataIntegrity/FED770/ROS8/FED770_ROS8_ROSError",
	 "DT/DataIntegrity/FED770/ROS8/FED770_ROS8_ROSEventLenght",
	 "DT/DataIntegrity/FED770/SC8/FED770_SC8_SCTriggerQuality",
	 "DT/DataIntegrity/FED770/ROS8/FED770_ROS8_ROB_mean"])


dtlayout(dqmitems, "Wheel-2/Sector9/Summary/TriggerQuality_W-2_Sec9",
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec9_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector9/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec9_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec9_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector9/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec9_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec9_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector9/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec9_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector9/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec9_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector9/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec9_St4"])

dtlayout(dqmitems, "DataIntegrity/FED770/FED770_ROS9_Summary",
	["DT/DataIntegrity/FED770/FED770_EventLenght",
	 "DT/DataIntegrity/FED770/SC9/FED770_SC9_SCTriggerBX",
	 "DT/DataIntegrity/FED770/ROS9/FED770_ROS9_Event_word_vs_time"],
	["DT/DataIntegrity/FED770/ROS9/FED770_ROS9_ROSError",
	 "DT/DataIntegrity/FED770/ROS9/FED770_ROS9_ROSEventLenght",
	 "DT/DataIntegrity/FED770/SC9/FED770_SC9_SCTriggerQuality",
	 "DT/DataIntegrity/FED770/ROS9/FED770_ROS9_ROB_mean"])


dtlayout(dqmitems, "Wheel-2/Sector10/Summary/TriggerQuality_W-2_Sec10",
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec10_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector10/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec10_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec10_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector10/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec10_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec10_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector10/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec10_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector10/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec10_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector10/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec10_St4"])

dtlayout(dqmitems, "DataIntegrity/FED770/FED770_ROS10_Summary",
	["DT/DataIntegrity/FED770/FED770_EventLenght",
	 "DT/DataIntegrity/FED770/SC10/FED770_SC10_SCTriggerBX",
	 "DT/DataIntegrity/FED770/ROS10/FED770_ROS10_Event_word_vs_time"],
	["DT/DataIntegrity/FED770/ROS10/FED770_ROS10_ROSError",
	 "DT/DataIntegrity/FED770/ROS10/FED770_ROS10_ROSEventLenght",
	 "DT/DataIntegrity/FED770/SC10/FED770_SC10_SCTriggerQuality",
	 "DT/DataIntegrity/FED770/ROS10/FED770_ROS10_ROB_mean"])


dtlayout(dqmitems, "Wheel-2/Sector11/Summary/TriggerQuality_W-2_Sec11",
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec11_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector11/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec11_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec11_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector11/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec11_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec11_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector11/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec11_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector11/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec11_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector11/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec11_St4"])

dtlayout(dqmitems, "DataIntegrity/FED770/FED770_ROS11_Summary",
	["DT/DataIntegrity/FED770/FED770_EventLenght",
	 "DT/DataIntegrity/FED770/SC11/FED770_SC11_SCTriggerBX",
	 "DT/DataIntegrity/FED770/ROS11/FED770_ROS11_Event_word_vs_time"],
	["DT/DataIntegrity/FED770/ROS11/FED770_ROS11_ROSError",
	 "DT/DataIntegrity/FED770/ROS11/FED770_ROS11_ROSEventLenght",
	 "DT/DataIntegrity/FED770/SC11/FED770_SC11_SCTriggerQuality",
	 "DT/DataIntegrity/FED770/ROS11/FED770_ROS11_ROB_mean"])


dtlayout(dqmitems, "Wheel-2/Sector12/Summary/TriggerQuality_W-2_Sec12",
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station1/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec12_St1",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector12/Station1/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec12_St1"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station2/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec12_St2",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector12/Station2/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec12_St2"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station3/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec12_St3",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector12/Station3/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec12_St3"],
	["DT/DTLocalTriggerTask/Wheel-2/Sector12/Station4/LocalTriggerPhi/DDU_BXvsQual_W-2_Sec12_St4",
	 "DT/DTLocalTriggerTask/Wheel-2/Sector12/Station4/LocalTriggerTheta/DDU_ThetaBXvsQual_W-2_Sec12_St4"])

dtlayout(dqmitems, "DataIntegrity/FED770/FED770_ROS12_Summary",
	["DT/DataIntegrity/FED770/FED770_EventLenght",
	 "DT/DataIntegrity/FED770/SC12/FED770_SC12_SCTriggerBX",
	 "DT/DataIntegrity/FED770/ROS12/FED770_ROS12_Event_word_vs_time"],
	["DT/DataIntegrity/FED770/ROS12/FED770_ROS12_ROSError",
	 "DT/DataIntegrity/FED770/ROS12/FED770_ROS12_ROSEventLenght",
	 "DT/DataIntegrity/FED770/SC12/FED770_SC12_SCTriggerQuality",
	 "DT/DataIntegrity/FED770/ROS12/FED770_ROS12_ROB_mean"])

dtlayout(dqmitems,"Wheel0/Summary/LocalTrigger(Client)_W0",
	["DT/Tests/DTLocalTrigger/Wheel0/LocalTriggerPhi/CorrFraction_Phi_W0"],
	["DT/Tests/DTLocalTrigger/Wheel0/LocalTriggerTheta/HFraction_Theta_W0"])

dtlayout(dqmitems,"Wheel1/Summary/LocalTrigger(Client)_W1",
	["DT/Tests/DTLocalTrigger/Wheel1/LocalTriggerPhi/CorrFraction_Phi_W1"],
	["DT/Tests/DTLocalTrigger/Wheel1/LocalTriggerTheta/HFraction_Theta_W1"])

dtlayout(dqmitems,"Wheel2/Summary/LocalTrigger(Client)_W2",
	["DT/Tests/DTLocalTrigger/Wheel2/LocalTriggerPhi/CorrFraction_Phi_W2"],
	["DT/Tests/DTLocalTrigger/Wheel2/LocalTriggerTheta/HFraction_Theta_W2"])

dtlayout(dqmitems,"Wheel-1/Summary/LocalTrigger(Client)_W-1",
	["DT/Tests/DTLocalTrigger/Wheel-1/LocalTriggerPhi/CorrFraction_Phi_W-1"],
	["DT/Tests/DTLocalTrigger/Wheel-1/LocalTriggerTheta/HFraction_Theta_W-1"])

dtlayout(dqmitems,"Wheel-2/Summary/LocalTrigger(Client)_W-2",
	["DT/Tests/DTLocalTrigger/Wheel-2/LocalTriggerPhi/CorrFraction_Phi_W-2"],
	["DT/Tests/DTLocalTrigger/Wheel-2/LocalTriggerTheta/HFraction_Theta_W-2"])

