def sistriplayout(i, p, *rows): i["SiStrip/Layouts/" + p] = DQMItem(layout=rows)

sistriplayout(dqmitems, "GlobalTracks",
  [{ 'path': "SiStrip/Tracks/NumberOfTracks_CosmicTk",
     'description': ' Number of Reconstructed Tracks by Cosmic Track Finder'},
   { 'path': "SiStrip/Tracks/NumberOfRecHitsPerTrack_CosmicTk",
     'description': ' Number of RecHits per Track by Cosmic Track Finder'}],
  [{ 'path': "SiStrip/Tracks/TrackPhi_CosmicTk",
     'description': ' Phi distribution of Reconstructed Tracks by Cosmic Track Finder'},
   { 'path': "SiStrip/Tracks/TrackEta_CosmicTk",
     'description': ' Eta distribution of Reconstructed Tracks by Cosmic Track Finder'}])
sistriplayout(dqmitems, "OnTrackCluster",
  [{ 'path': "SiStrip/MechanicalView/TOB/Summary_cStoN_OnTrack_in_TOB",
     'description': 'Signal-to-Noise from On-Track clusters in TIB'},
   { 'path': "SiStrip/MechanicalView/TIB/Summary_cStoN_OnTrack_in_TIB",
     'description': 'Signal-to-Noise from On-Track clusters in TOB'}],
  [{ 'path':"SiStrip/MechanicalView/TEC/Summary_cStoN_OnTrack_in_TEC",
     'description': 'Signal-to-Noise from On-Track clusters in TEC'},
   { 'path': "SiStrip/MechanicalView/TID/Summary_cStoN_OnTrack_in_TID",
     'description': 'Signal-to-Noise from On-Track clusters in TID'}])
sistriplayout(dqmitems, "OffTrackCluster",
  [{ 'path': "SiStrip/MechanicalView/TOB/Summary_cStoN_OffTrack_in_TOB",
     'description': 'Signal-to-Noise from Off-Track clusters in TIB'},
   { 'path': "SiStrip/MechanicalView/TIB/Summary_cStoN_OffTrack_in_TIB",
     'description': 'Signal-to-Noise from Off-Track clusters in TOB'}],
  [{ 'path':"SiStrip/MechanicalView/TEC/Summary_cStoN_OffTrack_in_TEC",
     'description': 'Signal-to-Noise from Off-Track clusters in TEC'},
   { 'path': "SiStrip/MechanicalView/TID/Summary_cStoN_OffTrack_in_TID",
     'description': 'Signal-to-Noise from Off-Track clusters in TID'}])
sistriplayout(dqmitems, "TOBSummary",
  ["SiStrip/MechanicalView/TOB/Summary_NumberOfDigis_in_TOB",
   "SiStrip/MechanicalView/TOB/Summary_NumberOfClusters_in_TOB"],
  ["SiStrip/MechanicalView/TOB/Summary_ClusterWidth_in_TOB"])
sistriplayout(dqmitems, "TIBSummary",
  ["SiStrip/MechanicalView/TIB/Summary_NumberOfDigis_in_TIB"],
  ["SiStrip/MechanicalView/TIB/Summary_NumberOfClusters_in_TIB"],
  ["SiStrip/MechanicalView/TIB/Summary_ClusterWidth_in_TIB"])
sistriplayout(dqmitems, "TECFSummary",
  ["SiStrip/MechanicalView/TEC/side_2/Summary_NumberOfDigis_in_side_2"],
  ["SiStrip/MechanicalView/TEC/side_2/Summary_NumberOfClusters_in_side_2"],
  ["SiStrip/MechanicalView/TEC/side_2/Summary_ClusterWidth_in_side_2"])
sistriplayout(dqmitems, "TECBSummary",
  ["SiStrip/MechanicalView/TEC/side_1/Summary_NumberOfDigis_in_side_1"],
  ["SiStrip/MechanicalView/TEC/side_1/Summary_NumberOfClusters_in_side_1"],
  ["SiStrip/MechanicalView/TEC/side_1/Summary_ClusterWidth_in_side_1"])
sistriplayout(dqmitems, "TIDFSummary",
  ["SiStrip/MechanicalView/TID/side_2/Summary_NumberOfDigis_in_side_2"],
  ["SiStrip/MechanicalView/TID/side_2/Summary_NumberOfClusters_in_side_2"],
  ["SiStrip/MechanicalView/TID/side_2/Summary_ClusterWidth_in_side_2"])
sistriplayout(dqmitems, "TIDBSummary",
  ["SiStrip/MechanicalView/TID/side_1/Summary_NumberOfDigis_in_side_1"],
  ["SiStrip/MechanicalView/TID/side_1/Summary_NumberOfClusters_in_side_1"],
  ["SiStrip/MechanicalView/TID/side_1/Summary_ClusterWidth_in_side_1"])
