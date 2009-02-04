import os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
LAYOUTS = ["%s/%s-layouts.py" % (CONFIGDIR, x) for x in
	  ("csc", "dt", "eb", "hcal", "hlt", "l1t", "l1temulator", "rpc", "pixel", "sistrip")]
LAYOUTS += ["%s/shift_%s_layout.py" % (CONFIGDIR, x) for x in
          ("csc", "dt", "eb", "hcal", "hlt", "l1t", "l1temulator", "rpc", "pixel", "sistrip")]

modules = ("GuiDQM", "GuiEventDisplay")
envsetup = "export QUIET_ASSERT=a"

server.serverDir   = '/home/dqm/gui'
server.baseUrl     = '/dqm/gui-test'
server.title       = 'CMS data quality'
server.serviceName = 'GUI test'

server.extend('EVDSnapshotUpload', '/home/dqm/iguana-snapshots')
server.source('EVDSnapshot', 'evd', '/home/dqm/iguana-snapshots')
server.source('DQMUnknown', 'unknown', 'DQMArchive', 9097)
server.source('DQMLive', 'dqm', '--listen 9091', '--collector srv-c2d05-18:9090')
server.source('DQMArchive', 'file', '/home/dqm/dqm.db', '--listen 9097')
server.source('DQMLayout', 'layouts', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-online.py")
