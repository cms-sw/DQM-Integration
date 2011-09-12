import FWCore.ParameterSet.Config as cms

from DQMServices.Core.DQM_cfg import *

DQM.collectorHost = 'dqm-prod-local.cms'
DQM.collectorPort = 9090

from DQMServices.Components.DQMEnvironment_cfi import *

global runTypes
global runType
runTypes = type('Enum', () , {'pp_run':0,'cosmic_run':1,'hi_run':2})
runType = runTypes.pp_run

dqmSaver.convention = 'Online'
dqmSaver.referenceHandling = 'all'
dqmSaver.dirName = '/home/dqmprolocal/output'
dqmSaver.producer = 'DQM'
dqmSaver.saveByTime = 1
dqmSaver.saveByLumiSection = -1
dqmSaver.saveByMinute = 8
dqmSaver.saveByRun = 1
dqmSaver.saveAtJobEnd = False

