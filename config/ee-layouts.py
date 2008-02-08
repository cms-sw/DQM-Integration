
def eelayout(i, p, *rows): i["Layouts/EE Layouts/" + p] = DQMItem(layout=rows)

eelayout(dqmitems, "00-Summary/00-Global-Summary",
  ["EcalEndcap/EESummaryClient/EE global summary EE -"],
  ["EcalEndcap/EESummaryClient/EE global summary EE +"])

eelayout(dqmitems, "00-Summary/01-Integrity-Summary",
  ["EcalEndcap/EESummaryClient/EEIT EE - integrity quality summary"],
  ["EcalEndcap/EESummaryClient/EEIT EE + integrity quality summary"])

eelayout(dqmitems, "00-Summary/02-Occupancy-Summary",
  ["EcalEndcap/EESummaryClient/EEOT EE - digi occupancy summary"],
  ["EcalEndcap/EESummaryClient/EEOT EE + digi occupancy summary"])

eelayout(dqmitems, "00-Summary/03-Cosmic-Summary",
  ["EcalEndcap/EESummaryClient/EECT EE - cosmic summary"],
  ["EcalEndcap/EESummaryClient/EECT EE + cosmic summary"])

eelayout(dqmitems, "00-Summary/04-PedestalOnline-Summary",
  ["EcalEndcap/EESummaryClient/EEPOT EE - pedestal quality summary G12"],
  ["EcalEndcap/EESummaryClient/EEPOT EE + pedestal quality summary G12"])

eelayout(dqmitems, "00-Summary/05-LaserL1-Summary",
  ["EcalEndcap/EESummaryClient/EELT EE - laser quality summary L1"],
  ["EcalEndcap/EESummaryClient/EELT EE + laser quality summary L1"])

eelayout(dqmitems, "00-Summary/06-Led-Summary",
  ["EcalEndcap/EESummaryClient/EELDT EE - led quality summary"],
  ["EcalEndcap/EESummaryClient/EELDT EE + led quality summary"])

eelayout(dqmitems, "00-Summary/07-Timing-Summary",
  ["EcalEndcap/EESummaryClient/EETMT EE - timing quality summary"],
  ["EcalEndcap/EESummaryClient/EETMT EE + timing quality summary"])

eelayout(dqmitems, "00-Summary/08-Trigger-Summary",
  ["EcalEndcap/EESummaryClient/EETTT EE - Et trigger tower summary"],
  ["EcalEndcap/EESummaryClient/EETTT EE + Et trigger tower summary"])

eelayout(dqmitems, "00-Summary/09-Trigger-Summary",
  ["EcalEndcap/EESummaryClient/EETTT EE - emulator error quality summary"],
  ["EcalEndcap/EESummaryClient/EETTT EE + emulator error quality summary"])

eelayout(dqmitems, "00-Summary/10-StatusFlags-Summary",
  ["EcalBarrel/EESummaryClient/EESFT EE - front-end status summary"],
  ["EcalBarrel/EESummaryClient/EESFT EE + front-end status summary"])

eelayout(dqmitems, "01-Integrity/00-Integrity",
  ["EcalEndcap/EEIntegrityTask/EEIT DCC size error"])

eelayout(dqmitems, "01-Integrity/EE-/EE-01/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE-01"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE-01"])

eelayout(dqmitems, "01-Integrity/EE-/EE-01/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE-01"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE-01"])

eelayout(dqmitems, "01-Integrity/EE-/EE-01/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE-01"],
  [None])

eelayout(dqmitems, "01-Integrity/EE-/EE-01/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE-01"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE-01"])

eelayout(dqmitems, "01-Integrity/EE-/EE-01/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE-01"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE-01"])

eelayout(dqmitems, "01-Integrity/EE-/EE-01/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE-01"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE-01"])

eelayout(dqmitems, "01-Integrity/EE-/EE-01/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE-01"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE-01"])

eelayout(dqmitems, "02-PedestalOnline/EE-/EE-01/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE-01"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE-01",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE-01"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-01/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE-01"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE-01",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE-01"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-01/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE-01"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE-01",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE-01"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-01/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE-01"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE-01",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE-01"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-01/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE-01"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE-01"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-01/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-01 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-01 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-01 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-01 G16"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-01/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE-01"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE-01",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE-01"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-01/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE-01"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE-01",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE-01"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-01/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE-01"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE-01",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE-01"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-01/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE-01"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE-01"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-01/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE-01 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-01 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE-01 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE-/EE-01/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE-01 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-01 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE-01 G16",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-01/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE-01"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE-01"])

eelayout(dqmitems, "05-Laser/EE-/EE-01/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE-01",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE-01"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE-01",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE-01"])

eelayout(dqmitems, "05-Laser/EE-/EE-01/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE-01",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE-01"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE-01",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE-01"])

eelayout(dqmitems, "05-Laser/EE-/EE-01/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE-01",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-01"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE-01",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-01"])

eelayout(dqmitems, "05-Laser/EE-/EE-01/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE-01 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE-01 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE-01 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-01/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE-01 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE-01 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE-01 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-01/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE-01",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE-01"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE-01",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE-01"])

eelayout(dqmitems, "05-Laser/EE-/EE-01/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE-01",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE-01"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE-01",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE-01"])

eelayout(dqmitems, "05-Laser/EE-/EE-01/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE-01 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE-01 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE-01 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-01/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE-01 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE-01 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE-01 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-01/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE-01"])

eelayout(dqmitems, "06-Led/EE-/EE-01/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE-01",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE-01"])

eelayout(dqmitems, "06-Led/EE-/EE-01/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE-01",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE-01"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE-01",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE-01"])
   
eelayout(dqmitems, "06-Led/EE-/EE-01/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE-01",
   "EcalEndcap/EELedClient/EELDT les shape A EE-01"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE-01",
   "EcalEndcap/EELedClient/EELDT led shape B EE-01"])
   
eelayout(dqmitems, "06-Led/EE-/EE-01/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE-01 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE-01 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE-01 G01",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-01/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE-01 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE-01 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE-01 G16",
   None])

eelayout(dqmitems, "07-Timing/EE-/EE-01/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-01"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE-01",
   "EcalEndcap/EETimingClient/EETMT timing rms EE-01"])

eelayout(dqmitems, "07-Timing/EE-/EE-01/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-01"],
  ["EcalEndcap/EETimingClient/EETMT timing EE-01"])

eelayout(dqmitems, "08-Trigger/EE-/EE-01/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE-01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE-01"])

eelayout(dqmitems, "08-Trigger/EE-/EE-01/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE-01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE-01"])

eelayout(dqmitems, "08-Trigger/EE-/EE-01/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE-01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE-01"])

eelayout(dqmitems, "08-Trigger/EE-/EE-01/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE-01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE-01"])

eelayout(dqmitems, "08-Trigger/EE-/EE-01/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE-01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE-01"])

eelayout(dqmitems, "08-Trigger/EE-/EE-01/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE-01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE-01"])

eelayout(dqmitems, "08-Trigger/EE-/EE-01/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE-01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE-01"])

eelayout(dqmitems, "08-Trigger/EE-/EE-01/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE-01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE-01"])

eelayout(dqmitems, "08-Trigger/EE-/EE-01/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE-01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE-01"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-01/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE-01"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE-01"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-01/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE-01"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE-01"])

eelayout(dqmitems, "10-StatusFlags/EE-/EE-01/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE-01"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE-01"])

eelayout(dqmitems, "01-Integrity/EE-/EE-02/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE-02"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE-02"])

eelayout(dqmitems, "01-Integrity/EE-/EE-02/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE-02"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE-02"])

eelayout(dqmitems, "01-Integrity/EE-/EE-02/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE-02"],
  [None])

eelayout(dqmitems, "01-Integrity/EE-/EE-02/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE-02"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE-02"])

eelayout(dqmitems, "01-Integrity/EE-/EE-02/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE-02"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE-02"])

eelayout(dqmitems, "01-Integrity/EE-/EE-02/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE-02"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE-02"])

eelayout(dqmitems, "01-Integrity/EE-/EE-02/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE-02"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE-02"])

eelayout(dqmitems, "02-PedestalOnline/EE-/EE-02/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE-02"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE-02",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE-02"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-02/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE-02"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE-02",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE-02"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-02/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE-02"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE-02",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE-02"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-02/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE-02"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE-02",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE-02"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-02/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE-02"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE-02"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-02/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-02 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-02 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-02 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-02 G16"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-02/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE-02"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE-02",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE-02"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-02/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE-02"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE-02",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE-02"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-02/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE-02"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE-02",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE-02"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-02/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE-02"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE-02"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-02/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE-02 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-02 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE-02 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE-/EE-02/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE-02 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-02 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE-02 G16",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-02/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE-02"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE-02"])

eelayout(dqmitems, "05-Laser/EE-/EE-02/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE-02",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE-02"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE-02",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE-02"])

eelayout(dqmitems, "05-Laser/EE-/EE-02/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE-02",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE-02"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE-02",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE-02"])

eelayout(dqmitems, "05-Laser/EE-/EE-02/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE-02",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-02"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE-02",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-02"])

eelayout(dqmitems, "05-Laser/EE-/EE-02/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE-02 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE-02 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE-02 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-02/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE-02 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE-02 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE-02 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-02/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE-02",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE-02"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE-02",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE-02"])

eelayout(dqmitems, "05-Laser/EE-/EE-02/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE-02",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE-02"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE-02",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE-02"])

eelayout(dqmitems, "05-Laser/EE-/EE-02/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE-02 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE-02 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE-02 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-02/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE-02 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE-02 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE-02 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-02/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE-02"])

eelayout(dqmitems, "06-Led/EE-/EE-02/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE-02",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE-02"])

eelayout(dqmitems, "06-Led/EE-/EE-02/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE-02",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE-02"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE-02",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE-02"])
   
eelayout(dqmitems, "06-Led/EE-/EE-02/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE-02",
   "EcalEndcap/EELedClient/EELDT les shape A EE-02"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE-02",
   "EcalEndcap/EELedClient/EELDT led shape B EE-02"])
   
eelayout(dqmitems, "06-Led/EE-/EE-02/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE-02 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE-02 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE-02 G01",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-02/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE-02 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE-02 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE-02 G16",
   None])

eelayout(dqmitems, "07-Timing/EE-/EE-02/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-02"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE-02",
   "EcalEndcap/EETimingClient/EETMT timing rms EE-02"])

eelayout(dqmitems, "07-Timing/EE-/EE-02/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-02"],
  ["EcalEndcap/EETimingClient/EETMT timing EE-02"])

eelayout(dqmitems, "08-Trigger/EE-/EE-02/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE-02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE-02"])

eelayout(dqmitems, "08-Trigger/EE-/EE-02/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE-02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE-02"])

eelayout(dqmitems, "08-Trigger/EE-/EE-02/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE-02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE-02"])

eelayout(dqmitems, "08-Trigger/EE-/EE-02/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE-02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE-02"])

eelayout(dqmitems, "08-Trigger/EE-/EE-02/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE-02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE-02"])

eelayout(dqmitems, "08-Trigger/EE-/EE-02/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE-02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE-02"])

eelayout(dqmitems, "08-Trigger/EE-/EE-02/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE-02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE-02"])

eelayout(dqmitems, "08-Trigger/EE-/EE-02/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE-02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE-02"])

eelayout(dqmitems, "08-Trigger/EE-/EE-02/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE-02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE-02"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-02/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE-02"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE-02"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-02/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE-02"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE-02"])

