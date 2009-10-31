def shifthcallayout(i, p, *rows): i["00 Shift/Hcal/" + p] = DQMItem(layout=rows)
shifthcallayout(dqmitems, "Hcal Report Summary",
                [{'path':"Hcal/EventInfo/reportSummaryMap",
                  'description':  "Shows average fraction of good cells per event in each Hcal subdetector (HB/HE/HO/HF/HO0/HO12/HFLumi).  Values should be greater than 0.95.  There are known dead cells in HO, so the HO/HO0/HO12 values will usually be lower than those of the other subdetectors."}]
                )
