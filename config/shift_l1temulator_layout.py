def l1temulayout(i, p, *rows): i["00 Shift/L1TEMU/" + p] = DQMItem(layout=rows)
  
l1temulayout(dqmitems,"00-Error flag Summary",
  	[{'path': "L1TEMU/CSCTF/CTFErrorFlag", 'description': "Missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#reportSummaryMap\">here</a>."}])

l1temulayout(dqmitems,"01-Num. Candidates (Data)",
  	[{'path': "L1TEMU/CSCTPG/CTPErrorFlag", 'description': "Missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#reportSummaryMap\">here</a>."}])

l1temulayout(dqmitems,"02-Num. Candidates (Emulator)",
  	[{'path': "L1TEMU/DTTF/DTFErrorFlag", 'description': "Missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#reportSummaryMap\">here</a>."}])

l1temulayout(dqmitems,"03-System Rates ",
  	[{'path': "L1TEMU/DTTPG/DTPErrorFlag", 'description': "Missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#reportSummaryMap\">here</a>."}])

l1temulayout(dqmitems,"04-System Rates ",
  	[{'path': "L1TEMU/ECAL/ETPErrorFlag", 'description': "Missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#reportSummaryMap\">here</a>."}])

l1temulayout(dqmitems,"05-System Rates ",
  	[{'path': "L1TEMU/GCT/GCTErrorFlag", 'description': "Missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#reportSummaryMap\">here</a>."}])

l1temulayout(dqmitems,"06-System Rates ",
  	[{'path': "L1TEMU/GMT/GMTErrorFlag", 'description': "Missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#reportSummaryMap\">here</a>."}])

l1temulayout(dqmitems,"07-System Rates ",
  	[{'path': "L1TEMU/GT/GLTErrorFlag", 'description': "Missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#reportSummaryMap\">here</a>."}])

l1temulayout(dqmitems,"08-System Rates ",
  	[{'path': "L1TEMU/HCAL/HTPErrorFlag", 'description': "Missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#reportSummaryMap\">here</a>."}])

l1temulayout(dqmitems,"09-System Rates ",
  	[{'path': "L1TEMU/RCT/RCTErrorFlag", 'description': "Missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#reportSummaryMap\">here</a>."}])

l1temulayout(dqmitems,"10-System Rates ",
  	[{'path': "L1TEMU/RPC/RPCErrorFlag", 'description': "Missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#reportSummaryMap\">here</a>."}])
