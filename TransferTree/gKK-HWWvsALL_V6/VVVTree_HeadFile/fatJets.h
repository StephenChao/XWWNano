#ifndef _fatJets_
#define _fatJets_

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include "TH2.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TMath.h"
#include "TLorentzVector.h"
//#include "DataFormats/Math/interface/deltaR.h"

#include <iostream>
#include <fstream>
#include <unordered_map>
#include <map>

#include <cstring>


#include <algorithm>
#include <numeric>
#include<vector>
#include <iostream>
 
#include "VVVUtils.h"

struct FatJet_P //define the necessary struct used by 
{
    vector<float>* v_FatJet_pt_;
    vector<float>* v_FatJet_eta_;
    vector<float>* v_FatJet_phi_;
    vector<float>* v_FatJet_msoftdrop_;
    vector<int>* v_FatJet_jetId_;
    vector<float>* v_FatJet_tau1_;
    vector<float>* v_FatJet_tau2_;
    vector<float>* v_FatJet_tau3_;
    vector<float>* v_FatJet_tau4_;

    vector<float>* v_FatJet_msoftdrop_raw_;
    vector<float>* v_FatJet_msoftdrop_nom_;
    vector<float>* v_FatJet_msoftdrop_corr_JMR_;
    vector<float>* v_FatJet_msoftdrop_corr_JMS_;
    vector<float>* v_FatJet_msoftdrop_corr_PUPPI_;


    vector<float>* v_FatJet_pt_nom_;
    
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWqq0c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWqq1c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWqq2c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWq0c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWq1c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWq2c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWev0c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWev1c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWmv0c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWmv1c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWtauev0c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWtauev1c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWtaumv0c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWtaumv1c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWtauhv0c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWtauhv1c_;
    vector<float>* v_FatJet_inclParTMDV1_probHbb_;
    vector<float>* v_FatJet_inclParTMDV1_probHcc_;
    vector<float>* v_FatJet_inclParTMDV1_probHss_;
    vector<float>* v_FatJet_inclParTMDV1_probHqq_;
    vector<float>* v_FatJet_inclParTMDV1_probHtauhtaue_;
    vector<float>* v_FatJet_inclParTMDV1_probHtauhtaum_;
    vector<float>* v_FatJet_inclParTMDV1_probHtauhtauh_;
    vector<float>* v_FatJet_inclParTMDV1_probQCDbb_;
    vector<float>* v_FatJet_inclParTMDV1_probQCDcc_;
    vector<float>* v_FatJet_inclParTMDV1_probQCDb_;
    vector<float>* v_FatJet_inclParTMDV1_probQCDc_;
    vector<float>* v_FatJet_inclParTMDV1_probQCDothers_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWqq0c_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWqq1c_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWq0c_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWq1c_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWev_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWmv_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWtauhv_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWtauev_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWtaumv_;

    //Start Hidden.

} ;




class FatJet_Collection {
    public : 
    FatJet_Collection();
    FatJet_Collection(FatJet_P FatJet_, int NMAXFatJet, int filterMode);
    size_t size();
    float Get(string order, string variable, int index); //defined in this file.

    private :
    // original branches
    vector<float>* v_FatJet_pt_;
    vector<float>* v_FatJet_eta_;
    vector<float>* v_FatJet_phi_;
    vector<float>* v_FatJet_msoftdrop_;
    vector<int>*   v_FatJet_jetId_;

    vector<float>* v_FatJet_tau1_;
    vector<float>* v_FatJet_tau2_;
    vector<float>* v_FatJet_tau3_;
    vector<float>* v_FatJet_tau4_;

    vector<float>* v_FatJet_msoftdrop_raw_;
    vector<float>* v_FatJet_msoftdrop_nom_;
    vector<float>* v_FatJet_msoftdrop_corr_JMR_;
    vector<float>* v_FatJet_msoftdrop_corr_JMS_;
    vector<float>* v_FatJet_msoftdrop_corr_PUPPI_;
    vector<float>* v_FatJet_pt_nom_;


        //Tagger V2

    vector<float>* v_FatJet_inclParTMDV1_probHWqqWqq0c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWqq1c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWqq2c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWq0c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWq1c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWq2c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWev0c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWev1c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWmv0c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWmv1c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWtauev0c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWtauev1c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWtaumv0c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWtaumv1c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWtauhv0c_;
    vector<float>* v_FatJet_inclParTMDV1_probHWqqWtauhv1c_;
    vector<float>* v_FatJet_inclParTMDV1_probHbb_;
    vector<float>* v_FatJet_inclParTMDV1_probHcc_;
    vector<float>* v_FatJet_inclParTMDV1_probHss_;
    vector<float>* v_FatJet_inclParTMDV1_probHqq_;
    vector<float>* v_FatJet_inclParTMDV1_probHtauhtaue_;
    vector<float>* v_FatJet_inclParTMDV1_probHtauhtaum_;
    vector<float>* v_FatJet_inclParTMDV1_probHtauhtauh_;
    vector<float>* v_FatJet_inclParTMDV1_probQCDbb_;
    vector<float>* v_FatJet_inclParTMDV1_probQCDcc_;
    vector<float>* v_FatJet_inclParTMDV1_probQCDb_;
    vector<float>* v_FatJet_inclParTMDV1_probQCDc_;
    vector<float>* v_FatJet_inclParTMDV1_probQCDothers_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWqq0c_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWqq1c_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWq0c_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWq1c_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWev_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWmv_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWtauhv_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWtauev_;
    vector<float>* v_FatJet_inclParTMDV1_probTopbWtaumv_;

    //Start Hidden.


    // filtered branches
    vector<float> FatJet_pt;
    vector<float> FatJet_eta;
    vector<float> FatJet_phi;
    vector<float> FatJet_msoftdrop;
    vector<int>   FatJet_jetId;

    vector<float> FatJet_tau1;
    vector<float> FatJet_tau2;
    vector<float> FatJet_tau3;
    vector<float> FatJet_tau4;
    vector<float> FatJet_msoftdrop_raw;
    vector<float> FatJet_msoftdrop_nom;
    vector<float> FatJet_msoftdrop_corr_JMR;
    vector<float> FatJet_msoftdrop_corr_JMS;
    vector<float> FatJet_msoftdrop_corr_PUPPI;


    vector<float> FatJet_pt_nom;


        //Tagger V2

