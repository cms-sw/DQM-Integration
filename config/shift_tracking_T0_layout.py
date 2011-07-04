def shifttrackinglayout(i, p, *rows): i["00 Shift/Tracking/" + p] = DQMItem(layout=rows)

shifttrackinglayout(dqmitems, "01 - Tracking ReportSummary",
 [{ 'path': "Tracking/EventInfo/reportSummaryMap",
    'description': " Quality Test results plotted for Tracking parameters : Chi2, TrackRate, #of Hits in Track - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "no" }}])
shifttrackinglayout(dqmitems, "02 - Tracks (pp collisions)",
 [{ 'path': "Tracking/TrackParameters/GeneralProperties/NumberOfGoodTracks_GenTk",
    'description': "Number of Reconstructed Tracks with high purity selection and pt > 1 GeV - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/HitProperties/GoodTrackNumberOfRecHitsPerTrack_GenTk",
    'description': "Number of RecHits per Track with high purity selection and pt > 1 GeV  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/GeneralProperties/GoodTrackPt_ImpactPoint_GenTk",
    'description': "Pt of Reconstructed Track with high purity selection and pt > 1 GeV  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "yes" }}],
 [{ 'path': "Tracking/TrackParameters/GeneralProperties/GoodTrackChi2oNDF_GenTk",
    'description': "Chi Square per DoF with high purity selection and pt > 1 GeV  -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/GeneralProperties/GoodTrackPhi_ImpactPoint_GenTk",
    'description': "Phi distribution of Reconstructed Tracks with high purity selection and pt > 1 GeV -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/GeneralProperties/GoodTrackEta_ImpactPoint_GenTk",
    'description': " Eta distribution of Reconstructed Tracks with high purity selection and pt > 1 GeV - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "yes" }}])

shifttrackinglayout(dqmitems, "03 - Tracks (Cosmic Tracking)",
 [{ 'path': "Tracking/TrackParameters/GeneralProperties/NumberOfTracks_CKFTk",
    'description': "Number of Reconstructed Tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/HitProperties/NumberOfRecHitsPerTrack_CKFTk",
    'description': "Number of RecHits per Track  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/GeneralProperties/TrackPt_CKFTk",
    'description': "Pt of Reconstructed Track  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "yes" }}],
 [{ 'path': "Tracking/TrackParameters/GeneralProperties/Chi2oNDF_CKFTk",
    'description': "Chi Sqare per DoF  -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/GeneralProperties/TrackPhi_CKFTk",
    'description': "Phi distribution of Reconstructed Tracks -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/GeneralProperties/TrackEta_CKFTk",
    'description': " Eta distribution of Reconstructed Tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "yes" }}])

          