eelayout(dqmitems, "10-StatusFlags/EE-/EE-02/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE-02"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE-02"])

eelayout(dqmitems, "01-Integrity/EE-/EE-03/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE-03"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE-03"])

eelayout(dqmitems, "01-Integrity/EE-/EE-03/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE-03"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE-03"])

eelayout(dqmitems, "01-Integrity/EE-/EE-03/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE-03"],
  [None])

eelayout(dqmitems, "01-Integrity/EE-/EE-03/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE-03"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE-03"])

eelayout(dqmitems, "01-Integrity/EE-/EE-03/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE-03"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE-03"])

eelayout(dqmitems, "01-Integrity/EE-/EE-03/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE-03"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE-03"])

eelayout(dqmitems, "01-Integrity/EE-/EE-03/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE-03"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE-03"])

eelayout(dqmitems, "02-PedestalOnline/EE-/EE-03/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE-03"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE-03",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE-03"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-03/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE-03"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE-03",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE-03"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-03/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE-03"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE-03",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE-03"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-03/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE-03"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE-03",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE-03"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-03/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE-03"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE-03"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-03/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-03 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-03 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-03 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-03 G16"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-03/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE-03"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE-03",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE-03"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-03/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE-03"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE-03",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE-03"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-03/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE-03"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE-03",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE-03"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-03/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE-03"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE-03"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-03/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE-03 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-03 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE-03 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE-/EE-03/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE-03 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-03 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE-03 G16",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-03/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE-03"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE-03"])

eelayout(dqmitems, "05-Laser/EE-/EE-03/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE-03",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE-03"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE-03",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE-03"])

eelayout(dqmitems, "05-Laser/EE-/EE-03/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE-03",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE-03"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE-03",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE-03"])

eelayout(dqmitems, "05-Laser/EE-/EE-03/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE-03",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-03"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE-03",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-03"])

eelayout(dqmitems, "05-Laser/EE-/EE-03/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE-03 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE-03 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE-03 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-03/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE-03 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE-03 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE-03 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-03/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE-03",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE-03"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE-03",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE-03"])

eelayout(dqmitems, "05-Laser/EE-/EE-03/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE-03",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE-03"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE-03",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE-03"])

eelayout(dqmitems, "05-Laser/EE-/EE-03/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE-03 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE-03 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE-03 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-03/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE-03 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE-03 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE-03 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-03/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE-03"])

eelayout(dqmitems, "06-Led/EE-/EE-03/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE-03",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE-03"])

eelayout(dqmitems, "06-Led/EE-/EE-03/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE-03",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE-03"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE-03",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE-03"])
   
eelayout(dqmitems, "06-Led/EE-/EE-03/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE-03",
   "EcalEndcap/EELedClient/EELDT les shape A EE-03"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE-03",
   "EcalEndcap/EELedClient/EELDT led shape B EE-03"])
   
eelayout(dqmitems, "06-Led/EE-/EE-03/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE-03 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE-03 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE-03 G01",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-03/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE-03 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE-03 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE-03 G16",
   None])

eelayout(dqmitems, "07-Timing/EE-/EE-03/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-03"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE-03",
   "EcalEndcap/EETimingClient/EETMT timing rms EE-03"])

eelayout(dqmitems, "07-Timing/EE-/EE-03/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-03"],
  ["EcalEndcap/EETimingClient/EETMT timing EE-03"])

eelayout(dqmitems, "08-Trigger/EE-/EE-03/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE-03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE-03"])

eelayout(dqmitems, "08-Trigger/EE-/EE-03/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE-03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE-03"])

eelayout(dqmitems, "08-Trigger/EE-/EE-03/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE-03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE-03"])

eelayout(dqmitems, "08-Trigger/EE-/EE-03/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE-03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE-03"])

eelayout(dqmitems, "08-Trigger/EE-/EE-03/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE-03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE-03"])

eelayout(dqmitems, "08-Trigger/EE-/EE-03/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE-03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE-03"])

eelayout(dqmitems, "08-Trigger/EE-/EE-03/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE-03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE-03"])

eelayout(dqmitems, "08-Trigger/EE-/EE-03/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE-03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE-03"])

eelayout(dqmitems, "08-Trigger/EE-/EE-03/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE-03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE-03"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-03/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE-03"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE-03"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-03/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE-03"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE-03"])

eelayout(dqmitems, "10-StatusFlags/EE-/EE-03/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE-03"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE-03"])

eelayout(dqmitems, "01-Integrity/EE-/EE-04/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE-04"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE-04"])

eelayout(dqmitems, "01-Integrity/EE-/EE-04/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE-04"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE-04"])

eelayout(dqmitems, "01-Integrity/EE-/EE-04/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE-04"],
  [None])

eelayout(dqmitems, "01-Integrity/EE-/EE-04/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE-04"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE-04"])

eelayout(dqmitems, "01-Integrity/EE-/EE-04/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE-04"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE-04"])

eelayout(dqmitems, "01-Integrity/EE-/EE-04/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE-04"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE-04"])

eelayout(dqmitems, "01-Integrity/EE-/EE-04/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE-04"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE-04"])

eelayout(dqmitems, "02-PedestalOnline/EE-/EE-04/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE-04"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE-04",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE-04"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-04/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE-04"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE-04",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE-04"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-04/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE-04"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE-04",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE-04"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-04/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE-04"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE-04",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE-04"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-04/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE-04"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE-04"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-04/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-04 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-04 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-04 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-04 G16"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-04/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE-04"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE-04",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE-04"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-04/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE-04"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE-04",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE-04"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-04/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE-04"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE-04",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE-04"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-04/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE-04"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE-04"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-04/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE-04 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-04 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE-04 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE-/EE-04/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE-04 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-04 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE-04 G16",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-04/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE-04"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE-04"])

eelayout(dqmitems, "05-Laser/EE-/EE-04/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE-04",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE-04"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE-04",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE-04"])

eelayout(dqmitems, "05-Laser/EE-/EE-04/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE-04",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE-04"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE-04",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE-04"])

eelayout(dqmitems, "05-Laser/EE-/EE-04/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE-04",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-04"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE-04",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-04"])

eelayout(dqmitems, "05-Laser/EE-/EE-04/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE-04 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE-04 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE-04 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-04/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE-04 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE-04 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE-04 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-04/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE-04",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE-04"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE-04",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE-04"])

eelayout(dqmitems, "05-Laser/EE-/EE-04/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE-04",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE-04"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE-04",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE-04"])

eelayout(dqmitems, "05-Laser/EE-/EE-04/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE-04 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE-04 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE-04 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-04/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE-04 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE-04 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE-04 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-04/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE-04"])

eelayout(dqmitems, "06-Led/EE-/EE-04/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE-04",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE-04"])

eelayout(dqmitems, "06-Led/EE-/EE-04/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE-04",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE-04"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE-04",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE-04"])
   
eelayout(dqmitems, "06-Led/EE-/EE-04/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE-04",
   "EcalEndcap/EELedClient/EELDT les shape A EE-04"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE-04",
   "EcalEndcap/EELedClient/EELDT led shape B EE-04"])
   
eelayout(dqmitems, "06-Led/EE-/EE-04/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE-04 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE-04 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE-04 G01",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-04/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE-04 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE-04 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE-04 G16",
   None])

eelayout(dqmitems, "07-Timing/EE-/EE-04/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-04"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE-04",
   "EcalEndcap/EETimingClient/EETMT timing rms EE-04"])

eelayout(dqmitems, "07-Timing/EE-/EE-04/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-04"],
  ["EcalEndcap/EETimingClient/EETMT timing EE-04"])

eelayout(dqmitems, "08-Trigger/EE-/EE-04/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE-04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE-04"])

eelayout(dqmitems, "08-Trigger/EE-/EE-04/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE-04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE-04"])

eelayout(dqmitems, "08-Trigger/EE-/EE-04/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE-04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE-04"])

eelayout(dqmitems, "08-Trigger/EE-/EE-04/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE-04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE-04"])

eelayout(dqmitems, "08-Trigger/EE-/EE-04/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE-04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE-04"])

eelayout(dqmitems, "08-Trigger/EE-/EE-04/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE-04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE-04"])

eelayout(dqmitems, "08-Trigger/EE-/EE-04/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE-04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE-04"])

eelayout(dqmitems, "08-Trigger/EE-/EE-04/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE-04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE-04"])

eelayout(dqmitems, "08-Trigger/EE-/EE-04/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE-04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE-04"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-04/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE-04"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE-04"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-04/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE-04"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE-04"])

eelayout(dqmitems, "10-StatusFlags/EE-/EE-04/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE-04"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE-04"])

eelayout(dqmitems, "01-Integrity/EE-/EE-05/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE-05"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE-05"])

eelayout(dqmitems, "01-Integrity/EE-/EE-05/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE-05"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE-05"])

eelayout(dqmitems, "01-Integrity/EE-/EE-05/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE-05"],
  [None])

eelayout(dqmitems, "01-Integrity/EE-/EE-05/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE-05"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE-05"])

eelayout(dqmitems, "01-Integrity/EE-/EE-05/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE-05"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE-05"])

eelayout(dqmitems, "01-Integrity/EE-/EE-05/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE-05"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE-05"])

eelayout(dqmitems, "01-Integrity/EE-/EE-05/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE-05"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE-05"])

eelayout(dqmitems, "02-PedestalOnline/EE-/EE-05/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE-05"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE-05",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE-05"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-05/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE-05"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE-05",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE-05"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-05/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE-05"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE-05",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE-05"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-05/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE-05"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE-05",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE-05"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-05/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE-05"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE-05"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-05/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-05 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-05 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-05 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-05 G16"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-05/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE-05"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE-05",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE-05"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-05/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE-05"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE-05",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE-05"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-05/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE-05"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE-05",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE-05"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-05/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE-05"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE-05"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-05/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE-05 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-05 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE-05 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE-/EE-05/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE-05 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-05 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE-05 G16",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-05/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE-05"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE-05"])

eelayout(dqmitems, "05-Laser/EE-/EE-05/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE-05",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE-05"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE-05",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE-05"])

eelayout(dqmitems, "05-Laser/EE-/EE-05/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE-05",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE-05"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE-05",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE-05"])

eelayout(dqmitems, "05-Laser/EE-/EE-05/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE-05",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-05"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE-05",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-05"])

eelayout(dqmitems, "05-Laser/EE-/EE-05/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE-05 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE-05 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE-05 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-05/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE-05 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE-05 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE-05 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-05/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE-05",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE-05"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE-05",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE-05"])

eelayout(dqmitems, "05-Laser/EE-/EE-05/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE-05",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE-05"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE-05",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE-05"])

eelayout(dqmitems, "05-Laser/EE-/EE-05/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE-05 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE-05 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE-05 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-05/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE-05 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE-05 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE-05 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-05/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE-05"])

eelayout(dqmitems, "06-Led/EE-/EE-05/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE-05",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE-05"])

eelayout(dqmitems, "06-Led/EE-/EE-05/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE-05",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE-05"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE-05",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE-05"])
   
eelayout(dqmitems, "06-Led/EE-/EE-05/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE-05",
   "EcalEndcap/EELedClient/EELDT les shape A EE-05"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE-05",
   "EcalEndcap/EELedClient/EELDT led shape B EE-05"])
   
eelayout(dqmitems, "06-Led/EE-/EE-05/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE-05 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE-05 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE-05 G01",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-05/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE-05 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE-05 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE-05 G16",
   None])

eelayout(dqmitems, "07-Timing/EE-/EE-05/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-05"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE-05",
   "EcalEndcap/EETimingClient/EETMT timing rms EE-05"])

eelayout(dqmitems, "07-Timing/EE-/EE-05/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-05"],
  ["EcalEndcap/EETimingClient/EETMT timing EE-05"])

eelayout(dqmitems, "08-Trigger/EE-/EE-05/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE-05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE-05"])

eelayout(dqmitems, "08-Trigger/EE-/EE-05/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE-05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE-05"])

eelayout(dqmitems, "08-Trigger/EE-/EE-05/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE-05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE-05"])

eelayout(dqmitems, "08-Trigger/EE-/EE-05/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE-05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE-05"])

eelayout(dqmitems, "08-Trigger/EE-/EE-05/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE-05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE-05"])

eelayout(dqmitems, "08-Trigger/EE-/EE-05/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE-05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE-05"])

eelayout(dqmitems, "08-Trigger/EE-/EE-05/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE-05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE-05"])

