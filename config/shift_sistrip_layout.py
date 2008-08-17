def sistriplayout(i, p, *rows): i["00 Shift/SiStrip/" + p] = DQMItem(layout=rows)

sistriplayout(dqmitems, "00 RawDataMonitoringSummary",
  [{ 'path': "SiStrip/ReadoutView/FedMonitoringSummary/FedCorruptBuffer",
     'description': '# of Corrupted Buffers vs FED ID'}],
  [{ 'path': "SiStrip/ReadoutView/FedMonitoringSummary/FedGenericErrors",
     'description': 'Total numbers of errors vs FED ID'}])
sistriplayout(dqmitems, "01 Tracks",
  [{ 'path': "SiStrip/Tracks/NumberOfTracks_CKFTk",
     'description': ' Number of Reconstructed Tracks by CKF'}],
  [{ 'path': "SiStrip/Tracks/NumberOfRecHitsPerTrack_CKFTk",
     'description': ' Number of RecHits per Track by CKF'}])
sistriplayout(dqmitems, "02 OnTrackCluster",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_ClusterStoNCorr_OnTrack_in_TIB",
     'description': 'Signal-to-Noise (corrected for the angle) for On-Track clusters in TIB'},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_ClusterStoNCorr_OnTrack_in_TOB",
     'description': 'Signal-to-Noise (corrected for the angle) for On-Track clusters in TOB'}],
  [{ 'path': "SiStrip/MechanicalView/TID/Summary_ClusterStoNCorr_OnTrack_in_TID",
     'description': 'Signal-to-Noise (corrected for the angle) for On-Track clusters in TID'},
   { 'path': "SiStrip/MechanicalView/TEC/Summary_ClusterStoNCorr_OnTrack_in_TEC",
     'description': 'Signal-to-Noise (corrected for the angle) for On-Track clusters in TEC'}])

