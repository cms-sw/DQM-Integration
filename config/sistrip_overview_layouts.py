def tklayout(i, p, *rows): i["Collisions/TrackingFeedBack/" + p] = DQMItem(layout=rows)

tklayout(dqmitems, "00 - Number Of Tracks",
 [{ 'path': "Tracking/TrackParameters/NumberOfTracks_GenTk",
    'description': "Number of Reconstructed Tracks  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOnlineDQMInstructions>SiStripOnlineDQMInstructions</a> "}])
tklayout(dqmitems, "01 - Track Pt",
 [{ 'path': "Tracking/TrackParameters/TrackPt_ImpactPoint_GenTk",
    'description': "Pt of Reconstructed Track  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOnlineDQMInstructions>SiStripOnlineDQMInstructions</a> "}])
tklayout(dqmitems, "02 - Track Phi",
 [{ 'path': "Tracking/TrackParameters/TrackPhi_ImpactPoint_GenTk",
    'description': "Phi distribution of Reconstructed Tracks  -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOnlineDQMInstructions>SiStripOnlineDQMInstructions</a> "}])
tklayout(dqmitems, "03 - Track Eta",
 [{ 'path': "Tracking/TrackParameters/TrackEta_ImpactPoint_GenTk",
    'description': " Eta distribution of Reconstructed Tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOnlineDQMInstructions>SiStripOnlineDQMInstructions</a> "}])
tklayout(dqmitems, "04 - X-Position Of Closest Approach",
 [{ 'path': "Tracking/TrackParameters/xPointOfClosestApproach_GenTk",
    'description': "x coordinate of closest point wrt the beam "}])
tklayout(dqmitems, "05 - Y-Position Of Closest Approach",
 [{ 'path': "Tracking/TrackParameters/yPointOfClosestApproach_GenTk",
    'description': "y coordinate of closest point wrt the beam "}])
tklayout(dqmitems, "06 - Z-Position Of Closest Approach",
 [{ 'path': "Tracking/TrackParameters/zPointOfClosestApproach_GenTk",
    'description': "z coordinate of closest point wrt the beam "}])    
tklayout(dqmitems, "07 - Cluster y width vs. cluster eta",
 [{ 'path': "Pixel/Barrel/sizeYvsEta_siPixelClusters_Barrel",
    'description': "Cluster y width as function of cluster eta",
    'draw': { 'withref': "no" }}])


