import PhysicsTools.HeppyCore.framework.config as cfg

#-------- SAMPLES AND TRIGGERS -----------
from CMGTools.RootTools.samples.samples_8TeVReReco_74X import * # <-- this one for the official sample
from CMGTools.ObjectStudies.samples.samples_METPOG_private import * #<-- this one for the private re-reco
from CMGTools.RootTools.samples.samples_13TeV_74X import *
from CMGTools.RootTools.samples.samples_13TeV_DATA2015 import *

from CMGTools.RootTools.samples.triggers_13TeV_Spring15 import triggers_1mu_iso_50ns, triggers_mumu

#-------- INITIAL FLAG

isDiJet=False
isZSkim=False
is1L=False

#-------- HOW TO RUN

test = 2

if test==0:
    selectedComponents = [DoubleMu_742, DoubleMu_740p9]
#    selectedComponents = [ DoubleMuParked_1Apr_RelVal_dm2012D_v2_newPFHCalib , DoubleMuParked_1Apr_RelVal_dm2012D_v2_oldPFHCalib , DoubleMuparked_1Apr_RelVal_dm2012D_v2 ]
    for comp in selectedComponents:
        comp.splitFactor = 251
        comp.files = comp.files[:]
        comp.triggers = triggers_8TeV_mumu

elif test==1:
    selectedComponents = [ RelValZMM_7_4_1,RelValZMM_7_4_0_pre9 ]
#    selectedComponents = [RelVal_741_Philfixes]
#    selectedComponents = relValkate
    for comp in selectedComponents:
#        comp.splitFactor = 1
        comp.splitFactor = 100
        comp.files = comp.files[:]

#elif test==2:
#    selectedComponents = [ TTJets_50ns ]
#    isZSkim=True
#    for comp in selectedComponents:
#        comp.triggers = triggers_mumu
#        comp.splitFactor = 1
#        comp.files = ['/afs/cern.ch/user/d/dalfonso/public/TTbarMadP850ns/0066F143-F8FD-E411-9A0B-D4AE526A0D2E.root']
##        comp.files = comp.files[:1]



   # ----------------------- Summer15 options -------------------------------------------------------------------- #
elif test==2:
    selectedComponents = [ DYJetsToLL_M50_50ns, TTJets_50ns  ]
    isZSkim=False
    for comp in selectedComponents:
        comp.triggers = triggers_mumu
        comp.splitFactor = 1000
        comp.files = comp.files[:]

elif test==3:
    selectedComponents = [ DYJetsToLL_M50_50ns,TTJets_50ns ]
    isZSkim=True
    for comp in selectedComponents:
        comp.triggers = triggers_mumu
        comp.splitFactor = 1000
        comp.files = comp.files[:]

elif test==4:
    selectedComponents = [ WJetsToLNu_50ns ]
    is1L=False
    for comp in selectedComponents:
        comp.splitFactor = 1000
        comp.files = comp.files[:]

elif test==5:
    selectedComponents = QCDPt_50ns
    isDiJet=True
    for comp in selectedComponents:
        comp.splitFactor = 1000
        comp.files = comp.files[:]

    # ------------------------------------------------------------------------------------------- #

### this is for the Zskim
elif test==13:
    isZSkim=True
    selectedComponents = [ DoubleMuon_Run2015B ]
    for comp in selectedComponents:
        comp.splitFactor = 1000
        comp.files = comp.files[:]
        comp.triggers = triggers_mumu
        comp.json = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_246908-251252_13TeV_PromptReco_Collisions15_JSON.json"
        comp.lumi= 0.0056
        print comp

### this is for the Wskim
elif test==14:
    is1L=False
    selectedComponents = [ SingleMuon_Run2015B ]
    for comp in selectedComponents:
        comp.splitFactor = 1000
        comp.files = comp.files[:]
        comp.json = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_246908-251252_13TeV_PromptReco_Collisions15_JSON.json"
        comp.lumi= 0.0056

### this is for the QCDlike
elif test==15:
    isDiJet=True
    selectedComponents = [ JetHT_Run2015B, HTMHT_Run2015B, MET_Run2015B ]
    for comp in selectedComponents:
        comp.splitFactor = 1000
        comp.files = comp.files[:]
        comp.json = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_246908-251252_13TeV_PromptReco_Collisions15_JSON.json"
        comp.lumi= 0.0056

# ------------------------------------------------------------------------------------------- #

from CMGTools.ObjectStudies.analyzers.metCoreModules_cff import *

cfg.Analyzer.nosubdir = True