    vector<float> FatJet_inclParTMDV1_probHWqqWqq0c;
    vector<float> FatJet_inclParTMDV1_probHWqqWqq1c;
    vector<float> FatJet_inclParTMDV1_probHWqqWqq2c;
    vector<float> FatJet_inclParTMDV1_probHWqqWq0c;
    vector<float> FatJet_inclParTMDV1_probHWqqWq1c;
    vector<float> FatJet_inclParTMDV1_probHWqqWq2c;
    vector<float> FatJet_inclParTMDV1_probHWqqWev0c;
    vector<float> FatJet_inclParTMDV1_probHWqqWev1c;
    vector<float> FatJet_inclParTMDV1_probHWqqWmv0c;
    vector<float> FatJet_inclParTMDV1_probHWqqWmv1c;
    vector<float> FatJet_inclParTMDV1_probHWqqWtauev0c;
    vector<float> FatJet_inclParTMDV1_probHWqqWtauev1c;
    vector<float> FatJet_inclParTMDV1_probHWqqWtaumv0c;
    vector<float> FatJet_inclParTMDV1_probHWqqWtaumv1c;
    vector<float> FatJet_inclParTMDV1_probHWqqWtauhv0c;
    vector<float> FatJet_inclParTMDV1_probHWqqWtauhv1c;
    vector<float> FatJet_inclParTMDV1_probHbb;
    vector<float> FatJet_inclParTMDV1_probHcc;
    vector<float> FatJet_inclParTMDV1_probHss;
    vector<float> FatJet_inclParTMDV1_probHqq;
    vector<float> FatJet_inclParTMDV1_probHtauhtaue;
    vector<float> FatJet_inclParTMDV1_probHtauhtaum;
    vector<float> FatJet_inclParTMDV1_probHtauhtauh;
    vector<float> FatJet_inclParTMDV1_probQCDbb;
    vector<float> FatJet_inclParTMDV1_probQCDcc;
    vector<float> FatJet_inclParTMDV1_probQCDb;
    vector<float> FatJet_inclParTMDV1_probQCDc;
    vector<float> FatJet_inclParTMDV1_probQCDothers;
    vector<float> FatJet_inclParTMDV1_probTopbWqq0c;
    vector<float> FatJet_inclParTMDV1_probTopbWqq1c;
    vector<float> FatJet_inclParTMDV1_probTopbWq0c;
    vector<float> FatJet_inclParTMDV1_probTopbWq1c;
    vector<float> FatJet_inclParTMDV1_probTopbWev;
    vector<float> FatJet_inclParTMDV1_probTopbWmv;
    vector<float> FatJet_inclParTMDV1_probTopbWtauhv;
    vector<float> FatJet_inclParTMDV1_probTopbWtauev;
    vector<float> FatJet_inclParTMDV1_probTopbWtaumv;

    //Start Hidden.



    // branches map
    std::map<std::string, vector<int>>   FatJet_order; //map to store different order information.
    std::map<std::string, vector<float> > FatJet_Branches;

    int NMAXFatJet;
    int filterMode;

    void brances_map();

    void Filter();
    void Filter_1();
    void Filter_2();

    void Order(int);
    void Order_1();
    void Order_2();
    void Order_3();
    void Order_4();
    void Order_5();
    void Order_6();
    void Order_7();

    void brances_Added();
     // See the instruction for template <typename T>
    template <typename T>
    void Out(vector<T>,vector<T> &);

    template <typename T>
    std::vector<int> sort_indexes(std::vector<T> v);

};

FatJet_Collection::FatJet_Collection(){
    NMAXFatJet = 0  ; 
    filterMode = -1 ;
}

