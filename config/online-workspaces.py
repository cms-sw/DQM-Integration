server.workspace('Summary', 'DQMSummary')
server.workspace('Everything', 'DQMContent', '^')
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
                 'ECAL/Layouts/00-Global-Summary')

server.workspace('EB', 'DQMContent', '^EcalBarrel/',
                 'EcalBarrel/Layouts/00-Summary/0-Global-Summary',
                 'EcalBarrel/Layouts/00-Summary/1-Integrity-Summary',
                 'EcalBarrel/Layouts/00-Summary/2-Occupancy-Summary',
                 'EcalBarrel/Layouts/00-Summary/3-Cosmic-Summary',
                 'EcalBarrel/Layouts/00-Summary/4-PedestalOnline-Summary',
                 'EcalBarrel/Layouts/00-Summary/5-LaserL1-Summary',
                 'EcalBarrel/Layouts/00-Summary/7-Timing-Summary',
                 'EcalBarrel/Layouts/00-Summary/8-Trigger-Summary',
                 'EcalBarrel/Layouts/00-Summary/9-Trigger-Summary')

server.workspace('EE', 'DQMContent', '^EcalEndcap/',
                 'EcalEndcap/Layouts/00-Summary/0-Global-Summary',
                 'EcalEndcap/Layouts/00-Summary/1-Integrity-Summary',
                 'EcalEndcap/Layouts/00-Summary/2-Occupancy-Summary',
                 'EcalEndcap/Layouts/00-Summary/3-Cosmic-Summary',
                 'EcalEndcap/Layouts/00-Summary/4-PedestalOnline-Summary',
                 'EcalEndcap/Layouts/00-Summary/5-LaserL1-Summary',
                 'EcalEndcap/Layouts/00-Summary/6-Led-Summary',
                 'EcalEndcap/Layouts/00-Summary/7-Timing-Summary',
                 'EcalEndcap/Layouts/00-Summary/8-Trigger-Summary',
                 'EcalEndcap/Layouts/00-Summary/9-Trigger-Summary')

server.workspace('L1T', 'DQMContent', '^L1T',
                 'L1TMonitor/Layouts/Summary/GT decision bit correlation',
                 'L1TMonitor/Layouts/Summary/GT FE Bx',
                 'L1TMonitor/Layouts/Summary/GT decision bits',
                 'L1TMonitor/Layouts/Summary/DTTF_quality',
                 'L1TMonitor/Layouts/Summary/DTTF_eta_value',
                 'L1TMonitor/Layouts/Summary/DTTF_phi_value',
                 'L1TMonitor/Layouts/Summary/DTTF_ntrack')

server.workspace('SiStrip', 'DQMContent', '^SiStrip/',
                 'SiStrip/Layouts/SiStrip_Digi_Summary')
