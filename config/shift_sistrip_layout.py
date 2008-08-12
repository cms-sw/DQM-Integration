def sistriplayout(i, p, *rows): i["00 Shift/SiStrip/" + p] = DQMItem(layout=rows)

sistriplayout(dqmitems, "00 Tracks",
  [{ 'path': "SiStrip/Tracks/NumberOfTracks_CKFTk",
     'description': ' Number of Reconstructed Tracks by CKF'},
   { 'path': "SiStrip/Tracks/NumberOfRecHitsPerTrack_CKFTk",
     'description': ' Number of RecHits per Track by CKF'}],
  [{ 'path': "SiStrip/Tracks/TrackPhi_CKFTk",
     'description': ' Phi distribution of Reconstructed Tracks by CKF'},
   { 'path': "SiStrip/Tracks/TrackEta_CKFTk",
     'description': ' Eta distribution of Reconstructed Tracks by CKF'}])
sistriplayout(dqmitems, "01 OnTrackCluster",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_ClusterStoNCorr_OnTrack_in_TIB",
     'description': 'Signal-to-Noise (corrected for the angle) for On-Track clusters in TIB'},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_ClusterStoNCorr_OnTrack_in_TOB",
     'description': 'Signal-to-Noise (corrected for the angle) for On-Track clusters in TOB'}],
  [{ 'path': "SiStrip/MechanicalView/TID/Summary_ClusterStoNCorr_OnTrack_in_TID",
     'description': 'Signal-to-Noise (corrected for the angle) for On-Track clusters in TID'},
   { 'path': "SiStrip/MechanicalView/TEC/Summary_ClusterStoNCorr_OnTrack_in_TEC",
     'description': 'Signal-to-Noise (corrected for the angle) for On-Track clusters in TEC'}])
sistriplayout(dqmitems, "02 OffTrackCluster",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_ClusterCharge_OffTrack_in_TIB",
     'description': 'Charge for Off-Track clusters in TIB'},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_ClusterCharge_OffTrack_in_TOB",
     'description': 'Charge for Off-Track clusters in TOB'}],
  [{ 'path': "SiStrip/MechanicalView/TID/Summary_ClusterCharge_OffTrack_in_TID",
     'description': 'Charge for Off-Track clusters in TID'},
   { 'path': "SiStrip/MechanicalView/TEC/Summary_ClusterCharge_OffTrack_in_TEC",
     'description': 'Charge for Off-Track clusters in TEC'}])

