import os.path

CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
PORT = 8030

# Define a list of allowed bases, then rewrite tools.proxy to
# select a base that was used in the request ('X-Forwarded-Host'
# or 'Host'; allow several in each).
#
# bases    = [ 'localhost:%d' % PORT,
#              '%s:%d' % (gethostname(), PORT),
#              'lxcms73.cern.ch' ],

modules = ("GuiDQM",)

envsetup = """
  source /home/dqm/rpms/slc4_ia32_gcc345/cms/webtools/1.0.0/etc/profile.d/dependencies-setup.sh
  # source $HOME/sw/rpms/slc4_ia32_gcc345/cms/webtools/1.0.0/etc/profile.d/dependencies-setup.sh
  export QUIET_ASSERT=a
"""

server.serverDir   = '/home/dqm/gui'
server.baseUrl     = '/dqm/online'
server.title       = 'CMS data quality'
server.serviceName = 'Online'

# server.source('dt',    'DQMLive', '--listen 9092', '--collector usc55ucr04.cms:9090')
# server.source('ecal',  'DQMLive', '--listen 9093', '--collector ecalod-22.cms:9090')
# server.source('hcal',  'DQMLive', '--listen 9094', '--collector rubus2d16-12:9090')
# server.source('hcalt', 'DQMLive', '--listen 9095', '--collector rubus2d16-12:9090')
# server.source('l1t',   'DQMLive', '--listen 9096', '--collector rubus2d16-14:9090')
server.source('test',    'DQMLive', '--listen 9091', '--collector localhost:9090')
#server.source('file',    'DQMArchive', '/home/dqm/dqm.db', '--listen 9097')
#server.source('layouts', 'DQMLayout',
#              CONFIGDIR + '/test-layouts.py',
#              CONFIGDIR + '/dt-layouts.py',
#              CONFIGDIR + '/eb-layouts.py',
#              CONFIGDIR + '/l1t-layouts.py')

# server.extend('DQMFileAccess', '/dev/null', '/tmp/lat/dqmdata')

execfile(CONFIGDIR + "/dqm-services.py", globals(), locals())
execfile(CONFIGDIR + "/online-workspaces.py", globals(), locals())
