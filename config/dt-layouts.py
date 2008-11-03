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


dtlayout(dqmitems, "00-Summary/08-SynchNoiseSummary",
         [{ 'path': "DT/04-Noise/SynchNoise/SynchNoiseSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a>  -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])

dtlayout(dqmitems, "00-Summary/09-TestPulseOccupancy",
         [{ 'path': "DT/99-TestPulses/OccupancySummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a>  -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Instructions for the <b>DT shifter</b></a>" }])


#### OCCUPANCIES #################################################################################

for wheel in range(-2, 3):
    for station in range (1, 5):
        for sector in range (1, 15):
            if station != 4 and (sector == 13 or sector == 14):
                continue
            name = "01-Occupancy/Wheel" + str(wheel) + "/St" + str(station) + "_Sec" + str(sector)
            histoname = "DT/01-Digi/Wheel" + str(wheel) + "/Station" + str(station) + "/Sector" + str(sector) + "/OccupancyAllHits_perCh_W" + str(wheel) + "_St" + str(station) + "_Sec" +  str(sector)
            dtlayout(dqmitems, name,[{ 'path': histoname}])

            
#### TIME BOXES #################################################################################

for wheel in range(-2, 3):
    for station in range (1, 5):
        for sector in range (1, 15):
            if station != 4 and (sector == 13 or sector == 14):
                continue
            name = "02-TimeBoxes/Wheel" + str(wheel) + "/St" + str(station) + "_Sec" + str(sector)
            histoname = "DT/01-Digi/Wheel" + str(wheel) + "/Station" + str(station) + "/Sector" + str(sector) + "/TimeBox_W" + str(wheel) + "_St" + str(station) + "_Sec" +  str(sector)
            histoname_SL1 = histoname + "_SL1"
            histoname_SL2 = histoname + "_SL2"
            histoname_SL3 = histoname + "_SL3"
            if station != 4:
                dtlayout(dqmitems, name,[{ 'path': histoname_SL1}],
                         [{ 'path': histoname_SL2}],
                         [{ 'path': histoname_SL3}])
            else:
                dtlayout(dqmitems, name,[{ 'path': histoname_SL1}],
                         [{ 'path': histoname_SL3}])
                
                
#### EVENT SIZE #################################################################################
for fed in range(770, 775):
    for ros in range(1, 13):
        name = "03-ROSEventSize/FED" + str(fed) + "/ROS" + str(ros)
        histoname = "DT/00-DataIntegrity/FED" + str(fed) + "/ROS" + str(ros) + "/FED" + str(fed) + "_ROS" + str(ros) + "_ROSEventLenght"
        dtlayout(dqmitems, name,[{ 'path': histoname}])
#    
#         
#         
#         
#         
        

