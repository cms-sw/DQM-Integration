def bmoverviewlayout(i, p, *rows): i["Collisions/BeamMonitorFeedBack/" + p] = DQMItem(layout=rows)

bmoverviewlayout(dqmitems, "00 - d0-phi0 of selected tracks",
                 [{ 'path': "BeamMonitor/Fit/d0_phi0",
                    'description': "d0-phi0 correlation of selected tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/BeamMonitorOnlineDQMInstructions>BeamMonitorOnlineDQMInstructions</a> "}])
bmoverviewlayout(dqmitems, "01 - z0 of selected tracks",
                 [{ 'path': "BeamMonitor/Fit/trk_z0",
                    'description': "Z0 distribution of selected tracks  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/BeamMonitorOnlineDQMInstructions>BeamMonitorOnlineDQMInstructions</a> "}])
bmoverviewlayout(dqmitems, "02 - x position of beam spot",
                 [{ 'path': "BeamMonitor/Fit/x0",
                    'description': "x coordinate of fitted beam spot"}])
bmoverviewlayout(dqmitems, "03 - y position of beam spot",
                 [{ 'path': "BeamMonitor/Fit/y0",
                    'description': "y coordinate of fitted beam spot"}])
bmoverviewlayout(dqmitems, "04 - z position of beam spot",
                 [{ 'path': "BeamMonitor/Fit/z0",
                    'description': "z coordinate of fitted beam spot"}])
bmoverviewlayout(dqmitems, "05 - sigma z of beam spot",
                 [{ 'path': "BeamMonitor/Fit/sigmaZ0",
                    'description': "sigma z of fitted beam spot"}])
bmoverviewlayout(dqmitems, "06 - fit results beam spot",
                 [{ 'path': "BeamMonitor/Fit/fitResults",
                    'description': "d_{0}-#phi correlation fit results of beam spot"}])
bmoverviewlayout(dqmitems, "07 - fit results primary vertex",
                 [{ 'path': "BeamMonitor/PrimaryVertex/pvResults",
                    'description': "Gaussian fit results of primary vertex"}])
