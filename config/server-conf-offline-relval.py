import os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

modules = ("GuiDQM",)
envsetup = """
 source /data/sw/cmsset_default.sh
 source /data/sw/slc4_ia32_gcc345/cms/webtools/1.3.0/etc/profile.d/dependencies-setup.sh
 source /data/sw/slc4_ia32_gcc345/external/py2-pil/1.1.6/etc/profile.d/init.sh
 source /data/sw/slc4_ia32_gcc345/external/libpng/1.2.10/etc/profile.d/init.sh
 source /data/sw/slc4_ia32_gcc345/external/libjpg/6b/etc/profile.d/init.sh
 source /data/sw/slc4_ia32_gcc345/external/libtiff/3.8.2/etc/profile.d/init.sh
 export QUIET_ASSERT=a
"""

server.port        = 8050
server.serverDir   = '/data/dqm/relval/gui'
server.baseUrl     = '/dqm/relval'
server.title       = 'CMS data quality'
server.serviceName = 'CERN RelVal'

server.source('DQMArchive', 'file', '/data/dqm/relval/dqm.db', '--listen 8051')
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/relval/upload')

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-relval.py")
