def csclayout(i, p, *rows): i["00 Shift/CSC/" + p] = DQMItem(layout=rows)
  
csclayout(dqmitems,"Chamber Occupancy Exceptions (Statistically Significant)",
  	[{'path': "CSC/Summary/CSC_STATS_occupancy", 'description': "For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#CSC_STATS_occupancy\">here</a>."}])

csclayout(dqmitems,"Chamber Errors and Warnings (Statistically Significant)",
  	[{'path': "CSC/Summary/CSC_STATS_format_err", 'description': "For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#CSC_STATS_format_err\">here</a>."},
  	 {'path': "CSC/Summary/CSC_STATS_l1sync_err", 'description': "For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#CSC_STATS_l1sync_err\">here</a>."}],
  	[{'path': "CSC/Summary/CSC_STATS_fifofull_err", 'description': "For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#CSC_STATS_fifofull_err\">here</a>."},
  	 {'path': "CSC/Summary/CSC_STATS_inputto_err", 'description': "For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#CSC_STATS_inputto_err\">here</a>."}])

csclayout(dqmitems,"Chambers without Data (Statistically Significant)",
  	[{'path': "CSC/Summary/CSC_STATS_wo_alct", 'description': "For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#CSC_STATS_wo_alct\">here</a>."},
  	 {'path': "CSC/Summary/CSC_STATS_wo_clct", 'description': "For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#CSC_STATS_wo_clct\">here</a>."}],
  	[{'path': "CSC/Summary/CSC_STATS_wo_cfeb", 'description': "For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#CSC_STATS_wo_cfeb\">here</a>."},
  	 {'path': "CSC/Summary/CSC_STATS_cfeb_bwords", 'description': "For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftCSC#CSC_STATS_cfeb_bwords\">here</a>."}])

