def shiftmuonlayout(i, p, *rows): i["00 Shift/Muons/" + p] = DQMItem(layout=rows)

shiftmuonlayout(dqmitems, "00-Muon Shift Histogram", [{ 'path': "Muons/MuonRecoAnalyzer/StaMuon_phi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])
