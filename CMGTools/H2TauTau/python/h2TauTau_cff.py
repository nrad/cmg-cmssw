import FWCore.ParameterSet.Config as cms

from CMGTools.H2TauTau.objects.tauMuObjectsMVAMET_cff import tauMuSequence
from CMGTools.H2TauTau.objects.tauEleObjectsMVAMET_cff import tauEleSequence
# from CMGTools.H2TauTau.objects.diTauObjectsMVAMET_cff import diTauSequence

# Need to explicitly import all modules in all sequences for cms.load(..)
# to work properly in the top-level config

from CMGTools.H2TauTau.skims.skim_cff import tauMuFullSelSkimSequence, tauEleFullSelSkimSequence, diTauFullSelSkimSequence

from CMGTools.H2TauTau.objects.mvaMetInputs_cff import mvaMetInputSequence, calibratedAK4PFJetsForPFMVAMEt, puJetIdForPFMVAMEt

from CMGTools.H2TauTau.objects.tauMuObjectsMVAMET_cff import mvaMETTauMu, cmgTauMu, cmgTauMuCor, cmgTauMuTauPtSel, cmgTauMuCorSVFitPreSel, cmgTauMuCorSVFitFullSel, tauMuMVAMetSequence, tauPreSelectionTauMu, muonPreSelectionTauMu

from CMGTools.H2TauTau.objects.tauEleObjectsMVAMET_cff import mvaMETTauEle, cmgTauEle, cmgTauEleCor, cmgTauEleTauPtSel, cmgTauEleCorSVFitPreSel, cmgTauEleCorSVFitFullSel, tauEleMVAMetSequence, tauPreSelectionTauEle, electronPreSelectionTauEle

from CMGTools.H2TauTau.skims.skim_cff import tauMuFullSelCount, tauEleFullSelCount, diTauFullSelCount

# generic

# MVA MET Inputs

mvaMetInputPath = cms.Path(
    mvaMetInputSequence
    )


# tau-mu ---

# full selection
tauMuPath = cms.Path(
    # metRegressionSequence + 
    tauMuSequence + 
    tauMuFullSelSkimSequence
    )

# tau-ele ---

# full selection
tauElePath = cms.Path(
    # metRegressionSequence + 
    tauEleSequence + 
    tauEleFullSelSkimSequence     
    )

# tau-tau ---

# # full selection
# diTauPath = cms.Path(
#     # metRegressionSequence + 
#     diTauSequence +
#     diTauFullSelSkimSequence     
#     )


