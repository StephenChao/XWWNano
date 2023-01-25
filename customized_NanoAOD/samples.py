from commands import getoutput
from optparse   import OptionParser
import os
import re
import json

class DAS:
    def __init__( self, DAS = {}, Nfiles = {} ):
        self.DAS = {}
        for ids in DAS:
            ds = self.DASName(ids)
            self.DAS[ds] = {}
            self.DAS[ds]["dataset"] = ids
            self.DAS[ds]["nfiles"]  = Nfiles.get(ds,1)

    def DASName(self,ids):
        ds = None
        if "stash" in ids:
            ids = os.path.normpath(ids)
            if "/stash/user/" in ids:
                ds = ids.split("/")[-1]
                if "log" in ds:
                    ds = ids.split("/")[-2]+ids.split("/")[-1]
        else :
            if "MINIAOD" in ids.split("/")[3]:
                ds = ids.split("/")[1] + "_" + ids.split("/")[2]
            if "MiniAODAPVv2" in ids : ds += "_APV"
        return ds

    def update(DAS, Nfiles = {}):
        for ds in DAS:
            self.DAS[ds] = {}
            self.DAS[ds]["dataset"] = DAS[ds]
            self.DAS[ds]["nfiles"]  = Nfiles.get(ds,1)
        for ds in self.DAS:
            self.DAS[ds]["nfiles"]  = Nfiles.get(ds,self.DAS[ds]["nfiles"])

    def FetchDataset(self,DAS,year,mc = True):
        self.DAS = {}
        Files = []
        if mc : MINIAOD = "MINIAODSIM"
        if not mc : MINIAOD = "MINIAOD"
        for ds in list(set(DAS)):
            File = getoutput('/cvmfs/cms.cern.ch/common/dasgoclient --query="dataset dataset=/%s/*20UL*MiniAOD*/%s" -limit=0 '%(ds,MINIAOD))
            Files += File.split("\n")
        if mc :
            if year == "16" : Version = r"(.*)20UL16(.*)(MiniAODv2|MiniAODAPVv2)(.*)"
            if year == "16APV" : Version = r"(.*)20UL16(.*)MiniAODAPVv2(.*)"
            if year == "16NonAPV" : Version = r"(.*)20UL16(.*)MiniAODv2(.*)"
            if year == "17" : Version = r"(.*)20UL17(.*)(MiniAODv2)(.*)"
            if year == "18" : Version = r"(.*)20UL18(.*)(MiniAODv2)(.*)"
        Files_ = []
        for ifile in list(set(Files)):
            version = re.compile(Version)
            if version.search(ifile):
                Files_.append(ifile)
        Files_.sort()
        with open("dataset.json","w") as f:
            json.dump(Files_,f,indent=4)
        return Files


DAS_2016_Common_    = [
    "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
]

DAS_2017_0Lepton_test_ = [
    "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
]

DAS_2017_0Lepton_ = [
    "/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
    "/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
    "/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
    "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
    "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
    "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
    "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
    "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
    "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
    "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-PUForMUOVal_106X_mc2017_realistic_v9_ext1-v2/MINIAODSIM",
    "/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
    "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
    "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9_ext1-v2/MINIAODSIM",
    "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
    "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9_ext1-v2/MINIAODSIM",
    "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
    "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
    "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9_ext1-v2/MINIAODSIM",
    "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
    "/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
    "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
    "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9_ext1-v2/MINIAODSIM",
    "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
    "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
    "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
    "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
]

DAS_2017_0Lepton_Missing_ = [
    "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
    "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
    "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
]

DAS_2018_0Lepton_Missing_ = [
    "/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
    "/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
    "/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
]

DAS_2016_1lepton_    = [
    "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
    "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
    "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
    "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
    "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
    "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
    "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
    "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
    "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
    "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
    "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
    "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
    "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
    "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
    "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
    "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
    "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
    "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
    "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
    "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
    "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
    "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
    "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
    "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/MINIAODSIM",
    "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
    "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
    "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_ext1-v2/MINIAODSIM",
    "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
    "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
    "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_ext1-v2/MINIAODSIM",
    "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
]

DAS_2016_1lepton_Data_ = [
    "/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
    "/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
    "/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
    "/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
    "/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
    "/SingleMuon/Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
    "/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
    "/SingleMuon/Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
    "/SingleMuon/Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
]

