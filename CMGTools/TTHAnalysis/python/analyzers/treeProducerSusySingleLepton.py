from CMGTools.TTHAnalysis.analyzers.treeProducerSusyCore import *
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *

susySingleLepton_globalVariables = susyCore_globalVariables + [
#susySingleLepton_globalVariables = [

            NTupleVariable("met_genPt", lambda ev : ev.met_genPtDef, help="gen E_{T}^{miss} pt from patch of Matthieus recipe which doesn't store genmet"),
            NTupleVariable("met_genPhi", lambda ev : ev.met_genPhiDef, help="gen E_{T}^{miss} phi from patch of Matthieus recipe which doesn't store genmet"),

            NTupleVariable("met_rawPt", lambda ev : ev.met.uncorrectedPt(), help="raw met p_{T}"),
            NTupleVariable("met_rawPhi", lambda ev : ev.met.uncorrectedPhi(), help="raw met phi"),
            NTupleVariable("met_rawSumEt", lambda ev : ev.met.uncorrectedSumEt(), help="raw met sumEt"),
            NTupleVariable("metNoHF_rawPt", lambda ev : ev.metNoHF.uncorrectedPt(), help="raw metNoHF p_{T}"),
            NTupleVariable("metNoHF_rawPhi", lambda ev : ev.metNoHF.uncorrectedPhi(), help="raw metNoHF phi"),
            NTupleVariable("metNoHF_rawSumetNoHF", lambda ev : ev.metNoHF.uncorrectedSumEt(), help="raw metNoHF sumetNoHF"),
            NTupleVariable("met_caloPt", lambda ev : ev.met.caloMETPt(), help="calo met p_{T}"),
            NTupleVariable("met_caloPhi", lambda ev : ev.met.caloMETPhi(), help="calo met phi"),
            NTupleVariable("met_caloSumEt", lambda ev : ev.met.caloMETSumEt(), help="calo met sumEt"),

            ##-------- custom jets ------------------------------------------
            NTupleVariable("htJet25", lambda ev : ev.htJet25, help="H_{T} computed from leptons and jets (with |eta|<2.4, pt > 25 GeV)"),
            NTupleVariable("mhtJet25", lambda ev : ev.mhtJet25, help="H_{T}^{miss} computed from leptons and jets (with |eta|<2.4, pt > 25 GeV)"),
            NTupleVariable("htJet40j", lambda ev : ev.htJet40j, help="H_{T} computed from only jets (with |eta|<2.4, pt > 40 GeV)"),
            NTupleVariable("htJet40", lambda ev : ev.htJet40, help="H_{T} computed from leptons and jets (with |eta|<2.4, pt > 40 GeV)"),
            NTupleVariable("mhtJet40", lambda ev : ev.mhtJet40, help="H_{T}^{miss} computed from leptons and jets (with |eta|<2.4, pt > 40 GeV)"),
            NTupleVariable("nSoftBJetLoose25",  lambda ev: sum([(sv.mva>0.3 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 25 passing CSV medium and SV from ivf with loose sv mva"),
            NTupleVariable("nSoftBJetMedium25", lambda ev: sum([(sv.mva>0.7 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 25 passing CSV medium and SV from ivf with medium sv mva"),
            NTupleVariable("nSoftBJetTight25",  lambda ev: sum([(sv.mva>0.9 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 25 passing CSV medium and SV from ivf with tight sv mva"),
            # ----------------------- MET filter information (temporary)  -------------------------------------------------------------------- #
            NTupleVariable("Flag_HBHENoiseFilterMinZeroPatched", lambda ev: ev.hbheFilterNew, help="HBEHE temporary filter decision"),
            ##------------------------------------------------

            # ----------------------- HT from LHE event (requires LHE analyzer to have run)  --------------------------------------------------------- #
            NTupleVariable("lheHT", lambda ev : ev.lheHT, help="H_{T} computed from quarks and gluons in Heppy LHEAnalyzer", mcOnly=True),
            NTupleVariable("lheHTIncoming", lambda ev : ev.lheHTIncoming, help="H_{T} computed from quarks and gluons in Heppy LHEAnalyzer (only LHE status<0 as mothers)", mcOnly=True),
            # ---------------------------------------------------------------------------------------------------------------------------------------- #

]
susySingleLepton_globalObjects = susyCore_globalObjects.copy()
susySingleLepton_globalObjects.update({
            # put more here
})

susySingleLepton_collections =  susyCore_collections.copy()
susySingleLepton_collections.update({

            # put more here
##            "genParticles"     : NTupleCollection("genPartAll",  genParticleWithMotherId, 200, help="all pruned genparticles"), # need to decide which gen collection ?
            "genParticles"     : NTupleCollection("genPartAll",  genParticleWithMotherIndex, 200, help="all pruned genparticles"),
            "packedGenParticles"     : NTupleCollection("genPartPkd",  packedGenParticleWithMotherIndex, 2000, help="all packed genparticles"),

            ## ---------------------------------------------
            "selectedLeptons" : NTupleCollection("LepGood", leptonTypeSusy, 8, help="Leptons after the preselection"),
            "otherLeptons"    : NTupleCollection("LepOther", leptonTypeSusy, 8, help="Leptons after the preselection"),
            "selectedTaus"    : NTupleCollection("TauGood", tauTypeSusy, 3, help="Taus after the preselection"),
            "selectedIsoTrack"    : NTupleCollection("isoTrack", isoTrackType, 50, help="isoTrack, sorted by pt"),
            "allTracks"    : NTupleCollection("track", isoTrackTypeSusy, 2000, help="all Tracks from PackedPFCandidates, sorted by pt"),

            ##------------------------------------------------
            "cleanJetsAll"       : NTupleCollection("Jet",     jetTypeSusy, 25, help="Cental jets after full selection and cleaning, sorted by pt"),
            "fatJets"         : NTupleCollection("FatJet",  fatJetType,  15, help="AK8 jets, sorted by pt"),
            "genJets"         : NTupleCollection("GenJet",  genJetType,  15, help="Gen Jets, sorted by pt"),
#            "reclusteredFatJets" : NTupleCollection("RCFatJet",     fourVectorType,20, help="FatJets1.2 reclusterd from ak4 cleanJetsAll pT > 30, eta <5 "),
            ##------------------------------------------------
            "ivf"       : NTupleCollection("SV",     svType, 20, help="SVs from IVF"),
})

