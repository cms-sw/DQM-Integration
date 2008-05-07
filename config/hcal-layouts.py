def hcallayout(i, p, *rows): i["Hcal/Layouts/" + p] = DQMItem(layout=rows)

hcallayout(dqmitems, "HCAL Data Format Summary",
           [{ 'path': "Hcal/DataFormatMonitor/HTR Error Word by Crate",
                   'description': 'Ignore only OpDat Err, Clock Err, Link Err, CapID Err, and FE Format Err' },
            "Hcal/DataFormatMonitor/Invalid HTR Data",
            "Hcal/DigiMonitor/Bad Digi Fraction"],
           ["Hcal/DataFormatMonitor/Event Fragment Size for each FED",
            "Hcal/DataFormatMonitor/EvN Inconsistent - HTR vs Ref HTR"],
           ["Hcal/DataFormatMonitor/Common Data Format violations",
            "Hcal/DataFormatMonitor/DCC Event Format violation",
            "Hcal/DataFormatMonitor/DCC Error and Warning",
            "Hcal/DataFormatMonitor/DCC Nonzero Spigot Conditions"]
           )

hcallayout(dqmitems, "HCAL Digitization Summary",
           ["Hcal/DigiMonitor/Digi Depth 1 Occupancy Map",
            "Hcal/DigiMonitor/Digi Depth 2 Occupancy Map",
            "Hcal/DigiMonitor/Digi Depth 3 Occupancy Map",
            "Hcal/DigiMonitor/Digi Depth 4 Occupancy Map"],
           ["Hcal/DigiMonitor/HB/HB # of Digis",
            "Hcal/DigiMonitor/HE/HE # of Digis",
            "Hcal/DigiMonitor/HF/HF # of Digis",
            "Hcal/DigiMonitor/HO/HO # of Digis"],
           ["Hcal/DigiMonitor/HB/HB Digi Shape - over thresh",
            "Hcal/DigiMonitor/HE/HE Digi Shape - over thresh",
            "Hcal/DigiMonitor/HF/HF Digi Shape - over thresh",
            "Hcal/DigiMonitor/HO/HO Digi Shape - over thresh"]
           )

hcallayout(dqmitems, "HCAL Reconstruction Summary",
           ["Hcal/RecHitMonitor/RecHit Total Energy"],
           ["Hcal/RecHitMonitor/HB/HB RecHit Energies",
            "Hcal/RecHitMonitor/HE/HE RecHit Energies",
            "Hcal/RecHitMonitor/HF/HF Short RecHit Energies",
            "Hcal/RecHitMonitor/HF/HF Long RecHit Energies",
            "Hcal/RecHitMonitor/HO/HO RecHit Energies"],
           ["Hcal/RecHitMonitor/HB/HB RecHit Times",
            "Hcal/RecHitMonitor/HE/HE RecHit Times",
            "Hcal/RecHitMonitor/HF/HF Short RecHit Times",
            "Hcal/RecHitMonitor/HF/HF Long RecHit Times",
            "Hcal/RecHitMonitor/HO/HO RecHit Times"]
           )

hcallayout(dqmitems, "HCAL Reconstruction Threshold Summary",
           ["Hcal/RecHitMonitor/RecHit Total Energy - Threshold"],
           ["Hcal/RecHitMonitor/HB/HB RecHit Total Energy - Threshold",
            "Hcal/RecHitMonitor/HE/HE RecHit Total Energy - Threshold",
            "Hcal/RecHitMonitor/HF/HF RecHit Total Energy - Threshold",
            "Hcal/RecHitMonitor/HO/HO RecHit Total Energy - Threshold"],
           ["Hcal/RecHitMonitor/HB/HB RecHit Times - Threshold",
            "Hcal/RecHitMonitor/HE/HE RecHit Times - Threshold",
            "Hcal/RecHitMonitor/HF/HF RecHit Times - Threshold",
            "Hcal/RecHitMonitor/HO/HO RecHit Times - Threshold"]
           )

hcallayout(dqmitems, "HCAL Hot Cell Summary",
           ["Hcal/HotCellMonitor/HCAL/HCALEnergy"],
           ["Hcal/HotCellMonitor/HB/HBHotCellOccMapThresh0",
            "Hcal/HotCellMonitor/HE/HEHotCellOccMapThresh0",
            "Hcal/HotCellMonitor/HF/HFHotCellOccMapThresh0",
            "Hcal/HotCellMonitor/HO/HOHotCellOccMapThresh0"]
           )

hcallayout(dqmitems, "HCAL Hot Cell NADA Summary",
           ["Hcal/HotCellMonitor/HCAL/HCALnadaNumHotCells",
            "Hcal/HotCellMonitor/HCAL/HCALnadaNumNegCells"],
           ["Hcal/HotCellMonitor/HB/HBnadaOccMap",
            "Hcal/HotCellMonitor/HE/HEnadaOccMap",
            "Hcal/HotCellMonitor/HF/HFnadaOccMap",
            "Hcal/HotCellMonitor/HO/HOnadaOccMap"]
           )

