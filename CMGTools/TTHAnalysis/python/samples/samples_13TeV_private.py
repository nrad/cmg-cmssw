
import PhysicsTools.HeppyCore.framework.config as cfg
#xsec from: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom 



T2DegStop_300_270 = cfg.MCComponent(
      dataset="/T2DegStop2j_300_270_GENSIM/nrad-T2DegStop2j_300_270_MINIAOD-a279b5108ada7c3c0926210c2a95f22e/USER",
      name = "T2DegStop_300_270",
      files =  ['root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop2j_300_270_GENSIM/T2DegStop2j_300_270_MINIAOD/a279b5108ada7c3c0926210c2a95f22e//T2DegStop2j_300_270_miniAOD_1_1_RGu.root',
                'root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop2j_300_270_GENSIM/T2DegStop2j_300_270_MINIAOD/a279b5108ada7c3c0926210c2a95f22e//T2DegStop2j_300_270_miniAOD_2_1_yQN.root',
                'root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop2j_300_270_GENSIM/T2DegStop2j_300_270_MINIAOD/a279b5108ada7c3c0926210c2a95f22e//T2DegStop2j_300_270_miniAOD_3_1_o3g.root',
                'root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop2j_300_270_GENSIM/T2DegStop2j_300_270_MINIAOD/a279b5108ada7c3c0926210c2a95f22e//T2DegStop2j_300_270_miniAOD_4_1_EPC.root',
                'root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop2j_300_270_GENSIM/T2DegStop2j_300_270_MINIAOD/a279b5108ada7c3c0926210c2a95f22e//T2DegStop2j_300_270_miniAOD_5_1_hmI.root',
                'root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop2j_300_270_GENSIM/T2DegStop2j_300_270_MINIAOD/a279b5108ada7c3c0926210c2a95f22e//T2DegStop2j_300_270_miniAOD_6_1_PA3.root',
                'root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop2j_300_270_GENSIM/T2DegStop2j_300_270_MINIAOD/a279b5108ada7c3c0926210c2a95f22e//T2DegStop2j_300_270_miniAOD_7_1_adn.root',
                'root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop2j_300_270_GENSIM/T2DegStop2j_300_270_MINIAOD/a279b5108ada7c3c0926210c2a95f22e//T2DegStop2j_300_270_miniAOD_8_1_wD2.root',
                'root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop2j_300_270_GENSIM/T2DegStop2j_300_270_MINIAOD/a279b5108ada7c3c0926210c2a95f22e//T2DegStop2j_300_270_miniAOD_9_1_sjf.root'],
      xSection = 8.51615,
      nGenEvents = 1,
      triggers = [],
      effCorrFactor = 1,
  )
