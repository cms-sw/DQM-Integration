def shiftdtlayout(i, p, *rows): i["00 Shift/DT/" + p] = DQMItem(layout=rows)

shiftdtlayout(dqmitems, "00-SegmentQualitySummary",
  [{ 'path': "DT/02-Segments/segmentSummary", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineDT>Description for the <b>Central DQM Offline shifter</b></a>" }])

shiftdtlayout(dqmitems, "01-SegmentOccupancy_W-2",
  [{ 'path': "DT/02-Segments/Wheel-2/numberOfSegments_W-2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineDT>Description for the <b>Central DQM Offline shifter</b></a>" }])

shiftdtlayout(dqmitems, "02-SegmentOccupancy_W-1",
  [{ 'path': "DT/02-Segments/Wheel-1/numberOfSegments_W-1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineDT>Description for the <b>Central DQM Offline shifter</b></a>" }])

shiftdtlayout(dqmitems, "03-SegmentOccupancy_W0",
  [{ 'path': "DT/02-Segments/Wheel0/numberOfSegments_W0", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineDT>Description for the <b>Central DQM Offline shifter</b></a>" }])

shiftdtlayout(dqmitems, "04-SegmentOccupancy_W1",
  [{ 'path': "DT/02-Segments/Wheel1/numberOfSegments_W1", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineDT>Description for the <b>Central DQM Offline shifter</b></a>" }])

shiftdtlayout(dqmitems, "05-SegmentOccupancy_W2",
  [{ 'path': "DT/02-Segments/Wheel2/numberOfSegments_W2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineDT>Description for the <b>Central DQM Offline shifter</b></a>" }])
