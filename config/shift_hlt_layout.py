def hltlayout(i, p, *rows): i["00 Shift/HLT/" + p] = DQMItem(layout=rows)
  
hltlayout(dqmitems,"00 FourVectors",
  	[{'path': "HLT/FourVectorHLT/HLT1Electron_etaphi", 'description': "Dummy. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