eelayout(dqmitems, "08-Trigger/EE-/EE-05/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE-05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE-05"])

eelayout(dqmitems, "08-Trigger/EE-/EE-05/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE-05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE-05"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-05/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE-05"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE-05"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-05/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE-05"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE-05"])

eelayout(dqmitems, "10-StatusFlags/EE-/EE-05/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE-05"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE-05"])

eelayout(dqmitems, "01-Integrity/EE-/EE-06/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE-06"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE-06"])

eelayout(dqmitems, "01-Integrity/EE-/EE-06/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE-06"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE-06"])

eelayout(dqmitems, "01-Integrity/EE-/EE-06/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE-06"],
  [None])

eelayout(dqmitems, "01-Integrity/EE-/EE-06/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE-06"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE-06"])

eelayout(dqmitems, "01-Integrity/EE-/EE-06/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE-06"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE-06"])

eelayout(dqmitems, "01-Integrity/EE-/EE-06/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE-06"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE-06"])

eelayout(dqmitems, "01-Integrity/EE-/EE-06/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE-06"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE-06"])

eelayout(dqmitems, "02-PedestalOnline/EE-/EE-06/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE-06"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE-06",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE-06"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-06/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE-06"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE-06",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE-06"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-06/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE-06"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE-06",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE-06"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-06/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE-06"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE-06",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE-06"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-06/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE-06"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE-06"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-06/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-06 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-06 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-06 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-06 G16"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-06/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE-06"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE-06",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE-06"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-06/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE-06"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE-06",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE-06"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-06/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE-06"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE-06",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE-06"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-06/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE-06"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE-06"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-06/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE-06 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-06 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE-06 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE-/EE-06/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE-06 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-06 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE-06 G16",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-06/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE-06"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE-06"])

eelayout(dqmitems, "05-Laser/EE-/EE-06/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE-06",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE-06"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE-06",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE-06"])

eelayout(dqmitems, "05-Laser/EE-/EE-06/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE-06",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE-06"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE-06",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE-06"])

eelayout(dqmitems, "05-Laser/EE-/EE-06/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE-06",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-06"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE-06",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-06"])

eelayout(dqmitems, "05-Laser/EE-/EE-06/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE-06 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE-06 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE-06 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-06/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE-06 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE-06 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE-06 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-06/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE-06",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE-06"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE-06",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE-06"])

eelayout(dqmitems, "05-Laser/EE-/EE-06/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE-06",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE-06"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE-06",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE-06"])

eelayout(dqmitems, "05-Laser/EE-/EE-06/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE-06 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE-06 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE-06 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-06/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE-06 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE-06 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE-06 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-06/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE-06"])

eelayout(dqmitems, "06-Led/EE-/EE-06/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE-06",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE-06"])

eelayout(dqmitems, "06-Led/EE-/EE-06/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE-06",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE-06"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE-06",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE-06"])
   
eelayout(dqmitems, "06-Led/EE-/EE-06/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE-06",
   "EcalEndcap/EELedClient/EELDT les shape A EE-06"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE-06",
   "EcalEndcap/EELedClient/EELDT led shape B EE-06"])
   
eelayout(dqmitems, "06-Led/EE-/EE-06/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE-06 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE-06 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE-06 G01",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-06/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE-06 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE-06 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE-06 G16",
   None])

eelayout(dqmitems, "07-Timing/EE-/EE-06/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-06"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE-06",
   "EcalEndcap/EETimingClient/EETMT timing rms EE-06"])

eelayout(dqmitems, "07-Timing/EE-/EE-06/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-06"],
  ["EcalEndcap/EETimingClient/EETMT timing EE-06"])

eelayout(dqmitems, "08-Trigger/EE-/EE-06/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE-06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE-06"])

eelayout(dqmitems, "08-Trigger/EE-/EE-06/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE-06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE-06"])

eelayout(dqmitems, "08-Trigger/EE-/EE-06/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE-06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE-06"])

eelayout(dqmitems, "08-Trigger/EE-/EE-06/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE-06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE-06"])

eelayout(dqmitems, "08-Trigger/EE-/EE-06/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE-06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE-06"])

eelayout(dqmitems, "08-Trigger/EE-/EE-06/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE-06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE-06"])

eelayout(dqmitems, "08-Trigger/EE-/EE-06/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE-06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE-06"])

eelayout(dqmitems, "08-Trigger/EE-/EE-06/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE-06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE-06"])

eelayout(dqmitems, "08-Trigger/EE-/EE-06/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE-06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE-06"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-06/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE-06"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE-06"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-06/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE-06"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE-06"])

eelayout(dqmitems, "10-StatusFlags/EE-/EE-06/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE-06"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE-06"])

eelayout(dqmitems, "01-Integrity/EE-/EE-07/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE-07"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE-07"])

eelayout(dqmitems, "01-Integrity/EE-/EE-07/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE-07"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE-07"])

eelayout(dqmitems, "01-Integrity/EE-/EE-07/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE-07"],
  [None])

eelayout(dqmitems, "01-Integrity/EE-/EE-07/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE-07"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE-07"])

eelayout(dqmitems, "01-Integrity/EE-/EE-07/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE-07"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE-07"])

eelayout(dqmitems, "01-Integrity/EE-/EE-07/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE-07"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE-07"])

eelayout(dqmitems, "01-Integrity/EE-/EE-07/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE-07"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE-07"])

eelayout(dqmitems, "02-PedestalOnline/EE-/EE-07/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE-07"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE-07",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE-07"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-07/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE-07"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE-07",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE-07"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-07/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE-07"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE-07",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE-07"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-07/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE-07"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE-07",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE-07"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-07/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE-07"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE-07"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-07/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-07 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-07 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-07 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-07 G16"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-07/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE-07"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE-07",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE-07"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-07/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE-07"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE-07",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE-07"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-07/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE-07"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE-07",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE-07"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-07/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE-07"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE-07"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-07/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE-07 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-07 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE-07 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE-/EE-07/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE-07 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-07 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE-07 G16",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-07/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE-07"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE-07"])

eelayout(dqmitems, "05-Laser/EE-/EE-07/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE-07",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE-07"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE-07",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE-07"])

eelayout(dqmitems, "05-Laser/EE-/EE-07/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE-07",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE-07"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE-07",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE-07"])

eelayout(dqmitems, "05-Laser/EE-/EE-07/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE-07",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-07"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE-07",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-07"])

eelayout(dqmitems, "05-Laser/EE-/EE-07/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE-07 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE-07 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE-07 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-07/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE-07 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE-07 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE-07 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-07/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE-07",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE-07"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE-07",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE-07"])

eelayout(dqmitems, "05-Laser/EE-/EE-07/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE-07",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE-07"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE-07",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE-07"])

eelayout(dqmitems, "05-Laser/EE-/EE-07/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE-07 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE-07 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE-07 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-07/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE-07 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE-07 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE-07 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-07/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE-07"])

eelayout(dqmitems, "06-Led/EE-/EE-07/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE-07",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE-07"])

eelayout(dqmitems, "06-Led/EE-/EE-07/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE-07",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE-07"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE-07",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE-07"])
   
eelayout(dqmitems, "06-Led/EE-/EE-07/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE-07",
   "EcalEndcap/EELedClient/EELDT les shape A EE-07"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE-07",
   "EcalEndcap/EELedClient/EELDT led shape B EE-07"])
   
eelayout(dqmitems, "06-Led/EE-/EE-07/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE-07 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE-07 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE-07 G01",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-07/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE-07 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE-07 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE-07 G16",
   None])

eelayout(dqmitems, "07-Timing/EE-/EE-07/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-07"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE-07",
   "EcalEndcap/EETimingClient/EETMT timing rms EE-07"])

eelayout(dqmitems, "07-Timing/EE-/EE-07/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-07"],
  ["EcalEndcap/EETimingClient/EETMT timing EE-07"])

eelayout(dqmitems, "08-Trigger/EE-/EE-07/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE-07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE-07"])

eelayout(dqmitems, "08-Trigger/EE-/EE-07/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE-07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE-07"])

eelayout(dqmitems, "08-Trigger/EE-/EE-07/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE-07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE-07"])

eelayout(dqmitems, "08-Trigger/EE-/EE-07/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE-07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE-07"])

eelayout(dqmitems, "08-Trigger/EE-/EE-07/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE-07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE-07"])

eelayout(dqmitems, "08-Trigger/EE-/EE-07/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE-07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE-07"])

eelayout(dqmitems, "08-Trigger/EE-/EE-07/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE-07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE-07"])

eelayout(dqmitems, "08-Trigger/EE-/EE-07/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE-07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE-07"])

eelayout(dqmitems, "08-Trigger/EE-/EE-07/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE-07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE-07"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-07/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE-07"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE-07"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-07/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE-07"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE-07"])

