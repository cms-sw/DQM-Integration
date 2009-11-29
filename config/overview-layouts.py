def overviewlayout(i, p, *rows): i["Overview/" + p] = DQMItem(layout=rows)

overviewlayout(dqmitems, "test1",
           [{ 'path':"EcalBarrel/EBSummaryClient/EB global summary",
             'description':"This shows ...."}]
           )

overviewlayout(dqmitems, "test2",
           [{ 'path':"DT/01-Digi/OccupancySummary",
	     'description':"This shows ...."}]
           )

