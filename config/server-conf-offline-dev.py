import os.path
global CONFIGDIR
BASEDIR   = os.path.dirname(os.path.dirname(__file__))
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

LAYOUTS = ["%s/shift_%s_T0_layout.py" % (CONFIGDIR, x) for x in
           ("castor","eb", "ee", "csc", "rpc", "hcal", "l1t", "l1temulator", "hlt", "pixel", "sistrip", "dt", "muons", "jetmet", "egamma")]
LAYOUTS += ["%s/%s_T0_layouts.py" % (CONFIGDIR, x) for x in
           ("castor","pixel","sistrip","hcal", "eb", "ee", "hltmuon")]
LAYOUTS += [CONFIGDIR + "/shift_hlt_relval_layout.py"]
LAYOUTS += [CONFIGDIR + "/hlt_relval-layouts.py"]

modules = ("GuiDQM",)
envsetup = "export QUIET_ASSERT=a"

server.port        = 8060
server.serverDir   = '/data/dqm/dev/gui'
server.baseUrl     = '/dqm/dev'
server.title       = 'CMS data quality'
server.serviceName = 'CERN Development'

server.plugin('render', BASEDIR + "/style/*.cc")
server.source('DQMUnknown', 'unknown', 8063)
              
server.source('DQMLive', 'dqm', 'localhost:8061', '--listen 8063',
	       '--load ' + server.pathOfPlugin('render'))
	      
server.source('DQMArchive', 'file',
              '/data/dqm/dev/idx', '^/Global/', '--listen 8063',
              '--load ' + server.pathOfPlugin('render'))              

server.extend('DQMFileAccess', '/dev/null', '/data/dqm/dev/upload',
              { 'Development': '/data/dqm/dev/data'})

server.source('DQMLayout', 'layouts', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-dev.py")