eelayout(dqmitems, "10-StatusFlags/EE-/EE-07/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE-07"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE-07"])

eelayout(dqmitems, "01-Integrity/EE-/EE-08/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE-08"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE-08"])

eelayout(dqmitems, "01-Integrity/EE-/EE-08/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE-08"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE-08"])

eelayout(dqmitems, "01-Integrity/EE-/EE-08/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE-08"],
  [None])

eelayout(dqmitems, "01-Integrity/EE-/EE-08/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE-08"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE-08"])

eelayout(dqmitems, "01-Integrity/EE-/EE-08/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE-08"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE-08"])

eelayout(dqmitems, "01-Integrity/EE-/EE-08/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE-08"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE-08"])

eelayout(dqmitems, "01-Integrity/EE-/EE-08/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE-08"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE-08"])

eelayout(dqmitems, "02-PedestalOnline/EE-/EE-08/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE-08"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE-08",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE-08"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-08/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE-08"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE-08",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE-08"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-08/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE-08"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE-08",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE-08"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-08/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE-08"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE-08",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE-08"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-08/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE-08"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE-08"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-08/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-08 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-08 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-08 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-08 G16"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-08/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE-08"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE-08",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE-08"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-08/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE-08"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE-08",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE-08"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-08/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE-08"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE-08",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE-08"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-08/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE-08"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE-08"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-08/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE-08 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-08 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE-08 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE-/EE-08/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE-08 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-08 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE-08 G16",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-08/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE-08"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE-08"])

eelayout(dqmitems, "05-Laser/EE-/EE-08/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE-08",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE-08"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE-08",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE-08"])

eelayout(dqmitems, "05-Laser/EE-/EE-08/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE-08",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE-08"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE-08",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE-08"])

eelayout(dqmitems, "05-Laser/EE-/EE-08/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE-08",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-08"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE-08",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-08"])

eelayout(dqmitems, "05-Laser/EE-/EE-08/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE-08 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE-08 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE-08 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-08/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE-08 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE-08 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE-08 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-08/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE-08",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE-08"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE-08",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE-08"])

eelayout(dqmitems, "05-Laser/EE-/EE-08/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE-08",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE-08"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE-08",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE-08"])

eelayout(dqmitems, "05-Laser/EE-/EE-08/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE-08 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE-08 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE-08 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-08/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE-08 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE-08 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE-08 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-08/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE-08"])

eelayout(dqmitems, "06-Led/EE-/EE-08/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE-08",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE-08"])

eelayout(dqmitems, "06-Led/EE-/EE-08/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE-08",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE-08"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE-08",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE-08"])
   
eelayout(dqmitems, "06-Led/EE-/EE-08/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE-08",
   "EcalEndcap/EELedClient/EELDT les shape A EE-08"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE-08",
   "EcalEndcap/EELedClient/EELDT led shape B EE-08"])
   
eelayout(dqmitems, "06-Led/EE-/EE-08/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE-08 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE-08 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE-08 G01",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-08/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE-08 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE-08 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE-08 G16",
   None])

eelayout(dqmitems, "07-Timing/EE-/EE-08/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-08"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE-08",
   "EcalEndcap/EETimingClient/EETMT timing rms EE-08"])

eelayout(dqmitems, "07-Timing/EE-/EE-08/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-08"],
  ["EcalEndcap/EETimingClient/EETMT timing EE-08"])

eelayout(dqmitems, "08-Trigger/EE-/EE-08/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE-08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE-08"])

eelayout(dqmitems, "08-Trigger/EE-/EE-08/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE-08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE-08"])

eelayout(dqmitems, "08-Trigger/EE-/EE-08/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE-08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE-08"])

eelayout(dqmitems, "08-Trigger/EE-/EE-08/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE-08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE-08"])

eelayout(dqmitems, "08-Trigger/EE-/EE-08/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE-08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE-08"])

eelayout(dqmitems, "08-Trigger/EE-/EE-08/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE-08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE-08"])

eelayout(dqmitems, "08-Trigger/EE-/EE-08/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE-08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE-08"])

eelayout(dqmitems, "08-Trigger/EE-/EE-08/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE-08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE-08"])

eelayout(dqmitems, "08-Trigger/EE-/EE-08/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE-08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE-08"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-08/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE-08"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE-08"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-08/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE-08"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE-08"])

eelayout(dqmitems, "10-StatusFlags/EE-/EE-08/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE-08"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE-08"])

eelayout(dqmitems, "01-Integrity/EE-/EE-09/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE-09"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE-09"])

eelayout(dqmitems, "01-Integrity/EE-/EE-09/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE-09"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE-09"])

eelayout(dqmitems, "01-Integrity/EE-/EE-09/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE-09"],
  [None])

eelayout(dqmitems, "01-Integrity/EE-/EE-09/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE-09"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE-09"])

eelayout(dqmitems, "01-Integrity/EE-/EE-09/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE-09"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE-09"])

eelayout(dqmitems, "01-Integrity/EE-/EE-09/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE-09"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE-09"])

eelayout(dqmitems, "01-Integrity/EE-/EE-09/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE-09"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE-09"])

eelayout(dqmitems, "02-PedestalOnline/EE-/EE-09/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE-09"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE-09",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE-09"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-09/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE-09"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE-09",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE-09"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-09/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE-09"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE-09",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE-09"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-09/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE-09"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE-09",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE-09"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-09/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE-09"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE-09"])

eelayout(dqmitems, "03-Pedestal/EE-/EE-09/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-09 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-09 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE-09 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE-09 G16"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-09/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE-09"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE-09",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE-09"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-09/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE-09"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE-09",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE-09"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-09/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE-09"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE-09",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE-09"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-09/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE-09"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE-09"])

eelayout(dqmitems, "04-TestPulse/EE-/EE-09/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE-09 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-09 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE-09 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE-/EE-09/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE-09 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE-09 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE-09 G16",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-09/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE-09"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE-09"])

eelayout(dqmitems, "05-Laser/EE-/EE-09/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE-09",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE-09"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE-09",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE-09"])

eelayout(dqmitems, "05-Laser/EE-/EE-09/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE-09",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE-09"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE-09",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE-09"])

eelayout(dqmitems, "05-Laser/EE-/EE-09/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE-09",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-09"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE-09",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE-09"])

eelayout(dqmitems, "05-Laser/EE-/EE-09/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE-09 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE-09 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE-09 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-09/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE-09 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE-09 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE-09 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-09/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE-09",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE-09"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE-09",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE-09"])

eelayout(dqmitems, "05-Laser/EE-/EE-09/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE-09",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE-09"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE-09",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE-09"])

eelayout(dqmitems, "05-Laser/EE-/EE-09/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE-09 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE-09 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE-09 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE-/EE-09/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE-09 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE-09 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE-09 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-09/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE-09"])

eelayout(dqmitems, "06-Led/EE-/EE-09/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE-09",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE-09"])

eelayout(dqmitems, "06-Led/EE-/EE-09/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE-09",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE-09"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE-09",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE-09"])
   
eelayout(dqmitems, "06-Led/EE-/EE-09/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE-09",
   "EcalEndcap/EELedClient/EELDT les shape A EE-09"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE-09",
   "EcalEndcap/EELedClient/EELDT led shape B EE-09"])
   
eelayout(dqmitems, "06-Led/EE-/EE-09/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE-09 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE-09 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE-09 G01",
   None])

eelayout(dqmitems, "06-Led/EE-/EE-09/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE-09 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE-09 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE-09 G16",
   None])

eelayout(dqmitems, "07-Timing/EE-/EE-09/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-09"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE-09",
   "EcalEndcap/EETimingClient/EETMT timing rms EE-09"])

eelayout(dqmitems, "07-Timing/EE-/EE-09/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE-09"],
  ["EcalEndcap/EETimingClient/EETMT timing EE-09"])

eelayout(dqmitems, "08-Trigger/EE-/EE-09/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE-09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE-09"])

eelayout(dqmitems, "08-Trigger/EE-/EE-09/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE-09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE-09"])

eelayout(dqmitems, "08-Trigger/EE-/EE-09/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE-09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE-09"])

eelayout(dqmitems, "08-Trigger/EE-/EE-09/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE-09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE-09"])

eelayout(dqmitems, "08-Trigger/EE-/EE-09/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE-09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE-09"])

eelayout(dqmitems, "08-Trigger/EE-/EE-09/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE-09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE-09"])

eelayout(dqmitems, "08-Trigger/EE-/EE-09/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE-09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE-09"])

eelayout(dqmitems, "08-Trigger/EE-/EE-09/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE-09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE-09"])

eelayout(dqmitems, "08-Trigger/EE-/EE-09/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE-09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE-09"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-09/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE-09"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE-09"])

eelayout(dqmitems, "09-Cosmic/EE-/EE-09/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE-09"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE-09"])

eelayout(dqmitems, "10-StatusFlags/EE-/EE-09/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE-09"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE-09"])

eelayout(dqmitems, "01-Integrity/EE+/EE+01/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE+01"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE+01"])

eelayout(dqmitems, "01-Integrity/EE+/EE+01/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE+01"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE+01"])

eelayout(dqmitems, "01-Integrity/EE+/EE+01/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE+01"],
  [None])

eelayout(dqmitems, "01-Integrity/EE+/EE+01/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE+01"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE+01"])

eelayout(dqmitems, "01-Integrity/EE+/EE+01/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE+01"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE+01"])

eelayout(dqmitems, "01-Integrity/EE+/EE+01/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE+01"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE+01"])

eelayout(dqmitems, "01-Integrity/EE+/EE+01/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE+01"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE+01"])

eelayout(dqmitems, "02-PedestalOnline/EE+/EE+01/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE+01"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE+01",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE+01"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+01/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE+01"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE+01",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE+01"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+01/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE+01"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE+01",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE+01"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+01/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE+01"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE+01",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE+01"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+01/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE+01"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE+01"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+01/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+01 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+01 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+01 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+01 G16"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+01/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE+01"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE+01",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE+01"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+01/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE+01"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE+01",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE+01"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+01/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE+01"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE+01",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE+01"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+01/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE+01"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE+01"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+01/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE+01 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+01 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE+01 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE+/EE+01/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE+01 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+01 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE+01 G16",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+01/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE+01"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE+01"])

eelayout(dqmitems, "05-Laser/EE+/EE+01/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE+01",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE+01"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE+01",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE+01"])

eelayout(dqmitems, "05-Laser/EE+/EE+01/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE+01",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE+01"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE+01",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE+01"])

eelayout(dqmitems, "05-Laser/EE+/EE+01/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE+01",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+01"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE+01",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+01"])

eelayout(dqmitems, "05-Laser/EE+/EE+01/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE+01 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE+01 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE+01 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+01/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE+01 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE+01 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE+01 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+01/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE+01",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE+01"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE+01",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE+01"])

eelayout(dqmitems, "05-Laser/EE+/EE+01/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE+01",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE+01"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE+01",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE+01"])

eelayout(dqmitems, "05-Laser/EE+/EE+01/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE+01 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE+01 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE+01 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+01/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE+01 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE+01 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE+01 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+01/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE+01"])

eelayout(dqmitems, "06-Led/EE+/EE+01/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE+01",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE+01"])

eelayout(dqmitems, "06-Led/EE+/EE+01/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE+01",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE+01"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE+01",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE+01"])
   
eelayout(dqmitems, "06-Led/EE+/EE+01/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE+01",
   "EcalEndcap/EELedClient/EELDT les shape A EE+01"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE+01",
   "EcalEndcap/EELedClient/EELDT led shape B EE+01"])
   
eelayout(dqmitems, "06-Led/EE+/EE+01/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE+01 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE+01 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE+01 G01",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+01/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE+01 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE+01 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE+01 G16",
   None])

eelayout(dqmitems, "07-Timing/EE+/EE+01/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+01"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE+01",
   "EcalEndcap/EETimingClient/EETMT timing rms EE+01"])

eelayout(dqmitems, "07-Timing/EE+/EE+01/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+01"],
  ["EcalEndcap/EETimingClient/EETMT timing EE+01"])

eelayout(dqmitems, "08-Trigger/EE+/EE+01/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE+01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE+01"])

eelayout(dqmitems, "08-Trigger/EE+/EE+01/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE+01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE+01"])

eelayout(dqmitems, "08-Trigger/EE+/EE+01/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE+01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE+01"])

eelayout(dqmitems, "08-Trigger/EE+/EE+01/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE+01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE+01"])

eelayout(dqmitems, "08-Trigger/EE+/EE+01/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE+01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE+01"])

eelayout(dqmitems, "08-Trigger/EE+/EE+01/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE+01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE+01"])

eelayout(dqmitems, "08-Trigger/EE+/EE+01/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE+01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE+01"])

eelayout(dqmitems, "08-Trigger/EE+/EE+01/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE+01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE+01"])

