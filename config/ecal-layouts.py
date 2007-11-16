
def ecallayout(i, p, *rows): i["Layouts/ECAL Layouts/" + p] = DQMItem(layout=rows)

ecallayout(dqmitems, "00-Global-Summary",
  [None,
   "EcalEndcap/EESummaryClient/EE global summary EE +",
   None],
  ["EcalBarrel/EBSummaryClient/EB global summary"],
  [None,
   "EcalEndcap/EESummaryClient/EE global summary EE -",
   None])

