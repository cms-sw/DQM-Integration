def shiftEcalBarrelLayout(i, p, *rows): i["Shift/EcalBarrel/" + p] = DQMItem(layout=rows)

shiftEcalBarrelLayout(dqmitems, "01-Integrity",
  ["EcalBarrel/EBSummaryClient/EBIT integrity quality summary"])

shiftEcalBarrelLayout(dqmitems, "02-PedestalOnline",
  ["EcalBarrel/EBSummaryClient/EBPOT pedestal quality summary G12"])

shiftEcalBarrelLayout(dqmitems, "03-DCCOccupancy",
  ["EcalBarrel/EcalInfo/EBMM DCC"])

shiftEcalBarrelLayout(dqmitems, "04-DigiOccupancy",
  ["EcalBarrel/EBOccupancyTask/EBOT digi occupancy"],
  ["EcalBarrel/EBOccupancyTask/EBOT digi occupancy projection eta",
   "EcalBarrel/EBOccupancyTask/EBOT digi occupancy projection phi"])

shiftEcalBarrelLayout(dqmitems, "05-RecHitOccupancy",
  ["EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy"],
  ["EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy projection eta",
   "EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy projection phi"])

shiftEcalBarrelLayout(dqmitems, "06-TPGDigisOccupancy",
  ["EcalBarrel/EBOccupancyTask/EBOT TP digi occupancy"],
  ["EcalBarrel/EBOccupancyTask/EBOT TP digi occupancy projection eta",
   "EcalBarrel/EBOccupancyTask/EBOT TP digi occupancy projection phi"])

shiftEcalBarrelLayout(dqmitems, "07-RecHitAndTPGProfiles",
  ["EcalBarrel/EcalInfo/EBMM hit number profile"],
  ["EcalBarrel/EcalInfo/EBMM TP digi number profile"])

shiftEcalBarrelLayout(dqmitems, "08-Cosmics",
  ["EcalBarrel/EBCosmicTask/Sel/EBCT energy sel EB-01"])

shiftEcalBarrelLayout(dqmitems, "09-Timing",
  ["EcalBarrel/EBSummaryClient/EBTMT timing quality summary"])

shiftEcalBarrelLayout(dqmitems, "10-ClustersEnergy",
  ["EcalBarrel/EBClusterTask/EBCLT BC energy map"],
  ["EcalBarrel/EBClusterTask/EBCLT BC energy projection eta",
   "EcalBarrel/EBClusterTask/EBCLT BC energy projection phi"])

shiftEcalBarrelLayout(dqmitems, "11-ClustersOccupancy",
  ["EcalBarrel/EBClusterTask/EBCLT BC number map"],
  ["EcalBarrel/EBClusterTask/EBCLT BC size map"])

shiftEcalBarrelLayout(dqmitems, "12-Laser",
  ["EcalBarrel/EBSummaryClient/EBLT laser quality summary L1"])