eelayout(dqmitems, "08-Trigger/EE+/EE+01/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE+01"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE+01"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+01/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE+01"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE+01"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+01/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE+01"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE+01"])

eelayout(dqmitems, "10-StatusFlags/EE+/EE+01/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE+01"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE+01"])

eelayout(dqmitems, "01-Integrity/EE+/EE+02/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE+02"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE+02"])

eelayout(dqmitems, "01-Integrity/EE+/EE+02/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE+02"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE+02"])

eelayout(dqmitems, "01-Integrity/EE+/EE+02/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE+02"],
  [None])

eelayout(dqmitems, "01-Integrity/EE+/EE+02/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE+02"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE+02"])

eelayout(dqmitems, "01-Integrity/EE+/EE+02/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE+02"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE+02"])

eelayout(dqmitems, "01-Integrity/EE+/EE+02/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE+02"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE+02"])

eelayout(dqmitems, "01-Integrity/EE+/EE+02/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE+02"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE+02"])

eelayout(dqmitems, "02-PedestalOnline/EE+/EE+02/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE+02"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE+02",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE+02"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+02/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE+02"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE+02",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE+02"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+02/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE+02"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE+02",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE+02"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+02/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE+02"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE+02",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE+02"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+02/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE+02"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE+02"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+02/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+02 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+02 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+02 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+02 G16"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+02/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE+02"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE+02",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE+02"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+02/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE+02"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE+02",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE+02"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+02/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE+02"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE+02",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE+02"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+02/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE+02"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE+02"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+02/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE+02 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+02 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE+02 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE+/EE+02/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE+02 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+02 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE+02 G16",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+02/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE+02"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE+02"])

eelayout(dqmitems, "05-Laser/EE+/EE+02/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE+02",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE+02"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE+02",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE+02"])

eelayout(dqmitems, "05-Laser/EE+/EE+02/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE+02",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE+02"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE+02",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE+02"])

eelayout(dqmitems, "05-Laser/EE+/EE+02/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE+02",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+02"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE+02",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+02"])

eelayout(dqmitems, "05-Laser/EE+/EE+02/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE+02 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE+02 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE+02 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+02/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE+02 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE+02 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE+02 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+02/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE+02",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE+02"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE+02",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE+02"])

eelayout(dqmitems, "05-Laser/EE+/EE+02/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE+02",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE+02"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE+02",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE+02"])

eelayout(dqmitems, "05-Laser/EE+/EE+02/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE+02 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE+02 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE+02 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+02/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE+02 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE+02 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE+02 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+02/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE+02"])

eelayout(dqmitems, "06-Led/EE+/EE+02/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE+02",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE+02"])

eelayout(dqmitems, "06-Led/EE+/EE+02/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE+02",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE+02"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE+02",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE+02"])
   
eelayout(dqmitems, "06-Led/EE+/EE+02/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE+02",
   "EcalEndcap/EELedClient/EELDT les shape A EE+02"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE+02",
   "EcalEndcap/EELedClient/EELDT led shape B EE+02"])
   
eelayout(dqmitems, "06-Led/EE+/EE+02/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE+02 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE+02 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE+02 G01",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+02/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE+02 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE+02 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE+02 G16",
   None])

eelayout(dqmitems, "07-Timing/EE+/EE+02/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+02"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE+02",
   "EcalEndcap/EETimingClient/EETMT timing rms EE+02"])

eelayout(dqmitems, "07-Timing/EE+/EE+02/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+02"],
  ["EcalEndcap/EETimingClient/EETMT timing EE+02"])

eelayout(dqmitems, "08-Trigger/EE+/EE+02/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE+02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE+02"])

eelayout(dqmitems, "08-Trigger/EE+/EE+02/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE+02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE+02"])

eelayout(dqmitems, "08-Trigger/EE+/EE+02/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE+02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE+02"])

eelayout(dqmitems, "08-Trigger/EE+/EE+02/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE+02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE+02"])

eelayout(dqmitems, "08-Trigger/EE+/EE+02/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE+02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE+02"])

eelayout(dqmitems, "08-Trigger/EE+/EE+02/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE+02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE+02"])

eelayout(dqmitems, "08-Trigger/EE+/EE+02/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE+02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE+02"])

eelayout(dqmitems, "08-Trigger/EE+/EE+02/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE+02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE+02"])

eelayout(dqmitems, "08-Trigger/EE+/EE+02/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE+02"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE+02"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+02/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE+02"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE+02"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+02/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE+02"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE+02"])

eelayout(dqmitems, "10-StatusFlags/EE+/EE+02/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE+02"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE+02"])

eelayout(dqmitems, "01-Integrity/EE+/EE+03/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE+03"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE+03"])

eelayout(dqmitems, "01-Integrity/EE+/EE+03/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE+03"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE+03"])

eelayout(dqmitems, "01-Integrity/EE+/EE+03/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE+03"],
  [None])

eelayout(dqmitems, "01-Integrity/EE+/EE+03/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE+03"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE+03"])

eelayout(dqmitems, "01-Integrity/EE+/EE+03/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE+03"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE+03"])

eelayout(dqmitems, "01-Integrity/EE+/EE+03/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE+03"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE+03"])

eelayout(dqmitems, "01-Integrity/EE+/EE+03/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE+03"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE+03"])

eelayout(dqmitems, "02-PedestalOnline/EE+/EE+03/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE+03"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE+03",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE+03"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+03/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE+03"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE+03",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE+03"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+03/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE+03"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE+03",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE+03"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+03/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE+03"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE+03",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE+03"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+03/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE+03"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE+03"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+03/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+03 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+03 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+03 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+03 G16"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+03/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE+03"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE+03",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE+03"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+03/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE+03"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE+03",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE+03"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+03/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE+03"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE+03",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE+03"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+03/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE+03"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE+03"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+03/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE+03 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+03 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE+03 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE+/EE+03/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE+03 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+03 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE+03 G16",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+03/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE+03"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE+03"])

eelayout(dqmitems, "05-Laser/EE+/EE+03/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE+03",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE+03"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE+03",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE+03"])

eelayout(dqmitems, "05-Laser/EE+/EE+03/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE+03",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE+03"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE+03",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE+03"])

eelayout(dqmitems, "05-Laser/EE+/EE+03/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE+03",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+03"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE+03",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+03"])

eelayout(dqmitems, "05-Laser/EE+/EE+03/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE+03 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE+03 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE+03 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+03/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE+03 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE+03 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE+03 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+03/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE+03",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE+03"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE+03",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE+03"])

eelayout(dqmitems, "05-Laser/EE+/EE+03/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE+03",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE+03"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE+03",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE+03"])

eelayout(dqmitems, "05-Laser/EE+/EE+03/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE+03 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE+03 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE+03 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+03/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE+03 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE+03 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE+03 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+03/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE+03"])

eelayout(dqmitems, "06-Led/EE+/EE+03/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE+03",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE+03"])

eelayout(dqmitems, "06-Led/EE+/EE+03/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE+03",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE+03"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE+03",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE+03"])
   
eelayout(dqmitems, "06-Led/EE+/EE+03/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE+03",
   "EcalEndcap/EELedClient/EELDT les shape A EE+03"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE+03",
   "EcalEndcap/EELedClient/EELDT led shape B EE+03"])
   
eelayout(dqmitems, "06-Led/EE+/EE+03/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE+03 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE+03 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE+03 G01",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+03/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE+03 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE+03 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE+03 G16",
   None])

eelayout(dqmitems, "07-Timing/EE+/EE+03/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+03"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE+03",
   "EcalEndcap/EETimingClient/EETMT timing rms EE+03"])

eelayout(dqmitems, "07-Timing/EE+/EE+03/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+03"],
  ["EcalEndcap/EETimingClient/EETMT timing EE+03"])

eelayout(dqmitems, "08-Trigger/EE+/EE+03/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE+03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE+03"])

eelayout(dqmitems, "08-Trigger/EE+/EE+03/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE+03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE+03"])

eelayout(dqmitems, "08-Trigger/EE+/EE+03/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE+03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE+03"])

eelayout(dqmitems, "08-Trigger/EE+/EE+03/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE+03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE+03"])

eelayout(dqmitems, "08-Trigger/EE+/EE+03/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE+03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE+03"])

eelayout(dqmitems, "08-Trigger/EE+/EE+03/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE+03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE+03"])

eelayout(dqmitems, "08-Trigger/EE+/EE+03/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE+03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE+03"])

eelayout(dqmitems, "08-Trigger/EE+/EE+03/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE+03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE+03"])

eelayout(dqmitems, "08-Trigger/EE+/EE+03/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE+03"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE+03"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+03/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE+03"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE+03"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+03/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE+03"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE+03"])

eelayout(dqmitems, "10-StatusFlags/EE+/EE+03/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE+03"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE+03"])

eelayout(dqmitems, "01-Integrity/EE+/EE+04/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE+04"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE+04"])

eelayout(dqmitems, "01-Integrity/EE+/EE+04/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE+04"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE+04"])

eelayout(dqmitems, "01-Integrity/EE+/EE+04/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE+04"],
  [None])

eelayout(dqmitems, "01-Integrity/EE+/EE+04/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE+04"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE+04"])

eelayout(dqmitems, "01-Integrity/EE+/EE+04/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE+04"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE+04"])

eelayout(dqmitems, "01-Integrity/EE+/EE+04/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE+04"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE+04"])

eelayout(dqmitems, "01-Integrity/EE+/EE+04/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE+04"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE+04"])

eelayout(dqmitems, "02-PedestalOnline/EE+/EE+04/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE+04"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE+04",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE+04"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+04/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE+04"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE+04",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE+04"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+04/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE+04"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE+04",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE+04"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+04/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE+04"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE+04",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE+04"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+04/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE+04"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE+04"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+04/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+04 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+04 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+04 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+04 G16"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+04/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE+04"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE+04",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE+04"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+04/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE+04"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE+04",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE+04"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+04/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE+04"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE+04",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE+04"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+04/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE+04"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE+04"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+04/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE+04 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+04 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE+04 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE+/EE+04/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE+04 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+04 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE+04 G16",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+04/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE+04"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE+04"])

eelayout(dqmitems, "05-Laser/EE+/EE+04/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE+04",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE+04"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE+04",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE+04"])

eelayout(dqmitems, "05-Laser/EE+/EE+04/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE+04",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE+04"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE+04",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE+04"])

eelayout(dqmitems, "05-Laser/EE+/EE+04/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE+04",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+04"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE+04",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+04"])

eelayout(dqmitems, "05-Laser/EE+/EE+04/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE+04 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE+04 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE+04 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+04/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE+04 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE+04 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE+04 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+04/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE+04",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE+04"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE+04",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE+04"])

eelayout(dqmitems, "05-Laser/EE+/EE+04/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE+04",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE+04"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE+04",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE+04"])

eelayout(dqmitems, "05-Laser/EE+/EE+04/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE+04 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE+04 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE+04 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+04/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE+04 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE+04 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE+04 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+04/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE+04"])

eelayout(dqmitems, "06-Led/EE+/EE+04/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE+04",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE+04"])

eelayout(dqmitems, "06-Led/EE+/EE+04/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE+04",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE+04"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE+04",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE+04"])
   
eelayout(dqmitems, "06-Led/EE+/EE+04/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE+04",
   "EcalEndcap/EELedClient/EELDT les shape A EE+04"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE+04",
   "EcalEndcap/EELedClient/EELDT led shape B EE+04"])
   
eelayout(dqmitems, "06-Led/EE+/EE+04/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE+04 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE+04 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE+04 G01",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+04/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE+04 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE+04 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE+04 G16",
   None])

eelayout(dqmitems, "07-Timing/EE+/EE+04/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+04"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE+04",
   "EcalEndcap/EETimingClient/EETMT timing rms EE+04"])

eelayout(dqmitems, "07-Timing/EE+/EE+04/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+04"],
  ["EcalEndcap/EETimingClient/EETMT timing EE+04"])

eelayout(dqmitems, "08-Trigger/EE+/EE+04/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE+04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE+04"])

eelayout(dqmitems, "08-Trigger/EE+/EE+04/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE+04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE+04"])

eelayout(dqmitems, "08-Trigger/EE+/EE+04/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE+04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE+04"])

eelayout(dqmitems, "08-Trigger/EE+/EE+04/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE+04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE+04"])

eelayout(dqmitems, "08-Trigger/EE+/EE+04/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE+04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE+04"])

eelayout(dqmitems, "08-Trigger/EE+/EE+04/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE+04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE+04"])

eelayout(dqmitems, "08-Trigger/EE+/EE+04/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE+04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE+04"])

eelayout(dqmitems, "08-Trigger/EE+/EE+04/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE+04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE+04"])

