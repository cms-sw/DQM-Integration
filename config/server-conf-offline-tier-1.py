import os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

modules = ("GuiDQM",)
envsetup = """
  export YUI_ROOT=/data/sw/$SCRAM_ARCH/external/yui/2.4.1
  export QUIET_ASSERT=a
"""

LAYOUTS = ["%s/shift_%s_T0_layout.py" % (CONFIGDIR, x) for x in ("eb", "ee", "csc", "rpc", "hcal", "l1t", "l1temulator", "hlt", "pixel", "sistrip", "dt", "muons", "jetmet", "egamma")]

server.port        = 8070
server.serverDir   = '/data/dqm/tier-1/gui'
server.baseUrl     = '/dqm/tier-1'
server.title       = 'CMS data quality'
server.serviceName = 'Tier-1'

server.source('DQMArchive', 'file', '/data/dqm/tier-1/dqm.db', '--listen 8071')
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/tier-1/upload')
server.source('DQMLayout', 'layouts', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-tier-0.py")