DAS_2017_0lepton_Data_ = [
    "/JetHT/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
    "/JetHT/Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
    "/JetHT/Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
    "/JetHT/Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
    "/JetHT/Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
]

DAS_2017_0lepton_Data_test_ = [
    "/JetHT/Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
]


CMSC_2017_0Lepton_MC_ = [
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/TTToHadronic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-PUForMUOVal_106X_mc2017_realistic_v9_ext1-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WW_TuneCP5_13TeV-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9_ext1-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9_ext1-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WZ_TuneCP5_13TeV-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9_ext1-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ZZ_TuneCP5_13TeV-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9_ext1-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
]

CMSC_2017_0Lepton_MC_missing_ = [
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V2/MC/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V2/MC/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V2/MC/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
]

CMSC_2017_0Lepton_MC_missing2_ = [
    "/stash/user/yuzhe/public/0lepton/custom_nano/2017MissingMC/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/2017MissingMC/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/2017MissingMC/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/2017MissingMC/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",    
]
CMSC_2017_MC_ = [ 
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/TTToHadronic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-PUForMUOVal_106X_mc2017_realistic_v9_ext1-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WW_TuneCP5_13TeV-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9_ext1-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9_ext1-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WZ_TuneCP5_13TeV-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9_ext1-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/WZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ZZ_TuneCP5_13TeV-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9_ext1-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/MC/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
  
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V2/MC/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V2/MC/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V2/MC/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",

    "/stash/user/yuzhe/public/0lepton/custom_nano/2017MissingMC/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/2017MissingMC/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/2017MissingMC/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/2017MissingMC/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",    

]
CMSC_2018_0Lepton_MC_ = [
    "/stash/user/yuzhe/public/0lepton/custom_nano/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/log1",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/log2",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/log3",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/log4",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/log5",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/log6",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/log7",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log1",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log10",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log2",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log3",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log4",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log5",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log6",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log7",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log9",
    "/stash/user/yuzhe/public/0lepton/custom_nano/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/WW_TuneCP5_13TeV-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/WZ_TuneCP5_13TeV-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/ZZTo2Q2Nu_TuneCP5_13TeV-amcatnloFXFX-pythia8",
]

CMSC_2018_0Lepton_MC_missing_ = [
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2018/V2/MC/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2018/V2/MC/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2018/V2/MC/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
]
CMSC_2018_MC_ = [ 
    "/stash/user/yuzhe/public/0lepton/custom_nano/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/log1",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/log2",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/log3",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/log4",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/log5",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/log6",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/log7",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log1",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log10",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log2",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log3",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log4",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log5",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log6",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log7",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/log9",
    "/stash/user/yuzhe/public/0lepton/custom_nano/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/WW_TuneCP5_13TeV-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/WZ_TuneCP5_13TeV-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    "/stash/user/yuzhe/public/0lepton/custom_nano/ZZTo2Q2Nu_TuneCP5_13TeV-amcatnloFXFX-pythia8",

    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2018/V2/MC/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2018/V2/MC/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2018/V2/MC/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",

 
]

CMSC_2016APV_Other_ =  [ 
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2016APV/HWminusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2016APV/HWplusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2016APV/HZJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2016APV/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2016APV/VBFHToWWToLNuQQ_M-125_TuneCP5_withDipoleRecoil_13TeV_powheg_jhugen751_pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3_APV",
]
CMSC_2016_Other_ =  [ 
 "/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2016/HWminusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
 "/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2016/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
 "/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2016/HWplusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1",

 "/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2016/HZJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
]
CMSC_2017_Other_ =  [ 
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2017/HWminusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2017/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2017/HWplusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2017/VBFHToWWToLNuQQ_M-125_TuneCP5_withDipoleRecoil_13TeV_powheg_jhugen751_pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v3",
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2017/HZJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
]
CMSC_2018_Other_ =  [ 
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2018/HWminusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2018/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2018/HWplusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2018/VBFHToWWToLNuQQ_M-125_TuneCP5_withDipoleRecoil_13TeV_powheg_jhugen751_pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3",
"/stash/user/yuzhe/public/0lepton/custom_nano/OtherChannels/2018/HZJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
]

############## HWW part begin  ##################


