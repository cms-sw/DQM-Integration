def shiftdtlayout(i, p, *rows): i["00 Shift/DT/" + p] = DQMItem(layout=rows)

shiftdtlayout(dqmitems, "00-DataIntegritySummary",
  [{ 'path': "DT/DataIntegrity/DataIntegritySummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description</a>" }])

shiftdtlayout(dqmitems, "01-OccupancySummary",
  [{ 'path': "DT/Digi/OccupancySummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description</a>" }])

shiftdtlayout(dqmitems, "02-SegmentSummary",
  [{ 'path': "DT/Segments/segmentSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description</a>" }])

shiftdtlayout(dqmitems, "03-LocalTriggerSummary",
  [{ 'path': "DT/LocalTrigger/DDU_CorrFractionSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftDT>Description</a>" }])

