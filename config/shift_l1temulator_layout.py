def l1temulayout(i, p, *rows): i["00 Shift/L1TEMU/" + p] = DQMItem(layout=rows)

l1temulayout(dqmitems,"00-Global Summary",
             [{'path': "L1TEMU/common/sysrates", 'description': "Data|Emulator disagreement rates per subsystem. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
              {'path': "L1TEMU/common/errorflag", 'description': "Data|Emulator overall disagreement flags. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
              {'path': "L1TEMU/common/sysncandData", 'description': "Number of trigger objects per subsystem observed in data. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
              {'path': "L1TEMU/common/sysncandEmul", 'description': "Number of trigger objects per subsystem expected by emulator. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

l1temulayout(dqmitems,"01-(Dis)Agreement Flag",
             [{'path': "L1TEMU/ECAL/ErrorFlag", 'description': "Data|Emulator disagreement type for ECAL trigger primitives. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
              {'path': "L1TEMU/HCAL/ErrorFlag", 'description': "Data|Emulator disagreement type for HCAL trigger primitives. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
              {'path': "L1TEMU/RCT/ErrorFlag", 'description': "Data|Emulator disagreement type for RCT. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
              {'path': "L1TEMU/GCT/ErrorFlag", 'description': "Data|Emulator disagreement type for GCT. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
              {'path': "L1TEMU/DTTPG/ErrorFlag", 'description': "Data|Emulator disagreement type for DT trigger primitives. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
              {'path': "L1TEMU/DTTF/ErrorFlag", 'description': "Data|Emulator disagreement type for DT track finder. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
              {'path': "L1TEMU/CSCTPG/ErrorFlag", 'description': "Data|Emulator disagreement type for CSC trigger primitives. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
              {'path': "L1TEMU/CSCTF/ErrorFlag", 'description': "Data|Emulator disagreement type for CSC track finder. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
              {'path': "L1TEMU/RPC/ErrorFlag", 'description': "Data|Emulator disagreement type for RPC. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
              {'path': "L1TEMU/GMT/ErrorFlag", 'description': "Data|Emulator disagreement type for GMT. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
              {'path': "L1TEMU/GT/ErrorFlag", 'description': "Data|Emulator disagreement type for GT. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