//Need to read some FatJet_ from input.
FatJet_Collection::FatJet_Collection(FatJet_P FatJet_ , int NMAXFatJet_, int filterMode_){
    v_FatJet_pt_                             = FatJet_.v_FatJet_pt_;
    v_FatJet_eta_                            = FatJet_.v_FatJet_eta_;
    v_FatJet_phi_                            = FatJet_.v_FatJet_phi_;
    v_FatJet_msoftdrop_                      = FatJet_.v_FatJet_msoftdrop_;
    v_FatJet_jetId_                          = FatJet_.v_FatJet_jetId_;


    v_FatJet_tau1_                           = FatJet_.v_FatJet_tau1_;
    v_FatJet_tau2_                           = FatJet_.v_FatJet_tau2_;
    v_FatJet_tau3_                           = FatJet_.v_FatJet_tau3_;
    v_FatJet_tau4_                           = FatJet_.v_FatJet_tau4_;
    v_FatJet_msoftdrop_raw_                  = FatJet_.v_FatJet_msoftdrop_raw_;
    v_FatJet_msoftdrop_nom_                  = FatJet_.v_FatJet_msoftdrop_nom_;
    v_FatJet_msoftdrop_corr_JMR_             = FatJet_.v_FatJet_msoftdrop_corr_JMR_;
    v_FatJet_msoftdrop_corr_JMS_             = FatJet_.v_FatJet_msoftdrop_corr_JMS_;
    v_FatJet_msoftdrop_corr_PUPPI_           = FatJet_.v_FatJet_msoftdrop_corr_PUPPI_;
   
  
    v_FatJet_pt_nom_                         = FatJet_.v_FatJet_pt_nom_;



    v_FatJet_inclParTMDV1_probHWqqWqq0c_      = FatJet_.v_FatJet_inclParTMDV1_probHWqqWqq0c_    ;
    v_FatJet_inclParTMDV1_probHWqqWqq1c_      = FatJet_.v_FatJet_inclParTMDV1_probHWqqWqq1c_    ;
    v_FatJet_inclParTMDV1_probHWqqWqq2c_      = FatJet_.v_FatJet_inclParTMDV1_probHWqqWqq2c_    ;
    v_FatJet_inclParTMDV1_probHWqqWq0c_       = FatJet_.v_FatJet_inclParTMDV1_probHWqqWq0c_     ;
    v_FatJet_inclParTMDV1_probHWqqWq1c_       = FatJet_.v_FatJet_inclParTMDV1_probHWqqWq1c_     ;
    v_FatJet_inclParTMDV1_probHWqqWq2c_       = FatJet_.v_FatJet_inclParTMDV1_probHWqqWq2c_     ;
    v_FatJet_inclParTMDV1_probHWqqWev0c_      = FatJet_.v_FatJet_inclParTMDV1_probHWqqWev0c_    ;
    v_FatJet_inclParTMDV1_probHWqqWev1c_      = FatJet_.v_FatJet_inclParTMDV1_probHWqqWev1c_    ;
    v_FatJet_inclParTMDV1_probHWqqWmv0c_      = FatJet_.v_FatJet_inclParTMDV1_probHWqqWmv0c_    ;
    v_FatJet_inclParTMDV1_probHWqqWmv1c_      = FatJet_.v_FatJet_inclParTMDV1_probHWqqWmv1c_    ;
    v_FatJet_inclParTMDV1_probHWqqWtauev0c_   = FatJet_.v_FatJet_inclParTMDV1_probHWqqWtauev0c_ ;
    v_FatJet_inclParTMDV1_probHWqqWtauev1c_   = FatJet_.v_FatJet_inclParTMDV1_probHWqqWtauev1c_ ;
    v_FatJet_inclParTMDV1_probHWqqWtaumv0c_   = FatJet_.v_FatJet_inclParTMDV1_probHWqqWtaumv0c_ ;
    v_FatJet_inclParTMDV1_probHWqqWtaumv1c_   = FatJet_.v_FatJet_inclParTMDV1_probHWqqWtaumv1c_ ;
    v_FatJet_inclParTMDV1_probHWqqWtauhv0c_   = FatJet_.v_FatJet_inclParTMDV1_probHWqqWtauhv0c_ ;
    v_FatJet_inclParTMDV1_probHWqqWtauhv1c_   = FatJet_.v_FatJet_inclParTMDV1_probHWqqWtauhv1c_ ;
    v_FatJet_inclParTMDV1_probHbb_            = FatJet_.v_FatJet_inclParTMDV1_probHbb_           ;
    v_FatJet_inclParTMDV1_probHcc_            = FatJet_.v_FatJet_inclParTMDV1_probHcc_           ;
    v_FatJet_inclParTMDV1_probHss_            = FatJet_.v_FatJet_inclParTMDV1_probHss_           ;
    v_FatJet_inclParTMDV1_probHqq_            = FatJet_.v_FatJet_inclParTMDV1_probHqq_           ;
    v_FatJet_inclParTMDV1_probHtauhtaue_      = FatJet_.v_FatJet_inclParTMDV1_probHtauhtaue_     ;
    v_FatJet_inclParTMDV1_probHtauhtaum_      = FatJet_.v_FatJet_inclParTMDV1_probHtauhtaum_     ;
    v_FatJet_inclParTMDV1_probHtauhtauh_      = FatJet_.v_FatJet_inclParTMDV1_probHtauhtauh_     ;
    v_FatJet_inclParTMDV1_probQCDbb_          = FatJet_.v_FatJet_inclParTMDV1_probQCDbb_         ;
    v_FatJet_inclParTMDV1_probQCDcc_          = FatJet_.v_FatJet_inclParTMDV1_probQCDcc_         ;
    v_FatJet_inclParTMDV1_probQCDb_           = FatJet_.v_FatJet_inclParTMDV1_probQCDb_          ;
    v_FatJet_inclParTMDV1_probQCDc_           = FatJet_.v_FatJet_inclParTMDV1_probQCDc_          ;
    v_FatJet_inclParTMDV1_probQCDothers_      = FatJet_.v_FatJet_inclParTMDV1_probQCDothers_     ;
    v_FatJet_inclParTMDV1_probTopbWqq0c_      = FatJet_.v_FatJet_inclParTMDV1_probTopbWqq0c_    ;
    v_FatJet_inclParTMDV1_probTopbWqq1c_      = FatJet_.v_FatJet_inclParTMDV1_probTopbWqq1c_    ;
    v_FatJet_inclParTMDV1_probTopbWq0c_       = FatJet_.v_FatJet_inclParTMDV1_probTopbWq0c_     ;
    v_FatJet_inclParTMDV1_probTopbWq1c_       = FatJet_.v_FatJet_inclParTMDV1_probTopbWq1c_     ;
    v_FatJet_inclParTMDV1_probTopbWev_        = FatJet_.v_FatJet_inclParTMDV1_probTopbWev_       ;
    v_FatJet_inclParTMDV1_probTopbWmv_        = FatJet_.v_FatJet_inclParTMDV1_probTopbWmv_       ;
    v_FatJet_inclParTMDV1_probTopbWtauhv_     = FatJet_.v_FatJet_inclParTMDV1_probTopbWtauhv_    ;
    v_FatJet_inclParTMDV1_probTopbWtauev_     = FatJet_.v_FatJet_inclParTMDV1_probTopbWtauev_    ;
    v_FatJet_inclParTMDV1_probTopbWtaumv_     = FatJet_.v_FatJet_inclParTMDV1_probTopbWtaumv_    ;



    NMAXFatJet = NMAXFatJet_;
    filterMode = filterMode_;

    Filter(); //jetId eta pt requirement check again. and set the array like FatJet_inclParTMDV1_probTopbWtaumv, using the vector_GetEntry, push_back one by one.
    brances_map(); //establish map between string and all the array needed, already filled the array in Filter().
    brances_Added(); //define completely new branches using the raw scores or something else.
    Order(1);
    Order(2);
    // Order(3);
    // Order(4);
    Order(5);
    // Order(6);
    Order(7);
}

// return value is std::vector<int> type!
template <typename T>
std::vector<int> FatJet_Collection::sort_indexes(std::vector<T> v) {
  std::vector<int> idx(v.size()); // First, define an empty vector that has the same length as v;
  std::iota(idx.begin(), idx.end(), 0); // Then, fill it like 0,1,2,3...
  std::sort(idx.begin(), idx.end(), [v](int i1, int i2) { return v[i1] > v[i2]; }); //Finall sort the idx with the v value.
  return idx;
}

