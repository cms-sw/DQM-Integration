def hltlayout(i, p, *rows): i["00 Shift/HLT/" + p] = DQMItem(layout=rows)
  
hltlayout(dqmitems,"00 Rates per HLT path",
  	[{'path': "HLT/HLTScalers_EvF/cur_rate", 'description': "Trigger Rate per path. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

hltlayout(dqmitems,"01 Rates per HLT path",
  	[{'path': "HLT/HLTScalers_EvF/detailedHltScalers", 'description': "Trigger Rate rejection per filter (Y) and path (X). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

hltlayout(dqmitems,"02 Events per HLT path",
  	[{'path': "HLT/HLTScalers_EvF/hltScalers", 'description': "Events per HLT path. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

hltlayout(dqmitems,"03 Exceptions per HLT path",
  	[{'path': "HLT/HLTScalers_EvF/hltExceptions", 'description': "Exceptions per HLT path. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])
