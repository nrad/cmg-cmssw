
import PhysicsTools.HeppyCore.framework.config as cfg
#xsec from: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom 
import subprocess

T2DegStop_300_270_RunII_dir="root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop_300_270_GEN-SIM/T2DegStop_300_270_MINIAOD-RunIISpring15-MCRUN2_74_V9-25ns/008934a25a3583950e0bb876accde101/"
fileList = subprocess.Popen(["gfal-ls "+ T2DegStop_300_270_RunII_dir ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
T2DegStop_300_270_RunII_files=[file[:-1] for file in fileList.stdout.readlines()]



T2DegStop_300_270 = cfg.MCComponent(
      dataset="/T2DegStop_300_270_GEN-SIM/nrad-T2DegStop_300_270_MINIAOD-RunIISpring15-MCRUN2_74_V9-25ns-008934a25a3583950e0bb876accde101/USER",
      name = "T2DegStop_300_270",
      files =  [T2DegStop_300_270_RunII_dir + x for x in T2DegStop_300_270_RunII_files
               ],
      xSection = 8.51615,
      nGenEvents = 1,
      triggers = [],
      effCorrFactor = 1,
  )