//To be noticed, here we already defined a vector named FatJet_Branches. string --> vector<float>
//We already defined the vectors like FatJet_pt.
void FatJet_Collection::brances_map(){
    FatJet_Branches["pt"]                             = FatJet_pt;
    FatJet_Branches["eta"]                            = FatJet_eta;
    FatJet_Branches["phi"]                            = FatJet_phi;
    FatJet_Branches["msoftdrop"]                      = FatJet_msoftdrop;
    FatJet_Branches["tau1"]                           = FatJet_tau1;
    FatJet_Branches["tau2"]                           = FatJet_tau2;
    FatJet_Branches["tau3"]                           = FatJet_tau3;
    FatJet_Branches["tau4"]                           = FatJet_tau4;
    FatJet_Branches["msoftdrop_raw"]                  = FatJet_msoftdrop_raw;
    FatJet_Branches["msoftdrop_nom"]                  = FatJet_msoftdrop_nom;
    FatJet_Branches["msoftdrop_corr_JMR"]             = FatJet_msoftdrop_corr_JMR;
    FatJet_Branches["msoftdrop_corr_JMS"]             = FatJet_msoftdrop_corr_JMS;
    FatJet_Branches["msoftdrop_corr_PUPPI"]           = FatJet_msoftdrop_corr_PUPPI;

    FatJet_Branches["pt_nom"]                         = FatJet_pt_nom;



    FatJet_Branches["inclParTMDV1_probHWqqWqq0c"]     =  FatJet_inclParTMDV1_probHWqqWqq0c          ;        
    FatJet_Branches["inclParTMDV1_probHWqqWqq1c"]     =  FatJet_inclParTMDV1_probHWqqWqq1c          ;        
    FatJet_Branches["inclParTMDV1_probHWqqWqq2c"]     =  FatJet_inclParTMDV1_probHWqqWqq2c          ;        
    FatJet_Branches["inclParTMDV1_probHWqqWq0c"]      =  FatJet_inclParTMDV1_probHWqqWq0c           ;        
    FatJet_Branches["inclParTMDV1_probHWqqWq1c"]      =  FatJet_inclParTMDV1_probHWqqWq1c           ;        
    FatJet_Branches["inclParTMDV1_probHWqqWq2c"]      =  FatJet_inclParTMDV1_probHWqqWq2c           ;        
    FatJet_Branches["inclParTMDV1_probHWqqWev0c"]     =  FatJet_inclParTMDV1_probHWqqWev0c          ;        
    FatJet_Branches["inclParTMDV1_probHWqqWev1c"]     =  FatJet_inclParTMDV1_probHWqqWev1c          ;        
    FatJet_Branches["inclParTMDV1_probHWqqWmv0c"]     =  FatJet_inclParTMDV1_probHWqqWmv0c          ;        
    FatJet_Branches["inclParTMDV1_probHWqqWmv1c"]     =  FatJet_inclParTMDV1_probHWqqWmv1c          ;        
    FatJet_Branches["inclParTMDV1_probHWqqWtauev0c"]  =  FatJet_inclParTMDV1_probHWqqWtauev0c       ;       
    FatJet_Branches["inclParTMDV1_probHWqqWtauev1c"]  =  FatJet_inclParTMDV1_probHWqqWtauev1c       ;       
    FatJet_Branches["inclParTMDV1_probHWqqWtaumv0c"]  =  FatJet_inclParTMDV1_probHWqqWtaumv0c       ;       
    FatJet_Branches["inclParTMDV1_probHWqqWtaumv1c"]  =  FatJet_inclParTMDV1_probHWqqWtaumv1c       ;       
    FatJet_Branches["inclParTMDV1_probHWqqWtauhv0c"]  =  FatJet_inclParTMDV1_probHWqqWtauhv0c       ;       
    FatJet_Branches["inclParTMDV1_probHWqqWtauhv1c"]  =  FatJet_inclParTMDV1_probHWqqWtauhv1c       ;       
    FatJet_Branches["inclParTMDV1_probHbb"]           =  FatJet_inclParTMDV1_probHbb                ;        
    FatJet_Branches["inclParTMDV1_probHcc"]           =  FatJet_inclParTMDV1_probHcc                ;        
    FatJet_Branches["inclParTMDV1_probHss"]           =  FatJet_inclParTMDV1_probHss                ;        
    FatJet_Branches["inclParTMDV1_probHqq"]           =  FatJet_inclParTMDV1_probHqq                ;            
    FatJet_Branches["inclParTMDV1_probHtauhtaue"]     =  FatJet_inclParTMDV1_probHtauhtaue          ;        
    FatJet_Branches["inclParTMDV1_probHtauhtaum"]     =  FatJet_inclParTMDV1_probHtauhtaum          ;        
    FatJet_Branches["inclParTMDV1_probHtauhtauh"]     =  FatJet_inclParTMDV1_probHtauhtauh          ;        
    FatJet_Branches["inclParTMDV1_probQCDbb"]         =  FatJet_inclParTMDV1_probQCDbb              ;     
    FatJet_Branches["inclParTMDV1_probQCDcc"]         =  FatJet_inclParTMDV1_probQCDcc              ;     
    FatJet_Branches["inclParTMDV1_probQCDb"]          =  FatJet_inclParTMDV1_probQCDb               ; 
    FatJet_Branches["inclParTMDV1_probQCDc"]          =  FatJet_inclParTMDV1_probQCDc               ; 
    FatJet_Branches["inclParTMDV1_probQCDothers"]     =  FatJet_inclParTMDV1_probQCDothers          ;        
    FatJet_Branches["inclParTMDV1_probTopbWqq0c"]     =  FatJet_inclParTMDV1_probTopbWqq0c          ;        
    FatJet_Branches["inclParTMDV1_probTopbWqq1c"]     =  FatJet_inclParTMDV1_probTopbWqq1c          ;        
    FatJet_Branches["inclParTMDV1_probTopbWq0c"]      =  FatJet_inclParTMDV1_probTopbWq0c           ;       
    FatJet_Branches["inclParTMDV1_probTopbWq1c"]      =  FatJet_inclParTMDV1_probTopbWq1c           ;       
    FatJet_Branches["inclParTMDV1_probTopbWev"]       =  FatJet_inclParTMDV1_probTopbWev            ;      
    FatJet_Branches["inclParTMDV1_probTopbWmv"]       =  FatJet_inclParTMDV1_probTopbWmv            ;      
    FatJet_Branches["inclParTMDV1_probTopbWtauhv"]    =  FatJet_inclParTMDV1_probTopbWtauhv         ;         
    FatJet_Branches["inclParTMDV1_probTopbWtauev"]    =  FatJet_inclParTMDV1_probTopbWtauev         ;         
    FatJet_Branches["inclParTMDV1_probTopbWtaumv"]    =  FatJet_inclParTMDV1_probTopbWtaumv         ;          



}

