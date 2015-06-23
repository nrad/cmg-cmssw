
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
                'root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop2j_300_270_GENSIM/T2DegStop2j_300_270_MINIAOD/a279b5108ada7c3c0926210c2a95f22e//T2DegStop2j_300_270_miniAOD_9_1_sjf.root'
               ],
      xSection = 8.51615,
      nGenEvents = 1,
      triggers = [],
      effCorrFactor = 1,
  )




T2DegStop_300_270_Phys14_genParticles_dir="root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop2j_300_270_GENSIM/T2DegStop2j_300_270_MINIAOD_withGenParticles-V2/a279b5108ada7c3c0926210c2a95f22e/"
T2DegStop_300_270_Phys14_genParticles_files=[
##"T2DegStop2j_300_270_miniAOD_100_1_C9a.root", ## for somereason this one is messed up!
"T2DegStop2j_300_270_miniAOD_101_1_QgK.root","T2DegStop2j_300_270_miniAOD_102_1_RkD.root","T2DegStop2j_300_270_miniAOD_103_1_PpA.root",
"T2DegStop2j_300_270_miniAOD_104_1_xhz.root","T2DegStop2j_300_270_miniAOD_105_1_Cfi.root","T2DegStop2j_300_270_miniAOD_106_1_PtN.root","T2DegStop2j_300_270_miniAOD_107_1_YM5.root",
"T2DegStop2j_300_270_miniAOD_108_1_KSX.root","T2DegStop2j_300_270_miniAOD_109_1_0bL.root","T2DegStop2j_300_270_miniAOD_10_1_mvq.root","T2DegStop2j_300_270_miniAOD_110_1_BkP.root",
"T2DegStop2j_300_270_miniAOD_111_1_wbM.root","T2DegStop2j_300_270_miniAOD_112_1_9N9.root","T2DegStop2j_300_270_miniAOD_113_1_iJD.root","T2DegStop2j_300_270_miniAOD_114_1_Yty.root",
"T2DegStop2j_300_270_miniAOD_115_1_k58.root","T2DegStop2j_300_270_miniAOD_116_1_x1I.root","T2DegStop2j_300_270_miniAOD_117_1_ESH.root","T2DegStop2j_300_270_miniAOD_118_1_qsp.root",
"T2DegStop2j_300_270_miniAOD_119_1_YQG.root","T2DegStop2j_300_270_miniAOD_11_1_VFo.root","T2DegStop2j_300_270_miniAOD_120_1_2f5.root","T2DegStop2j_300_270_miniAOD_121_1_d1v.root",
"T2DegStop2j_300_270_miniAOD_122_1_0FW.root","T2DegStop2j_300_270_miniAOD_123_1_k7v.root","T2DegStop2j_300_270_miniAOD_124_1_kVz.root","T2DegStop2j_300_270_miniAOD_125_1_rwL.root",
"T2DegStop2j_300_270_miniAOD_126_1_lx7.root","T2DegStop2j_300_270_miniAOD_127_1_wcR.root","T2DegStop2j_300_270_miniAOD_128_1_rFy.root","T2DegStop2j_300_270_miniAOD_129_1_UcL.root",
"T2DegStop2j_300_270_miniAOD_12_1_K8E.root","T2DegStop2j_300_270_miniAOD_130_1_Moa.root","T2DegStop2j_300_270_miniAOD_131_1_din.root","T2DegStop2j_300_270_miniAOD_132_1_C9P.root",
"T2DegStop2j_300_270_miniAOD_133_1_5Tx.root","T2DegStop2j_300_270_miniAOD_134_1_VPf.root","T2DegStop2j_300_270_miniAOD_135_1_pmW.root","T2DegStop2j_300_270_miniAOD_136_1_OQT.root",
"T2DegStop2j_300_270_miniAOD_137_1_ISb.root","T2DegStop2j_300_270_miniAOD_138_1_ySW.root","T2DegStop2j_300_270_miniAOD_139_1_8Ne.root","T2DegStop2j_300_270_miniAOD_13_1_crc.root",
"T2DegStop2j_300_270_miniAOD_140_1_rVF.root","T2DegStop2j_300_270_miniAOD_141_1_wxW.root","T2DegStop2j_300_270_miniAOD_142_1_Oqy.root","T2DegStop2j_300_270_miniAOD_143_1_7qs.root",
"T2DegStop2j_300_270_miniAOD_144_1_sDn.root","T2DegStop2j_300_270_miniAOD_145_1_rUr.root","T2DegStop2j_300_270_miniAOD_146_1_VeD.root","T2DegStop2j_300_270_miniAOD_147_1_rnF.root",
"T2DegStop2j_300_270_miniAOD_148_1_Iw8.root","T2DegStop2j_300_270_miniAOD_149_1_vBi.root","T2DegStop2j_300_270_miniAOD_14_1_kz1.root","T2DegStop2j_300_270_miniAOD_150_1_MQJ.root",
"T2DegStop2j_300_270_miniAOD_151_1_qEi.root","T2DegStop2j_300_270_miniAOD_152_1_6eQ.root","T2DegStop2j_300_270_miniAOD_153_1_Vw1.root","T2DegStop2j_300_270_miniAOD_154_1_8h6.root",
"T2DegStop2j_300_270_miniAOD_155_1_H8g.root","T2DegStop2j_300_270_miniAOD_156_1_Xso.root","T2DegStop2j_300_270_miniAOD_157_1_oku.root","T2DegStop2j_300_270_miniAOD_158_1_PHb.root",
"T2DegStop2j_300_270_miniAOD_159_1_JNp.root","T2DegStop2j_300_270_miniAOD_15_1_tOT.root","T2DegStop2j_300_270_miniAOD_160_1_mIF.root","T2DegStop2j_300_270_miniAOD_161_1_vy1.root",
"T2DegStop2j_300_270_miniAOD_162_1_Abf.root","T2DegStop2j_300_270_miniAOD_163_1_lY6.root","T2DegStop2j_300_270_miniAOD_164_1_161.root","T2DegStop2j_300_270_miniAOD_165_1_Mvg.root",
"T2DegStop2j_300_270_miniAOD_166_1_RD3.root","T2DegStop2j_300_270_miniAOD_167_1_EhA.root","T2DegStop2j_300_270_miniAOD_168_1_0Jr.root","T2DegStop2j_300_270_miniAOD_169_1_o1f.root",
"T2DegStop2j_300_270_miniAOD_16_1_5OA.root","T2DegStop2j_300_270_miniAOD_170_1_kKE.root","T2DegStop2j_300_270_miniAOD_171_1_Lzs.root","T2DegStop2j_300_270_miniAOD_172_1_BI5.root",
"T2DegStop2j_300_270_miniAOD_173_1_yaI.root","T2DegStop2j_300_270_miniAOD_174_1_djd.root","T2DegStop2j_300_270_miniAOD_175_1_AHM.root","T2DegStop2j_300_270_miniAOD_176_1_IR5.root",
"T2DegStop2j_300_270_miniAOD_177_1_i8X.root","T2DegStop2j_300_270_miniAOD_178_1_mL2.root","T2DegStop2j_300_270_miniAOD_179_1_he7.root","T2DegStop2j_300_270_miniAOD_17_1_rSa.root",
"T2DegStop2j_300_270_miniAOD_180_1_e9T.root","T2DegStop2j_300_270_miniAOD_181_1_vr0.root","T2DegStop2j_300_270_miniAOD_182_1_GNl.root","T2DegStop2j_300_270_miniAOD_183_1_WGA.root",
"T2DegStop2j_300_270_miniAOD_184_1_C2O.root","T2DegStop2j_300_270_miniAOD_185_1_OAK.root","T2DegStop2j_300_270_miniAOD_186_1_PZE.root","T2DegStop2j_300_270_miniAOD_187_1_GZM.root",
"T2DegStop2j_300_270_miniAOD_188_1_PXE.root","T2DegStop2j_300_270_miniAOD_189_1_yq3.root","T2DegStop2j_300_270_miniAOD_18_1_Xg9.root","T2DegStop2j_300_270_miniAOD_190_1_zaQ.root",
"T2DegStop2j_300_270_miniAOD_191_1_Qmo.root","T2DegStop2j_300_270_miniAOD_192_1_bXy.root","T2DegStop2j_300_270_miniAOD_193_1_EtQ.root","T2DegStop2j_300_270_miniAOD_194_1_4fS.root",
"T2DegStop2j_300_270_miniAOD_195_1_5ef.root","T2DegStop2j_300_270_miniAOD_198_1_2MC.root","T2DegStop2j_300_270_miniAOD_199_1_s37.root","T2DegStop2j_300_270_miniAOD_19_1_y6g.root",
"T2DegStop2j_300_270_miniAOD_1_1_KE4.root","T2DegStop2j_300_270_miniAOD_200_1_KKE.root","T2DegStop2j_300_270_miniAOD_201_1_FAc.root","T2DegStop2j_300_270_miniAOD_202_1_FH9.root",
"T2DegStop2j_300_270_miniAOD_203_1_T9Y.root","T2DegStop2j_300_270_miniAOD_204_1_0Wv.root","T2DegStop2j_300_270_miniAOD_205_1_xsS.root","T2DegStop2j_300_270_miniAOD_208_1_hY6.root",
"T2DegStop2j_300_270_miniAOD_209_1_6s9.root","T2DegStop2j_300_270_miniAOD_20_1_esL.root","T2DegStop2j_300_270_miniAOD_210_1_g94.root","T2DegStop2j_300_270_miniAOD_211_1_fs4.root",
"T2DegStop2j_300_270_miniAOD_212_1_BQF.root","T2DegStop2j_300_270_miniAOD_213_1_ufE.root","T2DegStop2j_300_270_miniAOD_214_1_uw8.root","T2DegStop2j_300_270_miniAOD_215_1_dsQ.root",
"T2DegStop2j_300_270_miniAOD_216_1_JTs.root","T2DegStop2j_300_270_miniAOD_217_1_l7g.root","T2DegStop2j_300_270_miniAOD_218_1_KRm.root","T2DegStop2j_300_270_miniAOD_219_1_10Z.root",
"T2DegStop2j_300_270_miniAOD_21_1_vLi.root","T2DegStop2j_300_270_miniAOD_220_1_jq7.root","T2DegStop2j_300_270_miniAOD_221_1_W2L.root","T2DegStop2j_300_270_miniAOD_222_1_gKk.root",
"T2DegStop2j_300_270_miniAOD_223_1_DLn.root","T2DegStop2j_300_270_miniAOD_224_1_Iym.root","T2DegStop2j_300_270_miniAOD_225_1_wS8.root","T2DegStop2j_300_270_miniAOD_226_1_ZMd.root",
"T2DegStop2j_300_270_miniAOD_227_1_Mku.root","T2DegStop2j_300_270_miniAOD_228_1_Qnn.root","T2DegStop2j_300_270_miniAOD_229_1_VCp.root","T2DegStop2j_300_270_miniAOD_22_1_nwy.root",
"T2DegStop2j_300_270_miniAOD_232_1_hG1.root","T2DegStop2j_300_270_miniAOD_233_1_1vH.root","T2DegStop2j_300_270_miniAOD_234_1_BQe.root","T2DegStop2j_300_270_miniAOD_235_1_a9Q.root",
"T2DegStop2j_300_270_miniAOD_236_1_HkJ.root","T2DegStop2j_300_270_miniAOD_237_1_2bg.root","T2DegStop2j_300_270_miniAOD_238_1_brs.root","T2DegStop2j_300_270_miniAOD_239_1_7JR.root",
"T2DegStop2j_300_270_miniAOD_23_1_ZOf.root","T2DegStop2j_300_270_miniAOD_240_1_KC5.root","T2DegStop2j_300_270_miniAOD_241_1_Mig.root","T2DegStop2j_300_270_miniAOD_242_1_40n.root",
"T2DegStop2j_300_270_miniAOD_243_1_9kr.root","T2DegStop2j_300_270_miniAOD_244_1_zm5.root","T2DegStop2j_300_270_miniAOD_245_1_S5o.root","T2DegStop2j_300_270_miniAOD_246_1_zhy.root",
"T2DegStop2j_300_270_miniAOD_247_1_FS0.root","T2DegStop2j_300_270_miniAOD_248_1_kSx.root","T2DegStop2j_300_270_miniAOD_249_1_c1x.root","T2DegStop2j_300_270_miniAOD_24_1_8j1.root",
"T2DegStop2j_300_270_miniAOD_250_1_hgo.root","T2DegStop2j_300_270_miniAOD_251_1_1ex.root","T2DegStop2j_300_270_miniAOD_252_1_xxC.root","T2DegStop2j_300_270_miniAOD_253_1_gvV.root",
"T2DegStop2j_300_270_miniAOD_254_1_siS.root","T2DegStop2j_300_270_miniAOD_255_1_QqP.root","T2DegStop2j_300_270_miniAOD_256_1_Mf9.root","T2DegStop2j_300_270_miniAOD_257_1_LoE.root",
"T2DegStop2j_300_270_miniAOD_258_1_EYm.root","T2DegStop2j_300_270_miniAOD_259_1_JCK.root","T2DegStop2j_300_270_miniAOD_25_1_viB.root","T2DegStop2j_300_270_miniAOD_260_1_BRV.root",
"T2DegStop2j_300_270_miniAOD_261_1_LWI.root","T2DegStop2j_300_270_miniAOD_262_1_hQ3.root","T2DegStop2j_300_270_miniAOD_263_1_n5A.root","T2DegStop2j_300_270_miniAOD_264_1_PX6.root",
"T2DegStop2j_300_270_miniAOD_265_1_V0N.root","T2DegStop2j_300_270_miniAOD_266_1_kHm.root","T2DegStop2j_300_270_miniAOD_267_1_njV.root","T2DegStop2j_300_270_miniAOD_268_1_0Fc.root",
"T2DegStop2j_300_270_miniAOD_269_1_KU3.root","T2DegStop2j_300_270_miniAOD_26_1_KZ3.root","T2DegStop2j_300_270_miniAOD_270_1_Ijz.root","T2DegStop2j_300_270_miniAOD_271_1_V7g.root",
"T2DegStop2j_300_270_miniAOD_272_1_G8E.root","T2DegStop2j_300_270_miniAOD_273_1_trK.root","T2DegStop2j_300_270_miniAOD_274_1_4Bs.root","T2DegStop2j_300_270_miniAOD_275_1_DOL.root",
"T2DegStop2j_300_270_miniAOD_276_1_nvL.root","T2DegStop2j_300_270_miniAOD_277_1_Y2G.root","T2DegStop2j_300_270_miniAOD_278_1_Sqo.root","T2DegStop2j_300_270_miniAOD_279_1_RcP.root",
"T2DegStop2j_300_270_miniAOD_27_1_QpG.root","T2DegStop2j_300_270_miniAOD_280_1_oqN.root","T2DegStop2j_300_270_miniAOD_281_1_rBG.root","T2DegStop2j_300_270_miniAOD_282_1_Kw9.root",
"T2DegStop2j_300_270_miniAOD_283_1_9aZ.root","T2DegStop2j_300_270_miniAOD_284_1_uB3.root","T2DegStop2j_300_270_miniAOD_285_1_NU2.root","T2DegStop2j_300_270_miniAOD_286_1_D6P.root",
"T2DegStop2j_300_270_miniAOD_287_1_tEk.root","T2DegStop2j_300_270_miniAOD_288_1_9Cy.root","T2DegStop2j_300_270_miniAOD_289_1_od8.root","T2DegStop2j_300_270_miniAOD_28_1_NOj.root",
"T2DegStop2j_300_270_miniAOD_290_1_5hz.root","T2DegStop2j_300_270_miniAOD_291_1_wfw.root","T2DegStop2j_300_270_miniAOD_292_1_Ox5.root","T2DegStop2j_300_270_miniAOD_293_1_4eJ.root",
"T2DegStop2j_300_270_miniAOD_294_1_r3s.root","T2DegStop2j_300_270_miniAOD_295_1_Goz.root","T2DegStop2j_300_270_miniAOD_296_1_kID.root","T2DegStop2j_300_270_miniAOD_297_1_5I5.root",
"T2DegStop2j_300_270_miniAOD_298_1_nvc.root","T2DegStop2j_300_270_miniAOD_299_1_V7B.root","T2DegStop2j_300_270_miniAOD_29_1_aN1.root","T2DegStop2j_300_270_miniAOD_2_1_2kH.root",
"T2DegStop2j_300_270_miniAOD_300_1_2li.root","T2DegStop2j_300_270_miniAOD_301_1_69q.root","T2DegStop2j_300_270_miniAOD_302_1_Waj.root","T2DegStop2j_300_270_miniAOD_303_1_Wuq.root",
"T2DegStop2j_300_270_miniAOD_304_1_LPC.root","T2DegStop2j_300_270_miniAOD_305_1_q8s.root","T2DegStop2j_300_270_miniAOD_306_1_EgA.root","T2DegStop2j_300_270_miniAOD_307_1_onL.root",
"T2DegStop2j_300_270_miniAOD_308_1_kE9.root","T2DegStop2j_300_270_miniAOD_309_1_Do0.root","T2DegStop2j_300_270_miniAOD_30_1_Dbz.root","T2DegStop2j_300_270_miniAOD_310_1_jCy.root",
"T2DegStop2j_300_270_miniAOD_311_1_Wiq.root","T2DegStop2j_300_270_miniAOD_312_1_ovB.root","T2DegStop2j_300_270_miniAOD_313_1_NyM.root","T2DegStop2j_300_270_miniAOD_314_1_ZrB.root",
"T2DegStop2j_300_270_miniAOD_315_1_8MT.root","T2DegStop2j_300_270_miniAOD_316_1_3WA.root","T2DegStop2j_300_270_miniAOD_317_1_ABa.root","T2DegStop2j_300_270_miniAOD_318_1_koi.root",
"T2DegStop2j_300_270_miniAOD_319_1_TG6.root","T2DegStop2j_300_270_miniAOD_31_1_CwZ.root","T2DegStop2j_300_270_miniAOD_320_1_ew2.root","T2DegStop2j_300_270_miniAOD_321_1_1M2.root",
"T2DegStop2j_300_270_miniAOD_322_1_PeQ.root","T2DegStop2j_300_270_miniAOD_323_1_W5Q.root","T2DegStop2j_300_270_miniAOD_324_1_r1S.root","T2DegStop2j_300_270_miniAOD_325_1_Caa.root",
"T2DegStop2j_300_270_miniAOD_326_1_LC9.root","T2DegStop2j_300_270_miniAOD_327_1_UzA.root","T2DegStop2j_300_270_miniAOD_328_1_zyl.root","T2DegStop2j_300_270_miniAOD_329_1_tzU.root",
"T2DegStop2j_300_270_miniAOD_330_1_cCW.root","T2DegStop2j_300_270_miniAOD_331_1_9t2.root","T2DegStop2j_300_270_miniAOD_332_1_TP1.root","T2DegStop2j_300_270_miniAOD_333_1_5i6.root",
"T2DegStop2j_300_270_miniAOD_334_1_MGx.root","T2DegStop2j_300_270_miniAOD_335_1_uLC.root","T2DegStop2j_300_270_miniAOD_336_1_odK.root","T2DegStop2j_300_270_miniAOD_337_1_hUG.root",
"T2DegStop2j_300_270_miniAOD_338_1_yx8.root","T2DegStop2j_300_270_miniAOD_339_1_FI4.root","T2DegStop2j_300_270_miniAOD_340_1_5kJ.root","T2DegStop2j_300_270_miniAOD_341_1_r5E.root",
"T2DegStop2j_300_270_miniAOD_342_1_46x.root","T2DegStop2j_300_270_miniAOD_343_1_50v.root","T2DegStop2j_300_270_miniAOD_344_1_UG2.root","T2DegStop2j_300_270_miniAOD_345_1_WiW.root",
"T2DegStop2j_300_270_miniAOD_346_1_Nyn.root","T2DegStop2j_300_270_miniAOD_347_1_2Ar.root","T2DegStop2j_300_270_miniAOD_348_1_Cp4.root","T2DegStop2j_300_270_miniAOD_349_1_Mj5.root",
"T2DegStop2j_300_270_miniAOD_34_1_9xa.root","T2DegStop2j_300_270_miniAOD_350_1_VfM.root","T2DegStop2j_300_270_miniAOD_351_1_BJC.root","T2DegStop2j_300_270_miniAOD_352_1_tlz.root",
"T2DegStop2j_300_270_miniAOD_353_1_h2s.root","T2DegStop2j_300_270_miniAOD_354_1_Wqk.root","T2DegStop2j_300_270_miniAOD_355_1_yrd.root","T2DegStop2j_300_270_miniAOD_358_1_n9T.root",
"T2DegStop2j_300_270_miniAOD_359_1_nv6.root","T2DegStop2j_300_270_miniAOD_35_1_iKL.root","T2DegStop2j_300_270_miniAOD_360_1_gLX.root","T2DegStop2j_300_270_miniAOD_361_1_MZB.root",
"T2DegStop2j_300_270_miniAOD_362_1_W6Y.root","T2DegStop2j_300_270_miniAOD_363_1_xh4.root","T2DegStop2j_300_270_miniAOD_364_1_89K.root","T2DegStop2j_300_270_miniAOD_365_1_7RU.root",
"T2DegStop2j_300_270_miniAOD_366_1_jxM.root","T2DegStop2j_300_270_miniAOD_367_1_016.root","T2DegStop2j_300_270_miniAOD_368_1_llb.root","T2DegStop2j_300_270_miniAOD_369_1_380.root",
"T2DegStop2j_300_270_miniAOD_36_1_uMG.root","T2DegStop2j_300_270_miniAOD_370_1_hcL.root","T2DegStop2j_300_270_miniAOD_371_1_EoK.root","T2DegStop2j_300_270_miniAOD_372_1_QrW.root",
"T2DegStop2j_300_270_miniAOD_373_1_zdn.root","T2DegStop2j_300_270_miniAOD_374_1_kmF.root","T2DegStop2j_300_270_miniAOD_375_1_wGi.root","T2DegStop2j_300_270_miniAOD_376_1_01C.root",
"T2DegStop2j_300_270_miniAOD_377_1_wOq.root","T2DegStop2j_300_270_miniAOD_378_1_a5n.root","T2DegStop2j_300_270_miniAOD_379_1_P6R.root","T2DegStop2j_300_270_miniAOD_37_1_u4d.root",
"T2DegStop2j_300_270_miniAOD_380_1_BD8.root","T2DegStop2j_300_270_miniAOD_381_1_Uk8.root","T2DegStop2j_300_270_miniAOD_382_1_waj.root","T2DegStop2j_300_270_miniAOD_383_1_ThM.root",
"T2DegStop2j_300_270_miniAOD_384_1_2rn.root","T2DegStop2j_300_270_miniAOD_385_1_2Nh.root","T2DegStop2j_300_270_miniAOD_386_1_1aJ.root","T2DegStop2j_300_270_miniAOD_387_1_JFL.root",
"T2DegStop2j_300_270_miniAOD_388_1_IJk.root","T2DegStop2j_300_270_miniAOD_389_1_5AO.root","T2DegStop2j_300_270_miniAOD_38_1_n6J.root","T2DegStop2j_300_270_miniAOD_390_1_Oys.root",
"T2DegStop2j_300_270_miniAOD_391_1_4CU.root","T2DegStop2j_300_270_miniAOD_392_1_5UO.root",
"T2DegStop2j_300_270_miniAOD_393_1_0Hn.root","T2DegStop2j_300_270_miniAOD_394_1_ddG.root",
"T2DegStop2j_300_270_miniAOD_395_1_cQE.root","T2DegStop2j_300_270_miniAOD_396_1_3yZ.root",
"T2DegStop2j_300_270_miniAOD_397_1_Ixs.root","T2DegStop2j_300_270_miniAOD_398_1_yfr.root",
"T2DegStop2j_300_270_miniAOD_399_1_w6M.root","T2DegStop2j_300_270_miniAOD_39_1_yvn.root",
"T2DegStop2j_300_270_miniAOD_3_1_3cg.root","T2DegStop2j_300_270_miniAOD_400_1_yGZ.root",
"T2DegStop2j_300_270_miniAOD_401_1_mDa.root","T2DegStop2j_300_270_miniAOD_402_1_tYX.root",
"T2DegStop2j_300_270_miniAOD_403_1_ODF.root","T2DegStop2j_300_270_miniAOD_404_1_qHN.root",
"T2DegStop2j_300_270_miniAOD_405_1_sbI.root","T2DegStop2j_300_270_miniAOD_406_1_y3E.root",
"T2DegStop2j_300_270_miniAOD_407_1_zyo.root","T2DegStop2j_300_270_miniAOD_408_1_9sT.root",
"T2DegStop2j_300_270_miniAOD_409_1_4B2.root","T2DegStop2j_300_270_miniAOD_40_1_bDM.root",
"T2DegStop2j_300_270_miniAOD_410_1_QEv.root","T2DegStop2j_300_270_miniAOD_411_1_7R6.root",
"T2DegStop2j_300_270_miniAOD_412_1_xAp.root","T2DegStop2j_300_270_miniAOD_413_1_Nbu.root",
"T2DegStop2j_300_270_miniAOD_414_1_kM1.root","T2DegStop2j_300_270_miniAOD_415_1_jcX.root",
"T2DegStop2j_300_270_miniAOD_416_1_vyO.root","T2DegStop2j_300_270_miniAOD_417_1_Z6r.root",
"T2DegStop2j_300_270_miniAOD_418_1_vyP.root","T2DegStop2j_300_270_miniAOD_419_1_T2T.root",
"T2DegStop2j_300_270_miniAOD_41_1_q4e.root","T2DegStop2j_300_270_miniAOD_420_1_QsE.root",
"T2DegStop2j_300_270_miniAOD_423_1_hN6.root","T2DegStop2j_300_270_miniAOD_424_1_ScP.root",
"T2DegStop2j_300_270_miniAOD_425_1_FGu.root","T2DegStop2j_300_270_miniAOD_426_1_bgg.root",
"T2DegStop2j_300_270_miniAOD_427_1_0wP.root","T2DegStop2j_300_270_miniAOD_428_1_O2Y.root",
"T2DegStop2j_300_270_miniAOD_429_1_cy7.root","T2DegStop2j_300_270_miniAOD_42_1_gHb.root",
"T2DegStop2j_300_270_miniAOD_430_1_wkr.root","T2DegStop2j_300_270_miniAOD_431_1_VQL.root",
"T2DegStop2j_300_270_miniAOD_432_1_Ysm.root","T2DegStop2j_300_270_miniAOD_433_1_mH6.root",
"T2DegStop2j_300_270_miniAOD_434_1_h5T.root","T2DegStop2j_300_270_miniAOD_435_1_yZa.root",
"T2DegStop2j_300_270_miniAOD_436_1_x7j.root","T2DegStop2j_300_270_miniAOD_437_1_O9Q.root",
"T2DegStop2j_300_270_miniAOD_438_1_VFG.root","T2DegStop2j_300_270_miniAOD_439_1_BLR.root",
"T2DegStop2j_300_270_miniAOD_43_1_klZ.root","T2DegStop2j_300_270_miniAOD_440_1_Lr6.root",
"T2DegStop2j_300_270_miniAOD_441_1_eOB.root","T2DegStop2j_300_270_miniAOD_442_1_CRO.root",
"T2DegStop2j_300_270_miniAOD_443_1_z8p.root","T2DegStop2j_300_270_miniAOD_444_1_zF4.root",
"T2DegStop2j_300_270_miniAOD_445_1_jqN.root","T2DegStop2j_300_270_miniAOD_446_1_k6U.root",
"T2DegStop2j_300_270_miniAOD_447_1_H30.root","T2DegStop2j_300_270_miniAOD_448_1_jiY.root",
"T2DegStop2j_300_270_miniAOD_449_1_pot.root","T2DegStop2j_300_270_miniAOD_44_1_CPM.root",
"T2DegStop2j_300_270_miniAOD_450_1_mcj.root","T2DegStop2j_300_270_miniAOD_451_1_1NQ.root",
"T2DegStop2j_300_270_miniAOD_452_1_olk.root","T2DegStop2j_300_270_miniAOD_453_1_N8Z.root",
"T2DegStop2j_300_270_miniAOD_454_1_5ku.root","T2DegStop2j_300_270_miniAOD_455_1_jP1.root",
"T2DegStop2j_300_270_miniAOD_456_1_fEV.root","T2DegStop2j_300_270_miniAOD_457_1_cEk.root",
"T2DegStop2j_300_270_miniAOD_458_1_2O5.root","T2DegStop2j_300_270_miniAOD_459_1_SVt.root",
"T2DegStop2j_300_270_miniAOD_45_1_aKn.root","T2DegStop2j_300_270_miniAOD_460_1_Frj.root",
"T2DegStop2j_300_270_miniAOD_461_1_YPc.root","T2DegStop2j_300_270_miniAOD_462_1_jXD.root",
"T2DegStop2j_300_270_miniAOD_463_1_GV1.root","T2DegStop2j_300_270_miniAOD_464_1_2Us.root",
"T2DegStop2j_300_270_miniAOD_465_1_YbZ.root","T2DegStop2j_300_270_miniAOD_466_1_q1D.root",
"T2DegStop2j_300_270_miniAOD_467_1_uPO.root","T2DegStop2j_300_270_miniAOD_468_1_zEu.root",
"T2DegStop2j_300_270_miniAOD_469_1_PYn.root","T2DegStop2j_300_270_miniAOD_46_1_Je1.root",
"T2DegStop2j_300_270_miniAOD_470_1_sB6.root","T2DegStop2j_300_270_miniAOD_471_1_8By.root",
"T2DegStop2j_300_270_miniAOD_472_1_IA8.root","T2DegStop2j_300_270_miniAOD_473_1_VCm.root",
"T2DegStop2j_300_270_miniAOD_474_1_igy.root","T2DegStop2j_300_270_miniAOD_475_1_DLY.root",
"T2DegStop2j_300_270_miniAOD_476_1_0VS.root","T2DegStop2j_300_270_miniAOD_477_1_3qV.root",
"T2DegStop2j_300_270_miniAOD_478_1_JnV.root","T2DegStop2j_300_270_miniAOD_479_1_VlO.root",
"T2DegStop2j_300_270_miniAOD_47_1_pBi.root","T2DegStop2j_300_270_miniAOD_480_1_NMc.root",
"T2DegStop2j_300_270_miniAOD_481_1_9pI.root","T2DegStop2j_300_270_miniAOD_482_1_GgM.root",
"T2DegStop2j_300_270_miniAOD_483_1_wjO.root","T2DegStop2j_300_270_miniAOD_484_1_eJe.root",
"T2DegStop2j_300_270_miniAOD_485_1_Whi.root","T2DegStop2j_300_270_miniAOD_486_1_5jR.root",
"T2DegStop2j_300_270_miniAOD_487_1_Qp9.root","T2DegStop2j_300_270_miniAOD_488_1_N1E.root",
"T2DegStop2j_300_270_miniAOD_489_1_W05.root","T2DegStop2j_300_270_miniAOD_48_1_aU1.root",
"T2DegStop2j_300_270_miniAOD_490_1_3Et.root","T2DegStop2j_300_270_miniAOD_491_1_WGw.root",
"T2DegStop2j_300_270_miniAOD_492_1_LFP.root","T2DegStop2j_300_270_miniAOD_493_1_mXs.root",
"T2DegStop2j_300_270_miniAOD_494_1_6Ew.root","T2DegStop2j_300_270_miniAOD_495_1_toL.root",
"T2DegStop2j_300_270_miniAOD_496_1_L2e.root","T2DegStop2j_300_270_miniAOD_497_1_InP.root",
"T2DegStop2j_300_270_miniAOD_49_1_C0F.root","T2DegStop2j_300_270_miniAOD_4_1_T1h.root",
"T2DegStop2j_300_270_miniAOD_50_1_V5k.root","T2DegStop2j_300_270_miniAOD_51_1_y4D.root",
"T2DegStop2j_300_270_miniAOD_52_1_1vJ.root","T2DegStop2j_300_270_miniAOD_53_1_wTe.root",
"T2DegStop2j_300_270_miniAOD_54_1_m1C.root","T2DegStop2j_300_270_miniAOD_55_1_rjX.root",
"T2DegStop2j_300_270_miniAOD_56_1_HVd.root","T2DegStop2j_300_270_miniAOD_57_1_UHq.root",
"T2DegStop2j_300_270_miniAOD_58_1_jdL.root","T2DegStop2j_300_270_miniAOD_59_1_Zw9.root",
"T2DegStop2j_300_270_miniAOD_5_1_C27.root","T2DegStop2j_300_270_miniAOD_60_1_NHC.root",
"T2DegStop2j_300_270_miniAOD_61_1_zv0.root","T2DegStop2j_300_270_miniAOD_62_1_ThN.root",
"T2DegStop2j_300_270_miniAOD_63_1_8by.root","T2DegStop2j_300_270_miniAOD_64_1_Kv1.root",
"T2DegStop2j_300_270_miniAOD_65_1_4YX.root","T2DegStop2j_300_270_miniAOD_66_1_wcG.root",
"T2DegStop2j_300_270_miniAOD_67_1_FQ3.root","T2DegStop2j_300_270_miniAOD_68_1_32a.root",
"T2DegStop2j_300_270_miniAOD_69_1_zO5.root","T2DegStop2j_300_270_miniAOD_6_1_WTa.root",
"T2DegStop2j_300_270_miniAOD_70_1_8pY.root","T2DegStop2j_300_270_miniAOD_71_1_0cn.root",
"T2DegStop2j_300_270_miniAOD_72_1_nWD.root","T2DegStop2j_300_270_miniAOD_73_1_jy3.root",
"T2DegStop2j_300_270_miniAOD_74_1_g4L.root","T2DegStop2j_300_270_miniAOD_75_1_U5w.root",
"T2DegStop2j_300_270_miniAOD_76_1_yK3.root","T2DegStop2j_300_270_miniAOD_77_1_OcC.root",
"T2DegStop2j_300_270_miniAOD_78_1_fBC.root","T2DegStop2j_300_270_miniAOD_79_1_AC9.root",
"T2DegStop2j_300_270_miniAOD_7_1_KH7.root","T2DegStop2j_300_270_miniAOD_80_1_cBu.root",
"T2DegStop2j_300_270_miniAOD_81_1_Ap8.root","T2DegStop2j_300_270_miniAOD_82_1_GA6.root",
"T2DegStop2j_300_270_miniAOD_83_1_pRR.root","T2DegStop2j_300_270_miniAOD_84_1_8Oo.root",
"T2DegStop2j_300_270_miniAOD_85_1_ZXq.root","T2DegStop2j_300_270_miniAOD_86_1_Kvn.root",
"T2DegStop2j_300_270_miniAOD_87_1_NPl.root","T2DegStop2j_300_270_miniAOD_88_1_0zw.root",
"T2DegStop2j_300_270_miniAOD_89_1_k3O.root","T2DegStop2j_300_270_miniAOD_8_1_Dwp.root",
"T2DegStop2j_300_270_miniAOD_90_1_TAj.root","T2DegStop2j_300_270_miniAOD_91_1_EHJ.root",
"T2DegStop2j_300_270_miniAOD_92_1_baE.root","T2DegStop2j_300_270_miniAOD_93_1_mHD.root",
"T2DegStop2j_300_270_miniAOD_94_1_mWz.root","T2DegStop2j_300_270_miniAOD_95_1_WvQ.root",
"T2DegStop2j_300_270_miniAOD_96_1_IIM.root","T2DegStop2j_300_270_miniAOD_97_1_E9Y.root",
"T2DegStop2j_300_270_miniAOD_98_1_gMg.root","T2DegStop2j_300_270_miniAOD_99_1_szs.root",
"T2DegStop2j_300_270_miniAOD_9_1_P3r.root",
]




