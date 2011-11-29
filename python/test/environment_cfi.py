import FWCore.ParameterSet.Config as cms

from DQMServices.Core.DQM_cfg import *

DQM.collectorHost = 'dqm-integration.cms'
DQM.collectorPort = 9090

from DQMServices.Components.DQMEnvironment_cfi import *

dqmSaver.convention = 'Online'
dqmSaver.referenceHandling = 'all'
dqmSaver.dirName = '/home/dqmdevlocal/output'
dqmSaver.producer = 'Playback'
dqmSaver.saveByTime = 1
dqmSaver.saveByLumiSection = -1
dqmSaver.saveByMinute = 8
dqmSaver.saveByRun = 1
dqmSaver.saveAtJobEnd = False

#RunType, and Runkey selection from RCMS
import sys
from FWCore.ParameterSet.VarParsing import VarParsing
from dqmPythonTypes import *

runParameters = VarParsing ('analysis')
runParameters.register ('runtype',
  'pp_run',
  VarParsing.multiplicity.singleton,
  VarParsing.varType.string,
  "Type of Run in CMS")

runParameters.register ('runkey',
  'pp_run',
  VarParsing.multiplicity.singleton,
  VarParsing.varType.string,
  "Run Keys of CMS")

# Fix to allow scram to compile
if len(sys.argv) > 1:
  runParameters.parseArguments()

runType = RunType(['pp_run','cosmic_run','hi_run','hpu_run'])
if not runParameters.runkey.strip():
  runParameters.runkey = 'pp_run'

runType.setRunType(runParameters.runkey.strip())
