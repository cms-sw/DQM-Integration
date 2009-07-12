def sistriplayout(i, p, *rows): i["SiStrip/Layouts/" + p] = DQMItem(layout=rows)

sistriplayout(dqmitems, "00 - ReportSummary",
 [{ 'path': "SiStrip/EventInfo/detFractionReportMap",
    'description': "Fraction of Good Detector Modules plotted in different parts of the Tracker - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "no" }},
  { 'path': "SiStrip/EventInfo/sToNReportMap",
    'description': "Accepted S/N Ratios in different parts of the Tracker. The values are 1 if the ratio is within the accepted range otherwise it is 0  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
 [{ 'path': "SiStrip/EventInfo/reportSummaryMap",
    'description': "Ovelall Report Summary where detector fraction and S/N flags are combined together -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "no" }}])
sistriplayout(dqmitems, "01 - FED Errors",
 [{ 'path': "SiStrip/ReadoutView/FedMonitoringSummary/BadActiveChannelStatusBits",
  'description': "FED IDs having connected channels, with a detected tickmark, with APV/Link errors - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FedMonitoringSummary/BadChannelStatusBits",
  'description': "FED IDs having connected channels with APV/Link Errors - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FedMonitoringSummary/AnyFEDErrors",
  'description': "FED IDs having any FED level error - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
 [{ 'path': "SiStrip/ReadoutView/FedMonitoringSummary/nUnlocked",
    'description': "Number of connected channels per event being without a detected tickmark - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FedMonitoringSummary/nOutOfSync",
    'description': "Number of connected channels per event being out-of-sync - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FedMonitoringSummary/nAPVAddressError",
    'description': "Number of connected APVs per event having wrong pipeline address tickmark - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "02 - OnTrackCluster (StoN)",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_ClusterStoNCorr_OnTrack_in_TIB",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TIB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_ClusterStoNCorr_OnTrack_in_TOB",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TOB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes" }}],
  [{ 'path': "SiStrip/MechanicalView/TID/Summary_ClusterStoNCorr_OnTrack_in_TID",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TID  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes" }},
  {  'path':"SiStrip/MechanicalView/TEC/Summary_ClusterStoNCorr_OnTrack_in_TEC",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TEC  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes" }}])
sistriplayout(dqmitems, "03 - OffTrackCluster (Total Number)",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_TotalNumberOfClusters_OffTrack_in_TIB",
     'description': "Total Number of Off-Track clusters in TIB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_TotalNumberOfClusters_OffTrack_in_TOB",
     'description': "Total Number of Off-Track clusters in TOB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes" }}],
  [{ 'path': "SiStrip/MechanicalView/TID/Summary_TotalNumberOfClusters_OffTrack_in_TID",
     'description': "Total Number of Off-Track clusters in TID  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes" }},
  {  'path':"SiStrip/MechanicalView/TEC/Summary_TotalNumberOfClusters_OffTrack_in_TEC",
     'description': "TotalNumberOf Off-Track clusters in TEC  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes" }}])
sistriplayout(dqmitems, "04 - Tracks - CKF",
 [{ 'path': "Tracking/TrackParameters/NumberOfTracks_CKFTk",
    'description': "Number of Reconstructed Tracks (CKF Algorithm) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/NumberOfRecHitsPerTrack_CKFTk",
    'description': "Number of RecHits per Track (CKF Algorithm) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/TrackPt_CKFTk",
    'description': "Pt of Reconstructed Track (CKF Algorithm) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
 [{ 'path': "Tracking/TrackParameters/Chi2overDoF_CKFTk",
    'description': "Chi Sqare per DoF (CKF Algorithm) -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/TrackPhi_CKFTk",
    'description': "Phi distribution of Reconstructed Tracks (CKF Algorithm) -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/TrackEta_CKFTk",
    'description': " Eta distribution of Reconstructed Tracks by CKF - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}])
sistriplayout(dqmitems, "05 - Tracks - Cosmic Track Finder",
 [{ 'path': "Tracking/TrackParameters/NumberOfTracks_CosmicTF",
    'description': "Number of Reconstructed Tracks (Cosmic Track Finder Algorithm) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/NumberOfRecHitsPerTrack_CosmicTF",
    'description': "Number of RecHits per Track (Cosmic Track Finder Algorithm) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/TrackPt_CosmicTF",
    'description': "Pt of Reconstructed Track (Cosmic Track Finder Algorithm) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
 [{ 'path': "Tracking/TrackParameters/Chi2overDoF_CosmicTF",
    'description': "Chi Sqare per DoF (Cosmic Track Finder Algorithm) -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/TrackPhi_CosmicTk",
    'description': "Phi distribution of Reconstructed Tracks (Cosmic Track Finder Algorithm) -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/TrackEta_CosmicTF",
    'description': " Eta distribution of Reconstructed Tracks by Cosmic Track Finder - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}])
sistriplayout(dqmitems, "06 - Tracks -Rod Search",
 [{ 'path': "Tracking/TrackParameters/NumberOfTracks_RSTk",
    'description': "Number of Reconstructed Tracks (Rod Search  Algorithm) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/NumberOfRecHitsPerTrack_RSTk",
    'description': "Number of RecHits per Track (Rod Search  Algorithm) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/TrackPt_RSTk",
    'description': "Pt of Reconstructed Track (Rod Search  Algorithm) - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}],
 [{ 'path': "Tracking/TrackParameters/Chi2overDoF_RSTk",
    'description': "Chi Sqare per DoF (Rod Search  Algorithm) -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/TrackPhi_RSTk",
    'description': "Phi distribution of Reconstructed Tracks (Rod Search  Algorithm) -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }},
  { 'path': "Tracking/TrackParameters/TrackEta_RSTk",
    'description': " Eta distribution of Reconstructed Tracks by Rod Search  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> ", 'draw': { 'withref': "yes" }}])
sistriplayout(dqmitems, "07 - Detailed FED Errors",
 [{ 'path': "SiStrip/ReadoutView/FedMonitoringSummary/AnyDAQProblems",
    'description': "FED IDs having DAQ problem - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FedMonitoringSummary/CorruptBuffers",
    'description': "FED IDs having corrupt FED buffers - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FedMonitoringSummary/AnyFEProblems",
    'description': "FED IDs having overflowed, missing or with bad majority address FE units - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
 [{ 'path': "SiStrip/ReadoutView/FedMonitoringSummary/FEOverflows",
    'description': "FED IDs having overflowed FE units - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FedMonitoringSummary/FEMissing",
    'description': "FED IDs having missing FE units - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FedMonitoringSummary/DataMissing",
    'description': "FED IDs having missing data but connected channels - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "08 - OnTrackCluster (Total Number)",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_TotalNumberOfClusters_OnTrack_in_TIB",
     'description': "Total Number of On-Track clusters in TIB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_TotalNumberOfClusters_OnTrack_in_TOB",
     'description': "Total Number of On-Track clusters in TOB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes" }}],
  [{ 'path': "SiStrip/MechanicalView/TID/Summary_TotalNumberOfClusters_OnTrack_in_TID",
     'description': "Total Number of On-Track clusters in TID  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes" }},
  {  'path':"SiStrip/MechanicalView/TEC/Summary_TotalNumberOfClusters_OnTrack_in_TEC",
     'description': "TotalNumberOf On-Track clusters in TEC  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes" }}])
sistriplayout(dqmitems, "09 - OffTrackCluster (Charge)",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_ClusterCharge_OffTrack_in_TIB",
     'description': "Charge for Off-Track clusters in TIB - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes"}},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_ClusterCharge_OffTrack_in_TOB",
     'description': "Charge for Off-Track clusters in TOB - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes"}}],
  [{ 'path': "SiStrip/MechanicalView/TID/Summary_ClusterCharge_OffTrack_in_TID",
     'description': "Charge for Off-Track clusters in TID - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes"}},             
   { 'path':"SiStrip/MechanicalView/TEC/Summary_ClusterCharge_OffTrack_in_TEC",
     'description': "Charge for Off-Track clusters in TEC - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripShiftersInstructionsForReReco>SiStripShiftersInstructionsForReReco</a> ", 'draw': { 'withref': "yes"}}])
sistriplayout(dqmitems, "10 - TIBSummary",
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_1/Summary_ClusterStoNCorr__OnTrack__TIB__layer__1",
     'description': "Corrected S/N ratio for TIB Layer #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TIB/layer_2/Summary_ClusterStoNCorr__OnTrack__TIB__layer__2",
     'description': "Corrected S/N ratio for TIB Layer #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_3/Summary_ClusterStoNCorr__OnTrack__TIB__layer__3",
     'description': "Corrected S/N ratio for TIB Layer #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TIB/layer_4/Summary_ClusterStoNCorr__OnTrack__TIB__layer__4",
     'description': "Corrected S/N ratio for TIB Layer #4 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])              
sistriplayout(dqmitems, "11 - TIDFSummary",
  [{ 'path': "SiStrip/MechanicalView/TID/side_2/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__side__2__wheel__1",
     'description': "Corrected S/N ratio for TIDF Wheel #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TID/side_2/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__side__2__wheel__2",
     'description': "Corrected S/N ratio for TIDF Wheel #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TID/side_2/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__side__2__wheel__3",
     'description': "Corrected S/N ratio for TIDF Wheel #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "12 - TIDBSummary",
  [{ 'path': "SiStrip/MechanicalView/TID/side_1/wheel_1/Summary_ClusterStoNCorr__OnTrack__TID__side__1__wheel__1",
     'description': "Corrected S/N ratio for TIDB Wheel #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TID/side_1/wheel_2/Summary_ClusterStoNCorr__OnTrack__TID__side__1__wheel__2",
     'description': "Corrected S/N ratio for TIDB Wheel #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TID/side_1/wheel_3/Summary_ClusterStoNCorr__OnTrack__TID__side__1__wheel__3",
     'description': "Corrected S/N ratio for TIDB Wheel #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "13 - TOBSummary",
  [{ 'path': "SiStrip/MechanicalView/TOB/layer_1/Summary_ClusterStoNCorr__OnTrack__TOB__layer__1",
     'description': "Corrected S/N ratio for TOB Layer #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/layer_2/Summary_ClusterStoNCorr__OnTrack__TOB__layer__2",
     'description': "Corrected S/N ratio for TOB Layer #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/layer_3/Summary_ClusterStoNCorr__OnTrack__TOB__layer__3",
     'description': "Corrected S/N ratio for TOB Layer #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TOB/layer_4/Summary_ClusterStoNCorr__OnTrack__TOB__layer__4",
     'description': "Corrected S/N ratio for TOB Layer #4 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/layer_5/Summary_ClusterStoNCorr__OnTrack__TOB__layer__5",
     'description': "Corrected S/N ratio for TOB Layer #5 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/layer_6/Summary_ClusterStoNCorr__OnTrack__TOB__layer__6",
     'description': "Corrected S/N ratio for TOB Layer #6 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "14 - TECFSummary",
  [{ 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__1",
     'description': "Corrected S/N ratio for TECF Wheel #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__2",
     'description': "Corrected S/N ratio for TECF Wheel #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__3",
     'description': "Corrected S/N ratio for TECF Wheel #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__4",
     'description': "Corrected S/N ratio for TECF Wheel #4 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__5",
     'description': "Corrected S/N ratio for TECF Wheel #5 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__6",
     'description': "Corrected S/N ratio for TECF Wheel #6 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__7",
     'description': "Corrected S/N ratio for TECF Wheel #7 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__8",
     'description': "Corrected S/N ratio for TECF Wheel #8 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_2/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__side__2__wheel__9",
     'description': "Corrected S/N ratio for TECF Wheel #9 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
sistriplayout(dqmitems, "15 - TECBSummary",
   [{ 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_1/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__1",
     'description': "Corrected S/N ratio for TECB Wheel #1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_2/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__2",
     'description': "Corrected S/N ratio for TECB Wheel #2 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_3/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__3",
     'description': "Corrected S/N ratio for TECB Wheel #3 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_4/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__4",
     'description': "Corrected S/N ratio for TECB Wheel #4 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_5/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__5",
     'description': "Corrected S/N ratio for TECB Wheel #5 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_6/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__6",
     'description': "Corrected S/N ratio for TECB Wheel #6 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_7/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__7",
     'description': "Corrected S/N ratio for TECB Wheel #7 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_8/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__8",
     'description': "Corrected S/N ratio for TECB Wheel #8 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/side_1/wheel_9/Summary_ClusterStoNCorr__OnTrack__TEC__side__1__wheel__9",
     'description': "Corrected S/N ratio for TECB Wheel #9 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])

