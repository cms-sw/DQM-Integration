import os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

modules = ("GuiDQM",)
envsetup = """
 source /data/sw/cmsset_default.sh
 source /data/sw/slc4_ia32_gcc345/cms/webtools/1.3.0/etc/profile.d/dependencies-setup.sh
 export QUIET_ASSERT=a
"""

server.port        = 8050
server.serverDir   = '/data/dqm/relval/gui'
server.baseUrl     = '/dqm/relval'
server.title       = 'CMS data quality'
server.serviceName = 'CERN RelVal'

server.source('file', 'DQMArchive', '/data/dqm/relval/dqm.db', '--listen 8051')
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/relval/upload')

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-relval.py")
