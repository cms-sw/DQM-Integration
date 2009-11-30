def tklayout(i, p, *rows): i["Overview/TrackingFeedBack/" + p] = DQMItem(layout=rows)

tklayout(dqmitems, "00 - Track Parameters",
 [{ 'path': "Tracking/TrackParameters/NumberOfTracks_GenTk",
    'description': "Number of Reconstructed Tracks  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOnlineDQMInstructions>SiStripOnlineDQMInstructions</a> "},
  { 'path': "Tracking/TrackParameters/TrackPt_ImpactPoint_GenTk",
    'description': "Pt of Reconstructed Track  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOnlineDQMInstructions>SiStripOnlineDQMInstructions</a> "},
  { 'path': "Tracking/TrackParameters/TrackPhi_ImpactPoint_GenTk",
    'description': "Phi distribution of Reconstructed Tracks  -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOnlineDQMInstructions>SiStripOnlineDQMInstructions</a> "},
  { 'path': "Tracking/TrackParameters/TrackEta_ImpactPoint_GenTk",
    'description': " Eta distribution of Reconstructed Tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOnlineDQMInstructions>SiStripOnlineDQMInstructions</a> "}]
    ,[{ 'path': "Tracking/TrackParameters/xPointOfClosestApproach_GenTk",
    'description': "x coordinate of closest point wrt the beam "},
  { 'path': "Tracking/TrackParameters/yPointOfClosestApproach_GenTk",
    'description': "y coordinate of closest point wrt the beam "},
  { 'path': "Tracking/TrackParameters/zPointOfClosestApproach_GenTk",
    'description': "z coordinate of closest point wrt the beam "}])