CMSC_2017_HWWSignal_ =[
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/Signal/GluGluHToWW_Pt-200ToInf_M-125_TuneCP5_MINLO_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/Signal/HWminusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/Signal/HWplusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/Signal/HZJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/Signal/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/Signal/VBFHToWWToLNuQQ_M-125_TuneCP5_withDipoleRecoil_13TeV_powheg_jhugen751_pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v3",
]
CMSC_2016_HWWSignal_ =[ 
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/Signal/GluGluHToWW_Pt-200ToInf_M-125_TuneCP5_MINLO_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/Signal/HWminusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/Signal/HWplusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/Signal/HZJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/Signal/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/Signal/VBFHToWWToLNuQQ_M-125_TuneCP5_withDipoleRecoil_13TeV_powheg_jhugen751_pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v5",
]
CMSC_2016APV_HWWSignal_ = [ 
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/Signal/GluGluHToWW_Pt-200ToInf_M-125_TuneCP5_MINLO_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/Signal/HWminusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/Signal/HWplusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/Signal/HZJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/Signal/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/Signal/VBFHToWWToLNuQQ_M-125_TuneCP5_withDipoleRecoil_13TeV_powheg_jhugen751_pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3_APV",

]
CMSC_2018_HWWSignal_ =[ 
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/Signal/GluGluHToWW_Pt-200ToInf_M-125_TuneCP5_MINLO_13TeV-powheg-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/Signal/HWminusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/Signal/HWplusJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/Signal/HZJ_HToWW_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/Signal/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/Signal/VBFHToWWToLNuQQ_M-125_TuneCP5_withDipoleRecoil_13TeV_powheg_jhugen751_pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3",
]

CMSC_2016_HWWBKG_ = [ 
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v3",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v3",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/TTToHadronic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/WW_TuneCP5_13TeV-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/WZ_TuneCP5_13TeV-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/MC/ZZ_TuneCP5_13TeV-pythia8_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1",
]

CMSC_2016APV_HWWBKG_ = [ 
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/TTToHadronic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/WW_TuneCP5_13TeV-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/WZ_TuneCP5_13TeV-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_APV",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/MC/ZZ_TuneCP5_13TeV-pythia8_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_APV",
]

CMSC_2017_HWWBKG_ = [ 
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/TTToHadronic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/WW_TuneCP5_13TeV-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/WZ_TuneCP5_13TeV-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/MC/ZZ_TuneCP5_13TeV-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1",
]

CMSC_2018_HWWBKG_ = [ 
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/TTToHadronic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/WW_TuneCP5_13TeV-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/WZ_TuneCP5_13TeV-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
"/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/MC/ZZ_TuneCP5_13TeV-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
]

CMSC_2016Bv1_     =["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/Data/JetHT_Run2016B-ver1_HIPM_UL2016_MiniAODv2-v2",]
CMSC_2016Bv2_     =["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/Data/JetHT_Run2016B-ver2_HIPM_UL2016_MiniAODv2-v2",]
CMSC_2016C_       =["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/Data/JetHT_Run2016C-HIPM_UL2016_MiniAODv2-v2",]
CMSC_2016D_       =["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/Data/JetHT_Run2016D-HIPM_UL2016_MiniAODv2-v2",]
CMSC_2016E_       =["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/Data/JetHT_Run2016E-HIPM_UL2016_MiniAODv2-v2",]
CMSC_2016F_HIPM_  = ["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016APV/Data/JetHT_Run2016F-HIPM_UL2016_MiniAODv2-v2",]
CMSC_2016F_       =["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/Data/JetHT_Run2016F-UL2016_MiniAODv2-v2",]
CMSC_2016G_       = ["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/Data/JetHT_Run2016G-UL2016_MiniAODv2-v2",]
CMSC_2016H_       = ["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2016/Data/JetHT_Run2016H-UL2016_MiniAODv2-v2",]
CMSC_2017B_       = ["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/Data/JetHT_Run2017B-UL2017_MiniAODv2-v1",]
CMSC_2017C_       = ["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/Data/JetHT_Run2017C-UL2017_MiniAODv2-v1",]
CMSC_2017D_       = ["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/Data/JetHT_Run2017D-UL2017_MiniAODv2-v1",]
CMSC_2017E_       = ["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/Data/JetHT_Run2017E-UL2017_MiniAODv2-v1",]
CMSC_2017F_       = ["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/Data/JetHT_Run2017F-UL2017_MiniAODv2-v1",]
CMSC_2018A_       = ["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/Data/JetHT_Run2018A-UL2018_MiniAODv2-v1",]
CMSC_2018B_       = ["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/Data/JetHT_Run2018B-UL2018_MiniAODv2-v1",]
CMSC_2018C_       = ["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/Data/JetHT_Run2018C-UL2018_MiniAODv2-v1",]
CMSC_2018D_       = ["/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/Data/JetHT_Run2018D-UL2018_MiniAODv2-v2",]

