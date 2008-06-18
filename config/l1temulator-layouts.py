def l1temulayout(i, p, *rows): i["L1TEMU/Layouts/" + p] = DQMItem(layout=rows)

def l1temucommon(i, dir, name):i["L1TEMU/Layouts/00-Global-Summary/%s" % name] = \
    DQMItem(layout=[["L1TEMU/%s/%s" % (dir, name)]]) 

l1temucommon(dqmitems, "common", "sysrates")
l1temucommon(dqmitems, "common", "errorflag")
l1temucommon(dqmitems, "common", "sysncandData")
l1temucommon(dqmitems, "common", "sysncandEmul")
