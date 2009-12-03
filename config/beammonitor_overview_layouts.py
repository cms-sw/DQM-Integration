def bmoverviewlayout(i, p, *rows): i["Collisions/BeamMonitorFeedBack/" + p] = DQMItem(layout=rows)

bmoverviewlayout(dqmitems, "00 - BeamMonitor Results",
                 [{ 'path': "BeamMonitor/Fit/d0_phi0",
                    'description': "d0-phi0 correlation of selected tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/BeamMonitorOnlineDQMInstructions>BeamMonitorOnlineDQMInstructions</a> "},
                  { 'path': "BeamMonitor/Fit/trk_z0",
                    'description': "Z0 distribution of selected tracks  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/BeamMonitorOnlineDQMInstructions>BeamMonitorOnlineDQMInstructions</a> "}],
                 [{ 'path': "BeamMonitor/Fit/x0",
                    'description': "x coordinate of fitted beam spot"},
                  { 'path': "BeamMonitor/Fit/y0",
                    'description': "y coordinate of fitted beam spot"}],
                 [{ 'path': "BeamMonitor/Fit/z0",
                    'description': "z coordinate of fitted beam spot"},
                  { 'path': "BeamMonitor/Fit/sigmaZ0",
                    'description': "sigma z of fitted beam spot"}]
                 )