eelayout(dqmitems, "08-Trigger/EE+/EE+04/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE+04"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE+04"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+04/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE+04"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE+04"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+04/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE+04"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE+04"])

eelayout(dqmitems, "10-StatusFlags/EE+/EE+04/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE+04"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE+04"])

eelayout(dqmitems, "01-Integrity/EE+/EE+05/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE+05"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE+05"])

eelayout(dqmitems, "01-Integrity/EE+/EE+05/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE+05"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE+05"])

eelayout(dqmitems, "01-Integrity/EE+/EE+05/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE+05"],
  [None])

eelayout(dqmitems, "01-Integrity/EE+/EE+05/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE+05"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE+05"])

eelayout(dqmitems, "01-Integrity/EE+/EE+05/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE+05"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE+05"])

eelayout(dqmitems, "01-Integrity/EE+/EE+05/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE+05"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE+05"])

eelayout(dqmitems, "01-Integrity/EE+/EE+05/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE+05"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE+05"])

eelayout(dqmitems, "02-PedestalOnline/EE+/EE+05/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE+05"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE+05",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE+05"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+05/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE+05"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE+05",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE+05"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+05/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE+05"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE+05",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE+05"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+05/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE+05"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE+05",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE+05"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+05/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE+05"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE+05"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+05/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+05 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+05 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+05 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+05 G16"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+05/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE+05"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE+05",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE+05"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+05/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE+05"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE+05",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE+05"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+05/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE+05"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE+05",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE+05"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+05/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE+05"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE+05"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+05/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE+05 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+05 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE+05 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE+/EE+05/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE+05 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+05 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE+05 G16",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+05/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE+05"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE+05"])

eelayout(dqmitems, "05-Laser/EE+/EE+05/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE+05",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE+05"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE+05",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE+05"])

eelayout(dqmitems, "05-Laser/EE+/EE+05/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE+05",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE+05"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE+05",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE+05"])

eelayout(dqmitems, "05-Laser/EE+/EE+05/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE+05",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+05"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE+05",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+05"])

eelayout(dqmitems, "05-Laser/EE+/EE+05/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE+05 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE+05 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE+05 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+05/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE+05 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE+05 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE+05 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+05/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE+05",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE+05"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE+05",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE+05"])

eelayout(dqmitems, "05-Laser/EE+/EE+05/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE+05",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE+05"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE+05",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE+05"])

eelayout(dqmitems, "05-Laser/EE+/EE+05/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE+05 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE+05 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE+05 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+05/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE+05 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE+05 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE+05 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+05/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE+05"])

eelayout(dqmitems, "06-Led/EE+/EE+05/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE+05",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE+05"])

eelayout(dqmitems, "06-Led/EE+/EE+05/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE+05",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE+05"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE+05",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE+05"])
   
eelayout(dqmitems, "06-Led/EE+/EE+05/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE+05",
   "EcalEndcap/EELedClient/EELDT les shape A EE+05"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE+05",
   "EcalEndcap/EELedClient/EELDT led shape B EE+05"])
   
eelayout(dqmitems, "06-Led/EE+/EE+05/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE+05 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE+05 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE+05 G01",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+05/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE+05 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE+05 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE+05 G16",
   None])

eelayout(dqmitems, "07-Timing/EE+/EE+05/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+05"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE+05",
   "EcalEndcap/EETimingClient/EETMT timing rms EE+05"])

eelayout(dqmitems, "07-Timing/EE+/EE+05/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+05"],
  ["EcalEndcap/EETimingClient/EETMT timing EE+05"])

eelayout(dqmitems, "08-Trigger/EE+/EE+05/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE+05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE+05"])

eelayout(dqmitems, "08-Trigger/EE+/EE+05/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE+05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE+05"])

eelayout(dqmitems, "08-Trigger/EE+/EE+05/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE+05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE+05"])

eelayout(dqmitems, "08-Trigger/EE+/EE+05/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE+05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE+05"])

eelayout(dqmitems, "08-Trigger/EE+/EE+05/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE+05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE+05"])

eelayout(dqmitems, "08-Trigger/EE+/EE+05/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE+05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE+05"])

eelayout(dqmitems, "08-Trigger/EE+/EE+05/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE+05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE+05"])

eelayout(dqmitems, "08-Trigger/EE+/EE+05/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE+05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE+05"])

eelayout(dqmitems, "08-Trigger/EE+/EE+05/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE+05"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE+05"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+05/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE+05"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE+05"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+05/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE+05"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE+05"])

eelayout(dqmitems, "10-StatusFlags/EE+/EE+05/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE+05"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE+05"])

eelayout(dqmitems, "01-Integrity/EE+/EE+06/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE+06"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE+06"])

eelayout(dqmitems, "01-Integrity/EE+/EE+06/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE+06"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE+06"])

eelayout(dqmitems, "01-Integrity/EE+/EE+06/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE+06"],
  [None])

eelayout(dqmitems, "01-Integrity/EE+/EE+06/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE+06"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE+06"])

eelayout(dqmitems, "01-Integrity/EE+/EE+06/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE+06"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE+06"])

eelayout(dqmitems, "01-Integrity/EE+/EE+06/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE+06"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE+06"])

eelayout(dqmitems, "01-Integrity/EE+/EE+06/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE+06"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE+06"])

eelayout(dqmitems, "02-PedestalOnline/EE+/EE+06/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE+06"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE+06",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE+06"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+06/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE+06"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE+06",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE+06"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+06/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE+06"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE+06",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE+06"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+06/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE+06"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE+06",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE+06"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+06/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE+06"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE+06"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+06/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+06 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+06 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+06 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+06 G16"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+06/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE+06"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE+06",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE+06"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+06/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE+06"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE+06",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE+06"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+06/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE+06"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE+06",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE+06"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+06/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE+06"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE+06"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+06/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE+06 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+06 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE+06 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE+/EE+06/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE+06 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+06 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE+06 G16",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+06/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE+06"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE+06"])

eelayout(dqmitems, "05-Laser/EE+/EE+06/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE+06",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE+06"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE+06",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE+06"])

eelayout(dqmitems, "05-Laser/EE+/EE+06/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE+06",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE+06"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE+06",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE+06"])

eelayout(dqmitems, "05-Laser/EE+/EE+06/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE+06",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+06"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE+06",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+06"])

eelayout(dqmitems, "05-Laser/EE+/EE+06/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE+06 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE+06 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE+06 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+06/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE+06 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE+06 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE+06 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+06/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE+06",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE+06"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE+06",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE+06"])

eelayout(dqmitems, "05-Laser/EE+/EE+06/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE+06",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE+06"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE+06",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE+06"])

eelayout(dqmitems, "05-Laser/EE+/EE+06/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE+06 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE+06 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE+06 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+06/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE+06 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE+06 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE+06 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+06/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE+06"])

eelayout(dqmitems, "06-Led/EE+/EE+06/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE+06",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE+06"])

eelayout(dqmitems, "06-Led/EE+/EE+06/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE+06",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE+06"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE+06",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE+06"])
   
eelayout(dqmitems, "06-Led/EE+/EE+06/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE+06",
   "EcalEndcap/EELedClient/EELDT les shape A EE+06"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE+06",
   "EcalEndcap/EELedClient/EELDT led shape B EE+06"])
   
eelayout(dqmitems, "06-Led/EE+/EE+06/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE+06 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE+06 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE+06 G01",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+06/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE+06 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE+06 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE+06 G16",
   None])

eelayout(dqmitems, "07-Timing/EE+/EE+06/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+06"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE+06",
   "EcalEndcap/EETimingClient/EETMT timing rms EE+06"])

eelayout(dqmitems, "07-Timing/EE+/EE+06/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+06"],
  ["EcalEndcap/EETimingClient/EETMT timing EE+06"])

eelayout(dqmitems, "08-Trigger/EE+/EE+06/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE+06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE+06"])

eelayout(dqmitems, "08-Trigger/EE+/EE+06/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE+06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE+06"])

eelayout(dqmitems, "08-Trigger/EE+/EE+06/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE+06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE+06"])

eelayout(dqmitems, "08-Trigger/EE+/EE+06/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE+06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE+06"])

eelayout(dqmitems, "08-Trigger/EE+/EE+06/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE+06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE+06"])

eelayout(dqmitems, "08-Trigger/EE+/EE+06/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE+06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE+06"])

eelayout(dqmitems, "08-Trigger/EE+/EE+06/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE+06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE+06"])

eelayout(dqmitems, "08-Trigger/EE+/EE+06/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE+06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE+06"])

eelayout(dqmitems, "08-Trigger/EE+/EE+06/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE+06"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE+06"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+06/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE+06"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE+06"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+06/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE+06"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE+06"])

eelayout(dqmitems, "10-StatusFlags/EE+/EE+06/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE+06"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE+06"])

eelayout(dqmitems, "01-Integrity/EE+/EE+07/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE+07"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE+07"])

eelayout(dqmitems, "01-Integrity/EE+/EE+07/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE+07"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE+07"])

eelayout(dqmitems, "01-Integrity/EE+/EE+07/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE+07"],
  [None])

eelayout(dqmitems, "01-Integrity/EE+/EE+07/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE+07"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE+07"])

eelayout(dqmitems, "01-Integrity/EE+/EE+07/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE+07"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE+07"])

eelayout(dqmitems, "01-Integrity/EE+/EE+07/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE+07"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE+07"])

eelayout(dqmitems, "01-Integrity/EE+/EE+07/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE+07"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE+07"])

eelayout(dqmitems, "02-PedestalOnline/EE+/EE+07/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE+07"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE+07",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE+07"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+07/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE+07"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE+07",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE+07"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+07/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE+07"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE+07",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE+07"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+07/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE+07"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE+07",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE+07"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+07/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE+07"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE+07"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+07/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+07 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+07 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+07 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+07 G16"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+07/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE+07"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE+07",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE+07"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+07/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE+07"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE+07",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE+07"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+07/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE+07"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE+07",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE+07"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+07/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE+07"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE+07"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+07/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE+07 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+07 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE+07 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE+/EE+07/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE+07 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+07 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE+07 G16",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+07/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE+07"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE+07"])

eelayout(dqmitems, "05-Laser/EE+/EE+07/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE+07",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE+07"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE+07",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE+07"])

eelayout(dqmitems, "05-Laser/EE+/EE+07/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE+07",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE+07"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE+07",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE+07"])

eelayout(dqmitems, "05-Laser/EE+/EE+07/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE+07",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+07"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE+07",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+07"])

eelayout(dqmitems, "05-Laser/EE+/EE+07/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE+07 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE+07 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE+07 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+07/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE+07 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE+07 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE+07 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+07/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE+07",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE+07"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE+07",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE+07"])

eelayout(dqmitems, "05-Laser/EE+/EE+07/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE+07",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE+07"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE+07",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE+07"])

eelayout(dqmitems, "05-Laser/EE+/EE+07/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE+07 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE+07 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE+07 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+07/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE+07 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE+07 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE+07 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+07/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE+07"])

eelayout(dqmitems, "06-Led/EE+/EE+07/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE+07",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE+07"])

eelayout(dqmitems, "06-Led/EE+/EE+07/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE+07",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE+07"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE+07",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE+07"])
   
eelayout(dqmitems, "06-Led/EE+/EE+07/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE+07",
   "EcalEndcap/EELedClient/EELDT les shape A EE+07"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE+07",
   "EcalEndcap/EELedClient/EELDT led shape B EE+07"])
   
eelayout(dqmitems, "06-Led/EE+/EE+07/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE+07 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE+07 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE+07 G01",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+07/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE+07 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE+07 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE+07 G16",
   None])

eelayout(dqmitems, "07-Timing/EE+/EE+07/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+07"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE+07",
   "EcalEndcap/EETimingClient/EETMT timing rms EE+07"])

eelayout(dqmitems, "07-Timing/EE+/EE+07/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+07"],
  ["EcalEndcap/EETimingClient/EETMT timing EE+07"])

eelayout(dqmitems, "08-Trigger/EE+/EE+07/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE+07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE+07"])

eelayout(dqmitems, "08-Trigger/EE+/EE+07/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE+07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE+07"])

eelayout(dqmitems, "08-Trigger/EE+/EE+07/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE+07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE+07"])

eelayout(dqmitems, "08-Trigger/EE+/EE+07/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE+07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE+07"])

eelayout(dqmitems, "08-Trigger/EE+/EE+07/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE+07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE+07"])

eelayout(dqmitems, "08-Trigger/EE+/EE+07/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE+07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE+07"])

eelayout(dqmitems, "08-Trigger/EE+/EE+07/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE+07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE+07"])

eelayout(dqmitems, "08-Trigger/EE+/EE+07/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE+07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE+07"])

