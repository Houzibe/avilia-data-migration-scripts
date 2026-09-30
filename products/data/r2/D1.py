import numpy as np

"""
consultations = np.array([
    {"name": "Dietician", "descr": "", "catid": 36, "source": 83},
    {"name": "Dietician - Initial", "descr": "", "catid": 36, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Doppler Ultrasound Per Region", "descr": "", "catid": 27, "source": 83},
])

laboratory_tests = np.array([
    {"name": "D-Dimer", "descr": "", "catid": 39, "source": 83},
    {"name": "Day 2 Hormonal Profile", "descr": "", "catid": 39, "source": 83},
    {"name": "Dehydroepiandrosterone Sulfate(Dhea-S)", "descr": "", "catid": 39, "source": 83},
    {"name": "Dust", "descr": "", "catid": 39, "source": 83},
])

medical_supplies = np.array([
    {"name": "Dressings (Opsite Dressing) Item 1 Unit", "descr": "", "catid": 34, "source": 83},
])

medications = np.array([
    {"name": "Dabigatran Etexilate (Pradaxa) Capsule 150 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dapagliflozin (Forxiga) Tablet 10 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Defal (Deflazacort) Tablet 30 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Degraded Gelatin Polypeptides + Electrolytes (Haemaccel) Infusion 3.5 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Dehydroepiandrosterone (Dhea) (Welikevitamins) Tablet 100 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Denosumab (Xgeva) Injection 120 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dequalinium Chloride (Dequadin) Tablet 250 μg", "descr": "", "catid": 35, "source": 83},
    
"""    
medications = np.array([
    {"name": "Desloratidine (Hayvent) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Desloratidine (Momento) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Desmopressin Acetate (Desmopressin) Tablet 0.2 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dexamethasone (Maxidex Eye Drops) Drops 0.1 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Dexamethasone (Xasten) Tablet 0.5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dexamethasone 0.4Mg + Gentamicin 1.0Mg + Clotrimazole 10Mg (Biocoten) Cream 20 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Dexamethasone Orphan (...) Injection 4 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Dextromethorphan Hydrobromide (Novalyn Dry Cough Child) Syrup 7.5 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Dextromethorphan Hydrobromide (Novalyn Dry Cough) Syrup 15 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Dhea (Swanson) Capsule 50 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diazepam (...) Injection 10 mg/2Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Diazepam (Unival) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diazepam (Valium) Injection 10 mg/2Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Dichlorobenzyl Alcohol + Amylmetacresol +/- Vitaminc (Sorepils) Tablet 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Dichlorobenzyl Alcohol + Amylmetacresol +/- Vitaminc (Strepsils Intensive) Tablet 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Dichlorobenzyl Alcohol + Amylmetacresol +/- Vitaminc (Strepsils) Tablet 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac (...) Drops 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac (Clofenac) Tablet 50 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac (Diclofenac Gel) Gel 20 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac (Olfen) Gel 50 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac (Olfen) Tablet 50 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac (Voltaren Emulgel) Cream 100 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac (Voltaren Emulgel) Cream 20 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac (Voltaren Emulgel) Cream 25 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac (Voltaren Emulgel) Cream 50 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac (Voltarene Eye Drop) Drops 0.1 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac 75Mg (...) Injection 75 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac 75Mg + Misoprostol 200Ug (Arthrotec 75) Tablet 75 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac 75Mg + Misoprostol 200Ug (Rostrec 75) Tablet 75 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Sodium (Lofenac Suppository) Suppository 50 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Sodium (Voltaren Retard) Tablet 100 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Sodium (Voltaren Suppository) Suppository 100 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Sodium (Voltaren Suppository) Suppository 12.5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Sodium (Voltaren Suppository) Suppository 50 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac-Cholestyramine (Flotac 75Mg) Capsule 75 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Digoxin (Digoxin-Bristol) Tablet 250 μg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dihydroartemisinin 120Mg + Piperaquine Phosphate 960Mg (P- Alaxin Ts) Tablet 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Dihydroartemisinin 40Mg + Piperaquine Phosphate 320Mg (Ibasunate) Tablet 360 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dihydroartemisinin 40Mg + Piperaquine Phosphate 320Mg (P-Alaxin) Syrup 80 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dihydroartemisinin 40Mg + Piperaquine Phosphate 320Mg (P-Alaxin) Tablet 360 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dihydrocodeine 30Mg (...) Tablet 30 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dihydrocodeine 30Mg (Dihydrocodeine) Tablet 30 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dinoprostone 0.5Mg (Cervitone Gel) Gel 0.5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diosmectite (Stoptrans) Powder 3 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Diosmin (Daflon) Tablet 500 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diphenhydramine + Dextromethorphan + Levomenthol (Benylin Dry Cough) Syrup 100 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Diphenhydramine + Dextromethorphan + Levomenthol (Benylin Dry Cough) Syrup 200 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Diphenhydramine Hcl + Ammonium Chloride + Sodium Citrate (D-Koff Syrup) Syrup 5 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Diphenhydramine Hcl + Ammonium Chloride + Sodium Citrate (Emzolyn Expectorant) Syrup 5 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Diphenhydramine Hcl + Ammonium Chloride + Sodium Citrate (Ngc Expectorant) Syrup 14 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Diphenhydramine Hcl + Ammonium Chloride + Sodium Citrate (Shaltoux 4Way) Syrup 14 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Diphenhydramine Hcl + Menthol (Emzolyn For Children) Syrup 7 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Diphenhydramine Hcl + Menthol (Ngc Child) Syrup 7 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Diphenoxylate 2.5Mg + Atropine 25Mcg (Lomotil) Tablet 2.5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diphtheria, Tetanus, Pertussis, Poliomyelitis (Tetraxim) Injection 0.5 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Diphtheria, Tetanus,Pertusis,Hepatitis B, Haemophilus (Pentavalent) Injection 0.5 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Disposable Infusion Pump (Pca) Item 200 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Disposable Mackintosh (...) Item 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Disposable Neonatal Spo2 Sensor (...) Item 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Dobutamine (...) Injection 250 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Docetaxel (Taxotere) Injection 80 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Docetaxel (Zuvitere) Injection 120 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dolutegravir + Lamivudine + Tenofovir (Acriptega) Tablet 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Domperidone (Motilium) Tablet 10 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Donepezil Hcl 5Mg (Aricept) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dopamine (...) Injection 200 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Dorzolamide + Timolol (Duosopt) Solution 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Doxazocin (Cadura Xl) Tablet 4 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Doxazocin (Cardura) Tablet 2 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Doxycycline (Doxycap) Capsule 100 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Drainage Bottles (Redivac Drain) Item 550 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Drip Giving Set (...) Item 500 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Drospirenone 3Mg + Ethinylestradiol 0.02Mg (Yaz) Tablet 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Dutasteride 0.5Mg +Tamsulosin Hydrochloride 0.4Mg (Duodart) Capsule 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Dutasteride 0.5Mg +Tamsulosin Hydrochloride 0.4Mg (Duostam) Tablet 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Dydrogesterone (Duphaston) Tablet 10 mg", "descr": "", "catid": 35, "source": 83},
])

others = np.array([
    {"name": "Daily ICU Management", "descr": "", "catid": 48, "source": 83},
    {"name": "Daily ICU Mgt + CPAP/HFNC", "descr": "", "catid": 48, "source": 83},
    {"name": "Daily ICU Mgt + Oxygen", "descr": "", "catid": 48, "source": 83},
    {"name": "Daily ICU Mgt + Ventilator", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "Dialysis", "descr": "", "catid": 37, "source": 83},
    {"name": "Dilation And Curretage", "descr": "", "catid": 37, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — D
# =============================================================================
# Total records on this sheet : 97
# Categories found            : consultations, diagnostic_imaging, laboratory_tests, medical_supplies, medications, others, surgeries
# Unmapped categories         : None
# =============================================================================
