def shiftmuonlayout(i, p, *rows): i["00 Shift/Muons/" + p] = DQMItem(layout=rows)

shiftmuonlayout(dqmitems, "01-staMuonPhiDirection",
                [{ 'path': "Muons/MuonRecoAnalyzer/StaMuon_phi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "02-staMuonEtaDirection",
                [{ 'path': "Muons/MuonRecoAnalyzer/StaMuon_eta", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "03-staMuonPt",
                [{ 'path': "Muons/MuonRecoAnalyzer/StaMuon_pt", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "04-staMuonNumRecHitPerTrack",
                [{ 'path': "Muons/cosmicMuons/NumberOfRecHitsPerTrack_sta", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "05-staMuonHitStaProvenance",
                [{ 'path': "Muons/SegmentTrackAnalyzer/trackHitStaProvenance_cosmicMuons", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "06-glbMuonPhiDirection",
                [{ 'path': "Muons/MuonRecoAnalyzer/GlbMuon_Glb_phi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "07-glbMuonEtaDirection",
                [{ 'path': "Muons/MuonRecoAnalyzer/GlbMuon_Glb_eta", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "08-glbMuonPt",
                [{ 'path': "Muons/MuonRecoAnalyzer/GlbMuon_Glb_pt", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "09-glbMuonNumRecHitPerTrack",
                [{ 'path': "Muons/globalCosmicMuons/NumberOfRecHitsPerTrack_glb", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "10-glbMuonHitStaProvenance",
                [{ 'path': "Muons/SegmentTrackAnalyzer/trackHitStaProvenance_globalCosmicMuons", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "11-glbMuonHitTkProvenance",
                [{ 'path': "Muons/SegmentTrackAnalyzer/trackHitTkProvenance_globalCosmicMuons", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "12-glbMuonPhiResiduals_TkGlb",
                [{ 'path': "Muons/MuonRecoAnalyzer/Res_TkGlb_phi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "13-glbMuonEtaResiduals_TkGlb",
                [{ 'path': "Muons/MuonRecoAnalyzer/Res_TkGlb_eta", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "14-glbMuonPtResiduals_TkGlb",
                [{ 'path': "Muons/MuonRecoAnalyzer/Res_TkGlb_pt", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "15-glbMuonPhiResiduals_GlbSta",
                [{ 'path': "Muons/MuonRecoAnalyzer/Res_GlbSta_phi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "16-glbMuonEtaResiduals_GlbSta",
                [{ 'path': "Muons/MuonRecoAnalyzer/Res_GlbSta_eta", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


shiftmuonlayout(dqmitems, "17-glbMuonPtResiduals_GlbSta",
                [{ 'path': "Muons/MuonRecoAnalyzer/Res_GlbSta_pt", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineMuon>Description</a>" }])