void FatJet_Collection::brances_Added(){
    vector<float> Branch;
 
    
    for (int iFJ = 0; iFJ != int(FatJet_pt.size()); ++iFJ ){
        float HWWMD_V2 = (
        FatJet_inclParTMDV1_probHWqqWqq0c[iFJ] + 
        FatJet_inclParTMDV1_probHWqqWqq1c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWqq2c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWq0c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWq1c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWq2c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWev0c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWev1c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWmv0c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWmv1c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWtauev0c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWtauev1c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWtaumv0c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWtaumv1c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWtauhv0c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWtauhv1c[iFJ] 
        )/(
        FatJet_inclParTMDV1_probHWqqWqq0c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWqq1c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWqq2c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWq0c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWq1c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWq2c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWev0c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWev1c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWmv0c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWmv1c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWtauev0c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWtauev1c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWtaumv0c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWtaumv1c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWtauhv0c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWtauhv1c[iFJ] +     
        FatJet_inclParTMDV1_probHbb[iFJ] +   
        FatJet_inclParTMDV1_probHcc[iFJ] +   
        FatJet_inclParTMDV1_probHss[iFJ] +   
        FatJet_inclParTMDV1_probHqq[iFJ] +   
        FatJet_inclParTMDV1_probHtauhtaue[iFJ] +   
        FatJet_inclParTMDV1_probHtauhtaum[iFJ] +   
        FatJet_inclParTMDV1_probHtauhtauh[iFJ] +   
        FatJet_inclParTMDV1_probQCDbb[iFJ] +   
        FatJet_inclParTMDV1_probQCDcc[iFJ] +   
        FatJet_inclParTMDV1_probQCDb[iFJ] +   
        FatJet_inclParTMDV1_probQCDc[iFJ] +   
        FatJet_inclParTMDV1_probQCDothers[iFJ] +   
        FatJet_inclParTMDV1_probTopbWqq0c[iFJ] +   
        FatJet_inclParTMDV1_probTopbWqq1c[iFJ] +   
        FatJet_inclParTMDV1_probTopbWq0c[iFJ] +   
        FatJet_inclParTMDV1_probTopbWq1c[iFJ] +   
        FatJet_inclParTMDV1_probTopbWev[iFJ] +   
        FatJet_inclParTMDV1_probTopbWmv[iFJ] +   
        FatJet_inclParTMDV1_probTopbWtauhv[iFJ] +   
        FatJet_inclParTMDV1_probTopbWtauev[iFJ] +   
        FatJet_inclParTMDV1_probTopbWtaumv[iFJ]
        );

        Branch.push_back(HWWMD_V2);
    } 
    FatJet_Branches["HWW_V2"] = Branch;
    Branch.clear();
    // General HWW tagger ordering.

        
    for (int iFJ = 0; iFJ != int(FatJet_pt.size()); ++iFJ ){
        float HWWvsQCDMD_V2 = (
        FatJet_inclParTMDV1_probHWqqWqq0c[iFJ] + 
        FatJet_inclParTMDV1_probHWqqWqq1c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWqq2c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWq0c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWq1c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWq2c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWev0c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWev1c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWmv0c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWmv1c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWtauev0c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWtauev1c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWtaumv0c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWtaumv1c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWtauhv0c[iFJ] +  
        FatJet_inclParTMDV1_probHWqqWtauhv1c[iFJ] 
        )/(
        FatJet_inclParTMDV1_probHWqqWqq0c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWqq1c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWqq2c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWq0c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWq1c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWq2c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWev0c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWev1c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWmv0c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWmv1c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWtauev0c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWtauev1c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWtaumv0c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWtaumv1c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWtauhv0c[iFJ] +   
        FatJet_inclParTMDV1_probHWqqWtauhv1c[iFJ] +     

        FatJet_inclParTMDV1_probQCDbb[iFJ] +   
        FatJet_inclParTMDV1_probQCDcc[iFJ] +   
        FatJet_inclParTMDV1_probQCDb[iFJ] +   
        FatJet_inclParTMDV1_probQCDc[iFJ] +   
        FatJet_inclParTMDV1_probQCDothers[iFJ]  
        );

        Branch.push_back(HWWvsQCDMD_V2);
        //HWWMD_v2 could change, just a temperary variable!
    } //HWWvs.QCD tagger ordering.
    
    FatJet_Branches["HWWvsQCD_V2"] = Branch;
    Branch.clear();
    //Test part1
    // for (int iBJ = 0; iBJ < FatJet_Branches["HWW_V2"].size(); iBJ++){
    //     cout << "Now the HWW_V2 branch" << iBJ << "is" << FatJet_Branches["HWW_V2"].at(iBJ) << endl;
    // }

    //Test part2
    // for (int iBJ = 0; iBJ < FatJet_Branches["HWW_V2"].size(); iBJ++){
    //     cout << "After the HWW_V2 branch" << iBJ << "is" << FatJet_Branches["HWW_V2"].at(iBJ) << endl;
    // }

    //New tagger.


    for (int iFJ = 0; iFJ != int(FatJet_pt_nom.size()); ++iFJ ){
        float out = -99 ; 
        if( FatJet_pt_nom[iFJ] > 200 ){
            out = FatJet_msoftdrop_nom[iFJ]/FatJet_msoftdrop_corr_PUPPI[iFJ];
        }
        Branch.push_back(out);
    }
    FatJet_Branches["msoftdrop_nom_noJWS"] = Branch;
    Branch.clear();


}

void FatJet_Collection::Filter(){
    if( filterMode == 1 ){
        Filter_1();
    }
    if( filterMode == 2 ){
        Filter_2();
    }
}