T2DegStop_300_270_Phys14_genParticles = cfg.MCComponent(
      dataset="/T2DegStop2j_300_270_GENSIM/nrad-T2DegStop2j_300_270_MINIAOD-a279b5108ada7c3c0926210c2a95f22e/USER",
      name = "T2DegStop_300_270_Phys14_genParticles",
      files =  [T2DegStop_300_270_Phys14_genParticles_dir + x for x in T2DegStop_300_270_Phys14_genParticles_files
               ],
      xSection = 8.51615,
      nGenEvents = 1,
      triggers = [],
      effCorrFactor = 1,
  )




import subprocess

T2DegStop_300_270_RunII_genParticles_dir="root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop_300_270_GEN-SIM/T2DegStop_300_270_MINIAOD-RunIISpring15-MCRUN2_74_V9-25ns/008934a25a3583950e0bb876accde101/"
fileList = subprocess.Popen(["gfal-ls "+ T2DegStop_300_270_RunII_genParticles_dir ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
T2DegStop_300_270_RunII_genParticles_files=[file[:-1] for file in fileList.stdout.readlines()]



T2DegStop_300_270_RunII_genParticles = cfg.MCComponent(
      dataset="/T2DegStop_300_270_GEN-SIM/nrad-T2DegStop_300_270_MINIAOD-RunIISpring15-MCRUN2_74_V9-25ns-008934a25a3583950e0bb876accde101/USER",
      name = "T2DegStop_300_270_RunII_genParticles",
      files =  [T2DegStop_300_270_RunII_genParticles_dir + x for x in T2DegStop_300_270_RunII_genParticles_files
               ],
      xSection = 8.51615,
      nGenEvents = 1,
      triggers = [],
      effCorrFactor = 1,
  )





