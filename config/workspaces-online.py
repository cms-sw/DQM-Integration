server.workspace('Summary', 'DQMSummary')
server.workspace('Everything', 'DQMContent', '^')
server.workspace('CSC', 'DQMContent', '^CSC/',
                 'CSC/Layouts/00 Top Physics Efficiency',
                 'CSC/Layouts/01 Station Physics Efficiency',
		 'CSC/Layouts/02 EMU Summary/EMU Test01 - DDUs in Readout',
		 'CSC/Layouts/02 EMU Summary/EMU Test03 - DDU Reported Errors',
		 'CSC/Layouts/02 EMU Summary/EMU Test04 - DDU Format Errors',
		 'CSC/Layouts/02 EMU Summary/EMU Test05 - DDU Inputs Status',
		 'CSC/Layouts/02 EMU Summary/EMU Test06 - DDU Inputs in ERROR-WARNING State',
		 'CSC/Layouts/02 EMU Summary/EMU Test08 - CSCs Reporting Data and Unpacked',
		 'CSC/Layouts/02 EMU Summary/EMU Test10 - CSCs with Errors and Warnings (Fractions)',
		 'CSC/Layouts/02 EMU Summary/EMU Test11 - CSCs without Data Blocks')

server.workspace('DT', 'DQMContent', '^DT/',
                 'DT/Layouts/00-Summary/00-DataIntegritySummary',
                 'DT/Layouts/00-Summary/01-OccupancySummary',
                 'DT/Layouts/00-Summary/02-SegmentSummary',
                 'DT/Layouts/00-Summary/03-DDU_TriggerCorrFactionSummary',
                 'DT/Layouts/00-Summary/04-DDU_Trigger2ndFactionSummary',
                 'DT/Layouts/00-Summary/05-DCC_TriggerCorrFactionSummary',
                 'DT/Layouts/00-Summary/06-DCC_Trigger2ndFactionSummary')

#server.workspace('ECAL', 'DQMContent', '^Ecal',
#                 'Ecal/Layouts/00-Global-Summary')

server.workspace('EB', 'DQMContent', '^EcalBarrel/',
                 'EcalBarrel/Layouts/00-Summary/00-Global-Summary',
                 'EcalBarrel/Layouts/00-Summary/01-Integrity-Summary',
                 'EcalBarrel/Layouts/00-Summary/02-Occupancy-Summary',
                 'EcalBarrel/Layouts/00-Summary/03-Cosmic-Summary',
                 'EcalBarrel/Layouts/00-Summary/04-PedestalOnline-Summary',
#                 'EcalBarrel/Layouts/00-Summary/05-LaserL1-Summary',
                 'EcalBarrel/Layouts/00-Summary/07-Timing-Summary',
                 'EcalBarrel/Layouts/00-Summary/08-Trigger-Summary',
                 'EcalBarrel/Layouts/00-Summary/09-Trigger-Summary')

#server.workspace('EE', 'DQMContent', '^EcalEndcap/',
#                 'EcalEndcap/Layouts/00-Summary/00-Global-Summary',
#                 'EcalEndcap/Layouts/00-Summary/01-Integrity-Summary',
#                 'EcalEndcap/Layouts/00-Summary/02-Occupancy-Summary',
#                 'EcalEndcap/Layouts/00-Summary/03-Cosmic-Summary',
#                 'EcalEndcap/Layouts/00-Summary/04-PedestalOnline-Summary',
#                 'EcalEndcap/Layouts/00-Summary/05-LaserL1-Summary',
#                 'EcalEndcap/Layouts/00-Summary/06-Led-Summary',
#                 'EcalEndcap/Layouts/00-Summary/07-Timing-Summary',
#                 'EcalEndcap/Layouts/00-Summary/08-Trigger-Summary',
#                 'EcalEndcap/Layouts/00-Summary/09-Trigger-Summary')

server.workspace('HCAL', 'DQMContent', '^Hcal',
                 'Hcal/Layouts/HCAL Pedestals',
                 'Hcal/Layouts/HCAL Unsuppressed Channels',
                 'Hcal/Layouts/HCAL Dead Cell Check',
                 'Hcal/Layouts/HCAL Hot Cell Check',
                 'Hcal/Layouts/HCAL Data Integrity Problems',
                 'Hcal/Layouts/HCAL Trigger Primitives')

server.workspace('L1T', 'DQMContent', '^L1T',
                 'L1T/L1TGT/algo_bits',
                 'L1T/L1TGT/event_lumi',
                 'L1T/L1TGT/evnum_trignum_lumi',
                 'L1T/L1TGMT/Regional_trigger',
                 'L1T/L1TGMT/GMT_candlumi',
                 'L1T/L1TGMT/GMT_phi',
                 'L1T/L1TGMT/GMT_etaphi',
                 'L1T/L1TGCT/IsoEmOccEtaPhi',
                 'L1T/L1TGCT/NonIsoEmOccEtaPhi',
                 'L1T/L1TRCT/RctIsoEmOccEtaPhi',
                 'L1T/L1TRCT/RctNonIsoEmOccEtaPhi',
                 'L1T/L1TRCT/RctRegionsLocalOccEtaPhi',
                 'L1T/L1TRCT/RctRegionsOccEtaPhi',
		 'L1T/L1TCSCTF/CSCTF_occupancies',
		 'L1T/L1TRPCTF/Client/RPCTF_phi_valuepacked_bad',
		 'L1T/L1TRPCTF/Client/RPCTF_phi_valuepacked_dead',
		 'L1T/L1TRPCTF/Client/RPCTF_deadchannels',
		 'L1T/L1TRPCTF/Client/RPCTF_noisychannels')

server.workspace('Pixel', 'DQMContent', '^Pixel/',
                 'Pixel/Layouts/Pixel_RawData_Toplevel_Summary',
                 'Pixel/Layouts/Pixel_Digi_Toplevel_Summary',
                 'Pixel/Layouts/Pixel_PIB_Summary')

server.workspace('RPC', 'DQMContent', '^RPC/',
		 'RPC/Layouts/RPC_Summary',
                 'RPC/Layouts/Wheel_1D_Occupancy',
                 'RPC/Layouts/Barrel_Occupancy')      

server.workspace('SiStrip', 'DQMContent', '^SiStrip/',
                 'SiStrip/Layouts/GlobalTracks',
                 'SiStrip/Layouts/OnTrackCluster',
                 'SiStrip/Layouts/OffTrackCluster',
                 'SiStrip/Layouts/TIBSummary',
                 'SiStrip/Layouts/TOBSummary',
                 'SiStrip/Layouts/TECFSummary',
                 'SiStrip/Layouts/TECBSummary',
                 'SiStrip/Layouts/TIDFSummary',
                 'SiStrip/Layouts/TIDBSummary')
