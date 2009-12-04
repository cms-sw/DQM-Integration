server.workspace('DQMQuality', 0, 'Summaries', 'Summary')
server.workspace('DQMSummary', 1, 'Summaries', 'Reports')
server.workspace('DQMShift',   2, 'Summaries', 'Shift')
server.workspace('DQMContent', 3, 'Summaries', 'Everything', '^')

server.workspace('DQMContent', 20, 'Tracker/Muons', 'Pixel', '^Pixel/',
                 'Pixel/Layouts/00 - Pixel_Error_Summary',
                 'Pixel/Layouts/01 - Pixel_Noise_Summary',
                 'Pixel/Layouts/02 - Pixel_Charge_Summary')

server.workspace('DQMContent', 20, 'Tracker/Muons', 'SiStrip', '^(SiStrip|Tracking)/',
                 'SiStrip/Layouts/00 - ReportSummary',
                 'SiStrip/Layouts/01 - FED-Detected Errors',
                 'SiStrip/Layouts/02 - # of Digi Trend',
                 'SiStrip/Layouts/03 - # of Cluster Trend',
                 'SiStrip/Layouts/04 - OffTrackCluster (Total Number)',
                 'SiStrip/Layouts/05 - Tracks')
               
server.workspace('DQMContent', 20, 'Tracker/Muons', 'CSC', '^CSC/',
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

server.workspace('DQMContent', 20, 'Tracker/Muons', 'DT', '^DT/',
                 'DT/Layouts/00-Summary/00-DataIntegritySummary',
                 'DT/Layouts/00-Summary/00-ROChannelSummary',
                 'DT/Layouts/00-Summary/01-OccupancySummary',
                 'DT/Layouts/00-Summary/02-SegmentSummary',
                 'DT/Layouts/00-Summary/03-DDU_TriggerCorrFractionSummary',
                 'DT/Layouts/00-Summary/04-DDU_Trigger2ndFractionSummary',
                 'DT/Layouts/00-Summary/05-DCC_TriggerCorrFractionSummary',
                 'DT/Layouts/00-Summary/06-DCC_Trigger2ndFractionSummary',
                 'DT/Layouts/00-Summary/07-NoiseChannelsSummary',
                 'DT/Layouts/00-Summary/08-SynchNoiseSummary')

server.workspace('DQMContent', 20, 'Tracker/Muons', 'RPC', '^RPC/',
                 'RPC/Layouts/RPC_Summary/Barrel/Barrel_TOP_Summary',
                 'RPC/Layouts/Occupancy_Summary/Wheels/RPC_BarrelOccupancy',
                 'RPC/Layouts/Occupancy_Summary/Wheels/RPC_EndCapOccupancy',
                 'RPC/Layouts/RPC_Summary/EndCap/EndCap_TOP_Summary') 

server.workspace('DQMContent', 30, 'Calorimeter', 'EcalPreshower', '^EcalPreshower/',
                'EcalPreshower/Layouts/01-IntegritySummary-EcalPreshower',
                'EcalPreshower/Layouts/02-OccupancySummary-EcalPreshower',
                'EcalPreshower/Layouts/03-RechitEnergySummary-EcalPreshower') 
                
server.workspace('DQMContent', 30, 'Calorimeter', 'EcalBarrel', '^EcalBarrel/',
                 'EcalBarrel/Layouts/00 Global Summary EcalBarrel',
                 'EcalBarrel/Layouts/01 Occupancy Summary EcalBarrel',
                 'EcalBarrel/Layouts/02 Cluster Summary EcalBarrel')

server.workspace('DQMContent', 30, 'Calorimeter', 'EcalEndcap', '^EcalEndcap/',
                 'EcalEndcap/Layouts/00 Global Summary EcalEndcap',
                 'EcalEndcap/Layouts/01 Occupancy Summary EcalEndcap',
                 'EcalEndcap/Layouts/02 Cluster Summary EcalEndcap')

server.workspace('DQMContent', 30, 'Calorimeter', 'HCAL', '^Hcal/',
                 "Hcal/Layouts/01 HCAL Summaries",
                 'Hcal/Layouts/HCAL Digi Problems',
                 'Hcal/Layouts/HCAL Dead Cell Check',
                 'Hcal/Layouts/HCAL Hot Cell Check',
                 'Hcal/Layouts/HCAL Data Format',
                 'Hcal/Layouts/HCAL Lumi Problems',
                 'Hcal/Layouts/HCAL Trigger Primitives'
                 )

server.workspace('DQMContent',30,'Calorimeter','HCALcalib', '^HcalCalib/',
                 'HcalCalib/Layouts/01 HcalCalib Summary',
                 'HcalCalib/Layouts/HcalCalib Pedestal Check',
                 'HcalCalib/Layouts/HcalCalib Laser Check',
                 'HcalCalib/Layouts/HcalCalib RecHit Energies')
		 
server.workspace('DQMContent', 30, 'Calorimeter', 'Castor', '^Castor/',
                 'Castor/Layouts/CASTOR RecHit Energies',
		 'Castor/Layouts/CASTOR RecHit Energy in modules',
		 'Castor/Layouts/CASTOR RecHit Energy in sectors',
		 'Castor/Layouts/CASTOR RecHit Occupancy',
                 'Castor/Layouts/CASTOR All Pedestal Values',
                 'Castor/Layouts/CASTOR Average Pulse Time',
		 'Castor/Layouts/CASTOR Average Pulse Energy'
                )
	  
server.workspace('DQMContent', 40, 'Trigger/Lumi', 'HLX', '^HLX',
                 'HLX/Layouts/HF-Comparison',
                 'HLX/Layouts/HLX-Averages',
                 'HLX/Layouts/HLX-Luminosity',
                 'HLX/Layouts/HLX-Occupancy-Check-Sums',
                 'HLX/Layouts/HLX-EtSumAndLumi-History-Plots')


server.workspace('DQMContent', 40, 'Trigger/Lumi', 'L1T', '^L1T/',
                 'L1T/L1TGT/algo_bits',
                 'L1T/L1TGT/tt_bits',
                 'L1T/L1TGT/gtfe_bx',
                 'L1T/L1TGMT/Regional_trigger',
                 'L1T/L1TGMT/GMT_etaphi',
                 'L1T/L1TGCT/IsoEmRankEtaPhi',
                 'L1T/L1TGCT/NonIsoEmRankEtaPhi',
                 'L1T/L1TGCT/AllJetsEtEtaPhi',
                 'L1T/L1TGCT/TauJetsEtEtaPhi',
                 'L1T/Layouts/03-RCT-Summary/RctEmNonIsoEmEtEtaPhi',
                 'L1T/Layouts/03-RCT-Summary/RctEmIsoEmEtEtaPhi',
                 'L1T/Layouts/03-RCT-Summary/RctRegionsEtEtaPhi',
                 'L1T/L1TDTTF/DTTF_TRACKS/INTEG/Occupancy Summary',
                 'L1T/L1TCSCTF/CSCTF_Chamber_Occupancies',
                 'L1T/L1TCSCTF/CSCTF_occupancies',
                 'L1T/L1TRPCTF/RPCTF_muons_eta_phi_bx0')

server.workspace('DQMContent', 40, 'Trigger/Lumi', 'L1TEMU', '^L1TEMU/',
                 'L1TEMU/common/sysrates',
                 'L1TEMU/common/errorflag',
                 'L1TEMU/common/sysncandData',
                 'L1TEMU/common/sysncandEmul',
                 'L1TEMU/GT/GLTErrorFlag',
                 'L1TEMU/GCT/GCTErrorFlag',
                 'L1TEMU/GMT/GMTErrorFlag',
                 'L1TEMU/RCT/RCTErrorFlag',
                 'L1TEMU/CSCTF/CTFErrorFlag',
                 'L1TEMU/CSCTPG/CTPErrorFlag',
                 'L1TEMU/DTTF/DTFErrorFlag',
                 'L1TEMU/DTTPG/DTPErrorFlag',
                 'L1TEMU/RPC/RPCErrorFlag',
                 'L1TEMU/ECAL/ETPErrorFlag',
                 'L1TEMU/HCAL/HTPErrorFlag')

server.workspace('DQMContent', 40, 'Trigger/Lumi', 'HLT', '^HLT/',
                'HLT/HLTMonMuon/Summary/PassingBits_Summary_Muon',
                'HLT/HLTMonMuon/Summary/HLTRate_Muon',
                'HLT/HLTMonMuon/L1PassThrough/Level1/HLTMuonL1_etaphi',
                'HLT/HLTMonMuon/L1PassThrough/Level1/HLTMuonL1_eta',
                'HLT/HLTMonMuon/L1PassThrough/Level1/HLTMuonL1_phi',
                'HLT/HLTMonElectron/Summary/HLTRate_Electron',
                'HLT/JetMET/All/JetMET_rate_All',
                'HLT/TauOnline/Inclusive/SingleTau/TriggerBits',
                'HLT/HLTScalers_SM/hltScalers',
                'HLT/FourVector/PathsSummary/HLT_Egamma_Pass_Any',
                'HLT/FourVector/PathsSummary/HLT_JetMET_Pass_Any',
                'HLT/FourVector/PathsSummary/HLT_Muon_Pass_Any',
                'HLT/FourVector/PathsSummary/HLT_Rest_Pass_Any',
                'HLT/FourVector/PathsSummary/HLT_Special_Pass_Any'
                )

server.workspace('DQMContent', 51,'Collisions', 'Tracking FeedBack', '^(Collisions|SiStrip|Tracking|Pixel)/',
                 'Collisions/TrackingFeedBack/00 - Number Of Tracks',
                 'Collisions/TrackingFeedBack/01 - Track Pt',
                 'Collisions/TrackingFeedBack/02 - Track Phi',
                 'Collisions/TrackingFeedBack/03 - Track Eta',
                 'Collisions/TrackingFeedBack/04 - X-Position Of Closest Approach',
                 'Collisions/TrackingFeedBack/05 - Y-Position Of Closest Approach',
                 'Collisions/TrackingFeedBack/06 - Z-Position Of Closest Approach',
                 'Collisions/TrackingFeedBack/07 - Cluster y width vs. cluster eta'
)
server.workspace('DQMContent', 52,'Collisions', 'Ecal FeedBack', '^(Collisions|EcalBarrel|EcalEndcap|EcalPreshower)/',
                 "Collisions/EcalFeedBack/00 Single Event Timing EE",
                 "Collisions/EcalFeedBack/01 Timing Mean EE",
                 "Collisions/EcalFeedBack/02 Timing Map EE -",
                 "Collisions/EcalFeedBack/02 Timing Map EE +",
                 "Collisions/EcalFeedBack/03 Occupancy EE -",
                 "Collisions/EcalFeedBack/03 Occupancy EE +",
                 "Collisions/EcalFeedBack/04 Single Event Timing EB",
                 "Collisions/EcalFeedBack/05 Timing Mean EB",
                 "Collisions/EcalFeedBack/06 Timing Map EB",
                 "Collisions/EcalFeedBack/07 Occupancy EB",
                 "Collisions/EcalFeedBack/08 ES Occupancy",
                 "Collisions/EcalFeedBack/09 ES Energy Map"
                 )
server.workspace('DQMContent', 53,'Collisions', 'Hcal FeedBack', '^(Collisions|Hcal)/',
                 "Collisions/HcalFeedBack/01 - Hcal Parameters"
                 )
server.workspace('DQMContent', 50,'Collisions', 'BeamMonitor FeedBack', '^(Collisions|BeamMonitor|Fit)/',
                 'Collisions/BeamMonitorFeedBack/00 - BeamMonitor Results'
                 )
server.workspace('DQMContent', 54,'Collisions', 'L1T FeedBack','^(Collisions|L1T)/',
                "Collisions/L1TFeedBack/00 Rate BSCL.BSCR",
                "Collisions/L1TFeedBack/01 Rate BSC splash right",
                "Collisions/L1TFeedBack/02 Rate BSC splash left",
                "Collisions/L1TFeedBack/03 Integ BSCL*BSCR Triggers vs LS",
                "Collisions/L1TFeedBack/04 Integ BSCL or BSCR Triggers vs LS",
                "Collisions/L1TFeedBack/05 Integ HF Triggers vs LS"
                )

server.workspace('DQMContent', 55,'Collisions', 'HLT FeedBack','^(Collisions|HLT)/',
                "Collisions/HLTFeedBack/00 HLT_Egamma_Pass_Any",
                "Collisions/HLTFeedBack/01 HLT_JetMET_Pass_Any",
                "Collisions/HLTFeedBack/02 HLT_Muon_Pass_Any",
                "Collisions/HLTFeedBack/03 HLT_Rest_Pass_Any",
                "Collisions/HLTFeedBack/04 HLT_Special_Pass_Any"
                )
