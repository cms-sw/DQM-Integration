server.workspace('Summary', 'DQMSummary')
server.workspace('Everything', 'DQMContent', '^')
server.workspace('CSC', 'DQMContent', '^CSC/',
		 'CSC/Layouts/EMU00 Summary/EMU Test00 - Readout Buffer Errors',
		 'CSC/Layouts/EMU00 Summary/EMU Test01 - DDUs in Readout',
		 'CSC/Layouts/EMU00 Summary/EMU Test02 - DDU Event Size',
		 'CSC/Layouts/EMU00 Summary/EMU Test03 - DDU Reported Errors',
		 'CSC/Layouts/EMU00 Summary/EMU Test04 - DDU Format Errors',
		 'CSC/Layouts/EMU00 Summary/EMU Test05 - DDU Inputs Status',
		 'CSC/Layouts/EMU00 Summary/EMU Test06 - DDU Inputs in ERROR/WARNING State',
		 'CSC/Layouts/EMU00 Summary/EMU Test08 - CSCs Reporting Data and Unpacked',
		 'CSC/Layouts/EMU00 Summary/EMU Test10 - CSCs with Errors and Warnings (Fractions)',
		 'CSC/Layouts/EMU00 Summary/EMU Test11 - CSCs without Data Blocks')

server.workspace('DT', 'DQMContent', '^DT/',
                 'DT/Layouts/DTIntegrityCheck_Summary',
                 'DT/Layouts/W1_St1_Signal',
                 'DT/Layouts/W1_St2_Signal',
                 'DT/Layouts/W1_St3_Signal',
                 'DT/Layouts/W1_St4_Signal',
                 'DT/Layouts/DTLocalTrigger_Station_1',
                 'DT/Layouts/DTLocalTrigger_Station_2',
                 'DT/Layouts/DTLocalTrigger_Station_3',
                 'DT/Layouts/DTLocalTrigger_Station_4',
                 'DT/Layouts/W1_St1_OccupancyPerLayer',
                 'DT/Layouts/W1_St2_OccupancyPerLayer',
                 'DT/Layouts/W1_St3_OccupancyPerLayer',
                 'DT/Layouts/W1_St4_OccupancyPerLayer',
                 'DT/Layouts/DTIntegrityCheck_station1_first',
                 'DT/Layouts/DTIntegrityCheck_station1_second',
                 'DT/Layouts/DTIntegrityCheck_station2_first',
                 'DT/Layouts/DTIntegrityCheck_station2_second',
                 'DT/Layouts/DTIntegrityCheck_station3_first',
                 'DT/Layouts/DTIntegrityCheck_station3_second',
                 'DT/Layouts/DTIntegrityCheck_station4_first',
                 'DT/Layouts/DTIntegrityCheck_station4_second')

server.workspace('ECAL', 'DQMContent', '^Ecal',
                 'Ecal/Layouts/00-Global-Summary')

server.workspace('EB', 'DQMContent', '^EcalBarrel/',
                 'EcalBarrel/Layouts/00-Summary/00-Global-Summary',
                 'EcalBarrel/Layouts/00-Summary/01-Integrity-Summary',
                 'EcalBarrel/Layouts/00-Summary/02-Occupancy-Summary',
                 'EcalBarrel/Layouts/00-Summary/03-Cosmic-Summary',
                 'EcalBarrel/Layouts/00-Summary/04-PedestalOnline-Summary',
                 'EcalBarrel/Layouts/00-Summary/05-LaserL1-Summary',
                 'EcalBarrel/Layouts/00-Summary/07-Timing-Summary',
                 'EcalBarrel/Layouts/00-Summary/08-Trigger-Summary',
                 'EcalBarrel/Layouts/00-Summary/09-Trigger-Summary')

server.workspace('EE', 'DQMContent', '^EcalEndcap/',
                 'EcalEndcap/Layouts/00-Summary/00-Global-Summary',
                 'EcalEndcap/Layouts/00-Summary/01-Integrity-Summary',
                 'EcalEndcap/Layouts/00-Summary/02-Occupancy-Summary',
                 'EcalEndcap/Layouts/00-Summary/03-Cosmic-Summary',
                 'EcalEndcap/Layouts/00-Summary/04-PedestalOnline-Summary',
                 'EcalEndcap/Layouts/00-Summary/05-LaserL1-Summary',
                 'EcalEndcap/Layouts/00-Summary/06-Led-Summary',
                 'EcalEndcap/Layouts/00-Summary/07-Timing-Summary',
                 'EcalEndcap/Layouts/00-Summary/08-Trigger-Summary',
                 'EcalEndcap/Layouts/00-Summary/09-Trigger-Summary')

server.workspace('HCAL', 'DQMContent', '^Hcal',
                 'Hcal/Layouts/HCAL Data Format Summary',
                 'Hcal/Layouts/HCAL Digitization Summary',
                 'Hcal/Layouts/HCAL Reconstruction Summary',
                 'Hcal/Layouts/HCAL Reconstruction Threshold Summary',
                 'Hcal/Layouts/HCAL Hot Cell Summary',
                 'Hcal/Layouts/HCAL Hot Cell NADA Summary',
                 'Hcal/Layouts/HCAL Dead Cell Summary',
                 'Hcal/Layouts/HCAL Barrel Summary',
                 'Hcal/Layouts/HCAL Endcap Summary',
                 'Hcal/Layouts/HCAL Forward Summary',
                 'Hcal/Layouts/HCAL Outer Summary')

server.workspace('L1T', 'DQMContent', '^L1T',
                 'L1T/Layouts/GT Information',
                 'L1T/Layouts/GMT Information',
                 'L1T/Layouts/GCT Information',
                 'L1T/Layouts/CSCTF Information',
                 'L1T/Layouts/DTTF Information')

server.workspace('RPC', 'DQMContent', '^RPC/')
server.workspace('SiStrip', 'DQMContent', '^SiStrip/',
                 'SiStrip/Layouts/SiStrip_Digi_Summary')
