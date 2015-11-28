
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


T2DegStop_300_270_FastSIM_dir0="root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/mzarucki/T2DegStop_300_270_FastSim_v3/T2DegStop_300_270_FastSim_v3/151123_113332/0000/"
T2DegStop_300_270_FastSIM_dir1="root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/mzarucki/T2DegStop_300_270_FastSim_v3/T2DegStop_300_270_FastSim_v3/151123_113332/0001/"
fileList0 = subprocess.Popen(["gfal-ls "+ T2DegStop_300_270_FastSIM_dir0 ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
fileList1 = subprocess.Popen(["gfal-ls "+ T2DegStop_300_270_FastSIM_dir1 ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
T2DegStop_300_270_FastSIM_files0=[file[:-1] for file in fileList0.stdout.readlines() if file[:-1].endswith(".root") ]
T2DegStop_300_270_FastSIM_files1=[file[:-1] for file in fileList1.stdout.readlines() if file[:-1].endswith(".root") ]

T2DegStop_300_270_FastSIM = cfg.MCComponent(
      dataset="/T2DegStop_300_270_FastSim/mzarucki-T2DegStop_300_270_FastSim-420683af1bb5170fe0b35a3c8f09b1ec/USER",
      name = "T2DegStop_300_270",
      files =  [T2DegStop_300_270_FastSIM_dir0 + x for x in T2DegStop_300_270_FastSIM_files0]  +
               [T2DegStop_300_270_FastSIM_dir1 + x for x in T2DegStop_300_270_FastSIM_files1],
      xSection = 8.51615,
      nGenEvents = 1,
      triggers = [],
      effCorrFactor = 1,
  )


T2DegStop_300_290_FastSIM_dir0="root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/mzarucki/T2DegStop_300_290_FastSim_v3/T2DegStop_300_290_FastSim_v3/151123_113025/0000/"
T2DegStop_300_290_FastSIM_dir1="root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/mzarucki/T2DegStop_300_290_FastSim_v3/T2DegStop_300_290_FastSim_v3/151123_113025/0001/"
fileList0 = subprocess.Popen(["gfal-ls "+ T2DegStop_300_290_FastSIM_dir0 ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
fileList1 = subprocess.Popen(["gfal-ls "+ T2DegStop_300_290_FastSIM_dir1 ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
T2DegStop_300_290_FastSIM_files0=[file[:-1] for file in fileList0.stdout.readlines() if file[:-1].endswith(".root") ]
T2DegStop_300_290_FastSIM_files1=[file[:-1] for file in fileList1.stdout.readlines() if file[:-1].endswith(".root") ]
T2DegStop_300_290_FastSIM = cfg.MCComponent(
      dataset="/T2DegStop_300_290_FastSim/mzarucki-T2DegStop_300_290_FastSim-420683af1bb5170fe0b35a3c8f09b1ec/USER",
      name = "T2DegStop_300_290",
      files =  [T2DegStop_300_290_FastSIM_dir0 + x for x in T2DegStop_300_290_FastSIM_files0]  +
               [T2DegStop_300_290_FastSIM_dir1 + x for x in T2DegStop_300_290_FastSIM_files1],
      xSection = 8.51615,
      nGenEvents = 1,
      triggers = [],
      effCorrFactor = 1,
  )

T2DegStop_300_240_FastSIM_dir0="root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/mzarucki/T2DegStop_300_240_FastSim_v3/T2DegStop_300_240_FastSim_v3/151123_113742/0000/"
T2DegStop_300_240_FastSIM_dir1="root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/mzarucki/T2DegStop_300_240_FastSim_v3/T2DegStop_300_240_FastSim_v3/151123_113742/0001/"
fileList0 = subprocess.Popen(["gfal-ls "+ T2DegStop_300_240_FastSIM_dir0 ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
fileList1 = subprocess.Popen(["gfal-ls "+ T2DegStop_300_240_FastSIM_dir1 ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
T2DegStop_300_240_FastSIM_files0=[file[:-1] for file in fileList0.stdout.readlines() if file[:-1].endswith(".root") ]
T2DegStop_300_240_FastSIM_files1=[file[:-1] for file in fileList1.stdout.readlines() if file[:-1].endswith(".root") ]
T2DegStop_300_240_FastSIM = cfg.MCComponent(
      dataset="/T2DegStop_300_240_FastSim/mzarucki-T2DegStop_300_240_FastSim-420683af1bb5170fe0b35a3c8f09b1ec/USER",
      name = "T2DegStop_300_240",
      files =  [T2DegStop_300_240_FastSIM_dir0 + x for x in T2DegStop_300_240_FastSIM_files0]  +
               [T2DegStop_300_240_FastSIM_dir1 + x for x in T2DegStop_300_240_FastSIM_files1],
      xSection = 8.51615,
      nGenEvents = 1,
      triggers = [],
      effCorrFactor = 1,
  )


