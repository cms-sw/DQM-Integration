def shiftegammalayout(i, p, *rows): i["00 Shift/Egamma/" + p] = DQMItem(layout=rows)

shiftegammalayout(dqmitems, "00-Egamma Shift Histogram", [{ 'path': "Egamma/PhotonAnalyzer/AllPhotons/Et above 0 GeV/nPhoAllEcal", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineEgamma>Description</a>" }])
