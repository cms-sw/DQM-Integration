def sistriplayout(i, p, *rows): i["00 Shift/SiStrip/" + p] = DQMItem(layout=rows)

sistriplayout(dqmitems, "01 Tracks - CKF ",
  [{ 'path': "Tracking/TrackParameters/NumberOfTracks_CKFTk",
     'description': "Number of Reconstructed Tracks by CKF - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> "}],
  [{ 'path': "Tracking/TrackParameters/NumberOfRecHitsPerTrack_CKFTk",
     'description': "Number of RecHits per Track by CKF  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> "}])
sistriplayout(dqmitems, "02 Tracks - CosmicTF ",
  [{ 'path': "Tracking/TrackParameters/NumberOfTracks_CosmicTk",
     'description': "Number of Reconstructed Tracks by Cosmic Track Finder  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> "}],
  [{ 'path': "Tracking/TrackParameters/NumberOfRecHitsPerTrack_CosmicTk",
     'description': "Number of RecHits per Track by Cosmic Track Finder  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> "}])
sistriplayout(dqmitems, "03 Tracks - RS ",
  [{ 'path': "Tracking/TrackParameters/NumberOfTracks_RSTk",
     'description': "Number of Reconstructed Tracks by Road Search  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> "}],
  [{ 'path': "Tracking/TrackParameters/NumberOfRecHitsPerTrack_RSTk",
     'description': "Number of RecHits per Track by Road Search  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> "}])
sistriplayout(dqmitems, "04 OnTrackCluster",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_ClusterStoNCorr_OnTrack_in_TIB",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TIB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_ClusterStoNCorr_OnTrack_in_TOB",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TOB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TID/Summary_ClusterStoNCorr_OnTrack_in_TID",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TID  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> "},
   { 'path': "SiStrip/MechanicalView/TEC/Summary_ClusterStoNCorr_OnTrack_in_TEC",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TEC  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> "}])

