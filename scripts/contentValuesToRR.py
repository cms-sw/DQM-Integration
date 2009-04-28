#!/usr/bin/env python

import sys, os, optparse, re
import ROOT, xmlrpclib
 
FOLDERS     = { 
  'reportSummaryContents': 'DQM', 
  'CertificationContents': 'Cert', 
  'DAQContents': 'DAQ', 
  'DCSContents': 'DCS' 
}
SERVER_URL = "http://cmswbm.cms/runregistry/xmlrpc"
SUBSYSTEMS  = {
  'CSC' :        'CSC',
  'DT' :         'DT',
  'EcalBarrel' : 'ECAL',
  'EcalEndcap' : 'ECAL',
  'Hcal' :       'HCAL',
  'L1T' :        'TRG',
  'L1TEMU' :     'TRG',
  'Pixel' :      'PIX',
  'RPC' :        'RPC',
  'SiStrip' :    'STRIP'
}

class OptionParser(optparse.OptionParser):
  """ Option parser class """
  def __init__(self):
    optparse.OptionParser.__init__(self, usage="%prog [options] root_file ...", version="%prog 0.0.1", conflict_handler="resolve")
    self.add_option("--shift", "-s", action="store", type="choice", dest="shift", choices=("online","offline"), help="specify shift type: online or offline values allowed")
    self.add_option("--url", action="store", type="string", dest="url", default=SERVER_URL, help="specify RR XML-RPC server URL. Default is " + SERVER_URL)
    self.add_option("--debug", "-d", action="store_true", dest="debug", default=False, help="print values and exit. Do not write to RR")

def getSummaryValues(file_name, shift_type):
  """ Method to extract keys from root file and return dict """
  ROOT.gROOT.Reset()

  result = {}

  f = ROOT.TFile(file_name, 'READ')

  root = f.GetDirectory("DQMData")
  if root == None: return result
  
  run = None
  for key in root.GetListOfKeys():
    if re.match("^Run [0-9]+$", key.ReadObj().GetName()) and key.IsFolder():
      result['run'] = int(re.sub("^Run ", "", key.ReadObj().GetName()))
      run = key.ReadObj()
      break

  if run == None: return result

  result['subs'] = {}

  for sub in run.GetListOfKeys():

    sub_name = sub.ReadObj().GetName()
    if not SUBSYSTEMS.has_key(sub_name): continue

    sub_key = SUBSYSTEMS[sub_name]

    if not result['subs'].has_key(sub_key):
      result['subs'][sub_key] = {}

    evInfo = sub.ReadObj().GetDirectory("Run summary/EventInfo")
    if evInfo == None: continue

    for folder_name in FOLDERS.keys():

      folder = evInfo.GetDirectory(folder_name)
      if folder == None: continue
      
      folder_id = FOLDERS[folder_name]
      if folder_id == 'DQM':
        folder_id = 'DQM ' + shift_type.upper()

      result['subs'][sub_key][folder_id] = {}

      for value in folder.GetListOfKeys():
        full_name = value.ReadObj().GetName()
        if not value.IsFolder() and re.match("^<.+>f=-{,1}[0-9\.]+</.+>$", full_name):
          value_name = re.sub("<(?P<n>[^>]+)>.+", "\g<n>", full_name)
          value_numb = float(re.sub("<.+>f=(?P<n>-{,1}[0-9\.]+)</.+>", "\g<n>", full_name))
          result['subs'][sub_key][folder_id][value_name] = value_numb

  f.Close()

  return result

def dict2json(d):
  """ Convert dictionary (embedded) to json string """
  s = '{'
  i = 0
  for k in d.keys():
    i = i + 1
    s = s + '"%s"=' % re.sub('"', '\\"', k)
    if type(d[k]) == type({}):
      s = s + dict2json(d[k])
    elif type(d[k]) == type(1.0) or type(d[k]) == type(1):
      s = s + str(d[k])
    else:
      s = s + '"%s"' % re.sub('"', '\\"', d[k])
    if i < len(d): s = s + ','  

  s = s + '}'
  return s

if __name__ == "__main__":
  
  # Create option parser and get options/arguments
  optManager  = OptionParser()
  (opts, args) = optManager.parse_args()
  opts = opts.__dict__

  # Check if at least one root file defined (can be many!)
  if len(args) == 0:
    print "At least one ROOT file must be priovided, use --help for hit"
    sys.exit(1)

  # Check if shift type is provided (mandatory!)
  if not opts['shift']:
    print "Shift type must be provided, use --help for hit"
    sys.exit(1)

  # Check if all files exists and are accessible
  for rfile in args:
    try:
      os.stat(rfile)
    except:
      print "File [", rfile, "] not exists or is not accessible?"
      sys.exit(2)

  server = xmlrpclib.ServerProxy(opts['url'])

  # Lets extract values from files one-by-one, construct hashmap and submit to
  # defined XML-RPC url 
  for rfile in args:

    values = getSummaryValues(file_name = rfile, shift_type = opts['shift'])

    try:
      json = dict2json(values)
      if opts['debug']:
        print json
      else:
        result = server.SummaryValuesWriter.write(json)
        print "RR: %d rows modified for file %s" % (result, rfile)
    except xmlrpclib.Error, errstring:
      print "ERROR", errstring
      sys.exit(3)
  
  sys.exit(0)


