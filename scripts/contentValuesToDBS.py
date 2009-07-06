#!/usr/bin/env python

from contentValuesLib import *

SERVER_URL = "http://cmswbm.cms/runregistry/xmlrpc"

class OptionParser(optparse.OptionParser):
  """ Option parser class """
  def __init__(self):
    optparse.OptionParser.__init__(self, usage="%prog [options] root_file ...", version="%prog 0.0.1", conflict_handler="resolve")
    self.add_option("--url", action="store", type="string", dest="url", default=SERVER_URL, help="specify DBS DQM XML-RPC server URL. Default is " + SERVER_URL)
    self.add_option("--debug", "-d", action="store_true", dest="debug", default=False, help="print values and exit. Do not write to DBS")

if __name__ == "__main__":
  
  # Create option parser and get options/arguments
  optManager  = OptionParser()
  (opts, args) = optManager.parse_args()
  opts = opts.__dict__

  # Check if at least one root file defined (can be many!)
  if len(args) == 0:
    print "At least one ROOT file must be priovided, use --help for hit"
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

    values = getSummaryValues(file_name = rfile, shift_type = None)

    try:
      if opts['debug']:
        print values
      else:
        result = server.insertdq_auto(values)
        print "DBS DQM: %d rows modified for file %s" % (result, rfile)
    except xmlrpclib.Error, errstring:
      print "ERROR", errstring
      sys.exit(3)
  
  sys.exit(0)