##------------------------------------------
##  PRODUCER
##------------------------------------------


from CMGTools.ObjectStudies.analyzers.treeProducerMET import *

treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerMET',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     PDFWeights = PDFWeights,
     globalVariables = met_globalVariables,
     globalObjects = met_globalObjects,
     collections = met_collections,
     defaultFloatType = 'F',
     treename = 'METtree'
)

##------------------------------------------
##  SEQUENCE
##------------------------------------------

metAna.doTkMet = True
metAna.recoilComponents = [
  {'pdgId':211,'etaLow':-3,'etaHigh':-2.5,'name':'charged_m30_m25'},
  {'pdgId':211,'etaLow':-2.5,'etaHigh':-2,'name':'charged_m25_m20'},
  {'pdgId':211,'etaLow':-2.,'etaHigh':-1.5,'name':'charged_m20_m15'},
  {'pdgId':211,'etaLow':-1.5,'etaHigh':-1,'name':'charged_m15_m10'},
  {'pdgId':211,'etaLow':-1,'etaHigh':-0.5,'name':'charged_m10_m05'},
  {'pdgId':211,'etaLow':-0.5,'etaHigh':0,'name':'charged_m05_0'},
  {'pdgId':211,'etaLow':0,'etaHigh':0.5,'name':'charged_0_p05'},
  {'pdgId':211,'etaLow':0.5,'etaHigh':1,'name':'charged_p05_p10'},
  {'pdgId':211,'etaLow':1,'etaHigh':1.5,'name':'charged_p10_p15'},
  {'pdgId':211,'etaLow':1.5,'etaHigh':2,'name':'charged_p15_p20'},
  {'pdgId':211,'etaLow':2,'etaHigh':2.5,'name':'charged_p20_p25'},
  {'pdgId':211,'etaLow':2.5,'etaHigh':3,'name':'charged_p25_p30'},
  {'pdgId':230,'etaLow':-3,'etaHigh':-2.5,'name':'neutral_m30_m25'},
  {'pdgId':230,'etaLow':-2.5,'etaHigh':-2,'name':'neutral_m25_m20'},
  {'pdgId':230,'etaLow':-2.,'etaHigh':-1.5,'name':'neutral_m20_m15'},
  {'pdgId':230,'etaLow':-1.5,'etaHigh':-1,'name':'neutral_m15_m10'},
  {'pdgId':230,'etaLow':-1,'etaHigh':-0.5,'name':'neutral_m10_m05'},
  {'pdgId':230,'etaLow':-0.5,'etaHigh':0,'name':'neutral_m05_0'},
  {'pdgId':230,'etaLow':0,'etaHigh':0.5,'name':'neutral_0_p05'},
  {'pdgId':230,'etaLow':0.5,'etaHigh':1,'name':'neutral_p05_p10'},
  {'pdgId':230,'etaLow':1,'etaHigh':1.5,'name':'neutral_p10_p15'},
  {'pdgId':230,'etaLow':1.5,'etaHigh':2,'name':'neutral_p15_p20'},
  {'pdgId':230,'etaLow':2,'etaHigh':2.5,'name':'neutral_p20_p25'},
  {'pdgId':230,'etaLow':2.5,'etaHigh':3,'name':'neutral_p25_p30'},
  {'pdgId':22,'etaLow':-3,'etaHigh':-2.5,'name':'gamma_m30_m25'},
  {'pdgId':22,'etaLow':-2.5,'etaHigh':-2,'name':'gamma_m25_m20'},
  {'pdgId':22,'etaLow':-2.,'etaHigh':-1.5,'name':'gamma_m20_m15'},
  {'pdgId':22,'etaLow':-1.5,'etaHigh':-1,'name':'gamma_m15_m10'},
  {'pdgId':22,'etaLow':-1,'etaHigh':-0.5,'name':'gamma_m10_m05'},
  {'pdgId':22,'etaLow':-0.5,'etaHigh':0,'name':'gamma_m05_0'},
  {'pdgId':22,'etaLow':0,'etaHigh':0.5,'name':'gamma_0_p05'},
  {'pdgId':22,'etaLow':0.5,'etaHigh':1,'name':'gamma_p05_p10'},
  {'pdgId':22,'etaLow':1,'etaHigh':1.5,'name':'gamma_p10_p15'},
  {'pdgId':22,'etaLow':1.5,'etaHigh':2,'name':'gamma_p15_p20'},
  {'pdgId':22,'etaLow':2,'etaHigh':2.5,'name':'gamma_p20_p25'},
  {'pdgId':22,'etaLow':2.5,'etaHigh':3,'name':'gamma_p25_p30'},

  {'pdgId':1,'etaLow':-5,'etaHigh':-4.5,'name':'hHF_m50_m45'},
  {'pdgId':1,'etaLow':-4.5,'etaHigh':-4,'name':'hHF_m45_m40'},
  {'pdgId':1,'etaLow':-4,'etaHigh':-3.5,'name':'hHF_m40_m35'},
  {'pdgId':1,'etaLow':-3.5,'etaHigh':-3,'name':'hHF_m35_m30'},
  {'pdgId':1,'etaLow':3,'etaHigh':3.5,'name':'hHF_m05_0'},
  {'pdgId':1,'etaLow':3.5,'etaHigh':4,'name':'hHF_0_p05'},
  {'pdgId':1,'etaLow':4,'etaHigh':4.5,'name':'hHF_p05_p10'},
  {'pdgId':1,'etaLow':4.5,'etaHigh':5,'name':'hHF_p10_p15'},
  {'pdgId':2,'etaLow':-5,'etaHigh':-4.5,'name':'egammaHF_m50_m45'},
  {'pdgId':2,'etaLow':-4.5,'etaHigh':-4,'name':'egammaHF_m45_m40'},
  {'pdgId':2,'etaLow':-4,'etaHigh':-3.5,'name':'egammaHF_m40_m35'},
  {'pdgId':2,'etaLow':-3.5,'etaHigh':-3,'name':'egammaHF_m35_m30'},
  {'pdgId':2,'etaLow':3,'etaHigh':3.5,'name':'egammaHF_m05_0'},
  {'pdgId':2,'etaLow':3.5,'etaHigh':4,'name':'egammaHF_0_p05'},
  {'pdgId':2,'etaLow':4,'etaHigh':4.5,'name':'egammaHF_p05_p10'},
  {'pdgId':2,'etaLow':4.5,'etaHigh':5,'name':'egammaHF_p10_p15'},
]
#  226   case 211: return h;
#  227   case 11: return e;
#  228   case 13: return mu;
#  229   case 22: return gamma;
#  230   case 130: return h0;
#  231   case 1: return h_HF;
#  232   case 2: return egamma_HF;

