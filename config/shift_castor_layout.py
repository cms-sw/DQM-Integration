def shiftcastorlayout(i, p, *rows): i["00 Shift/Castor/" + p] = DQMItem(layout=rows)



shiftcastorlayout(dqmitems, "CASTOR Channel Status",
           [{ 'path': "Castor/EventInfo/reportSummaryMap - CASTOR Channel Status",
             'description':"1 - OK, 0 - dead, -1 - noisy"}]
           )

shiftcastorlayout(dqmitems, "CASTOR event products",
           [{ 'path': "Castor/EventInfo/CastorEventProduct",
             'description':"check whether CASTOR objects are present in the events"}]
           )
              
shiftcastorlayout(dqmitems, "CASTOR RecHit Energies",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHit Energies- above threshold on RecHitEnergy",
             'description':"Energy of all Castor RecHits"}]
           )          
	  
shiftcastorlayout(dqmitems, "CASTOR RecHit Energy in modules",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHit Energy in modules- above threshold",
             'description':"RecHitEnergy in each of 14 CASTOR modules"}]
           )          
	 
shiftcastorlayout(dqmitems, "CASTOR RecHit Energy in sectors",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHit Energy in sectors- above threshold",
             'description':"RecHitEnergy in each of 16 CASTOR sectors"}]
           )         
	  
shiftcastorlayout(dqmitems, "CASTOR RecHitEnergy 2D Map",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHit 2D Energy Map- above threshold",
             'description':"2D Energy Map"}]
           )
	  	  
shiftcastorlayout(dqmitems, "CASTOR All Digi Values",
           [{ 'path': "Castor/CastorDigiMonitor/Castor All Digi Values",
             'description':""}]
           )         

shiftcastorlayout(dqmitems, "CASTOR average pulse in bunch crossings",
           [{ 'path': "Castor/CastorPSMonitor/CASTOR average pulse in bunch crossings",
             'description':"average pulse in bunch crossings"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=0 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=0 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=1 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=1 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=2 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=2 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=3 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=3 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=4 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=4 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=5 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=5 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=6 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=6 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )   

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=7 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=7 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=8 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=8 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=9 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=9 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=10 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=10 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=11 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=11 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=12 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=12 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=13 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=13 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=14 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=14 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 

shiftcastorlayout(dqmitems, "Castor Pulse Shape for sector=15 (in all 14 modules)",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=15 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           ) 


