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
  baseUrl     = '/dqm/online-playback',
  title       = 'CMS data quality',
  views       = CONFIGDIR + '/online-views.py',
  services    = CONFIGDIR + '/dqm-services.py',
  serviceName = "Online Playback",
  backends    = [
    DQMBackendSpec('collector', 'Collector', [ '--listen 9091 --collector srv-c2d05-18:9090' ]),
    DQMBackendSpec('dqm', 'Client', [ '--listen 9092 --collector localhost:9091' ]),
    # DQMBackendSpec('dt', 'Layout', [ CONFIGDIR + '/dt-layouts.py' ]),
    # DQMBackendSpec('hcal', 'Layout', [ CONFIGDIR + '/hcal-layouts.py' ]),
    # DQMBackendSpec('ecal', 'Layout', [ CONFIGDIR + '/ecal-layouts.py' ]),
    # DQMBackendSpec('eb', 'Layout', [ CONFIGDIR + '/eb-layouts.py' ]),
    # DQMBackendSpec('ee', 'Layout', [ CONFIGDIR + '/ee-layouts.py' ]),
    # DQMBackendSpec('strip','Layout', [ CONFIGDIR + '/strip-layouts.py' ]),
    # DQMBackendSpec('rpc','Layout', [ CONFIGDIR + '/rpc-layouts.py' ]),
    # DQMBackendSpec('csc','Layout', [ CONFIGDIR + '/csc-layouts.py' ]),
    # DQMBackendSpec('pixel','Layout', [ CONFIGDIR + '/pixel-layouts.py' ]),
    # DQMBackendSpec('l1t', 'Layout', [ CONFIGDIR + '/l1t-layouts.py' ])
  ])
