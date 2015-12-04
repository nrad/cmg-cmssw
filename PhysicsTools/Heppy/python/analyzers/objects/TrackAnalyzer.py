import operator
import itertools
import copy
import types

from ROOT import TLorentzVector

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.framework.event import Event
from PhysicsTools.HeppyCore.statistics.counter import Counter, Counters
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.Lepton import Lepton
from PhysicsTools.Heppy.physicsobjects.Tau import Tau
from PhysicsTools.Heppy.physicsobjects.IsoTrack import IsoTrack

from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaPhi, bestMatch , matchObjectCollection3

import PhysicsTools.HeppyCore.framework.config as cfg

from ROOT import heppy
import math




class TrackAnalyzer( Analyzer ):

    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(TrackAnalyzer,self).__init__(cfg_ana,cfg_comp,looperName)
        self.IsoTrackIsolationComputer = heppy.IsolationComputer()


        #self.jetCollection             = getattr(cfg_ana, "jetCollection", "cleanJetsAll" ) 
        #self.postFix                   = getattr(cfg_ana,"collectionPostFix","track")
        self.trackOpt                   = getattr(cfg_ana, "trackOpt" )
        self.do_mc_match                = getattr(cfg_ana,"do_mc_match",True)
        #print "---"*12
        #print "   "*3 , "Track Analyzer Is On!" ,  "   "*3
        #print "---"*12
        self.makeAllTracks = getattr(cfg_ana, "makeAllTracks", True)


        self.isoDR = 0.3   ,
        self.ptPartMin = 0 ,

        if self.trackOpt.lower() == "reco":
            self.do_mc_match        =     getattr(cfg_ana,  "do_mc_match",True)
            self.jetCollection      =     getattr(cfg_ana,  "jetCollection",     "cleanJetsAll")
            self.preFix             =     getattr(cfg_ana,  "collectionPreFix" ,"Tracks")
            self.candidates         =     'packedPFCandidates'
            self.candidateTypes     =     'std::vector<pat::PackedCandidate>' 
        elif self.trackOpt.lower() == "gen":
            self.do_mc_match        =     False
            self.jetCollection      =     getattr(cfg_ana,  "jetCollection",     "cleanGenJets")
            self.preFix             =     getattr(cfg_ana,  "collectionPreFix" , "GenTracks")
            self.candidates         =     'packedGenParticles'
            self.candidateTypes     =     'std::vector<pat::PackedGenParticle>' 
        else:
            assert False, "track option not recognized...selected reco or gen"

        print "------------" * 3 
        print self.do_mc_match              
        print self.jetCollection 
        print self.preFix        
        print self.candidates    
        print self.candidateTypes
        print "------------" * 3 


    #----------------------------------------
    # DECLARATION OF HANDLES OF TRACKS   
    #----------------------------------------
    def declareHandles(self):
        super(TrackAnalyzer, self).declareHandles()
        #self.handles['packedCandidates'] = AutoHandle( 'packedPFCandidates', 'std::vector<pat::PackedCandidate>')
        self.handles[self.preFix] = AutoHandle( self.candidates, self.candidateTypes)

    def beginLoop(self, setup):
        super(TrackAnalyzer,self).beginLoop(setup)
        self.counters.addCounter('events')
        count = self.counters.counter('events')
        count.register('all events')
        count.register('has >=1 selected Track')
        count.register('has >=1 selected Iso Track')


    def matchTrackToJets(self,trk,jets,drMin=0.4):
        """ adds the index and dr of the best matched jet to the track  """
        trk.matchedJetIndex=-1
        trk.matchedJetDr=99999
        for ij,jet in enumerate(jets):
            dR = deltaR(trk,jet)
            if dR < trk.matchedJetDr:
                trk.matchedJetDr    = dR
                if dR < drMin:  
                    trk.matchedJetIndex = ij

    def getTrackCosPhiToJets(self,trk,jets):
        nJets = len(jets)
        trk.CosPhiJet1  = -99
        trk.CosPhiJet12  = -99
        trk.CosPhiJetAll  = -99
        jetTot = TLorentzVector()
        jv = TLorentzVector()
        for ij,jet in enumerate(jets):
          jv.SetPtEtaPhiM(jet.pt(), jet.eta(),jet.phi(),jet.mass())
          jetTot += jv 
          if ij ==0:
             trk.CosPhiJet1=math.cos(trk.phi()-jetTot.Phi() )
          if ij ==1 or nJets==1:
             trk.CosPhiJet12=math.cos(trk.phi()-jetTot.Phi() )
          if ij == nJets-1:
             trk.CosPhiJetAll=math.cos(trk.phi()-jetTot.Phi() )



    #def matchTracksToJets(self, tracks,jets,drMin= 0.4):
    #  for trk in tracks:
    #    matchTrackToJets(trk,jets,drMin=drMin)



    def matchTrackToGen(self,tracks, event):
        #matchTau = matchObjectCollection3(event.selectedIsoTrack, event.gentaus + event.gentauleps + event.genleps, deltaRMax = 0.5)
        #print "genTaus", [x.pdgId for x in event.gentaus]
        #print "gentauleps", [x.pdgId for x in event.gentauleps]
        #print "genleps", [x.pdgId for x in event.genleps]
        #print "matchTau:", matchTau
        #matchGen = matchObjectCollection3(event.allTracks, event.packedGenParticles, deltaRMax = 0.5)
        matchGen = matchObjectCollection3(tracks, event.packedGenParticles, deltaRMax = 0.5)
        #print "matchGen:", matchGen
        #print [x.pdgId() for x in matchGen]
        for lep in tracks:
            gen = matchGen[lep]
            #if gen:
            #  print "---matched:"
            #  print gen
            #  print lep
            #  print deltaR(gen,lep) 
            #  print "----", gen.pdgId(),gen.motherRef().index() ,event.packedGenParticles[gen.motherRef().index()].pdgId(), gen.motherRef().pdgId()
            #lep.mcMatchId = gen.motherRef().pdgId() if gen else 0
            lep.mcMatchId = 1 if gen else 0
    

    #------------------
    # MAKE LIST
    #------------------
    def makeTrack(self, event):
        #print "---"*12
        #print "   "*3 , "Making Tracks!" ,  "   "*3
        #print "---"*12

        self.allTracks   = []

        #patcands = self.handles['packedCandidates'].product()
        cands = self.handles[self.preFix].product()

        if self.trackOpt.lower() == "reco":
            print "opt reco"
            charged = [ p for p in cands if ( p.charge() != 0 and p.fromPV() > 1 ) ]
            self.IsoTrackIsolationComputer.setPackedCandidates(cands, 1, 9999, 9999.)
        elif self.trackOpt.lower() == "gen":
            print "opt gen"
            charged = [ p for p in cands if ( p.charge() != 0  ) ]
        else:
            assert False    

        rawTracks = map( IsoTrack, charged )
        #jets = event.jets
        #jets = event.cleanJetsAll
        jets = getattr(event,self.jetCollection)

        for track in rawTracks:
            if track.pt() > 1 and abs( track.eta() ) <  2.5:
                if self.trackOpt.lower() == "reco":
                    #isoSum = self.IsoTrackIsolationComputer.chargedAbsIso(track.physObj, self.isoDR, 0., self.ptPartMin)
                    #track.absIso = isoSum - track.pt()
                    track.absIso = 0
                elif self.trackOpt.lower() == "gen":
                    track.absIso = 0
                #self.matchTrackToJets(track,jets,drMin=0.4)
                self.matchTrackToJets(track,jets,drMin=0.4)
                self.getTrackCosPhiToJets(track,jets)
                print "---------------------------"
                print track.matchedJetIndex , track.matchedJetDr
                print track.CosPhiJet1, track.CosPhiJet12, track.CosPhiJetAll
                self.allTracks.append(track)

        

        if self.makeAllTracks:
            self.allTracks.sort(key = lambda l : l.pt(), reverse = True)

        self.counters.counter('events').inc('all events')
        if(len(self.allTracks)): self.counters.counter('events').inc('has >=1 selected Iso Track')



    def printInfo(self, event):
        print 'event to Veto'
        print '----------------'

        if len(event.selectedIsoTrack)>0:
            print 'lenght: ',len(event.selectedIsoTrack)
            print 'track candidate pt: ',event.selectedIsoTrack[0].pt()
            print 'track candidate eta: ',event.selectedIsoTrack[0].eta()
            print 'track candidate phi: ',event.selectedIsoTrack[0].phi()
            print 'track candidate mass: ',event.selectedIsoTrack[0].mass()
            print 'pdgId candidate : ',event.selectedIsoTrack[0].pdgId()
            print 'dz: ',event.selectedIsoTrack[0].dz()
            print 'iso: ',event.selectedIsoTrack[0].absIso
            print 'matchId: ',event.selectedIsoTrack[0].mcMatchId 
        print '----------------'


    def process(self, event):

        if self.cfg_ana.setOff:
            return True

        self.readCollections( event.input )
        self.makeTrack(event)

        print self.allTracks
        print [x.pt() for x in self.allTracks]
        setattr( event,self.preFix, self.allTracks)

        #if len(event.selectedIsoTrack)==0 : return True
        if len(self.allTracks)==0 : return True



### ===> do matching
        
        if not self.cfg_comp.isMC:
            return True

        if hasattr(event, 'gentaus') and hasattr(event, 'gentauleps') and hasattr(event, 'genleps') and self.do_mc_match :
            #print "-------------------------------  MATCHING TRACKS --------------------------------------------"
            self.matchTrackToGen(self.allTracks, event)        
            #print "-----------"

        return True


setattr(TrackAnalyzer,"defaultConfig",cfg.Analyzer(
    class_object=TrackAnalyzer,
    setOff=True,
    trackOpt = "reco",
    #makeAllTracks = False,
    
    #####
    #candidates='packedPFCandidates',
    #candidatesTypes='std::vector<pat::PackedCandidate>',
    #ptMin = 5, # for pion 
    #ptMinEMU = 5, # for EMU
    #dzMax = 0.1,
    #####
    #dzPartMax = 0.1,
    #maxAbsIso = 8,
    #####
    #doRelIsolation = False,
    #MaxIsoSum = 0.1, ### unused
    #MaxIsoSumEMU = 0.2, ### unused
    #doSecondVeto = False,
    #####
  )
)
