server.workspace('Summary', 'DQMSummary')
server.workspace('Everything', 'DQMContent', '^')
server.workspace('CSC', 'DQMContent', '^CSC/',
		 'CSC/Layouts/EMU00 Summary/EMU Test01 - DDUs in Readout',
		 'CSC/Layouts/EMU00 Summary/EMU Test03 - DDU Reported Errors',
		 'CSC/Layouts/EMU00 Summary/EMU Test04 - DDU Format Errors',
		 'CSC/Layouts/EMU00 Summary/EMU Test05 - DDU Inputs Status',
		 'CSC/Layouts/EMU00 Summary/EMU Test06 - DDU Inputs in ERROR-WARNING State',
		 'CSC/Layouts/EMU00 Summary/EMU Test08 - CSCs Reporting Data and Unpacked',
		 'CSC/Layouts/EMU00 Summary/EMU Test10 - CSCs with Errors and Warnings (Fractions)',
		 'CSC/Layouts/EMU00 Summary/EMU Test11 - CSCs without Data Blocks')

server.workspace('DT', 'DQMContent', '^DT/',
                 'DT/DataIntegrity/FED770/FED770_ROSSummary',
                 'DT/DataIntegrity/FED771/FED771_ROSSummary',
                 'DT/DataIntegrity/FED772/FED772_ROSSummary',
                 'DT/DataIntegrity/FED773/FED773_ROSSummary',
                 'DT/DataIntegrity/FED774/FED774_ROSSummary')

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
                 'Hcal/Layouts/HCAL Barrel Summary',
                 'Hcal/Layouts/HCAL Endcap Summary',
                 'Hcal/Layouts/HCAL Forward Summary',
                 'Hcal/Layouts/HCAL Outer Summary')

server.workspace('L1T', 'DQMContent', '^L1T',
                 'L1T/Layouts/GT-Summary/algo_bits',
                 'L1T/Layouts/GMT-Summary/GMT_etaphi',
                 'L1T/Layouts/GMT-Summary/etaphi_DTCSC_and_RPC',
                 'L1T/Layouts/GMT-Summary/Regional_trigger',
                 'L1T/Layouts/GCT-Summary/IsoEmRankEtaPhiSumm',
                 'L1T/Layouts/GCT-Summary/NonIsoEmRankEtaPhiSumm',
                 'L1T/Layouts/GCT-Summary/IsoEmRank',
                 'L1T/Layouts/GCT-Summary/NonIsoEmRank',
                 'L1T/Layouts/RCT-Summary/RctIsoEmOccEtaPhi',
                 'L1T/Layouts/RCT-Summary/RctNonIsoEmOccEtaPhi',
                 'L1T/Layouts/CSCTF-Summary/CSCTF_occupancies',
                 'L1T/Layouts/DTTF-Summary/DT_TPG_phi_map',
                 'L1T/Layouts/RPCTF-Summary/RPCTF_muons_eta_phipacked')

server.workspace('RPC', 'DQMContent', '^RPC/')
server.workspace('SiStrip', 'DQMContent', '^SiStrip/',
                 'SiStrip/Layouts/SiStrip_Digi_Summary')