metAna.doSpecialMet = False

metSequence = cfg.Sequence(
    metCoreSequence +[treeProducer]
    )

###---- to switch off the comptrssion
#treeProducer.isCompressed = 0

# -------------------- lepton modules below needed for the Muon Selection

if isZSkim:
    ttHLepSkim.ptCuts = [20,10]
    ttHLepSkim.minLeptons = 2
    metSequence.insert(metSequence.index(lepAna)+1,ttHLepSkim)
    metSequence.insert(metSequence.index(lepAna)+2,ttHZskim)

if is1L:
    ttHLepSkim.minLeptons = 1
    metSequence.insert(metSequence.index(lepAna)+1,ttHLepSkim)

if comp.isData :
    eventFlagsAna.processName = 'HLT'

# --------------------

triggerFlagsAna.triggerBits = {
            'SingleMu' : triggers_1mu_iso_50ns, # [ 'HLT_IsoMu17_eta2p1_v*', 'HLT_IsoTkMu17_eta2p1_v*'  ] + [ 'HLT_IsoMu20_v*', 'HLT_IsoTkMu20_v*'  ] $
            'DoubleMu' : triggers_mumu, # [ "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*", "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*" ]                    $
}


# ------------------------------------------------------------------------------------------- #
##------------------------------------------
##  SERVICES
##------------------------------------------

from PhysicsTools.HeppyCore.framework.services.tfile import TFileService 
output_service = cfg.Service(
      TFileService,
      'outputfile',
      name="outputfile",
      fname='METtree.root',
      option='recreate'
    )


# the following is declared in case this cfg is used in input to the heppy.py script                                                                                           
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events

# -------------------- Running Download from EOS

from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
event_class = EOSEventsWithDownload
if getHeppyOption("nofetch"):
    event_class = Events 


# -------------------- Running pre-processor

from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
preprocessor = CmsswPreprocessor("$CMSSW_BASE/src/CMGTools/ObjectStudies/cfg/MetType1_dump.py")

#printComps(config.components, True)               
config = cfg.Config( components = selectedComponents,
                     sequence = metSequence,
                     services = [output_service],
#                     preprocessor=preprocessor, # comment if pre-processor non needed
                     events_class = event_class)
#                     events_class = Events)

#printComps(config.components, True)
        