eelayout(dqmitems, "08-Trigger/EE+/EE+07/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE+07"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE+07"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+07/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE+07"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE+07"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+07/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE+07"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE+07"])

eelayout(dqmitems, "10-StatusFlags/EE+/EE+07/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE+07"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE+07"])

eelayout(dqmitems, "01-Integrity/EE+/EE+08/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE+08"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE+08"])

eelayout(dqmitems, "01-Integrity/EE+/EE+08/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE+08"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE+08"])

eelayout(dqmitems, "01-Integrity/EE+/EE+08/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE+08"],
  [None])

eelayout(dqmitems, "01-Integrity/EE+/EE+08/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE+08"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE+08"])

eelayout(dqmitems, "01-Integrity/EE+/EE+08/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE+08"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE+08"])

eelayout(dqmitems, "01-Integrity/EE+/EE+08/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE+08"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE+08"])

eelayout(dqmitems, "01-Integrity/EE+/EE+08/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE+08"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE+08"])

eelayout(dqmitems, "02-PedestalOnline/EE+/EE+08/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE+08"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE+08",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE+08"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+08/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE+08"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE+08",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE+08"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+08/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE+08"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE+08",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE+08"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+08/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE+08"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE+08",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE+08"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+08/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE+08"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE+08"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+08/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+08 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+08 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+08 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+08 G16"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+08/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE+08"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE+08",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE+08"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+08/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE+08"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE+08",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE+08"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+08/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE+08"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE+08",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE+08"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+08/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE+08"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE+08"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+08/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE+08 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+08 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE+08 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE+/EE+08/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE+08 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+08 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE+08 G16",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+08/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE+08"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE+08"])

eelayout(dqmitems, "05-Laser/EE+/EE+08/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE+08",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE+08"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE+08",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE+08"])

eelayout(dqmitems, "05-Laser/EE+/EE+08/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE+08",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE+08"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE+08",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE+08"])

eelayout(dqmitems, "05-Laser/EE+/EE+08/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE+08",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+08"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE+08",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+08"])

eelayout(dqmitems, "05-Laser/EE+/EE+08/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE+08 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE+08 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE+08 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+08/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE+08 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE+08 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE+08 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+08/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE+08",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE+08"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE+08",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE+08"])

eelayout(dqmitems, "05-Laser/EE+/EE+08/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE+08",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE+08"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE+08",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE+08"])

eelayout(dqmitems, "05-Laser/EE+/EE+08/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE+08 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE+08 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE+08 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+08/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE+08 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE+08 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE+08 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+08/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE+08"])

eelayout(dqmitems, "06-Led/EE+/EE+08/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE+08",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE+08"])

eelayout(dqmitems, "06-Led/EE+/EE+08/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE+08",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE+08"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE+08",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE+08"])
   
eelayout(dqmitems, "06-Led/EE+/EE+08/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE+08",
   "EcalEndcap/EELedClient/EELDT les shape A EE+08"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE+08",
   "EcalEndcap/EELedClient/EELDT led shape B EE+08"])
   
eelayout(dqmitems, "06-Led/EE+/EE+08/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE+08 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE+08 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE+08 G01",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+08/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE+08 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE+08 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE+08 G16",
   None])

eelayout(dqmitems, "07-Timing/EE+/EE+08/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+08"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE+08",
   "EcalEndcap/EETimingClient/EETMT timing rms EE+08"])

eelayout(dqmitems, "07-Timing/EE+/EE+08/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+08"],
  ["EcalEndcap/EETimingClient/EETMT timing EE+08"])

eelayout(dqmitems, "08-Trigger/EE+/EE+08/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE+08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE+08"])

eelayout(dqmitems, "08-Trigger/EE+/EE+08/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE+08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE+08"])

eelayout(dqmitems, "08-Trigger/EE+/EE+08/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE+08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE+08"])

eelayout(dqmitems, "08-Trigger/EE+/EE+08/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE+08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE+08"])

eelayout(dqmitems, "08-Trigger/EE+/EE+08/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE+08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE+08"])

eelayout(dqmitems, "08-Trigger/EE+/EE+08/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE+08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE+08"])

eelayout(dqmitems, "08-Trigger/EE+/EE+08/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE+08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE+08"])

eelayout(dqmitems, "08-Trigger/EE+/EE+08/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE+08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE+08"])

eelayout(dqmitems, "08-Trigger/EE+/EE+08/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE+08"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE+08"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+08/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE+08"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE+08"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+08/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE+08"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE+08"])

eelayout(dqmitems, "10-StatusFlags/EE+/EE+08/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE+08"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE+08"])

eelayout(dqmitems, "01-Integrity/EE+/EE+09/00-Channel-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality EE+09"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE+09"])

eelayout(dqmitems, "01-Integrity/EE+/EE+09/01-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/Gain/EEIT gain EE+09"],
  ["EcalEndcap/EEIntegrityTask/ChId/EEIT ChId EE+09"])

eelayout(dqmitems, "01-Integrity/EE+/EE+09/02-Gain-Integrity",
  ["EcalEndcap/EEIntegrityTask/GainSwitch/EEIT gain switch EE+09"],
  [None])

eelayout(dqmitems, "01-Integrity/EE+/EE+09/03-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/TTId/EEIT TTId EE+09"],
  ["EcalEndcap/EEIntegrityTask/TTBlockSize/EEIT TTBlockSize EE+09"])

eelayout(dqmitems, "01-Integrity/EE+/EE+09/04-MemBox-Global-Integrity",
  ["EcalEndcap/EEIntegrityClient/EEIT data integrity quality MEM EE+09"],
  ["EcalEndcap/EEOccupancyTask/EEOT MEM digi occupancy EE+09"])

eelayout(dqmitems, "01-Integrity/EE+/EE+09/05-MemBox-Channel-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemChId/EEIT MemChId EE+09"],
  ["EcalEndcap/EEIntegrityTask/MemGain/EEIT MemGain EE+09"])

eelayout(dqmitems, "01-Integrity/EE+/EE+09/06-MemBox-TT-Integrity",
  ["EcalEndcap/EEIntegrityTask/MemTTId/EEIT MemTTId EE+09"],
  ["EcalEndcap/EEIntegrityTask/MemSize/EEIT MemSize EE+09"])

eelayout(dqmitems, "02-PedestalOnline/EE+/EE+09/Gain12/00-PedestalOnline",
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal quality G12 EE+09"],
  ["EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal mean G12 EE+09",
   "EcalEndcap/EEPedestalOnlineClient/EEPOT pedestal rms G12 EE+09"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+09/Gain01/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G01 EE+09"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G01 EE+09",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G01 EE+09"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+09/Gain06/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G06 EE+09"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G06 EE+09",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G06 EE+09"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+09/Gain12/00-Pedestal",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality G12 EE+09"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal mean G12 EE+09",
   "EcalEndcap/EEPedestalClient/EEPT pedestal rms G12 EE+09"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+09/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G01 EE+09"],
  ["EcalEndcap/EEPedestalClient/EEPT pedestal quality PNs G16 EE+09"])

eelayout(dqmitems, "03-Pedestal/EE+/EE+09/PNs/00-Pedestal-PNs",
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+09 G01",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+09 G01"],
  ["EcalEndcap/EEPedestalTask/PN/Gain01/EEPDT PNs pedestal EE+09 G16",
   "EcalEndcap/EEPedestalClient/EEPDT PNs rms EE+09 G16"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+09/Gain01/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G01 EE+09"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G01 EE+09",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G01 EE+09"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+09/Gain06/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G06 EE+09"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G06 EE+09",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G06 EE+09"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+09/Gain12/00-TestPulse",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality G12 EE+09"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse amplitude G12 EE+09",
   "EcalEndcap/EETestPulseClient/EETPT test pulse shape G12 EE+09"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+09/PNs/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G01 EE+09"],
  ["EcalEndcap/EETestPulseClient/EETPT test pulse quality PNs G16 EE+09"])

eelayout(dqmitems, "04-TestPulse/EE+/EE+09/PNs/Gain01/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs pedestal EE+09 G01",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+09 G01"],
  ["EcalEndcap/EETestPulseTask/PN/Gain01/EEPDT PNs amplitude EE+09 G01",
   None])

eelayout(dqmitems, "04-TestPulse/EE+/EE+09/PNs/Gain16/00-TestPulse-PNs",
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs pedestal EE+09 G16",
   "EcalEndcap/EETestPulseClient/EEPDT PNs pedestal rms EE+09 G16"],
  ["EcalEndcap/EETestPulseTask/PN/Gain16/EEPDT PNs amplitude EE+09 G16",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+09/00-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 EE+09"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 EE+09"])

eelayout(dqmitems, "05-Laser/EE+/EE+09/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser quality L1 PNs G01 EE+09",
   "EcalEndcap/EELaserClient/EELT laser quality L1 PNs G16 EE+09"],
  ["EcalEndcap/EELaserClient/EELT laser quality L4 PNs G01 EE+09",
   "EcalEndcap/EELaserClient/EELT laser quality L4 PNs G16 EE+09"])

