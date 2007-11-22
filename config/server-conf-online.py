import os.path, socket
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
PORT = 8030

envsetup = """
 source ~cmssw/cmsset_default.sh
 source /home/dqm/rpms/slc4_ia32_gcc345/cms/webtools/1.0.0/etc/profile.d/dependencies-setup.sh
 export QUIET_ASSERT=a
"""

server = DQMServerSpec (
  port       = PORT,
  localBase   = '%s:%d' % (socket.gethostname(), PORT),
  serverDir   = '/home/dqm/gui',
  baseUrl     = '/dqm/online',
  title       = 'CMS data quality',
  views       = CONFIGDIR + '/online-views.py',
  services    = CONFIGDIR + '/dqm-services.py',
  serviceName = "Online",
  backends    = [
    DQMBackendSpec('dqm', 'Client', [ '--collector localhost:9090' ], waitFor = 'commands'),
    DQMBackendSpec('dt', 'Layout', [ CONFIGDIR + '/dt-layouts.py' ]),
    DQMBackendSpec('l1t', 'Layout', [ CONFIGDIR + '/l1t-layouts.py' ]),
    DQMBackendSpec('ecal', 'Layout', [ CONFIGDIR + '/ecal-layouts.py' ]),
    DQMBackendSpec('eb', 'Layout', [ CONFIGDIR + '/eb-layouts.py' ]),
    DQMBackendSpec('ee', 'Layout', [ CONFIGDIR + '/ee-layouts.py' ]),
    DQMBackendSpec('strip','Layout', [ CONFIGDIR + '/strip-layouts.py' ]),
    DQMBackendSpec('pixel','Layout', [ CONFIGDIR + '/pixel-layouts.py' ]),
    DQMBackendSpec('hcal', 'Layout', [ CONFIGDIR + '/hcal-layouts.py' ])