DAS_HGData_2018_ = [
    "/EGamma/Run2018A-UL2018_MiniAODv2-v1/MINIAOD",
    "/EGamma/Run2018B-UL2018_MiniAODv2-v1/MINIAOD",
    "/EGamma/Run2018C-UL2018_MiniAODv2-v1/MINIAOD",
    "/EGamma/Run2018D-UL2018_MiniAODv2-v2/MINIAOD",

]
CMSC_HGSignal_2018_ = [
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M2200",
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M2000",
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M3000",
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M700",
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M1200",
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M2400",
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M1000",
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M1600",
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M1800",
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M800",
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M1400",
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M2600",
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M900",
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M3500",
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M600",
]
CMSC_Signal_2017_VBF_ = [
    "/stash/user/yuzhe/public/0lepton/custom_nano/V2/2017/Signal/VBFHToWWToAny_M-125_TuneCP5_withDipoleRecoil_13TeV-powheg-jhugen751-pythia8_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2",
]
CMSC_Signal_2018_VBF_ = [
    "/stash/user/yuzhe/public/0lepton/custom_nano/V2/2018/Signal/VBFHToWWToAny_M-125_TuneCP5_withDipoleRecoil_13TeV-powheg-jhugen751-pythia8_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2",
]

DAS_examples_ = [
    "/VBFHToWWToAny_M-125_TuneCP5_withDipoleRecoil_13TeV-powheg-jhugen751-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
]
CMSC_examples_ = [
    "/stash/user/fudawei/samples/mc/2018/ZpToHGamma/ZpToHGamma_M600",
]
DAS_examples = lambda : DAS(DAS_examples_)
CMSC_examples = lambda:DAS(CMSC_examples_)


CMSC_Signal_2017_VBF = lambda :DAS(CMSC_Signal_2017_VBF_)
CMSC_Signal_2018_VBF = lambda :DAS(CMSC_Signal_2018_VBF_)


DAS_HGData_2018 = lambda : DAS(DAS_HGData_2018_)
CMSC_HGSignal_2018 = lambda : DAS(CMSC_HGSignal_2018_)



CMSC_2017_HWWSignal = lambda : DAS(CMSC_2017_HWWSignal_)
CMSC_2016_HWWSignal = lambda : DAS(CMSC_2016_HWWSignal_)
CMSC_2016APV_HWWSignal = lambda : DAS(CMSC_2016APV_HWWSignal_)
CMSC_2018_HWWSignal = lambda : DAS(CMSC_2018_HWWSignal_)

CMSC_2016_HWWBKG = lambda : DAS(CMSC_2016_HWWBKG_)
CMSC_2016APV_HWWBKG = lambda : DAS(CMSC_2016APV_HWWBKG_)
CMSC_2017_HWWBKG = lambda : DAS(CMSC_2017_HWWBKG_)
CMSC_2018_HWWBKG = lambda : DAS(CMSC_2018_HWWBKG_)


CMSC_2016Bv1 = lambda : DAS(CMSC_2016Bv1_)
CMSC_2016Bv2 = lambda : DAS(CMSC_2016Bv2_)
CMSC_2016C = lambda : DAS(CMSC_2016C_)
CMSC_2016D = lambda : DAS(CMSC_2016D_)
CMSC_2016E = lambda : DAS(CMSC_2016E_)
CMSC_2016F_HIPM = lambda : DAS(CMSC_2016F_HIPM_)
CMSC_2016F = lambda : DAS(CMSC_2016F_)
CMSC_2016G = lambda : DAS(CMSC_2016G_)
CMSC_2016H = lambda : DAS(CMSC_2016H_)
CMSC_2017B = lambda : DAS(CMSC_2017B_)
CMSC_2017C = lambda : DAS(CMSC_2017C_)
CMSC_2017D = lambda : DAS(CMSC_2017D_)
CMSC_2017E = lambda : DAS(CMSC_2017E_)
CMSC_2017F = lambda : DAS(CMSC_2017F_)
CMSC_2018A = lambda : DAS(CMSC_2018A_)
CMSC_2018B = lambda : DAS(CMSC_2018B_)
CMSC_2018C = lambda : DAS(CMSC_2018C_)
CMSC_2018D = lambda : DAS(CMSC_2018D_)

