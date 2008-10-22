def shiftdtlayout(i, p, *rows): i["00 Shift/DT/" + p] = DQMItem(layout=rows)

shiftdtlayout(dqmitems, "00-DT Shift Histogram",
  [{ 'path': "DT/DTSegmentsTask/02-Segments/segmentSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a>" }])

#shiftdtlayout(dqmitems, "00-DataIntegritySummary",
#  [{ 'path': "DT/00-DataIntegrity/DataIntegritySummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a>" }])

#shiftdtlayout(dqmitems, "01-OccupancySummary",
#  [{ 'path': "DT/01-Digi/OccupancySummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a>" }])

#shiftdtlayout(dqmitems, "02-SegmentSummary",
#  [{ 'path': "DT/02-Segments/segmentSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a>" }])

#shiftdtlayout(dqmitems, "03-DDU_TriggerCorrFactionSummary",
#  [{ 'path': "DT/03-LocalTrigger/DDU_CorrFractionSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a>" }])

# shiftdtlayout(dqmitems, "04-DCC-TriggerCorrFactionSummary",
#   [{ 'path': "DT/03-LocalTrigger/DCC/DCC_CorrFractionSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a>" }])

#shiftdtlayout(dqmitems, "05-DDU_Trigger2ndFactionSummary",
#  [{ 'path': "DT/03-LocalTrigger/DDU_2ndFractionSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a>" }])

# shiftdtlayout(dqmitems, "06-DCC-Trigger2ndFactionSummary",
#   [{ 'path': "DT/03-LocalTrigger/DCC/DCC_2ndFractionSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description for the <b>Central DQM shifter</b></a>" }])

###########

# shiftdtlayout(dqmitems, "00-DataIntegritySummary",
#   [{ 'path': "DT/DataIntegrity/DataIntegritySummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description</a>" }])

# shiftdtlayout(dqmitems, "01-OccupancySummary",
#   [{ 'path': "DT/Digi/OccupancySummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description</a>" }])

# shiftdtlayout(dqmitems, "02-SegmentSummary",
#   [{ 'path': "DT/Segments/segmentSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description</a>" }])

# shiftdtlayout(dqmitems, "03-LocalTriggerSummary",
#   [{ 'path': "DT/LocalTrigger/DDU_CorrFractionSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description</a>" }])

