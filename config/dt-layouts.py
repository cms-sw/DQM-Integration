def dtlayout(i, p, *rows): i["DT/Layouts/" + p] = DQMItem(layout=rows)

dtlayout(dqmitems, "00-Summary/00-DataIntegritySummary",
  [{ 'path': "DT/00-DataIntegrity/DataIntegritySummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

dtlayout(dqmitems, "00-Summary/01-OccupancySummary",
  [{ 'path': "DT/01-Digi/OccupancySummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

dtlayout(dqmitems, "00-Summary/02-SegmentSummary",
  [{ 'path': "DT/02-Segments/segmentSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

dtlayout(dqmitems, "00-Summary/03-DDU_TriggerCorrFactionSummary",
  [{ 'path': "DT/03-LocalTrigger/DDU_CorrFractionSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

dtlayout(dqmitems, "00-Summary/04-DDU_Trigger2ndFactionSummary",
  [{ 'path': "DT/03-LocalTrigger/DDU_2ndFractionSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

dtlayout(dqmitems, "00-Summary/05-DCC_TriggerCorrFactionSummary",
  [{ 'path': "DT/03-LocalTrigger/DCC/DCC_CorrFractionSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a>  -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])


dtlayout(dqmitems, "00-Summary/06-DCC_Trigger2ndFactionSummary",
  [{ 'path': "DT/03-LocalTrigger/DCC/DCC_2ndFractionSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a>  -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])


dtlayout(dqmitems, "00-Summary/07-NoiseChannelsSummary",
  [{ 'path': "DT/04-Noise/NoiseSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a>  -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])


#### OCCUPANCIES #################################################################################


##################################################################################################
# Begin Wheel0
##################################################################################################
# Occupancy Wheel0
#           St1

dtlayout(dqmitems, "01-Occupancy/Wheel0/St1_Sec1",
         [{ 'path': "DT/01-Digi/Wheel0/Station1/Sector1/OccupancyAllHits_perCh_W0_St1_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St1_Sec2",
         [{ 'path': "DT/01-Digi/Wheel0/Station1/Sector2/OccupancyAllHits_perCh_W0_St1_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St1_Sec3",
         [{ 'path': "DT/01-Digi/Wheel0/Station1/Sector3/OccupancyAllHits_perCh_W0_St1_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St1_Sec4",
         [{ 'path': "DT/01-Digi/Wheel0/Station1/Sector4/OccupancyAllHits_perCh_W0_St1_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St1_Sec5",
         [{ 'path': "DT/01-Digi/Wheel0/Station1/Sector5/OccupancyAllHits_perCh_W0_St1_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St1_Sec6",
         [{ 'path': "DT/01-Digi/Wheel0/Station1/Sector6/OccupancyAllHits_perCh_W0_St1_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St1_Sec7",
         [{ 'path': "DT/01-Digi/Wheel0/Station1/Sector7/OccupancyAllHits_perCh_W0_St1_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St1_Sec8",
         [{ 'path': "DT/01-Digi/Wheel0/Station1/Sector8/OccupancyAllHits_perCh_W0_St1_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St1_Sec9",
         [{ 'path': "DT/01-Digi/Wheel0/Station1/Sector9/OccupancyAllHits_perCh_W0_St1_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St1_Sec10",
         [{ 'path': "DT/01-Digi/Wheel0/Station1/Sector10/OccupancyAllHits_perCh_W0_St1_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St1_Sec11",
         [{ 'path': "DT/01-Digi/Wheel0/Station1/Sector11/OccupancyAllHits_perCh_W0_St1_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St1_Sec12",
         [{ 'path': "DT/01-Digi/Wheel0/Station1/Sector12/OccupancyAllHits_perCh_W0_St1_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

##################################################################################################
# Occupancy Wheel0
#           St2

dtlayout(dqmitems, "01-Occupancy/Wheel0/St2_Sec1",
         [{ 'path': "DT/01-Digi/Wheel0/Station2/Sector1/OccupancyAllHits_perCh_W0_St2_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St2_Sec2",
         [{ 'path': "DT/01-Digi/Wheel0/Station2/Sector2/OccupancyAllHits_perCh_W0_St2_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St2_Sec3",
         [{ 'path': "DT/01-Digi/Wheel0/Station2/Sector3/OccupancyAllHits_perCh_W0_St2_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St2_Sec4",
         [{ 'path': "DT/01-Digi/Wheel0/Station2/Sector4/OccupancyAllHits_perCh_W0_St2_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St2_Sec5",
         [{ 'path': "DT/01-Digi/Wheel0/Station2/Sector5/OccupancyAllHits_perCh_W0_St2_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St2_Sec6",
         [{ 'path': "DT/01-Digi/Wheel0/Station2/Sector6/OccupancyAllHits_perCh_W0_St2_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St2_Sec7",
         [{ 'path': "DT/01-Digi/Wheel0/Station2/Sector7/OccupancyAllHits_perCh_W0_St2_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St2_Sec8",
         [{ 'path': "DT/01-Digi/Wheel0/Station2/Sector8/OccupancyAllHits_perCh_W0_St2_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St2_Sec9",
         [{ 'path': "DT/01-Digi/Wheel0/Station2/Sector9/OccupancyAllHits_perCh_W0_St2_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St2_Sec10",
         [{ 'path': "DT/01-Digi/Wheel0/Station2/Sector10/OccupancyAllHits_perCh_W0_St2_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St2_Sec11",
         [{ 'path': "DT/01-Digi/Wheel0/Station2/Sector11/OccupancyAllHits_perCh_W0_St2_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St2_Sec12",
         [{ 'path': "DT/01-Digi/Wheel0/Station2/Sector12/OccupancyAllHits_perCh_W0_St2_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

##################################################################################################
# Occupancy Wheel0
#           St3

dtlayout(dqmitems, "01-Occupancy/Wheel0/St3_Sec1",
         [{ 'path': "DT/01-Digi/Wheel0/Station3/Sector1/OccupancyAllHits_perCh_W0_St3_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St3_Sec2",
         [{ 'path': "DT/01-Digi/Wheel0/Station3/Sector2/OccupancyAllHits_perCh_W0_St3_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St3_Sec3",
         [{ 'path': "DT/01-Digi/Wheel0/Station3/Sector3/OccupancyAllHits_perCh_W0_St3_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St3_Sec4",
         [{ 'path': "DT/01-Digi/Wheel0/Station3/Sector4/OccupancyAllHits_perCh_W0_St3_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St3_Sec5",
         [{ 'path': "DT/01-Digi/Wheel0/Station3/Sector5/OccupancyAllHits_perCh_W0_St3_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St3_Sec6",
         [{ 'path': "DT/01-Digi/Wheel0/Station3/Sector6/OccupancyAllHits_perCh_W0_St3_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St3_Sec7",
         [{ 'path': "DT/01-Digi/Wheel0/Station3/Sector7/OccupancyAllHits_perCh_W0_St3_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St3_Sec8",
         [{ 'path': "DT/01-Digi/Wheel0/Station3/Sector8/OccupancyAllHits_perCh_W0_St3_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St3_Sec9",
         [{ 'path': "DT/01-Digi/Wheel0/Station3/Sector9/OccupancyAllHits_perCh_W0_St3_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St3_Sec10",
         [{ 'path': "DT/01-Digi/Wheel0/Station3/Sector10/OccupancyAllHits_perCh_W0_St3_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St3_Sec11",
         [{ 'path': "DT/01-Digi/Wheel0/Station3/Sector11/OccupancyAllHits_perCh_W0_St3_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St3_Sec12",
         [{ 'path': "DT/01-Digi/Wheel0/Station3/Sector12/OccupancyAllHits_perCh_W0_St3_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])


##################################################################################################
# Occupancy Wheel0
#           St4

dtlayout(dqmitems, "01-Occupancy/Wheel0/St4_Sec1",
         [{ 'path': "DT/01-Digi/Wheel0/Station4/Sector1/OccupancyAllHits_perCh_W0_St4_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St4_Sec2",
         [{ 'path': "DT/01-Digi/Wheel0/Station4/Sector2/OccupancyAllHits_perCh_W0_St4_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St4_Sec3",
         [{ 'path': "DT/01-Digi/Wheel0/Station4/Sector3/OccupancyAllHits_perCh_W0_St4_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St4_Sec4",
         [{ 'path': "DT/01-Digi/Wheel0/Station4/Sector4/OccupancyAllHits_perCh_W0_St4_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St4_Sec5",
         [{ 'path': "DT/01-Digi/Wheel0/Station4/Sector5/OccupancyAllHits_perCh_W0_St4_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St4_Sec6",
         [{ 'path': "DT/01-Digi/Wheel0/Station4/Sector6/OccupancyAllHits_perCh_W0_St4_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St4_Sec7",
         [{ 'path': "DT/01-Digi/Wheel0/Station4/Sector7/OccupancyAllHits_perCh_W0_St4_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St4_Sec8",
         [{ 'path': "DT/01-Digi/Wheel0/Station4/Sector8/OccupancyAllHits_perCh_W0_St4_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St4_Sec9",
         [{ 'path': "DT/01-Digi/Wheel0/Station4/Sector9/OccupancyAllHits_perCh_W0_St4_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St4_Sec10",
         [{ 'path': "DT/01-Digi/Wheel0/Station4/Sector10/OccupancyAllHits_perCh_W0_St4_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St4_Sec11",
         [{ 'path': "DT/01-Digi/Wheel0/Station4/Sector11/OccupancyAllHits_perCh_W0_St4_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St4_Sec12",
         [{ 'path': "DT/01-Digi/Wheel0/Station4/Sector12/OccupancyAllHits_perCh_W0_St4_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St4_Sec13",
         [{ 'path': "DT/01-Digi/Wheel0/Station4/Sector13/OccupancyAllHits_perCh_W0_St4_Sec13", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel0/St4_Sec14",
         [{ 'path': "DT/01-Digi/Wheel0/Station4/Sector14/OccupancyAllHits_perCh_W0_St4_Sec14", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])


##################################################################################################
# Begin Wheel1
##################################################################################################
# Occupancy Wheel1
#           St1

dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec1",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector1/OccupancyAllHits_perCh_W1_St1_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec2",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector2/OccupancyAllHits_perCh_W1_St1_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec3",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector3/OccupancyAllHits_perCh_W1_St1_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec4",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector4/OccupancyAllHits_perCh_W1_St1_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec5",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector5/OccupancyAllHits_perCh_W1_St1_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec6",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector6/OccupancyAllHits_perCh_W1_St1_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec7",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector7/OccupancyAllHits_perCh_W1_St1_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec8",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector8/OccupancyAllHits_perCh_W1_St1_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec9",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector9/OccupancyAllHits_perCh_W1_St1_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec10",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector10/OccupancyAllHits_perCh_W1_St1_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec11",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector11/OccupancyAllHits_perCh_W1_St1_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec12",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector12/OccupancyAllHits_perCh_W1_St1_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

##################################################################################################
# Occupancy Wheel1
#           St2

dtlayout(dqmitems, "01-Occupancy/Wheel1/St2_Sec1",
         [{ 'path': "DT/01-Digi/Wheel1/Station2/Sector1/OccupancyAllHits_perCh_W1_St2_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St2_Sec2",
         [{ 'path': "DT/01-Digi/Wheel1/Station2/Sector2/OccupancyAllHits_perCh_W1_St2_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St2_Sec3",
         [{ 'path': "DT/01-Digi/Wheel1/Station2/Sector3/OccupancyAllHits_perCh_W1_St2_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St2_Sec4",
         [{ 'path': "DT/01-Digi/Wheel1/Station2/Sector4/OccupancyAllHits_perCh_W1_St2_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St2_Sec5",
         [{ 'path': "DT/01-Digi/Wheel1/Station2/Sector5/OccupancyAllHits_perCh_W1_St2_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St2_Sec6",
         [{ 'path': "DT/01-Digi/Wheel1/Station2/Sector6/OccupancyAllHits_perCh_W1_St2_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St2_Sec7",
         [{ 'path': "DT/01-Digi/Wheel1/Station2/Sector7/OccupancyAllHits_perCh_W1_St2_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St2_Sec8",
         [{ 'path': "DT/01-Digi/Wheel1/Station2/Sector8/OccupancyAllHits_perCh_W1_St2_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St2_Sec9",
         [{ 'path': "DT/01-Digi/Wheel1/Station2/Sector9/OccupancyAllHits_perCh_W1_St2_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St2_Sec10",
         [{ 'path': "DT/01-Digi/Wheel1/Station2/Sector10/OccupancyAllHits_perCh_W1_St2_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St2_Sec11",
         [{ 'path': "DT/01-Digi/Wheel1/Station2/Sector11/OccupancyAllHits_perCh_W1_St2_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St2_Sec12",
         [{ 'path': "DT/01-Digi/Wheel1/Station2/Sector12/OccupancyAllHits_perCh_W1_St2_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

##################################################################################################
# Occupancy Wheel1
#           St3

dtlayout(dqmitems, "01-Occupancy/Wheel1/St3_Sec1",
         [{ 'path': "DT/01-Digi/Wheel1/Station3/Sector1/OccupancyAllHits_perCh_W1_St3_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St3_Sec2",
         [{ 'path': "DT/01-Digi/Wheel1/Station3/Sector2/OccupancyAllHits_perCh_W1_St3_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St3_Sec3",
         [{ 'path': "DT/01-Digi/Wheel1/Station3/Sector3/OccupancyAllHits_perCh_W1_St3_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St3_Sec4",
         [{ 'path': "DT/01-Digi/Wheel1/Station3/Sector4/OccupancyAllHits_perCh_W1_St3_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St3_Sec5",
         [{ 'path': "DT/01-Digi/Wheel1/Station3/Sector5/OccupancyAllHits_perCh_W1_St3_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St3_Sec6",
         [{ 'path': "DT/01-Digi/Wheel1/Station3/Sector6/OccupancyAllHits_perCh_W1_St3_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St3_Sec7",
         [{ 'path': "DT/01-Digi/Wheel1/Station3/Sector7/OccupancyAllHits_perCh_W1_St3_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St3_Sec8",
         [{ 'path': "DT/01-Digi/Wheel1/Station3/Sector8/OccupancyAllHits_perCh_W1_St3_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St3_Sec9",
         [{ 'path': "DT/01-Digi/Wheel1/Station3/Sector9/OccupancyAllHits_perCh_W1_St3_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St3_Sec10",
         [{ 'path': "DT/01-Digi/Wheel1/Station3/Sector10/OccupancyAllHits_perCh_W1_St3_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St3_Sec11",
         [{ 'path': "DT/01-Digi/Wheel1/Station3/Sector11/OccupancyAllHits_perCh_W1_St3_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St3_Sec12",
         [{ 'path': "DT/01-Digi/Wheel1/Station3/Sector12/OccupancyAllHits_perCh_W1_St3_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])


##################################################################################################
# Occupancy Wheel1
#           St4

dtlayout(dqmitems, "01-Occupancy/Wheel1/St4_Sec1",
         [{ 'path': "DT/01-Digi/Wheel1/Station4/Sector1/OccupancyAllHits_perCh_W1_St4_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St4_Sec2",
         [{ 'path': "DT/01-Digi/Wheel1/Station4/Sector2/OccupancyAllHits_perCh_W1_St4_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St4_Sec3",
         [{ 'path': "DT/01-Digi/Wheel1/Station4/Sector3/OccupancyAllHits_perCh_W1_St4_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St4_Sec4",
         [{ 'path': "DT/01-Digi/Wheel1/Station4/Sector4/OccupancyAllHits_perCh_W1_St4_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St4_Sec5",
         [{ 'path': "DT/01-Digi/Wheel1/Station4/Sector5/OccupancyAllHits_perCh_W1_St4_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St4_Sec6",
         [{ 'path': "DT/01-Digi/Wheel1/Station4/Sector6/OccupancyAllHits_perCh_W1_St4_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St4_Sec7",
         [{ 'path': "DT/01-Digi/Wheel1/Station4/Sector7/OccupancyAllHits_perCh_W1_St4_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St4_Sec8",
         [{ 'path': "DT/01-Digi/Wheel1/Station4/Sector8/OccupancyAllHits_perCh_W1_St4_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St4_Sec9",
         [{ 'path': "DT/01-Digi/Wheel1/Station4/Sector9/OccupancyAllHits_perCh_W1_St4_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St4_Sec10",
         [{ 'path': "DT/01-Digi/Wheel1/Station4/Sector10/OccupancyAllHits_perCh_W1_St4_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St4_Sec11",
         [{ 'path': "DT/01-Digi/Wheel1/Station4/Sector11/OccupancyAllHits_perCh_W1_St4_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St4_Sec12",
         [{ 'path': "DT/01-Digi/Wheel1/Station4/Sector12/OccupancyAllHits_perCh_W1_St4_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St4_Sec13",
         [{ 'path': "DT/01-Digi/Wheel1/Station4/Sector13/OccupancyAllHits_perCh_W1_St4_Sec13", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St4_Sec14",
         [{ 'path': "DT/01-Digi/Wheel1/Station4/Sector14/OccupancyAllHits_perCh_W1_St4_Sec14", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])


dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec1",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector1/OccupancyAllHits_perCh_W1_St1_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec2",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector2/OccupancyAllHits_perCh_W1_St1_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec3",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector3/OccupancyAllHits_perCh_W1_St1_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec4",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector4/OccupancyAllHits_perCh_W1_St1_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec5",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector5/OccupancyAllHits_perCh_W1_St1_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec6",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector6/OccupancyAllHits_perCh_W1_St1_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec7",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector7/OccupancyAllHits_perCh_W1_St1_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec8",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector8/OccupancyAllHits_perCh_W1_St1_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec9",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector9/OccupancyAllHits_perCh_W1_St1_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec10",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector10/OccupancyAllHits_perCh_W1_St1_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec11",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector11/OccupancyAllHits_perCh_W1_St1_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel1/St1_Sec12",
         [{ 'path': "DT/01-Digi/Wheel1/Station1/Sector12/OccupancyAllHits_perCh_W1_St1_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])


##################################################################################################
# Begin Wheel2
##################################################################################################
# Occupancy Wheel2
#           St1

dtlayout(dqmitems, "01-Occupancy/Wheel2/St1_Sec1",
         [{ 'path': "DT/01-Digi/Wheel2/Station1/Sector1/OccupancyAllHits_perCh_W2_St1_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St1_Sec2",
         [{ 'path': "DT/01-Digi/Wheel2/Station1/Sector2/OccupancyAllHits_perCh_W2_St1_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St1_Sec3",
         [{ 'path': "DT/01-Digi/Wheel2/Station1/Sector3/OccupancyAllHits_perCh_W2_St1_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St1_Sec4",
         [{ 'path': "DT/01-Digi/Wheel2/Station1/Sector4/OccupancyAllHits_perCh_W2_St1_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St1_Sec5",
         [{ 'path': "DT/01-Digi/Wheel2/Station1/Sector5/OccupancyAllHits_perCh_W2_St1_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St1_Sec6",
         [{ 'path': "DT/01-Digi/Wheel2/Station1/Sector6/OccupancyAllHits_perCh_W2_St1_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St1_Sec7",
         [{ 'path': "DT/01-Digi/Wheel2/Station1/Sector7/OccupancyAllHits_perCh_W2_St1_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St1_Sec8",
         [{ 'path': "DT/01-Digi/Wheel2/Station1/Sector8/OccupancyAllHits_perCh_W2_St1_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St1_Sec9",
         [{ 'path': "DT/01-Digi/Wheel2/Station1/Sector9/OccupancyAllHits_perCh_W2_St1_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St1_Sec10",
         [{ 'path': "DT/01-Digi/Wheel2/Station1/Sector10/OccupancyAllHits_perCh_W2_St1_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St1_Sec11",
         [{ 'path': "DT/01-Digi/Wheel2/Station1/Sector11/OccupancyAllHits_perCh_W2_St1_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St1_Sec12",
         [{ 'path': "DT/01-Digi/Wheel2/Station1/Sector12/OccupancyAllHits_perCh_W2_St1_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

##################################################################################################
# Occupancy Wheel2
#           St2

dtlayout(dqmitems, "01-Occupancy/Wheel2/St2_Sec1",
         [{ 'path': "DT/01-Digi/Wheel2/Station2/Sector1/OccupancyAllHits_perCh_W2_St2_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St2_Sec2",
         [{ 'path': "DT/01-Digi/Wheel2/Station2/Sector2/OccupancyAllHits_perCh_W2_St2_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St2_Sec3",
         [{ 'path': "DT/01-Digi/Wheel2/Station2/Sector3/OccupancyAllHits_perCh_W2_St2_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St2_Sec4",
         [{ 'path': "DT/01-Digi/Wheel2/Station2/Sector4/OccupancyAllHits_perCh_W2_St2_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St2_Sec5",
         [{ 'path': "DT/01-Digi/Wheel2/Station2/Sector5/OccupancyAllHits_perCh_W2_St2_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St2_Sec6",
         [{ 'path': "DT/01-Digi/Wheel2/Station2/Sector6/OccupancyAllHits_perCh_W2_St2_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St2_Sec7",
         [{ 'path': "DT/01-Digi/Wheel2/Station2/Sector7/OccupancyAllHits_perCh_W2_St2_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St2_Sec8",
         [{ 'path': "DT/01-Digi/Wheel2/Station2/Sector8/OccupancyAllHits_perCh_W2_St2_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St2_Sec9",
         [{ 'path': "DT/01-Digi/Wheel2/Station2/Sector9/OccupancyAllHits_perCh_W2_St2_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St2_Sec10",
         [{ 'path': "DT/01-Digi/Wheel2/Station2/Sector10/OccupancyAllHits_perCh_W2_St2_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St2_Sec11",
         [{ 'path': "DT/01-Digi/Wheel2/Station2/Sector11/OccupancyAllHits_perCh_W2_St2_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St2_Sec12",
         [{ 'path': "DT/01-Digi/Wheel2/Station2/Sector12/OccupancyAllHits_perCh_W2_St2_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

##################################################################################################
# Occupancy Wheel2
#           St3

dtlayout(dqmitems, "01-Occupancy/Wheel2/St3_Sec1",
         [{ 'path': "DT/01-Digi/Wheel2/Station3/Sector1/OccupancyAllHits_perCh_W2_St3_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St3_Sec2",
         [{ 'path': "DT/01-Digi/Wheel2/Station3/Sector2/OccupancyAllHits_perCh_W2_St3_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St3_Sec3",
         [{ 'path': "DT/01-Digi/Wheel2/Station3/Sector3/OccupancyAllHits_perCh_W2_St3_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St3_Sec4",
         [{ 'path': "DT/01-Digi/Wheel2/Station3/Sector4/OccupancyAllHits_perCh_W2_St3_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St3_Sec5",
         [{ 'path': "DT/01-Digi/Wheel2/Station3/Sector5/OccupancyAllHits_perCh_W2_St3_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St3_Sec6",
         [{ 'path': "DT/01-Digi/Wheel2/Station3/Sector6/OccupancyAllHits_perCh_W2_St3_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St3_Sec7",
         [{ 'path': "DT/01-Digi/Wheel2/Station3/Sector7/OccupancyAllHits_perCh_W2_St3_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St3_Sec8",
         [{ 'path': "DT/01-Digi/Wheel2/Station3/Sector8/OccupancyAllHits_perCh_W2_St3_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St3_Sec9",
         [{ 'path': "DT/01-Digi/Wheel2/Station3/Sector9/OccupancyAllHits_perCh_W2_St3_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St3_Sec10",
         [{ 'path': "DT/01-Digi/Wheel2/Station3/Sector10/OccupancyAllHits_perCh_W2_St3_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St3_Sec11",
         [{ 'path': "DT/01-Digi/Wheel2/Station3/Sector11/OccupancyAllHits_perCh_W2_St3_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St3_Sec12",
         [{ 'path': "DT/01-Digi/Wheel2/Station3/Sector12/OccupancyAllHits_perCh_W2_St3_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])


##################################################################################################
# Occupancy Wheel2
#           St4

dtlayout(dqmitems, "01-Occupancy/Wheel2/St4_Sec1",
         [{ 'path': "DT/01-Digi/Wheel2/Station4/Sector1/OccupancyAllHits_perCh_W2_St4_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St4_Sec2",
         [{ 'path': "DT/01-Digi/Wheel2/Station4/Sector2/OccupancyAllHits_perCh_W2_St4_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St4_Sec3",
         [{ 'path': "DT/01-Digi/Wheel2/Station4/Sector3/OccupancyAllHits_perCh_W2_St4_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St4_Sec4",
         [{ 'path': "DT/01-Digi/Wheel2/Station4/Sector4/OccupancyAllHits_perCh_W2_St4_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St4_Sec5",
         [{ 'path': "DT/01-Digi/Wheel2/Station4/Sector5/OccupancyAllHits_perCh_W2_St4_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St4_Sec6",
         [{ 'path': "DT/01-Digi/Wheel2/Station4/Sector6/OccupancyAllHits_perCh_W2_St4_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St4_Sec7",
         [{ 'path': "DT/01-Digi/Wheel2/Station4/Sector7/OccupancyAllHits_perCh_W2_St4_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St4_Sec8",
         [{ 'path': "DT/01-Digi/Wheel2/Station4/Sector8/OccupancyAllHits_perCh_W2_St4_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St4_Sec9",
         [{ 'path': "DT/01-Digi/Wheel2/Station4/Sector9/OccupancyAllHits_perCh_W2_St4_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St4_Sec10",
         [{ 'path': "DT/01-Digi/Wheel2/Station4/Sector10/OccupancyAllHits_perCh_W2_St4_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St4_Sec11",
         [{ 'path': "DT/01-Digi/Wheel2/Station4/Sector11/OccupancyAllHits_perCh_W2_St4_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St4_Sec12",
         [{ 'path': "DT/01-Digi/Wheel2/Station4/Sector12/OccupancyAllHits_perCh_W2_St4_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St4_Sec13",
         [{ 'path': "DT/01-Digi/Wheel2/Station4/Sector13/OccupancyAllHits_perCh_W2_St4_Sec13", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel2/St4_Sec14",
         [{ 'path': "DT/01-Digi/Wheel2/Station4/Sector14/OccupancyAllHits_perCh_W2_St4_Sec14", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])



##################################################################################################
# Begin Wheel-1
##################################################################################################
# Occupancy Wheel-1
#           St1

dtlayout(dqmitems, "01-Occupancy/Wheel-1/St1_Sec1",
         [{ 'path': "DT/01-Digi/Wheel-1/Station1/Sector1/OccupancyAllHits_perCh_W-1_St1_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St1_Sec2",
         [{ 'path': "DT/01-Digi/Wheel-1/Station1/Sector2/OccupancyAllHits_perCh_W-1_St1_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St1_Sec3",
         [{ 'path': "DT/01-Digi/Wheel-1/Station1/Sector3/OccupancyAllHits_perCh_W-1_St1_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St1_Sec4",
         [{ 'path': "DT/01-Digi/Wheel-1/Station1/Sector4/OccupancyAllHits_perCh_W-1_St1_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St1_Sec5",
         [{ 'path': "DT/01-Digi/Wheel-1/Station1/Sector5/OccupancyAllHits_perCh_W-1_St1_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St1_Sec6",
         [{ 'path': "DT/01-Digi/Wheel-1/Station1/Sector6/OccupancyAllHits_perCh_W-1_St1_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St1_Sec7",
         [{ 'path': "DT/01-Digi/Wheel-1/Station1/Sector7/OccupancyAllHits_perCh_W-1_St1_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St1_Sec8",
         [{ 'path': "DT/01-Digi/Wheel-1/Station1/Sector8/OccupancyAllHits_perCh_W-1_St1_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St1_Sec9",
         [{ 'path': "DT/01-Digi/Wheel-1/Station1/Sector9/OccupancyAllHits_perCh_W-1_St1_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St1_Sec10",
         [{ 'path': "DT/01-Digi/Wheel-1/Station1/Sector10/OccupancyAllHits_perCh_W-1_St1_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St1_Sec11",
         [{ 'path': "DT/01-Digi/Wheel-1/Station1/Sector11/OccupancyAllHits_perCh_W-1_St1_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St1_Sec12",
         [{ 'path': "DT/01-Digi/Wheel-1/Station1/Sector12/OccupancyAllHits_perCh_W-1_St1_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

##################################################################################################
# Occupancy Wheel-1
#           St2

dtlayout(dqmitems, "01-Occupancy/Wheel-1/St2_Sec1",
         [{ 'path': "DT/01-Digi/Wheel-1/Station2/Sector1/OccupancyAllHits_perCh_W-1_St2_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St2_Sec2",
         [{ 'path': "DT/01-Digi/Wheel-1/Station2/Sector2/OccupancyAllHits_perCh_W-1_St2_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St2_Sec3",
         [{ 'path': "DT/01-Digi/Wheel-1/Station2/Sector3/OccupancyAllHits_perCh_W-1_St2_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St2_Sec4",
         [{ 'path': "DT/01-Digi/Wheel-1/Station2/Sector4/OccupancyAllHits_perCh_W-1_St2_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St2_Sec5",
         [{ 'path': "DT/01-Digi/Wheel-1/Station2/Sector5/OccupancyAllHits_perCh_W-1_St2_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St2_Sec6",
         [{ 'path': "DT/01-Digi/Wheel-1/Station2/Sector6/OccupancyAllHits_perCh_W-1_St2_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St2_Sec7",
         [{ 'path': "DT/01-Digi/Wheel-1/Station2/Sector7/OccupancyAllHits_perCh_W-1_St2_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St2_Sec8",
         [{ 'path': "DT/01-Digi/Wheel-1/Station2/Sector8/OccupancyAllHits_perCh_W-1_St2_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St2_Sec9",
         [{ 'path': "DT/01-Digi/Wheel-1/Station2/Sector9/OccupancyAllHits_perCh_W-1_St2_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St2_Sec10",
         [{ 'path': "DT/01-Digi/Wheel-1/Station2/Sector10/OccupancyAllHits_perCh_W-1_St2_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St2_Sec11",
         [{ 'path': "DT/01-Digi/Wheel-1/Station2/Sector11/OccupancyAllHits_perCh_W-1_St2_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St2_Sec12",
         [{ 'path': "DT/01-Digi/Wheel-1/Station2/Sector12/OccupancyAllHits_perCh_W-1_St2_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

##################################################################################################
# Occupancy Wheel-1
#           St3

dtlayout(dqmitems, "01-Occupancy/Wheel-1/St3_Sec1",
         [{ 'path': "DT/01-Digi/Wheel-1/Station3/Sector1/OccupancyAllHits_perCh_W-1_St3_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St3_Sec2",
         [{ 'path': "DT/01-Digi/Wheel-1/Station3/Sector2/OccupancyAllHits_perCh_W-1_St3_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St3_Sec3",
         [{ 'path': "DT/01-Digi/Wheel-1/Station3/Sector3/OccupancyAllHits_perCh_W-1_St3_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St3_Sec4",
         [{ 'path': "DT/01-Digi/Wheel-1/Station3/Sector4/OccupancyAllHits_perCh_W-1_St3_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St3_Sec5",
         [{ 'path': "DT/01-Digi/Wheel-1/Station3/Sector5/OccupancyAllHits_perCh_W-1_St3_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St3_Sec6",
         [{ 'path': "DT/01-Digi/Wheel-1/Station3/Sector6/OccupancyAllHits_perCh_W-1_St3_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St3_Sec7",
         [{ 'path': "DT/01-Digi/Wheel-1/Station3/Sector7/OccupancyAllHits_perCh_W-1_St3_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St3_Sec8",
         [{ 'path': "DT/01-Digi/Wheel-1/Station3/Sector8/OccupancyAllHits_perCh_W-1_St3_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St3_Sec9",
         [{ 'path': "DT/01-Digi/Wheel-1/Station3/Sector9/OccupancyAllHits_perCh_W-1_St3_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St3_Sec10",
         [{ 'path': "DT/01-Digi/Wheel-1/Station3/Sector10/OccupancyAllHits_perCh_W-1_St3_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St3_Sec11",
         [{ 'path': "DT/01-Digi/Wheel-1/Station3/Sector11/OccupancyAllHits_perCh_W-1_St3_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St3_Sec12",
         [{ 'path': "DT/01-Digi/Wheel-1/Station3/Sector12/OccupancyAllHits_perCh_W-1_St3_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])


##################################################################################################
# Occupancy Wheel-1
#           St4

dtlayout(dqmitems, "01-Occupancy/Wheel-1/St4_Sec1",
         [{ 'path': "DT/01-Digi/Wheel-1/Station4/Sector1/OccupancyAllHits_perCh_W-1_St4_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St4_Sec2",
         [{ 'path': "DT/01-Digi/Wheel-1/Station4/Sector2/OccupancyAllHits_perCh_W-1_St4_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St4_Sec3",
         [{ 'path': "DT/01-Digi/Wheel-1/Station4/Sector3/OccupancyAllHits_perCh_W-1_St4_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St4_Sec4",
         [{ 'path': "DT/01-Digi/Wheel-1/Station4/Sector4/OccupancyAllHits_perCh_W-1_St4_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St4_Sec5",
         [{ 'path': "DT/01-Digi/Wheel-1/Station4/Sector5/OccupancyAllHits_perCh_W-1_St4_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St4_Sec6",
         [{ 'path': "DT/01-Digi/Wheel-1/Station4/Sector6/OccupancyAllHits_perCh_W-1_St4_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St4_Sec7",
         [{ 'path': "DT/01-Digi/Wheel-1/Station4/Sector7/OccupancyAllHits_perCh_W-1_St4_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St4_Sec8",
         [{ 'path': "DT/01-Digi/Wheel-1/Station4/Sector8/OccupancyAllHits_perCh_W-1_St4_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St4_Sec9",
         [{ 'path': "DT/01-Digi/Wheel-1/Station4/Sector9/OccupancyAllHits_perCh_W-1_St4_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St4_Sec10",
         [{ 'path': "DT/01-Digi/Wheel-1/Station4/Sector10/OccupancyAllHits_perCh_W-1_St4_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St4_Sec11",
         [{ 'path': "DT/01-Digi/Wheel-1/Station4/Sector11/OccupancyAllHits_perCh_W-1_St4_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St4_Sec12",
         [{ 'path': "DT/01-Digi/Wheel-1/Station4/Sector12/OccupancyAllHits_perCh_W-1_St4_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St4_Sec13",
         [{ 'path': "DT/01-Digi/Wheel-1/Station4/Sector13/OccupancyAllHits_perCh_W-1_St4_Sec13", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-1/St4_Sec14",
         [{ 'path': "DT/01-Digi/Wheel-1/Station4/Sector14/OccupancyAllHits_perCh_W-1_St4_Sec14", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])


##################################################################################################
# Begin Wheel-2
##################################################################################################
# Occupancy Wheel-2
#           St1

dtlayout(dqmitems, "01-Occupancy/Wheel-2/St1_Sec1",
         [{ 'path': "DT/01-Digi/Wheel-2/Station1/Sector1/OccupancyAllHits_perCh_W-2_St1_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St1_Sec2",
         [{ 'path': "DT/01-Digi/Wheel-2/Station1/Sector2/OccupancyAllHits_perCh_W-2_St1_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St1_Sec3",
         [{ 'path': "DT/01-Digi/Wheel-2/Station1/Sector3/OccupancyAllHits_perCh_W-2_St1_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St1_Sec4",
         [{ 'path': "DT/01-Digi/Wheel-2/Station1/Sector4/OccupancyAllHits_perCh_W-2_St1_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St1_Sec5",
         [{ 'path': "DT/01-Digi/Wheel-2/Station1/Sector5/OccupancyAllHits_perCh_W-2_St1_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St1_Sec6",
         [{ 'path': "DT/01-Digi/Wheel-2/Station1/Sector6/OccupancyAllHits_perCh_W-2_St1_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St1_Sec7",
         [{ 'path': "DT/01-Digi/Wheel-2/Station1/Sector7/OccupancyAllHits_perCh_W-2_St1_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St1_Sec8",
         [{ 'path': "DT/01-Digi/Wheel-2/Station1/Sector8/OccupancyAllHits_perCh_W-2_St1_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St1_Sec9",
         [{ 'path': "DT/01-Digi/Wheel-2/Station1/Sector9/OccupancyAllHits_perCh_W-2_St1_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St1_Sec10",
         [{ 'path': "DT/01-Digi/Wheel-2/Station1/Sector10/OccupancyAllHits_perCh_W-2_St1_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St1_Sec11",
         [{ 'path': "DT/01-Digi/Wheel-2/Station1/Sector11/OccupancyAllHits_perCh_W-2_St1_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St1_Sec12",
         [{ 'path': "DT/01-Digi/Wheel-2/Station1/Sector12/OccupancyAllHits_perCh_W-2_St1_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

##################################################################################################
# Occupancy Wheel-2
#           St2

dtlayout(dqmitems, "01-Occupancy/Wheel-2/St2_Sec1",
         [{ 'path': "DT/01-Digi/Wheel-2/Station2/Sector1/OccupancyAllHits_perCh_W-2_St2_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St2_Sec2",
         [{ 'path': "DT/01-Digi/Wheel-2/Station2/Sector2/OccupancyAllHits_perCh_W-2_St2_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St2_Sec3",
         [{ 'path': "DT/01-Digi/Wheel-2/Station2/Sector3/OccupancyAllHits_perCh_W-2_St2_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St2_Sec4",
         [{ 'path': "DT/01-Digi/Wheel-2/Station2/Sector4/OccupancyAllHits_perCh_W-2_St2_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St2_Sec5",
         [{ 'path': "DT/01-Digi/Wheel-2/Station2/Sector5/OccupancyAllHits_perCh_W-2_St2_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St2_Sec6",
         [{ 'path': "DT/01-Digi/Wheel-2/Station2/Sector6/OccupancyAllHits_perCh_W-2_St2_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St2_Sec7",
         [{ 'path': "DT/01-Digi/Wheel-2/Station2/Sector7/OccupancyAllHits_perCh_W-2_St2_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St2_Sec8",
         [{ 'path': "DT/01-Digi/Wheel-2/Station2/Sector8/OccupancyAllHits_perCh_W-2_St2_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St2_Sec9",
         [{ 'path': "DT/01-Digi/Wheel-2/Station2/Sector9/OccupancyAllHits_perCh_W-2_St2_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St2_Sec10",
         [{ 'path': "DT/01-Digi/Wheel-2/Station2/Sector10/OccupancyAllHits_perCh_W-2_St2_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St2_Sec11",
         [{ 'path': "DT/01-Digi/Wheel-2/Station2/Sector11/OccupancyAllHits_perCh_W-2_St2_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St2_Sec12",
         [{ 'path': "DT/01-Digi/Wheel-2/Station2/Sector12/OccupancyAllHits_perCh_W-2_St2_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

##################################################################################################
# Occupancy Wheel-2
#           St3

dtlayout(dqmitems, "01-Occupancy/Wheel-2/St3_Sec1",
         [{ 'path': "DT/01-Digi/Wheel-2/Station3/Sector1/OccupancyAllHits_perCh_W-2_St3_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St3_Sec2",
         [{ 'path': "DT/01-Digi/Wheel-2/Station3/Sector2/OccupancyAllHits_perCh_W-2_St3_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St3_Sec3",
         [{ 'path': "DT/01-Digi/Wheel-2/Station3/Sector3/OccupancyAllHits_perCh_W-2_St3_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St3_Sec4",
         [{ 'path': "DT/01-Digi/Wheel-2/Station3/Sector4/OccupancyAllHits_perCh_W-2_St3_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St3_Sec5",
         [{ 'path': "DT/01-Digi/Wheel-2/Station3/Sector5/OccupancyAllHits_perCh_W-2_St3_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St3_Sec6",
         [{ 'path': "DT/01-Digi/Wheel-2/Station3/Sector6/OccupancyAllHits_perCh_W-2_St3_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St3_Sec7",
         [{ 'path': "DT/01-Digi/Wheel-2/Station3/Sector7/OccupancyAllHits_perCh_W-2_St3_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St3_Sec8",
         [{ 'path': "DT/01-Digi/Wheel-2/Station3/Sector8/OccupancyAllHits_perCh_W-2_St3_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St3_Sec9",
         [{ 'path': "DT/01-Digi/Wheel-2/Station3/Sector9/OccupancyAllHits_perCh_W-2_St3_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St3_Sec10",
         [{ 'path': "DT/01-Digi/Wheel-2/Station3/Sector10/OccupancyAllHits_perCh_W-2_St3_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St3_Sec11",
         [{ 'path': "DT/01-Digi/Wheel-2/Station3/Sector11/OccupancyAllHits_perCh_W-2_St3_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St3_Sec12",
         [{ 'path': "DT/01-Digi/Wheel-2/Station3/Sector12/OccupancyAllHits_perCh_W-2_St3_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])


##################################################################################################
# Occupancy Wheel-2
#           St4

dtlayout(dqmitems, "01-Occupancy/Wheel-2/St4_Sec1",
         [{ 'path': "DT/01-Digi/Wheel-2/Station4/Sector1/OccupancyAllHits_perCh_W-2_St4_Sec1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St4_Sec2",
         [{ 'path': "DT/01-Digi/Wheel-2/Station4/Sector2/OccupancyAllHits_perCh_W-2_St4_Sec2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St4_Sec3",
         [{ 'path': "DT/01-Digi/Wheel-2/Station4/Sector3/OccupancyAllHits_perCh_W-2_St4_Sec3", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St4_Sec4",
         [{ 'path': "DT/01-Digi/Wheel-2/Station4/Sector4/OccupancyAllHits_perCh_W-2_St4_Sec4", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St4_Sec5",
         [{ 'path': "DT/01-Digi/Wheel-2/Station4/Sector5/OccupancyAllHits_perCh_W-2_St4_Sec5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St4_Sec6",
         [{ 'path': "DT/01-Digi/Wheel-2/Station4/Sector6/OccupancyAllHits_perCh_W-2_St4_Sec6", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St4_Sec7",
         [{ 'path': "DT/01-Digi/Wheel-2/Station4/Sector7/OccupancyAllHits_perCh_W-2_St4_Sec7", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St4_Sec8",
         [{ 'path': "DT/01-Digi/Wheel-2/Station4/Sector8/OccupancyAllHits_perCh_W-2_St4_Sec8", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St4_Sec9",
         [{ 'path': "DT/01-Digi/Wheel-2/Station4/Sector9/OccupancyAllHits_perCh_W-2_St4_Sec9", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St4_Sec10",
         [{ 'path': "DT/01-Digi/Wheel-2/Station4/Sector10/OccupancyAllHits_perCh_W-2_St4_Sec10", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St4_Sec11",
         [{ 'path': "DT/01-Digi/Wheel-2/Station4/Sector11/OccupancyAllHits_perCh_W-2_St4_Sec11", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St4_Sec12",
         [{ 'path': "DT/01-Digi/Wheel-2/Station4/Sector12/OccupancyAllHits_perCh_W-2_St4_Sec12", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St4_Sec13",
         [{ 'path': "DT/01-Digi/Wheel-2/Station4/Sector13/OccupancyAllHits_perCh_W-2_St4_Sec13", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])
dtlayout(dqmitems, "01-Occupancy/Wheel-2/St4_Sec14",
         [{ 'path': "DT/01-Digi/Wheel-2/Station4/Sector14/OccupancyAllHits_perCh_W-2_St4_Sec14", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a> - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

