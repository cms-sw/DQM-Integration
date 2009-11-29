def overviewlayout(i, p, *rows): i["Overview/" + p] = DQMItem(layout=rows)

overviewlayout(dqmitems, "test1",
           [{ 'path':"Hcal/EventInfo/reportSummaryMap",
             'description':"This shows ...."}]
           )

overviewlayout(dqmitems, "test2",
           [{ 'path':"CSC/EventInfo/CMSSW_Version",
	     'description':"This shows ...."}]
           )