eelayout(dqmitems, "05-Laser/EE+/EE+09/L1/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L1A EE+09",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1A EE+09"],
  ["EcalEndcap/EELaserClient/EELT amplitude L1B EE+09",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L1B EE+09"])

eelayout(dqmitems, "05-Laser/EE+/EE+09/L1/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L1A EE+09",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+09"],
  ["EcalEndcap/EELaserClient/EELT laser timing L1B EE+09",
   "EcalEndcap/EELaserClient/EELT laser shape L1A EE+09"])

eelayout(dqmitems, "05-Laser/EE+/EE+09/L1/02-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs pedestal EE+09 G01 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain01/EEPDT PNs pedestal rms EE+09 G01 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain01/EEPDT PNs amplitude EE+09 G01 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+09/L1/03-Laser",
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs pedestal EE+09 G16 L1",
   "EcalEndcap/EELaserClient/Laser1/PN/Gain16/EEPDT PNs pedestal rms EE+09 G16 L1"],
  ["EcalEndcap/EELaserTask/Laser1/PN/Gain16/EEPDT PNs amplitude EE+09 G16 L1",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+09/L4/00-Laser",
  ["EcalEndcap/EELaserClient/EELT amplitude L4A EE+09",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4A EE+09"],
  ["EcalEndcap/EELaserClient/EELT amplitude L4B EE+09",
   "EcalEndcap/EELaserClient/EELT amplitude over PN L4B EE+09"])

eelayout(dqmitems, "05-Laser/EE+/EE+09/L4/01-Laser",
  ["EcalEndcap/EELaserClient/EELT laser timing L4A EE+09",
   "EcalEndcap/EELaserClient/EELT laser shape L4A EE+09"],
  ["EcalEndcap/EELaserClient/EELT laser timing L4B EE+09",
   "EcalEndcap/EELaserClient/EELT laser shape L4B EE+09"])

eelayout(dqmitems, "05-Laser/EE+/EE+09/L4/02-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs pedestal EE+09 G01 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain01/EEPDT PNs pedestal rms EE+09 G01 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain01/EEPDT PNs amplitude EE+09 G01 L4",
   None])

eelayout(dqmitems, "05-Laser/EE+/EE+09/L4/03-Laser",
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs pedestal EE+09 G16 L4",
   "EcalEndcap/EELaserClient/Laser4/PN/Gain16/EEPDT PNs pedestal rms EE+09 G16 L4"],
  ["EcalEndcap/EELaserTask/Laser4/PN/Gain16/EEPDT PNs amplitude EE+09 G16 L4",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+09/00-Led",
  ["EcalEndcap/EELedClient/EELDT led quality EE+09"])

eelayout(dqmitems, "06-Led/EE+/EE+09/01-Led",
  ["EcalEndcap/EELedClient/EELDT led quality PNs G01 EE+09",
   "EcalEndcap/EELedClient/EELDT led quality PNs G16 EE+09"])

eelayout(dqmitems, "06-Led/EE+/EE+09/L1/00-Led",
  ["EcalEndcap/EELedClient/EELDT amplitude A EE+09",
   "EcalEndcap/EELedClient/EELDT amplitude A over PN EE+09"],
  ["EcalEndcap/EELedClient/EELDT amplitude B EE+09",
   "EcalEndcap/EELedClient/EELDT amplitude B over PN EE+09"])
   
eelayout(dqmitems, "06-Led/EE+/EE+09/L1/01-Led",
  ["EcalEndcap/EELedClient/EELDT led timing A EE+09",
   "EcalEndcap/EELedClient/EELDT les shape A EE+09"],
  ["EcalEndcap/EELedClient/EELDT led timing B EE+09",
   "EcalEndcap/EELedClient/EELDT led shape B EE+09"])
   
eelayout(dqmitems, "06-Led/EE+/EE+09/L1/02-Led",
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs pedestal EE+09 G01",
   "EcalEndcap/EELedClient/PN/Gain01/EEPDT PNs pedestal rms EE+09 G01"],
  ["EcalEndcap/EELedTask/PN/Gain01/EEPDT PNs amplitude EE+09 G01",
   None])

eelayout(dqmitems, "06-Led/EE+/EE+09/L1/03-Led",
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs pedestal EE+09 G16",
   "EcalEndcap/EELedClient/PN/Gain16/EEPDT PNs pedestal rms EE+09 G16"],
  ["EcalEndcap/EELedTask/PN/Gain16/EEPDT PNs amplitude EE+09 G16",
   None])

eelayout(dqmitems, "07-Timing/EE+/EE+09/00-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+09"],
  ["EcalEndcap/EETimingClient/EETMT timing mean EE+09",
   "EcalEndcap/EETimingClient/EETMT timing rms EE+09"])

eelayout(dqmitems, "07-Timing/EE+/EE+09/01-Timing",
  ["EcalEndcap/EETimingClient/EETMT timing quality EE+09"],
  ["EcalEndcap/EETimingClient/EETMT timing EE+09"])

eelayout(dqmitems, "08-Trigger/EE+/EE+09/01-Trigger",
  ["EcalEndcap/EETriggerTowerTask/EETTT EmulError EE+09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Et map Real Digis EE+09"])

eelayout(dqmitems, "08-Trigger/EE+/EE+09/02-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 000 EE+09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 000 EE+09"])

eelayout(dqmitems, "08-Trigger/EE+/EE+09/03-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 001 EE+09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 001 EE+09"])

eelayout(dqmitems, "08-Trigger/EE+/EE+09/04-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 011 EE+09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 011 EE+09"])

eelayout(dqmitems, "08-Trigger/EE+/EE+09/05-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 100 EE+09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 100 EE+09"])

eelayout(dqmitems, "08-Trigger/EE+/EE+09/06-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bit 101 EE+09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bit 101 EE+09"])

eelayout(dqmitems, "08-Trigger/EE+/EE+09/07-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFlagError Bits 110+111 EE+09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT Flags Real Digis Bits 110+111 EE+09"])

eelayout(dqmitems, "08-Trigger/EE+/EE+09/08-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 0 EE+09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 0 EE+09"])

eelayout(dqmitems, "08-Trigger/EE+/EE+09/09-Trigger",
  ["EcalEndcap/EETriggerTowerClient/EETTT EmulFineGrainVetoError Flag 1 EE+09"],
  ["EcalEndcap/EETriggerTowerClient/EETTT FineGrainVeto Real Digis Flag 1 EE+09"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+09/00-Cosmic",
  ["EcalEndcap/EECosmicTask/Sel/EECT energy sel EE+09"],
  ["EcalEndcap/EBCosmicTask/Cut/EECT energy cut EE+09"])

eelayout(dqmitems, "09-Cosmic/EE+/EE+09/01-Cosmic",
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 1x1 energy spectrum EE+09"],
  ["EcalEndcap/EECosmicTask/Spectrum/EECT 3x3 energy spectrum EE+09"])

eelayout(dqmitems, "10-StatusFlags/EE+/EE+09/00-StatusFlags",
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status EE+09"],
  ["EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT front-end status bits EE+09"])

eelayout(dqmitems, "11-Cluster/00-Cluster",
  ["EcalEndcap/EEClusterTask/EECLT BC energy",
   "EcalEndcap/EEClusterTask/EECLT BC size"],
  ["EcalEndcap/EEClusterTask/EECLT BC number",
   None])

eelayout(dqmitems, "11-Cluster/01-Cluster",
  ["EcalEndcap/EEClusterTask/EECLT BC energy map EE -"],
  ["EcalEndcap/EEClusterTask/EECLT BC energy projection R EE -",
   "EcalEndcap/EEClusterTask/EECLT BC energy projection phi EE -"])

eelayout(dqmitems, "11-Cluster/02-Cluster",
  ["EcalEndcap/EEClusterTask/EECLT BC energy map EE +"],
  ["EcalEndcap/EEClusterTask/EECLT BC energy projection R EE +",
   "EcalEndcap/EEClusterTask/EECLT BC energy projection phi EE +"])

eelayout(dqmitems, "11-Cluster/03-Cluster",
  ["EcalEndcap/EEClusterTask/EECLT BC size map EE -"],
  ["EcalEndcap/EEClusterTask/EECLT BC size projection R EE -",
   "EcalEndcap/EEClusterTask/EECLT BC size projection phi EE -"])

eelayout(dqmitems, "11-Cluster/04-Cluster",
  ["EcalEndcap/EEClusterTask/EECLT BC size map EE +"],
  ["EcalEndcap/EEClusterTask/EECLT BC size projection R EE +",
   "EcalEndcap/EEClusterTask/EECLT BC size projection phi EE +"])

eelayout(dqmitems, "11-Cluster/05-Cluster",
  ["EcalEndcap/EEClusterTask/EECLT BC ET map EE -"],
  ["EcalEndcap/EEClusterTask/EECLT BC ET projection R EE -",
   "EcalEndcap/EEClusterTask/EECLT BC ET projection phi EE -"])

eelayout(dqmitems, "11-Cluster/06-Cluster",
  ["EcalEndcap/EEClusterTask/EECLT BC ET map EE +"],
  ["EcalEndcap/EEClusterTask/EECLT BC ET projection R EE +",
   "EcalEndcap/EEClusterTask/EECLT BC ET projection phi EE +"])

eelayout(dqmitems, "11-Cluster/07-Cluster",
  ["EcalEndcap/EEClusterTask/EECLT BC number map EE -"],
  ["EcalEndcap/EEClusterTask/EECLT BC number projection R EE -",
   "EcalEndcap/EEClusterTask/EECLT BC number projection phi EE -"])

eelayout(dqmitems, "11-Cluster/08-Cluster",
  ["EcalEndcap/EEClusterTask/EECLT BC number map EE +"],
  ["EcalEndcap/EEClusterTask/EECLT BC number projection R EE +",
   "EcalEndcap/EEClusterTask/EECLT BC number projection phi EE +"])

eelayout(dqmitems, "11-Cluster/09-Cluster",
  ["EcalEndcap/EEClusterTask/EECLT SC energy",
   "EcalEndcap/EEClusterTask/EECLT SC size"],
  ["EcalEndcap/EEClusterTask/EECLT SC number",
   None])

eelayout(dqmitems, "11-Cluster/10-Cluster",
  ["EcalEndcap/EEClusterTask/EECLT s1s9",
   "EcalEndcap/EEClusterTask/EECLT s9s25"],
  ["EcalEndcap/EEClusterTask/EECLT dicluster invariant mass",
   None])

eelayout(dqmitems, "12-Occupancy/00-Occupancy",
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE - projection R",
   "EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE - projection phi"])

eelayout(dqmitems, "12-Occupancy/01-Occupancy",
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +"],
  ["EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE + projection R",
   "EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE + projection phi"])

eelayout(dqmitems, "12-Occupancy/02-Occupancy",
  ["EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE -"],
  ["EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE - projection R",
   "EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE - projection phi"])

eelayout(dqmitems, "12-Occupancy/03-Occupancy",
  ["EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE +"],
  ["EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE + projection R",
   "EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE + projection phi"])

eelayout(dqmitems, "12-Occupancy/04-Occupancy",
  ["EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE -"],
  ["EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE - projection R",
   "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE - projection phi"])

eelayout(dqmitems, "12-Occupancy/05-Occupancy",
  ["EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE +"],
  ["EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE + projection R",
   "EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE + projection phi"])

eelayout(dqmitems, "12-Occupancy/06-Occupancy",
  ["EcalEndcap/EEOccupancyTask/EEOT TP digi occupancy EE -"],
  ["EcalEndcap/EEOccupancyTask/EEOT TP digi occupancy EE - projection R",
   "EcalEndcap/EEOccupancyTask/EEOT TP digi occupancy EE - projection phi"])

eelayout(dqmitems, "12-Occupancy/07-Occupancy",
  ["EcalEndcap/EEOccupancyTask/EEOT TP digi occupancy EE +"],
  ["EcalEndcap/EEOccupancyTask/EEOT TP digi occupancy EE + projection R",
   "EcalEndcap/EEOccupancyTask/EEOT TP digi occupancy EE + projection phi"])

eelayout(dqmitems, "12-Occupancy/08-Occupancy",
  ["EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE -"],
  ["EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE - projection R",
   "EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE - projection phi"])

eelayout(dqmitems, "12-Occupancy/09-Occupancy",
  ["EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE +"],
  ["EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE + projection R",
   "EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE + projection phi"])