void FatJet_Collection::Filter_1(){
    // jetid , eta requirement
    // https://twiki.cern.ch/twiki/bin/view/CMS/JetID
    // https://twiki.cern.ch/twiki/bin/view/CMS/JetID13TeVUL
    // Please note: For AK8 jets, the corresponding (CHS or PUPPI) AK4 jet ID should be used.
    // For 2016 samples : jetId==3 means: pass loose and tight ID, fail tightLepVeto, jetId==7 means: pass loose, tight, tightLepVeto ID.
    // For 2017 and 2018 samples : jetId==2 means: pass tight ID, fail tightLepVeto, jetId==6 means: pass tight and tightLepVeto ID.
    
    //There are different jetIds, so that's why we have two different files in 2016 and 2017.

    for (size_t iFJ = 0; iFJ != v_FatJet_pt_->size(); ++iFJ ){

        int   iFatJet_jetId  = v_FatJet_jetId_->at(iFJ) ; if( iFatJet_jetId&2 != 2 ){ continue; }
        float iFatJet_jeteta = v_FatJet_eta_->at(iFJ)   ; if( fabs(iFatJet_jeteta) > 2.4 ){ continue; }
        float iFatJet_jetpt  = v_FatJet_pt_->at(iFJ)    ; if( iFatJet_jetpt < 200 ){ continue; }

        FatJet_pt.push_back(v_FatJet_pt_->at(iFJ));
        FatJet_eta.push_back(v_FatJet_eta_->at(iFJ));
        FatJet_phi.push_back(v_FatJet_phi_->at(iFJ));
        FatJet_msoftdrop.push_back(v_FatJet_msoftdrop_->at(iFJ));
        FatJet_jetId.push_back(v_FatJet_jetId_->at(iFJ));

        FatJet_tau1.push_back(v_FatJet_tau1_->at(iFJ));
        FatJet_tau2.push_back(v_FatJet_tau2_->at(iFJ));
        FatJet_tau3.push_back(v_FatJet_tau3_->at(iFJ));
        FatJet_tau4.push_back(v_FatJet_tau4_->at(iFJ));

        //V2
        FatJet_inclParTMDV1_probHWqqWqq0c.push_back( v_FatJet_inclParTMDV1_probHWqqWqq0c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWqq1c.push_back( v_FatJet_inclParTMDV1_probHWqqWqq1c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWqq2c.push_back( v_FatJet_inclParTMDV1_probHWqqWqq2c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWq0c.push_back( v_FatJet_inclParTMDV1_probHWqqWq0c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWq1c.push_back( v_FatJet_inclParTMDV1_probHWqqWq1c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWq2c.push_back( v_FatJet_inclParTMDV1_probHWqqWq2c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWev0c.push_back( v_FatJet_inclParTMDV1_probHWqqWev0c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWev1c.push_back( v_FatJet_inclParTMDV1_probHWqqWev1c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWmv0c.push_back( v_FatJet_inclParTMDV1_probHWqqWmv0c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWmv1c.push_back( v_FatJet_inclParTMDV1_probHWqqWmv1c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWtauev0c.push_back( v_FatJet_inclParTMDV1_probHWqqWtauev0c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWtauev1c.push_back( v_FatJet_inclParTMDV1_probHWqqWtauev1c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWtaumv0c.push_back( v_FatJet_inclParTMDV1_probHWqqWtaumv0c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWtaumv1c.push_back( v_FatJet_inclParTMDV1_probHWqqWtaumv1c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWtauhv0c.push_back( v_FatJet_inclParTMDV1_probHWqqWtauhv0c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWtauhv1c.push_back( v_FatJet_inclParTMDV1_probHWqqWtauhv1c_->at(iFJ));
        FatJet_inclParTMDV1_probHbb.push_back( v_FatJet_inclParTMDV1_probHbb_->at(iFJ));
        FatJet_inclParTMDV1_probHcc.push_back( v_FatJet_inclParTMDV1_probHcc_->at(iFJ));
        FatJet_inclParTMDV1_probHss.push_back( v_FatJet_inclParTMDV1_probHss_->at(iFJ));
        FatJet_inclParTMDV1_probHqq.push_back( v_FatJet_inclParTMDV1_probHqq_->at(iFJ));
        FatJet_inclParTMDV1_probHtauhtaue.push_back( v_FatJet_inclParTMDV1_probHtauhtaue_->at(iFJ));
        FatJet_inclParTMDV1_probHtauhtaum.push_back( v_FatJet_inclParTMDV1_probHtauhtaum_->at(iFJ));
        FatJet_inclParTMDV1_probHtauhtauh.push_back( v_FatJet_inclParTMDV1_probHtauhtauh_->at(iFJ));
        FatJet_inclParTMDV1_probQCDbb.push_back( v_FatJet_inclParTMDV1_probQCDbb_->at(iFJ));
        FatJet_inclParTMDV1_probQCDcc.push_back( v_FatJet_inclParTMDV1_probQCDcc_->at(iFJ));
        FatJet_inclParTMDV1_probQCDb.push_back( v_FatJet_inclParTMDV1_probQCDb_->at(iFJ));
        FatJet_inclParTMDV1_probQCDc.push_back( v_FatJet_inclParTMDV1_probQCDc_->at(iFJ));
        FatJet_inclParTMDV1_probQCDothers.push_back( v_FatJet_inclParTMDV1_probQCDothers_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWqq0c.push_back( v_FatJet_inclParTMDV1_probTopbWqq0c_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWqq1c.push_back( v_FatJet_inclParTMDV1_probTopbWqq1c_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWq0c.push_back( v_FatJet_inclParTMDV1_probTopbWq0c_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWq1c.push_back( v_FatJet_inclParTMDV1_probTopbWq1c_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWev.push_back( v_FatJet_inclParTMDV1_probTopbWev_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWmv.push_back( v_FatJet_inclParTMDV1_probTopbWmv_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWtauhv.push_back( v_FatJet_inclParTMDV1_probTopbWtauhv_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWtauev.push_back( v_FatJet_inclParTMDV1_probTopbWtauev_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWtaumv.push_back( v_FatJet_inclParTMDV1_probTopbWtaumv_->at(iFJ));

        if( v_FatJet_msoftdrop_raw_->size() > iFJ ){
            FatJet_msoftdrop_raw.push_back(v_FatJet_msoftdrop_raw_->at(iFJ));
        }
        else{
            FatJet_msoftdrop_raw.push_back(-99.);
        }

        if( v_FatJet_msoftdrop_nom_->size() > iFJ ){
            FatJet_msoftdrop_nom.push_back(v_FatJet_msoftdrop_nom_->at(iFJ));
        }
        else{
            FatJet_msoftdrop_nom.push_back(-99.);
        }

        if( v_FatJet_msoftdrop_corr_JMR_->size() > iFJ ){
            FatJet_msoftdrop_corr_JMR.push_back(v_FatJet_msoftdrop_corr_JMR_->at(iFJ));
        }
        else{
            FatJet_msoftdrop_corr_JMR.push_back(-99.);
        }

        if( v_FatJet_msoftdrop_corr_JMS_->size() > iFJ ){
            FatJet_msoftdrop_corr_JMS.push_back(v_FatJet_msoftdrop_corr_JMS_->at(iFJ));
        }
        else{
            FatJet_msoftdrop_corr_JMS.push_back(-99.);
        }

        if( v_FatJet_msoftdrop_corr_PUPPI_->size() > iFJ ){
            FatJet_msoftdrop_corr_PUPPI.push_back(v_FatJet_msoftdrop_corr_PUPPI_->at(iFJ));
        }
        else{
            FatJet_msoftdrop_corr_PUPPI.push_back(-99.);
        }

        if( v_FatJet_pt_nom_->size() > iFJ ){
            FatJet_pt_nom.push_back(v_FatJet_pt_nom_->at(iFJ));
        }
        else{
            FatJet_pt_nom.push_back(-99.);
        }

    }
}

void FatJet_Collection::Filter_2(){
    // jetid , eta requirement
    // https://twiki.cern.ch/twiki/bin/view/CMS/JetID
    // https://twiki.cern.ch/twiki/bin/view/CMS/JetID13TeVUL
    // Please note: For AK8 jets, the corresponding (CHS or PUPPI) AK4 jet ID should be used.
    // For 2016 samples : jetId==3 means: pass loose and tight ID, fail tightLepVeto, jetId==7 means: pass loose, tight, tightLepVeto ID.
    // For 2017 and 2018 samples : jetId==2 means: pass tight ID, fail tightLepVeto, jetId==6 means: pass tight and tightLepVeto ID.
    for (size_t iFJ = 0; iFJ != v_FatJet_pt_->size(); ++iFJ ){

        int   iFatJet_jetId  = v_FatJet_jetId_->at(iFJ) ; if( iFatJet_jetId&2 != 2 ){ continue; }
        float iFatJet_jeteta = v_FatJet_eta_->at(iFJ)   ; if( fabs(iFatJet_jeteta) > 2.4 ){ continue; }
        float iFatJet_jetpt  = v_FatJet_pt_nom_->at(iFJ)    ; if( iFatJet_jetpt < 200 ){ continue; }

        FatJet_pt.push_back(v_FatJet_pt_->at(iFJ));
        FatJet_eta.push_back(v_FatJet_eta_->at(iFJ));
        FatJet_phi.push_back(v_FatJet_phi_->at(iFJ));
        FatJet_msoftdrop.push_back(v_FatJet_msoftdrop_->at(iFJ));
        FatJet_jetId.push_back(v_FatJet_jetId_->at(iFJ));

        FatJet_tau1.push_back(v_FatJet_tau1_->at(iFJ));
        FatJet_tau2.push_back(v_FatJet_tau2_->at(iFJ));
        FatJet_tau3.push_back(v_FatJet_tau3_->at(iFJ));
        FatJet_tau4.push_back(v_FatJet_tau4_->at(iFJ));

        //New tagger.

        FatJet_inclParTMDV1_probHWqqWqq0c.push_back( v_FatJet_inclParTMDV1_probHWqqWqq0c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWqq1c.push_back( v_FatJet_inclParTMDV1_probHWqqWqq1c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWqq2c.push_back( v_FatJet_inclParTMDV1_probHWqqWqq2c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWq0c.push_back( v_FatJet_inclParTMDV1_probHWqqWq0c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWq1c.push_back( v_FatJet_inclParTMDV1_probHWqqWq1c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWq2c.push_back( v_FatJet_inclParTMDV1_probHWqqWq2c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWev0c.push_back( v_FatJet_inclParTMDV1_probHWqqWev0c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWev1c.push_back( v_FatJet_inclParTMDV1_probHWqqWev1c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWmv0c.push_back( v_FatJet_inclParTMDV1_probHWqqWmv0c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWmv1c.push_back( v_FatJet_inclParTMDV1_probHWqqWmv1c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWtauev0c.push_back( v_FatJet_inclParTMDV1_probHWqqWtauev0c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWtauev1c.push_back( v_FatJet_inclParTMDV1_probHWqqWtauev1c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWtaumv0c.push_back( v_FatJet_inclParTMDV1_probHWqqWtaumv0c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWtaumv1c.push_back( v_FatJet_inclParTMDV1_probHWqqWtaumv1c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWtauhv0c.push_back( v_FatJet_inclParTMDV1_probHWqqWtauhv0c_->at(iFJ));
        FatJet_inclParTMDV1_probHWqqWtauhv1c.push_back( v_FatJet_inclParTMDV1_probHWqqWtauhv1c_->at(iFJ));
        FatJet_inclParTMDV1_probHbb.push_back( v_FatJet_inclParTMDV1_probHbb_->at(iFJ));
        FatJet_inclParTMDV1_probHcc.push_back( v_FatJet_inclParTMDV1_probHcc_->at(iFJ));
        FatJet_inclParTMDV1_probHss.push_back( v_FatJet_inclParTMDV1_probHss_->at(iFJ));
        FatJet_inclParTMDV1_probHqq.push_back( v_FatJet_inclParTMDV1_probHqq_->at(iFJ));
        FatJet_inclParTMDV1_probHtauhtaue.push_back( v_FatJet_inclParTMDV1_probHtauhtaue_->at(iFJ));
        FatJet_inclParTMDV1_probHtauhtaum.push_back( v_FatJet_inclParTMDV1_probHtauhtaum_->at(iFJ));
        FatJet_inclParTMDV1_probHtauhtauh.push_back( v_FatJet_inclParTMDV1_probHtauhtauh_->at(iFJ));
        FatJet_inclParTMDV1_probQCDbb.push_back( v_FatJet_inclParTMDV1_probQCDbb_->at(iFJ));
        FatJet_inclParTMDV1_probQCDcc.push_back( v_FatJet_inclParTMDV1_probQCDcc_->at(iFJ));
        FatJet_inclParTMDV1_probQCDb.push_back( v_FatJet_inclParTMDV1_probQCDb_->at(iFJ));
        FatJet_inclParTMDV1_probQCDc.push_back( v_FatJet_inclParTMDV1_probQCDc_->at(iFJ));
        FatJet_inclParTMDV1_probQCDothers.push_back( v_FatJet_inclParTMDV1_probQCDothers_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWqq0c.push_back( v_FatJet_inclParTMDV1_probTopbWqq0c_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWqq1c.push_back( v_FatJet_inclParTMDV1_probTopbWqq1c_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWq0c.push_back( v_FatJet_inclParTMDV1_probTopbWq0c_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWq1c.push_back( v_FatJet_inclParTMDV1_probTopbWq1c_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWev.push_back( v_FatJet_inclParTMDV1_probTopbWev_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWmv.push_back( v_FatJet_inclParTMDV1_probTopbWmv_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWtauhv.push_back( v_FatJet_inclParTMDV1_probTopbWtauhv_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWtauev.push_back( v_FatJet_inclParTMDV1_probTopbWtauev_->at(iFJ));
        FatJet_inclParTMDV1_probTopbWtaumv.push_back( v_FatJet_inclParTMDV1_probTopbWtaumv_->at(iFJ));

        if( v_FatJet_msoftdrop_raw_->size() > iFJ ){
            FatJet_msoftdrop_raw.push_back(v_FatJet_msoftdrop_raw_->at(iFJ));
        }
        else{
            FatJet_msoftdrop_raw.push_back(-99.);
        }

        if( v_FatJet_msoftdrop_nom_->size() > iFJ ){
            FatJet_msoftdrop_nom.push_back(v_FatJet_msoftdrop_nom_->at(iFJ));
        }
        else{
            FatJet_msoftdrop_nom.push_back(-99.);
        }

        if( v_FatJet_msoftdrop_corr_JMR_->size() > iFJ ){
            FatJet_msoftdrop_corr_JMR.push_back(v_FatJet_msoftdrop_corr_JMR_->at(iFJ));
        }
        else{
            FatJet_msoftdrop_corr_JMR.push_back(-99.);
        }

        if( v_FatJet_msoftdrop_corr_JMS_->size() > iFJ ){
            FatJet_msoftdrop_corr_JMS.push_back(v_FatJet_msoftdrop_corr_JMS_->at(iFJ));
        }
        else{
            FatJet_msoftdrop_corr_JMS.push_back(-99.);
        }

        if( v_FatJet_msoftdrop_corr_PUPPI_->size() > iFJ ){
            FatJet_msoftdrop_corr_PUPPI.push_back(v_FatJet_msoftdrop_corr_PUPPI_->at(iFJ));
        }
        else{
            FatJet_msoftdrop_corr_PUPPI.push_back(-99.);
        }



        if( v_FatJet_pt_nom_->size() > iFJ ){
            FatJet_pt_nom.push_back(v_FatJet_pt_nom_->at(iFJ));
        }
        else{
            FatJet_pt_nom.push_back(-99.);
        }

    }
}

size_t FatJet_Collection::size(){
    return FatJet_pt.size();
}

void FatJet_Collection::Order(int mode){
    if((mode == 1) && (NMAXFatJet == 3)){ Order_1(); }
    if((mode == 2) && (NMAXFatJet == 3)){ Order_2(); }
    if((mode == 3) && (NMAXFatJet == 3)){ Order_3(); }
    if((mode == 4) && (NMAXFatJet == 3)){ Order_4(); }
    if((mode == 5) && (NMAXFatJet == 3)){ Order_5(); }

    if((mode == 6) && (NMAXFatJet == 3)){ Order_6(); } //HWWMD H4q tagger order.
    if((mode == 7) && (NMAXFatJet == 3)){ Order_7(); } //HWWMD V2 tagger order.
    

}

void FatJet_Collection::Order_1(){
    vector<int> FJorder;
    if( FatJet_pt.size() == 2 ){
        FJorder.push_back(0);
        FJorder.push_back(1);
        FJorder.push_back(-99);
    }
    if( FatJet_pt.size() == 3 ){
        FJorder.push_back(0);
        FJorder.push_back(1);
        FJorder.push_back(2);
    }
    else{
        FJorder.push_back(-99);
        FJorder.push_back(-99);
        FJorder.push_back(-99);
    }
    FatJet_order["PT"] = FJorder;
}

void FatJet_Collection::Order_2(){
    vector<int> FJorder;
    vector<int> FJorder_tmp = sort_indexes(FatJet_msoftdrop);
    if( FatJet_pt.size() == 2 ){
        FJorder.push_back(FJorder_tmp[0]);
        FJorder.push_back(-99);
        FJorder.push_back(FJorder_tmp[1]);
    }
    if( FatJet_pt.size() == 3 ){
        FJorder = FJorder_tmp ;
    }
    else{
        FJorder.push_back(-99);
        FJorder.push_back(-99);
        FJorder.push_back(-99);
    }
    FatJet_order["Mass"] = FJorder;
}

void FatJet_Collection::Order_3(){
    // deep-W MD ordered
    vector<float> OrderBranch;
    OrderBranch = FatJet_Branches["deepTagMD_WvsQCD"];

    vector<int> FJorder;
    vector<int> FJorder_tmp = sort_indexes(OrderBranch);
    if( FatJet_pt.size() == 2 ){
        FJorder.push_back(FJorder_tmp[0]);
        FJorder.push_back(-99);
        FJorder.push_back(FJorder_tmp[1]);
    }
    if( FatJet_pt.size() == 3 ){
        FJorder = FJorder_tmp ;
    }
    else{
        FJorder.push_back(-99);
        FJorder.push_back(-99);
        FJorder.push_back(-99);
    }
    FatJet_order["deep-W-MD"] = FJorder;
}

void FatJet_Collection::Order_4(){
    // paricle-net W MD ordered
    vector<float> OrderBranch;
    OrderBranch = FatJet_Branches["particleNetMD_WvsQCD"];

    vector<int> FJorder;
    vector<int> FJorder_tmp = sort_indexes(OrderBranch);
    if( FatJet_pt.size() == 2 ){
        FJorder.push_back(FJorder_tmp[0]);
        FJorder.push_back(-99);
        FJorder.push_back(FJorder_tmp[1]);
    }
    if( FatJet_pt.size() == 3 ){
        FJorder = FJorder_tmp ;
    }
    else{
        FJorder.push_back(-99);
        FJorder.push_back(-99);
        FJorder.push_back(-99);
    }
    FatJet_order["PNet-W-MD"] = FJorder;
}

void FatJet_Collection::Order_5(){
    // paricle-net W MD ordered
    vector<float> OrderBranch;
    OrderBranch = FatJet_Branches["pt_nom"];

    vector<int> FJorder;
    vector<int> FJorder_tmp = sort_indexes(OrderBranch);
    if( FatJet_pt.size() == 2 ){
        FJorder.push_back(FJorder_tmp[0]);
        FJorder.push_back(FJorder_tmp[1]);
        FJorder.push_back(-99);
    }
    if( FatJet_pt.size() == 3 ){
        FJorder = FJorder_tmp ;
    }
    else{
        FJorder.push_back(-99);
        FJorder.push_back(-99);
        FJorder.push_back(-99);
    }
    FatJet_order["pt_nom"] = FJorder;
}

void FatJet_Collection::Order_6(){
    //General Higgs tagger ordered
    vector<float> OrderBranch;
    OrderBranch = FatJet_Branches["deepHWWMDV1_HallvsQCD"];

    vector<int> FJorder;
    vector<int> FJorder_tmp = sort_indexes(OrderBranch);
    if( FatJet_pt.size() == 2 ){
        FJorder.push_back(FJorder_tmp[0]);
        FJorder.push_back(-99);
        FJorder.push_back(FJorder_tmp[1]);
    }
    if( FatJet_pt.size() == 3 ){
        FJorder = FJorder_tmp ;
    }
    else{
        FJorder.push_back(-99);
        FJorder.push_back(-99);
        FJorder.push_back(-99);
    }
    FatJet_order["HWW-H4q-MD"] = FJorder;
}

void FatJet_Collection::Order_7(){
    //newest Higgs tagger ordered
    vector<float> OrderBranch;
    OrderBranch = FatJet_Branches["HWW_V2"];

    vector<int> FJorder;
    vector<int> FJorder_tmp = sort_indexes(OrderBranch);
    if( FatJet_pt.size() == 2 ){
        FJorder.push_back(FJorder_tmp[0]);
        FJorder.push_back(-99);
        FJorder.push_back(FJorder_tmp[1]);
    }
    if( FatJet_pt.size() == 3 ){
        FJorder = FJorder_tmp ;
    }
    else{
        FJorder.push_back(-99);
        FJorder.push_back(-99);
        FJorder.push_back(-99);
    }
    FatJet_order["HWW-V2-MD"] = FJorder;
    // To be noticed here, the FatJet_order is a map!!! string --> vector. just like the dict in python.
    // The function provided the FatJet_order["HWW-V2-MD"] , a vector contain jet order information like [0,1,2] or [2,1,0]
}



float FatJet_Collection::Get(string order, string variable, int index){
    int id = FatJet_order[order][index];
    if( id == -99 ){
        return -99.;
    }
    else{
        return FatJet_Branches[variable].at(id);
    }
    // To get the given order's no.index variable.
}

// template <typename T>
// void FatJet_Collection::Out(vector<T> In_branch, vector<T> & Out_branch){
    // for (size_t iFJ = 0; iFJ != FJorder.size(); ++iFJ ){ 
        // if(iFJ < In_branch.size()){ Out_branch.push_back( In_branch.at(FJorder.at(iFJ)) ); }
        // else{ Out_branch.push_back(-99); }
    // }
// }

#endif
