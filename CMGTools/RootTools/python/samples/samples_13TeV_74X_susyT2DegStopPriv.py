
import PhysicsTools.HeppyCore.framework.config as cfg
#xsec from: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom 
import subprocess


## T2DegStop
## ------------------------------------------------------
#"/T2DegStop_300_270_GEN-SIM/nrad-T2DegStop_300_270_MINIAODv2-RunIISpring15-MCRUN2_74_V9-25ns-4dc17ff0fe241c35c03aa547f2361414/USER"


#old miniaod T2DegStop_300_270_RunII_dir="root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop_300_270_GEN-SIM/T2DegStop_300_270_MINIAOD-RunIISpring15-MCRUN2_74_V9-25ns/008934a25a3583950e0bb876accde101/"
#T2DegStop_300_270_RunII_dir="root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop_300_270_GEN-SIM/T2DegStop_300_270_MINIAODv2-RunIISpring15-MCRUN2_74_V9-25ns/4dc17ff0fe241c35c03aa547f2361414/"
T2DegStop_300_270_RunII_dir="root://xrootd.unl.edu//store/user/nrad/T2DegStop_300_270_GEN-SIM/T2DegStop_300_270_MINIAODv2-RunIISpring15-MCRUN2_74_V9-25ns/4dc17ff0fe241c35c03aa547f2361414/"
#fileList = subprocess.Popen(["gfal-ls "+ T2DegStop_300_270_RunII_dir ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#T2DegStop_300_270_RunII_files=[file[:-1] for file in fileList.stdout.readlines()]
fileList = [
              "T2DegStop_300_270_RunII_25ns_miniAODv2_100_1_1au.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_10_1_aLZ.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_11_1_sgC.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_12_1_iDf.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_13_1_6o0.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_14_1_bv0.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_15_1_9KN.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_16_1_EOz.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_17_1_v07.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_18_1_tBv.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_19_1_z3G.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_1_1_a2Q.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_20_1_aOM.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_21_1_4Wa.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_22_1_N6I.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_23_1_Bi7.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_24_1_FW8.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_25_1_oSl.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_26_1_BBq.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_27_1_5Rx.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_28_1_U5r.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_29_1_2ag.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_2_1_JCa.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_30_1_kwV.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_31_1_enB.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_32_1_ARE.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_33_1_u6N.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_34_1_ZLa.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_35_1_HK2.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_36_1_N5s.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_37_1_VAr.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_38_1_O7O.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_39_1_GfT.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_3_1_Rut.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_40_1_4Hv.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_41_1_1BM.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_42_1_NZA.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_43_1_QVZ.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_44_1_rAi.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_45_1_pUA.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_46_1_w6G.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_47_1_sxj.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_48_1_NSc.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_49_1_vKM.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_4_1_IDD.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_50_1_kfx.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_51_1_R2v.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_52_1_s2y.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_53_1_Cra.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_54_1_b1W.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_55_1_7ir.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_56_1_5ZY.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_57_1_SVz.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_58_1_oIE.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_59_1_VWN.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_5_1_3oh.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_60_1_Olh.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_61_1_tDV.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_62_1_H3N.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_63_1_1t8.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_64_1_7YP.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_65_1_UOt.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_66_1_ELK.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_67_1_JId.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_68_1_D34.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_69_1_tBp.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_6_1_ph1.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_70_1_Fge.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_71_1_W5P.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_72_1_qfx.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_73_1_9D0.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_74_1_DR1.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_75_1_kTe.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_76_1_x4z.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_77_1_XWq.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_78_1_ibr.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_79_1_ih3.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_7_1_1GE.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_80_1_6w8.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_81_1_b6B.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_82_1_mrf.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_83_1_x2Q.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_84_1_9lQ.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_85_1_0Wx.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_86_1_8eg.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_87_1_TiS.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_88_1_yhe.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_89_1_RVd.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_8_1_Lvj.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_90_1_dlX.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_91_1_alh.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_92_1_15D.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_93_1_63r.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_94_1_e0Q.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_95_1_7aa.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_96_1_S1X.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_97_1_Jiz.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_98_1_wly.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_99_1_AtY.root",
              "T2DegStop_300_270_RunII_25ns_miniAODv2_9_1_Lob.root"
                                                                      ]

T2DegStop_300_270 = cfg.MCComponent(
      dataset="/T2DegStop_300_270_GEN-SIM/nrad-T2DegStop_300_270_MINIAOD-RunIISpring15-MCRUN2_74_V9-25ns-008934a25a3583950e0bb876accde101/USER",
      name = "T2DegStop_300_270",
      files =  [T2DegStop_300_270_RunII_dir + x for x in fileList
               ],
      xSection = 8.51615,
      nGenEvents = 1,
      triggers = [],
      effCorrFactor = 1,
  )





