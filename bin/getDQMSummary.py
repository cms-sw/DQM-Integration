#!/usr/bin/env python
import os, sys, re
from ROOT import *

# DQM Report Summary Parser ---- Yuri Gotra May-30-2008
# getDQMSummary.py ~/3d/DQM_R000043434.root



usage = "usage: %s <DQM_File.root>" %         os.path.basename(sys.argv[0])

if len(sys.argv) < 2:
   print usage
   sys.exit(2)
else:
   argv = sys.argv
   infile = argv[1]
   outfile = argv[2]
   print argv[1]
   f = TFile(infile, 'read')
   ff = open(outfile,'w')


Detectors = ['Pixel', 'SiStrip', 'EcalBarrel', 'Hcal', 'DT', 'RPC', 'CSC', 'L1TEMU', 'L1T']

reportSummary = "<reportSummary>"
DQMDataDir = "DQMData"
EventInfoDir = "/Run summary/EventInfo"
ReportSummaryContentsDir = "/Run summary/EventInfo/reportSummaryContents"
summary = std.vector(float)()
reportSummaryContents = std.vector(string)()
f.cd(DQMDataDir)
dirtmp = gDirectory
dirlist = dirtmp.GetListOfKeys()
iter = dirlist.MakeIterator()
key = iter.Next()
td = None

while key:
   td = key.ReadObj()
   dirName = td.GetName()
   if(re.search('Run (\d+)', dirName)):
       rundirname = dirName
       break
   key = iter.Next()

def getDQMDetSummaryResult():
   reportSummaryDir = DQMDataDir + '/' + rundirname + '/' + subdet + EventInfoDir
   f.cd(reportSummaryDir)
   reportSummaryDir = gDirectory
   dirlist = reportSummaryDir.GetListOfKeys()
   iter = dirlist.MakeIterator()
   key = iter.Next()
   tk = None
   while key:
       tk = key.ReadObj()
       keyName = tk.GetName()
       if(re.search(reportSummary, keyName)):
           ms = re.split('=', keyName)
           m = re.search('-?\d?\.?\d+', ms[1])
           detsummary = m.group(0)
           break
       key = iter.Next()
   return detsummary

def getDQMSegSummaryResult():
   SummaryContentsDir = DQMDataDir + '/' + rundirname + '/' + subdet + ReportSummaryContentsDir
   f.cd(SummaryContentsDir)
   SummaryContentsDir = gDirectory
   dirlist = SummaryContentsDir.GetListOfKeys()
   iter = dirlist.MakeIterator()
   key = iter.Next()
   tk = None
   while key:
       tk = key.ReadObj()
       keyName = tk.GetName()
       mn = re.search('(<.+?>)', keyName)
       if(mn):
           reportSummaryContent = mn.group(0)
           ms = re.split('=', keyName)
           m = re.search('-?\d?\.?\d+', ms[1])
           segsummary = m.group(0)
           summary.push_back(float(segsummary))
           reportSummaryContents.push_back(reportSummaryContent)
       key = iter.Next()
   return reportSummaryContents, summary

for subdet in Detectors:
   print >>ff, '============================'
   print >>ff, rundirname, subdet
   getDQMSegSummaryResult()
   summary.push_back(float(getDQMDetSummaryResult()))
   reportSummaryContents.push_back(reportSummary)
   j = 0
   for i in summary:
       print >> ff, reportSummaryContents[j], int(1000*i)
       j = j + 1
   summary.clear()
   reportSummaryContents.clear()
print >> ff, '============================' 
