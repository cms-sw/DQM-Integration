def l1tlayout(i, p, *rows): i["Layouts/L1TEMU Layouts/" + p] = DQMItem(layout=rows)

l1tlayout(dqmitems, "Summary/Data Emulator comparison",
  ["L1TEMU/errorflag",
   "L1TEMU/sysrates",
   "L1TEMU/sysncandData",
   "L1TEMU/sysncandEmul"])