hcallayout(dqmitems, "HCAL Dead Cell Summary",
           ["Hcal/DeadCellMonitor/HB/HB_deadADCOccupancyMap",
            "Hcal/DeadCellMonitor/HE/HE_deadADCOccupancyMap",
            "Hcal/DeadCellMonitor/HF/HF_deadADCOccupancyMap",
            "Hcal/DeadCellMonitor/HO/HO_deadADCOccupancyMap"],
           ["Hcal/DeadCellMonitor/HB/HB_CoolCell_belowPed",
            "Hcal/DeadCellMonitor/HE/HE_CoolCell_belowPed",
            "Hcal/DeadCellMonitor/HF/HF_CoolCell_belowPed",
            "Hcal/DeadCellMonitor/HO/HO_CoolCell_belowPed"],
           ["Hcal/DeadCellMonitor/HB/HB_NADA_CoolCellMap",
            "Hcal/DeadCellMonitor/HE/HE_NADA_CoolCellMap",
            "Hcal/DeadCellMonitor/HF/HF_NADA_CoolCellMap",
            "Hcal/DeadCellMonitor/HO/HO_NADA_CoolCellMap"]
           )

hcallayout(dqmitems, "HCAL Barrel Summary",
           ["Hcal/DigiMonitor/HB/HB # of Digis",
            "Hcal/DigiMonitor/HB/HB QIE ADC Value"],
           ["Hcal/RecHitMonitor/HB/HB RecHit Energies",
            "Hcal/RecHitMonitor/HB/HB RecHit Times",
            "Hcal/RecHitMonitor/HB/HB RecHit Total Energy - Threshold",
            "Hcal/RecHitMonitor/HB/HB RecHit Times - Threshold"],
           ["Hcal/HotCellMonitor/HB/HBHotCellOccMapThresh0",
            "Hcal/HotCellMonitor/HB/HBnadaOccMap"],
           ["Hcal/DeadCellMonitor/HB/HB_deadADCOccupancyMap",
            "Hcal/DeadCellMonitor/HB/HB_CoolCell_belowPed",
            "Hcal/DeadCellMonitor/HB/HB_NADA_CoolCellMap"],
)

hcallayout(dqmitems, "HCAL Endcap Summary",
           ["Hcal/DigiMonitor/HE/HE # of Digis",
            "Hcal/DigiMonitor/HE/HE QIE ADC Value"],
           ["Hcal/RecHitMonitor/HE/HE RecHit Energies",
            "Hcal/RecHitMonitor/HE/HE RecHit Times",
            "Hcal/RecHitMonitor/HE/HE RecHit Total Energy - Threshold",
            "Hcal/RecHitMonitor/HE/HE RecHit Times - Threshold"],
           ["Hcal/HotCellMonitor/HE/HEHotCellOccMapThresh0",
            "Hcal/HotCellMonitor/HE/HEnadaOccMap"],
           ["Hcal/DeadCellMonitor/HE/HE_deadADCOccupancyMap",
            "Hcal/DeadCellMonitor/HE/HE_CoolCell_belowPed",
            "Hcal/DeadCellMonitor/HE/HE_NADA_CoolCellMap"],
)

hcallayout(dqmitems, "HCAL Forward Summary",
           ["Hcal/DigiMonitor/HF/HF # of Digis",
            "Hcal/DigiMonitor/HF/HF QIE ADC Value"],
           ["Hcal/RecHitMonitor/HF/HF Short RecHit Energies",
            "Hcal/RecHitMonitor/HF/HF Long RecHit Energies",
            "Hcal/RecHitMonitor/HF/HF RecHit Times",
            "Hcal/RecHitMonitor/HF/HF RecHit Total Energy - Threshold",
            "Hcal/RecHitMonitor/HF/HF RecHit Times - Threshold"],
           ["Hcal/HotCellMonitor/HF/HFHotCellOccMapThresh0",
            "Hcal/HotCellMonitor/HF/HFnadaOccMap"],
           ["Hcal/DeadCellMonitor/HF/HF_deadADCOccupancyMap",
            "Hcal/DeadCellMonitor/HF/HF_CoolCell_belowPed",
            "Hcal/DeadCellMonitor/HF/HF_NADA_CoolCellMap"],
)

hcallayout(dqmitems, "HCAL Outer Summary",
           ["Hcal/DigiMonitor/HO/HO # of Digis",
            "Hcal/DigiMonitor/HO/HO QIE ADC Value"],
           ["Hcal/RecHitMonitor/HO/HO RecHit Energies",
            "Hcal/RecHitMonitor/HO/HO RecHit Times",
            "Hcal/RecHitMonitor/HO/HO RecHit Total Energy - Threshold",
            "Hcal/RecHitMonitor/HO/HO RecHit Times - Threshold"],
           ["Hcal/HotCellMonitor/HO/HOHotCellOccMapThresh0",
            "Hcal/HotCellMonitor/HO/HOnadaOccMap"],
           ["Hcal/DeadCellMonitor/HO/HO_deadADCOccupancyMap",
            "Hcal/DeadCellMonitor/HO/HO_CoolCell_belowPed",
            "Hcal/DeadCellMonitor/HO/HO_NADA_CoolCellMap"],
)

