import os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

modules = ("GuiDQM",)
envsetup = """
  export YUI_ROOT=/data/sw/$SCRAM_ARCH/external/yui/2.4.1
  export QUIET_ASSERT=a
"""

server.port        = 8040
server.serverDir   = '/data/dqm/caf/gui'
server.baseUrl     = '/dqm/caf'
server.title       = 'CMS data quality'
server.serviceName = 'CERN CAF'

server.source('DQMArchive', 'file', '/data/dqm/caf/dqm.db', '--listen 8041')
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/caf/upload')

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-caf.py")
