def shiftcastorlayout(i, p, *rows): i["00 Shift/Castor/" + p] = DQMItem(layout=rows)


# Report Summary Map
shiftcastorlayout(dqmitems, "Castor Report Summary",
                [{'path':"Castor/EventInfo/reportSummaryMap",
                  'description':  ""}]
                )
             
shiftcastorlayout(dqmitems, "CASTOR RecHit Energies",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHit Energies - 1GeV cut on RecHitEnergy",
             'description':"Energy of all Castor RecHits"}]
           )          
	  
shiftcastorlayout(dqmitems, "CASTOR RecHit Energy in modules",
           [{ 'path': "Castor/CastorRecHitsValid/CastorRecHits Energy in modules - 1GeV cut on RecHitEnergy",
             'description':""}]
           )          
	 
shiftcastorlayout(dqmitems, "CASTOR RecHit Energy in sectors",
           [{ 'path': "Castor/CastorRecHitsValid/CastorRecHits Energy in sectors - 1GeV cut on RecHitEnergy",
             'description':""}]
           )          
	  
	  
shiftcastorlayout(dqmitems, "CASTOR RecHit Occupancy",
           [{ 'path': "Castor/CastorRecHitsValid/CastorRecHits occupancy - sector vs module",
             'description':""}]
           )         
	  
	  	  
shiftcastorlayout(dqmitems, "CASTOR All Pedestal Values",
           [{ 'path': "Castor/CastorPedestalMonitor/Castor All Pedestal Values",
             'description':""}]
           )         
	   
	   
	  	  
shiftcastorlayout(dqmitems, "CASTOR Average Pulse Time",
           [{ 'path': "Castor/CastorLEDMonitor/Castor Average Pulse Time",
             'description':""}]
           )         
	  
	  
	   	  	  
shiftcastorlayout(dqmitems, "CASTOR Average Pulse Energy",
           [{ 'path': "Castor/CastorLEDMonitor/Castor Average Pulse Energy",
             'description':""}]
           )         
	   
