def sistriplayout(i, p, *rows): i["Layouts/SiStrip Layouts/" + p] = DQMItem(layout=rows)

sistriplayout(dqmitems, "GlobalTracks",
  ["SiStrip/Tracks/NumberOfTracks_CosmicTk"],
  ["SiStrip/Tracks/NumberOfRecHitsPerTrack_CosmicTk"],
  ["SiStrip/Tracks/TrackPhi_CosmicTk"],
  ["SiStrip/Tracks/TrackEta_CosmicTk"])
sistriplayout(dqmitems, "OnTrackCluster",
  ["SiStrip/MechanicalView/TOB/Summary_cStoNCorr_OnTrack_in_TOB"],
  ["SiStrip/MechanicalView/TIB/Summary_cStoNCorr_OnTrack_in_TIB"],
  ["SiStrip/MechanicalView/TEC/Summary_cStoNCorr_OnTrack_in_TEC"],
  ["SiStrip/MechanicalView/TID/Summary_cStoNCorr_OnTrack_in_TID"])
sistriplayout(dqmitems, "OffTrackCluster",
  ["SiStrip/MechanicalView/TOB/Summary_cStoNCorr_OffTrack_in_TOB"],
  ["SiStrip/MechanicalView/TIB/Summary_cStoNCorr_OffTrack_in_TIB"],
  ["SiStrip/MechanicalView/TEC/Summary_cStoNCorr_OffTrack_in_TEC"],
  ["SiStrip/MechanicalView/TID/Summary_cStoNCorr_OffTrack_in_TID"])
sistriplayout(dqmitems, "TOBSummary",
  ["SiStrip/MechanicalView/TOB/Summary_NumberOfDigis_in_TOB"],
  ["SiStrip/MechanicalView/TOB/Summary_NumberOfClusters_in_TOB"],
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
