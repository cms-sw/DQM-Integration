import os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

modules = ("GuiDQM",)
envsetup = "export QUIET_ASSERT=a"

server.port        = 8060
server.serverDir   = '/data/dqm/dev/gui'
server.baseUrl     = '/dqm/dev'
server.title       = 'CMS data quality'
server.serviceName = 'CERN Development'

server.source('DQMLive', 'live', '--collector localhost:8061', '--listen 8062')
server.source('DQMArchive', 'file', '/data/dqm/dev/dqm.db', '--listen 8063')
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/dev/upload')

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-dev.py")
