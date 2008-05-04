def sistriplayout(i, p, *rows): i["Layouts/SiStrip Layouts/" + p] = DQMItem(layout=rows)
sistriplayout(dqmitems, "GlobalTracks",
  ["SiStrip/Tracks/NumberOfTracks_CosmicTk"],
  ["SiStrip/Tracks/NumberOfRecHitsPerTrack_CosmicTk"],
  ["SiStrip/Tracks/TrackPhi_CosmicTk"],
  ["SiStrip/Tracks/TrackEta_CosmicTk"])
sistriplayout(dqmitems, "SiStrip_NumberOfDigis_Summary",
  ["SiStrip/MechanicalView/TIB/Summary_NumberOfDigis_in_TIB"],
  ["SiStrip/MechanicalView/TOB/Summary_NumberOfDigis_in_TOB"],
  ["SiStrip/MechanicalView/TID/Summary_NumberOfDigis_in_TID"],
  ["SiStrip/MechanicalView/TEC/Summary_NumberOfDigis_in_TEC"])
sistriplayout(dqmitems, "SiStrip_cStoNCorr_OnTrack_Summary",
  ["SiStrip/MechanicalView/TIB/Summary_cStoNCorr_OnTrack_in_TIB"],
  ["SiStrip/MechanicalView/TOB/Summary_cStoNCorr_OnTrack_in_TOB"],
  ["SiStrip/MechanicalView/TID/Summary_cStoNCorr_OnTrack_in_TID"],
  ["SiStrip/MechanicalView/TEC/Summary_cStoNCorr_OnTrack_in_TEC"])