############## HWW part end  ##################

CMSC_2016_1lepton_MC_ = [
]

    
CMSC_2016_1lepton_MC_ = [
]

CMSC_2016_1lepton_data_ = [
]

DAS_2016_gKK_APV_ = [
]

DAS_2016_gKK_NonAPV_ = [
]

DAS_2017_gKK_ = [
]

DAS_2018_gKK_ = [
]


CMSC_2016APV_Signal_ = [
]

CMSC_2016NonAPV_Signal_ = [
]


CMSC_2017_Signal_ = [
]
CMSC_2016_MC_ = [
]
CMSC_2016APV_MC_ = [
]


CMSC_2017B_0Lepton_data_=[
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/data/JetHT_Run2017B-UL2017_MiniAODv2-v1",
]

CMSC_2017C_0Lepton_data_=[
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/data/JetHT_Run2017C-UL2017_MiniAODv2-v1",
]

CMSC_2017D_0Lepton_data_=[
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/data/JetHT_Run2017D-UL2017_MiniAODv2-v1",
]

CMSC_2017E_0Lepton_data_=[
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/data/JetHT_Run2017E-UL2017_MiniAODv2-v1",
]

CMSC_2017F_0Lepton_data_=[
    "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V1/data/JetHT_Run2017F-UL2017_MiniAODv2-v1",
]




CMSC_2018_Signal_ = [
]

CMSC_2018A_0Lepton_data_ = [
    "/stash/user/yuzhe/public/0lepton/custom_nano/18A/JetHT_A",
]
CMSC_2018B_0Lepton_data_ = [
    "/stash/user/yuzhe/public/0lepton/custom_nano/18B/JetHT_B",
]
CMSC_2018C_0Lepton_data_ = [
    "/stash/user/yuzhe/public/0lepton/custom_nano/18C/JetHT_C",
]
CMSC_2018D_0Lepton_data_ = [
    "/stash/user/yuzhe/public/0lepton/custom_nano/18D/JetHT_D",
]


# /stash/user/qilongguo/public/gKK/private_NanoAOD/2018/V2/Signal/
# "/stash/user/qilongguo/public/gKK/private_NanoAOD/2017/V2/Signal/$1",

# ================ DAS  =================
# ================ 2016 =================
DAS_2016_Common  = lambda : DAS(DAS_2016_Common_)
DAS_2016_1lepton = lambda : DAS(DAS_2016_1lepton_)
DAS_2016_1lepton_Data = lambda : DAS(DAS_2016_1lepton_Data_)

DAS_2016_gKK_APV = lambda : DAS(DAS_2016_gKK_APV_)
DAS_2016_gKK_NonAPV = lambda : DAS(DAS_2016_gKK_NonAPV_)

# ================ 2017 =================
DAS_2017_0Lepton = lambda : DAS(DAS_2017_0Lepton_)
DAS_2017_0Lepton_Missing = lambda : DAS(DAS_2017_0Lepton_Missing_)


DAS_2017_0Lepton_test = lambda : DAS(DAS_2017_0Lepton_test_)
DAS_2017_0lepton_Data = lambda : DAS(DAS_2017_0lepton_Data_)
DAS_2017_0lepton_Data_test = lambda : DAS(DAS_2017_0lepton_Data_test_)

DAS_2017_gKK = lambda : DAS(DAS_2017_gKK_)

# ================ 2018 =================
DAS_2018_0Lepton_Missing = lambda : DAS(DAS_2018_0Lepton_Missing_)
DAS_2018_gKK = lambda : DAS(DAS_2018_gKK_)




