def castorlayout(i, p, *rows): i["Castor/Layouts/" + p] = DQMItem(layout=rows)

              
castorlayout(dqmitems, "CASTOR RecHit Energies",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHit Energies",
             'description':"Energy of all Castor RecHits"}]
           )          
	  
castorlayout(dqmitems, "CASTOR RecHit Energy in modules",
           [{ 'path': "Castor/CastorRecHitsValid/CastorRecHits Energy in modules",
             'description':""}]
           )          
	 
castorlayout(dqmitems, "CASTOR RecHit Energy in sectors",
           [{ 'path': "Castor/CastorRecHitsValid/CastorRecHits Energy in sectors",
             'description':""}]
           )          
	  
	  
castorlayout(dqmitems, "CASTOR RecHit Occupancy",
           [{ 'path': "Castor/CastorRecHitsValid/CastorRecHits occupancy - sector vs module",
             'description':""}]
           )         
	  
	  	  
castorlayout(dqmitems, "CASTOR All Pedestal Values",
           [{ 'path': "Castor/CastorPedestalMonitor/Castor All Pedestal Values",
             'description':""}]
           )         
	   
	   
	  	  
castorlayout(dqmitems, "CASTOR Average Pulse Time",
           [{ 'path': "Castor/CastorLEDMonitor/Castor Average Pulse Time",
             'description':""}]
           )         
	  
	  
	   	  	  
castorlayout(dqmitems, "CASTOR Average Pulse Energy",
           [{ 'path': "Castor/CastorLEDMonitor/Castor Average Pulse Energy",
             'description':""}]
           )         
	   
	   	  

