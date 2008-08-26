server.workspace('DQMQuality', 0, 'Summaries', 'Summary')
server.workspace('DQMSummary', 1, 'Summaries', 'Reports')
server.workspace('DQMShift',   2, 'Summaries', 'Shift')

server.workspace('DQMContent', 10, 'Tracker', 'Pixel', '^Pixel/',
                 'Pixel/Layouts/Pixel_RawData_Toplevel_Summary',
                 'Pixel/Layouts/Pixel_Digi_Toplevel_Summary',
                 'Pixel/Layouts/Pixel_PIB_Summary')

server.workspace('DQMContent', 10, 'Tracker', 'SiStrip', '^SiStrip/',
                 'SiStrip/Layouts/00 - Tracks',
                 'SiStrip/Layouts/01 - OnTrackCluster',
                 'SiStrip/Layouts/02 - OffTrackCluster',
                 'SiStrip/Layouts/03 - TIBSummary',
                 'SiStrip/Layouts/06 - TOBSummary',
                 'SiStrip/Layouts/07 - TECFSummary',
                 'SiStrip/Layouts/08 - TECBSummary',
                 'SiStrip/Layouts/04 - TIDFSummary',
                 'SiStrip/Layouts/05 - TIDBSummary',
                 'SiStrip/Layouts/09 - FedMonitoringSummary')

#server.workspace('DQMContent', 20, 'Calorimeter', 'ECAL', '^Ecal',
#                 'Ecal/Layouts/00-Global-Summary',
#                 'Ecal/Layouts/01-Occupancy-Summary',
#                 'Ecal/Layouts/02-Cluster-Summary')

server.workspace('DQMContent', 20, 'Calorimeter', 'EcalBarrel', '^EcalBarrel/',
                 'EcalBarrel/Layouts/00-Summary/00-Global-Summary',
                 'EcalBarrel/Layouts/00-Summary/01-Integrity-Summary',
                 'EcalBarrel/Layouts/00-Summary/02-Occupancy-Summary',
                 'EcalBarrel/Layouts/00-Summary/03-Cosmic-Summary',
                 'EcalBarrel/Layouts/00-Summary/04-PedestalOnline-Summary',
                 'EcalBarrel/Layouts/00-Summary/05-Timing-Summary',
                 'EcalBarrel/Layouts/00-Summary/06-Trigger-Summary',
                 'EcalBarrel/Layouts/00-Summary/07-Trigger-Summary',
                 'EcalBarrel/Layouts/00-Summary/08-StatusFlags-Summary')

server.workspace('DQMContent', 20, 'Calorimeter', 'EcalEndcap', '^EcalEndcap/',
                 'EcalEndcap/Layouts/00-Summary/00-Global-Summary',
                 'EcalEndcap/Layouts/00-Summary/01-Integrity-Summary',
                 'EcalEndcap/Layouts/00-Summary/02-Occupancy-Summary',
                 'EcalEndcap/Layouts/00-Summary/03-Cosmic-Summary',
                 'EcalEndcap/Layouts/00-Summary/04-PedestalOnline-Summary',
                 'EcalEndcap/Layouts/00-Summary/05-Timing-Summary',
                 'EcalEndcap/Layouts/00-Summary/06-Trigger-Summary',
                 'EcalEndcap/Layouts/00-Summary/07-Trigger-Summary',
                 'EcalEndcap/Layouts/00-Summary/08-StatusFlags-Summary')

server.workspace('DQMContent', 20, 'Calorimeter', 'HCAL', '^Hcal/',
                 'Hcal/Layouts/HCAL Pedestals',
                 'Hcal/Layouts/HCAL Unsuppressed Channels',
                 'Hcal/Layouts/HCAL Dead Cell Check',
                 'Hcal/Layouts/HCAL Hot Cell Check',
                 'Hcal/Layouts/HCAL Data Integrity Problems',
                 'Hcal/Layouts/HCAL Trigger Primitives')

server.workspace('DQMContent', 30, 'Muon', 'CSC', '^CSC/',
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

server.workspace('DQMContent', 30, 'Muon', 'DT', '^DT/',
                 'DT/Layouts/00-Summary/00-DataIntegritySummary',
                 'DT/Layouts/00-Summary/01-OccupancySummary',
                 'DT/Layouts/00-Summary/02-SegmentSummary',
                 'DT/Layouts/00-Summary/03-DDU_TriggerCorrFactionSummary',
                 'DT/Layouts/00-Summary/04-DDU_Trigger2ndFactionSummary',
                 'DT/Layouts/00-Summary/05-DCC_TriggerCorrFactionSummary',
                 'DT/Layouts/00-Summary/06-DCC_Trigger2ndFactionSummary',
                 'DT/Layouts/00-Summary/07-NoiseChannelsSummary')

server.workspace('DQMContent', 30, 'Muon', 'RPC', '^RPC/',
		 '00 Shift/RPC/00-BarrelOccupancy')

server.workspace('DQMContent', 40, 'Trigger/DAQ', 'L1T', '^L1T/',
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

server.workspace('DQMContent', 40, 'Trigger/DAQ', 'L1TEMU', '^L1TEMU/')
server.workspace('DQMContent', 41, 'Trigger/DAQ', 'HLT', '^HLT/')

server.workspace('DQMContent', 90, 'Other', 'Everything', '^')
server.workspace('EVDSnapshot', 99, 'Other', 'Event display', '/home/dqm/iguana-snapshots')