# ================ cmsc =================
# Other Channels
CMSC_2016APV_Other = lambda : DAS(CMSC_2016APV_Other_)
CMSC_2016_Other = lambda : DAS(CMSC_2016_Other_)
CMSC_2017_Other = lambda : DAS(CMSC_2017_Other_)
CMSC_2018_Other = lambda : DAS(CMSC_2018_Other_)

# ================ 2016 =================

CMSC_2016_1lepton_MC = lambda : DAS(CMSC_2016_1lepton_MC_)
CMSC_2016_1lepton_data = lambda : DAS(CMSC_2016_1lepton_data_)

CMSC_2016APV_Signal = lambda : DAS(CMSC_2016APV_Signal_)
CMSC_2016NonAPV_Signal = lambda : DAS(CMSC_2016NonAPV_Signal_)
CMSC_2016_MC = lambda : DAS(CMSC_2016_MC_)
CMSC_2016APV_MC = lambda : DAS(CMSC_2016APV_MC_)



# ================ 2017 =================
CMSC_2017_MC = lambda : DAS(CMSC_2017_MC_)

CMSC_2017_0Lepton_MC         = lambda : DAS(CMSC_2017_0Lepton_MC_)
CMSC_2017_0Lepton_MC_missing = lambda : DAS(CMSC_2017_0Lepton_MC_missing_)
CMSC_2017_0Lepton_MC_missing2 = lambda : DAS(CMSC_2017_0Lepton_MC_missing2_)

CMSC_2017_Signal = lambda : DAS(CMSC_2017_Signal_)

CMSC_2017B_0Lepton_data = lambda : DAS(CMSC_2017B_0Lepton_data_)
CMSC_2017C_0Lepton_data = lambda : DAS(CMSC_2017C_0Lepton_data_)
CMSC_2017D_0Lepton_data = lambda : DAS(CMSC_2017D_0Lepton_data_)
CMSC_2017E_0Lepton_data = lambda : DAS(CMSC_2017E_0Lepton_data_)
CMSC_2017F_0Lepton_data = lambda : DAS(CMSC_2017F_0Lepton_data_)

# ================ 2018 =================
CMSC_2018_MC = lambda : DAS(CMSC_2018_MC_)

CMSC_2018_0Lepton_MC         = lambda : DAS(CMSC_2018_0Lepton_MC_)
CMSC_2018_0Lepton_MC_missing = lambda : DAS(CMSC_2018_0Lepton_MC_missing_)

CMSC_2018_Signal = lambda : DAS(CMSC_2018_Signal_)

CMSC_2018A_0Lepton_data = lambda : DAS(CMSC_2018A_0Lepton_data_)
CMSC_2018B_0Lepton_data = lambda : DAS(CMSC_2018B_0Lepton_data_)
CMSC_2018C_0Lepton_data = lambda : DAS(CMSC_2018C_0Lepton_data_)
CMSC_2018D_0Lepton_data = lambda : DAS(CMSC_2018D_0Lepton_data_)


if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option('--DAS',  action="store",type="string",dest="DAS"       ,default=None )
    (options, args) = parser.parse_args()

    DAS_mc_0lepton = [
        "QCD_HT1000to1500_*_13TeV-madgraphMLM-pythia8",
        "QCD_HT1500to2000_*_13TeV-madgraphMLM-pythia8",
        "QCD_HT2000toInf_*_13TeV-madgraphMLM-pythia8",
        "WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8",
        "ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8",
        "TTToHadronic_TuneCP5_13TeV-powheg-pythia8",
        "TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",
        "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8",
        "ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8",
        "ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8",
        "ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8",
        "WW_TuneCP5_13TeV-pythia8",
        "ZZ_TuneCP5_13TeV-pythia8",
        "WZ_TuneCP5_13TeV-pythia8",
        "WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8",
        "WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8",
        "WZZ_TuneCP5_13TeV-amcatnlo-pythia8",
        "ZZZ_TuneCP5_13TeV-amcatnlo-pythia8",
    ]

    Das_mc_gKK = [
        "GkkTogRadionTogVV_*",
    ]

    DAS_  = DAS()
    # DAS_.FetchDataset(Das_mc_gKK,16,mc=True)
    DAS_.FetchDataset(Das_mc_gKK,"16NonAPV",mc=True)
    # DAS_.FetchDataset(Das_mc_gKK,"16APV",mc=True)
    