import os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

modules = ("GuiDQM",)
envsetup = """
  export YUI_ROOT=/data/sw/$SCRAM_ARCH/external/yui/2.4.1
  export QUIET_ASSERT=a
"""

LAYOUTS = ["%s/shift_%s_T0_layout.py" % (CONFIGDIR, x) for x in ("eb", "ee", "sistrip")]

server.port        = 8030
server.serverDir   = '/data/dqm/tier-0/gui'
server.baseUrl     = '/dqm/tier-0'
server.title       = 'CMS data quality'
server.serviceName = 'CERN Tier-0'

server.source('DQMArchive', 'file', '/data/dqm/tier-0/dqm.db', '--listen 8031')
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/tier-0/upload')
server.source('DQMLayout', 'layouts', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-tier-0.py")
