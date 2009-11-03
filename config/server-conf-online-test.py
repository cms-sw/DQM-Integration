import os.path
global CONFIGDIR
BASEDIR   = os.path.dirname(os.path.dirname(__file__))
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

LAYOUTS = ["%s/%s-layouts.py" % (CONFIGDIR, x) for x in
	   ("castor","csc", "dt", "eb", "ee", "hcal", "hlt", "hlx", "l1t", "l1temulator", "rpc", "pixel", "sistrip")]
LAYOUTS += ["%s/shift_%s_layout.py" % (CONFIGDIR, x) for x in
            ("castor","csc", "dt", "eb", "ee", "hcal", "hlt", "hlx", "l1t", "l1temulator", "rpc", "pixel", "sistrip" , "fed" )]

modules = ("GuiDQM",)
envsetup = "export QUIET_ASSERT=a"

server.serverDir   = '/home/dqm/gui'
server.baseUrl     = '/dqm/online-test'
server.title       = 'CMS data quality'
server.serviceName = 'Online test'

server.plugin('render', BASEDIR + "/style/*.cc")
server.extend('DQMFileAccess', None, None,
              { "dqm": "/dqmdata/dqm/done",
                "ispy": "/dqmdata/EventDisplay/done" })
server.extend('DQMRenderLink', server.pathOfPlugin('render'))
server.source('DQMUnknown', 'unknown')
server.source('DQMOverlay', 'overlay')
server.source('DQMStripChart', 'stripchart')
server.source('DQMLive', 'dqm', 'localhost:9090')
server.source('DQMArchive', 'file', '/home/dqm/ix', '^/Global/')
server.source('DQMLayout', 'layouts', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-online.py")
