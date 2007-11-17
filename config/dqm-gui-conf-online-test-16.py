from socket import gethostname
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

envsetup = """
  source ~cmssw/cmsset_default.sh
  source /home/dqm/rpms/slc4_ia32_gcc345/cms/webtools/1.0.0/etc/profile.d/dependencies-setup.sh
  export QUIET_ASSERT=a
"""

server = DQMServerSpec (
  port        = PORT,
  localBase   = '%s:%d' % (gethostname(), PORT),
  serverDir   = '/home/dqm/gui',
  baseUrl     = '/dqm/online-test',
  title       = 'CMS data quality',
  views       = CONFIGDIR + '/online-views.py',
  services    = CONFIGDIR + '/dqm-services.py',
  serviceName = "Online test",
  backends    = [
    # DQMBackendSpec('dt', 'Client', [ 'usc55ucr04.cms:9090' ], waitFor = 'commands'),
    # DQMBackendSpec('ecal', 'Client', [ 'ecalod-22.cms:9090' ], waitFor = 'commands'),
    # DQMBackendSpec('hcal', 'Client', [ 'rubus2d16-12:9090' ], waitFor = 'commands'),
    # DQMBackendSpec('hcalt', 'Client', [ 'rubus2d16-12:9090' ], waitFor = 'commands'),
    # DQMBackendSpec('l1t', 'Client', [ 'rubus2d16-14:9090' ], waitFor = 'commands'),
    DQMBackendSpec('test', 'Client', [ '--collector localhost:9090' ], waitFor = 'commands'),
    DQMBackendSpec('dtlayouts', 'Layout', [ CONFIGDIR + '/dt-layouts.py' ]),
    DQMBackendSpec('l1tlayouts', 'Layout', [ CONFIGDIR + '/l1t-layouts.py' ]),
    DQMBackendSpec('eblayouts', 'Layout', [ CONFIGDIR + '/eb-layouts.py' ])
  ])
