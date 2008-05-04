def shifthlxlayout(i, p, *rows): i["Shift/HLX/" + p] = DQMItem(layout=rows)

shifthlxlayout(dqmitems, "Shifter HLX Summary",
  ["HLX/HFCompare/HFCompareEtSum"],
  ["HLX/HFCompare/HFCompareOccBelowSet1","HLX/HFCompare/HFCompareOccBetweenSet1",
   "HLX/HFCompare/HFCompareOccAboveSet1"],
  ["HLX/HFCompare/HFCompareOccBelowSet2","HLX/HFCompare/HFCompareOccBetweenSet2",
   "HLX/HFCompare/HFCompareOccAboveSet2"],
  ["HLX/Average/AvgEtSum"],
  ["HLX/Average/AvgOccBelowSet1","HLX/Average/AvgOccBetweenSet1",
   "HLX/Average/AvgOccAboveSet1"],
  ["HLX/Average/AvgOccBelowSet2","HLX/Average/AvgOccBetweenSet2",
   "HLX/Average/AvgOccAboveSet2"])




