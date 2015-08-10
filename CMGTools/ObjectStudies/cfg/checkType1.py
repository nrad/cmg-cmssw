from math import pi, sqrt, cos, sin

import ROOT
ROOT.gStyle.SetOptStat(0)
from DataFormats.FWLite import Events, Handle
from PhysicsTools.PythonAnalysis import *

small = False

edmCollections = { \
  "slimmedMETs"                       :("vector<pat::MET>",      "slimmedMETs"                         , "",        "RECO"   )  ,
#  "patJets"                           :("vector<pat::Jet>",      "patJets"                             , "",        "RERUN" )  ,
#  "patJetsResDown"                    :("vector<pat::Jet>",      "patJetsResDown"                      , "",        "RERUN" )  ,
#  "patJetsResUp"                      :("vector<pat::Jet>",      "patJetsResUp"                        , "",        "RERUN" )  ,
#  "patSmearedJets"                    :("vector<pat::Jet>",      "patSmearedJets"                      , "",        "RERUN" )  ,
#  "selectedPatJets"                   :("vector<pat::Jet>",      "selectedPatJets"                     , "",        "RERUN" )  ,
#  "selectedPatJetsForMetT1T2Corr"     :("vector<pat::Jet>",      "selectedPatJetsForMetT1T2Corr"       , "",        "RERUN" )  ,
#  "selectedPatJetsForMetT1T2SmearCorr":("vector<pat::Jet>",      "selectedPatJetsForMetT1T2SmearCorr"  , "",        "RERUN" )  ,
#  "selectedPatJetsForMetT2Corr"       :("vector<pat::Jet>",      "selectedPatJetsForMetT2Corr"         , "",        "RERUN" )  ,
#  "selectedPatJetsForMetT2SmearCorr"  :("vector<pat::Jet>",      "selectedPatJetsForMetT2SmearCorr"    , "",        "RERUN" )  ,
#  "shiftedPatJetEnDown"               :("vector<pat::Jet>",      "shiftedPatJetEnDown"                 , "",        "RERUN" )  ,
#  "shiftedPatJetEnUp"                 :("vector<pat::Jet>",      "shiftedPatJetEnUp"                   , "",        "RERUN" )  ,
#  "shiftedPatJetResDown"              :("vector<pat::Jet>",      "shiftedPatJetResDown"                , "",        "RERUN" )  ,
#  "shiftedPatJetResUp"                :("vector<pat::Jet>",      "shiftedPatJetResUp"                  , "",        "RERUN" )  ,
#  "patPFMetT1Txy"                     :("vector<pat::MET>",      "patPFMetT1Txy"                       , "",        "RERUN" )  ,
  "slimmedMETsRERUN"                  :("vector<pat::MET>",      "slimmedMETs"                         , "",        "RERUN" ),
  "slimmedMETsNoHFRERUN"                  :("vector<pat::MET>",      "slimmedMETsNoHF"                         , "",        "RERUN" ),
}

handles={k:Handle(edmCollections[k][0]) for k in edmCollections.keys()}

#files = ["/afs/hephy.at/user/r/rschoefbeck/CMS/cmssw/CMSSW_7_4_6_patch1/src/corMETMiniAOD_data_noResiduals.root"]
files = ["/afs/hephy.at/user/r/rschoefbeck/CMS/cmssw/CMSSW_7_4_6_patch1/src/corMETMiniAOD_data_residuals.root"]

events = Events(files)
events.toBegin()
products={}
missingCollections=[]
print "Number of events:",events.size()

nevents = min(3, events.size())

for nev in range(nevents):
  if nev%100==0:print nev,'/',nevents
  events.to(nev)
  eaux=events.eventAuxiliary()
  run=eaux.run()           
  event=eaux.event()
  lumi=eaux.luminosityBlock()
  for k in [ x for x in edmCollections.keys() if x not in missingCollections]:
    try:
      events.getByLabel(edmCollections[k][1:],handles[k])
      products[k]=handles[k].product()
    except:
      products[k]=None
      print "Not found:",k
      missingCollections.append(k)

#  dx,dy=0.,0.
#  print "\n%i:%i:%i"%(run,lumi,event)
#  print "reclustered Jets",
#  for i, j in enumerate(products["selectedPatJets" ]):
##  for i, j in enumerate(products["patSmearedJets" ]):
##    if j.pt()>10:
#      dx -= j.px()*(1-j.jecFactor("L1FastJet"))#-j.jecFactor(0)) #j(L1L2L3-L1)-j(raw)# 1-("L1FastJet")-(0)
#      dy -= j.py()*(1-j.jecFactor("L1FastJet"))#-j.jecFactor(0))
##      dx -= j.px()*(1-j.jecFactor(0))
##      dy -= j.py()*(1-j.jecFactor(0))
#      print "%f"%(j.pt()),
#  print
  
  oldMET = products["slimmedMETs"][0]  
  newMET = products["slimmedMETsRERUN"][0] 
  newMETNoHF = products["slimmedMETsNoHFRERUN"][0] 
  print  
  print "mAOD raw         MET", oldMET.uncorrectedPt()
  print "mAOD type1       MET", oldMET.pt()
  print "RERUN raw        MET", newMET.uncorrectedPt()
  print "RERUN type1      MET", newMET.pt()
  print "RERUN NOHF raw   MET", newMETNoHF.uncorrectedPt()
  print "RERUN NOHF type1 MET", newMETNoHF.pt()
#  print "new raw MET", newMET.uncorrectedPt()
#  print "new type1 MET", newMET.pt()
#  print "should be ...", sqrt((newMET.uncorrectedPt()*cos(newMET.uncorrectedPhi()) + dx)**2 + (newMET.uncorrectedPt()*sin(newMET.uncorrectedPhi()) + dy)**2)
 
