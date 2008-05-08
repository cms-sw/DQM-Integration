def hcallayout(i, p, *rows): i["Hcal/Layouts/" + p] = DQMItem(layout=rows)

hcallayout(dqmitems, "HCAL Data Format Summary",
           [{ 'path': "Hcal/DataFormatMonitor/HTR Error Word by Crate",
                   'description': 'Ignore only OpDat Err, Clock Err, Link Err, CapID Err, and FE Format Err' },
            "Hcal/DataFormatMonitor/Invalid HTR Data"],
           ["Hcal/DataFormatMonitor/Ev Frag Size 2d",
            "Hcal/DataFormatMonitor/EvN Inconsistent - HTR vs Ref HTR"],
           ["Hcal/DataFormatMonitor/Common Data Format violations",
            "Hcal/DataFormatMonitor/DCC Event Format violation",
            "Hcal/DataFormatMonitor/DCC Error and Warning",
            "Hcal/DataFormatMonitor/DCC Nonzero Spigot Conditions"]
           )
