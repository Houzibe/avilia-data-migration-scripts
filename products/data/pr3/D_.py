import numpy as np


consultations = np.array([
    {"name": "Dental Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Dental Review", "descr": "", "catid": 36, "source": 83},
    {"name": "Dental Specialist Consult-Orthodontist", "descr": "", "catid": 36, "source": 83},
    {"name": "Dental Specialist Consult-Orthodontist Review", "descr": "", "catid": 36, "source": 83},
    {"name": "Dental Specialist Consult-Others (Maxillofacial) Review", "descr": "", "catid": 36, "source": 83},
    {"name": "Dental Specialist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Dermatologist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Dermatologist Consultation Follow-Up", "descr": "", "catid": 36, "source": 83},
    {"name": "Dietician Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Dietician Review", "descr": "", "catid": 36, "source": 83},
])


diagnostic_imaging = np.array([
    {"name": "Diagnostic Mammo", "descr": "", "catid": 27, "source": 83},
    {"name": "Doppler (Both Legs)", "descr": "", "catid": 27, "source": 83},
    {"name": "Doppler (Renal Artery)", "descr": "", "catid": 27, "source": 83},
    {"name": "Doppler Scan Per Limb", "descr": "", "catid": 27, "source": 83},
    {"name": "Doppler Ultrasound", "descr": "", "catid": 27, "source": 83},
    {"name": "Dorsal Spine", "descr": "", "catid": 27, "source": 83},
    {"name": "Dorsal Spine (Thoracic)", "descr": "", "catid": 27, "source": 83},
])


infusions = np.array([
    {"name": "10% Detrose (500Ml)", "descr": "", "catid": 47, "source": 83},
    {"name": "4.3% Dextrose / 0.18% Saline (500Ml)", "descr": "", "catid": 47, "source": 83},
    {"name": "5% Detrose / Saline (500Ml)", "descr": "", "catid": 47, "source": 83},
    {"name": "5% Dextrose / Water (500Ml)", "descr": "", "catid": 47, "source": 83},
    {"name": "Darrow’S Solution Full Strength", "descr": "", "catid": 47, "source": 83},
    {"name": "Darrow’S Solution Half Strength", "descr": "", "catid": 47, "source": 83},
    {"name": "Dextrose 50% Inj", "descr": "", "catid": 47, "source": 83},
    {"name": "Dextrose Saline 4.3%", "descr": "", "catid": 47, "source": 83},
    {"name": "Dextrose Saline 5%", "descr": "", "catid": 47, "source": 83},
    {"name": "Dextrose Water 10%", "descr": "", "catid": 47, "source": 83},
    {"name": "Dextrose Water 5%", "descr": "", "catid": 47, "source": 83},
    {"name": "Dextrose Water 50%", "descr": "", "catid": 47, "source": 83},
    {"name": "Dextrose,4.3%/Norm.Saline,0.18", "descr": "", "catid": 47, "source": 83},
    {"name": "Dextrose,5% Infusion 0.5L", "descr": "", "catid": 47, "source": 83},
    {"name": "Dextrose/Saline O.5L", "descr": "", "catid": 47, "source": 83},
])


laboratory_tests = np.array([
    {"name": "D-Dimer", "descr": "", "catid": 39, "source": 83},
    {"name": "D-Dimer Quantitative", "descr": "", "catid": 39, "source": 83},
    {"name": "Dengue Virus", "descr": "", "catid": 39, "source": 83},
    {"name": "Differential White Cell Count ( WBC-Diff)", "descr": "", "catid": 39, "source": 83},
    {"name": "Direct Bilirubin", "descr": "", "catid": 39, "source": 83},
    {"name": "Direct Coomb'S Test", "descr": "", "catid": 39, "source": 83},
    {"name": "Drug & Alcohol Screen Test", "descr": "", "catid": 39, "source": 83},
])


medical_devices = np.array([
    {"name": "Digital Thermometre", "descr": "", "catid": 29, "source": 83},
])


medical_supplies = np.array([
    {"name": "Dispensing Envelop", "descr": "", "catid": 34, "source": 83},
    {"name": "Disposable Glove", "descr": "", "catid": 34, "source": 83},
])


medications = np.array([
    {"name": "Dabigatran 110Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dabigatran 150Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Daflon 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Daflon Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Daflon Tab 1000Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Daflon Tab 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dalacin T Topical Solution 30Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Dalacin T Tropical Soluton 50Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Dantrolene (Dantrium) 25Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Daonil", "descr": "", "catid": 35, "source": 83},
    {"name": "Dapagliflozin 10Mg Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Day And Night Nurse Capsule", "descr": "", "catid": 35, "source": 83},
    {"name": "Deep Heat Spray", "descr": "", "catid": 35, "source": 83},
    {"name": "Depixol 40Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Depo Provera", "descr": "", "catid": 35, "source": 83},
    {"name": "Depo Provera 150Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Depo Provera Injection 250Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Depo- Provera 150Mg Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Depomedrol Inj 40Mg/Amp", "descr": "", "catid": 35, "source": 83},
    {"name": "Depomedrol Inj 80Mg/Amp", "descr": "", "catid": 35, "source": 83},
    {"name": "Dequadin Lozenges", "descr": "", "catid": 35, "source": 83},
    {"name": "Dequalinium Lozenges250Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dermazine Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Dermazine Cream 25G", "descr": "", "catid": 35, "source": 83},
    {"name": "Dermazine Cream 50G", "descr": "", "catid": 35, "source": 83},
    {"name": "Dermovate Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Dermovate Cream 25G", "descr": "", "catid": 35, "source": 83},
    {"name": "Dexamethasone 1Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dexamethasone 1Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Dexamethasone 4Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Dexamethasone 4Mg Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Dexamethasone 8Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Dexamethasone Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Dexamethasonetablets 0.5Mg And 4Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dextrose Water 10%*500Ml Inf.", "descr": "", "catid": 35, "source": 83},
    {"name": "Diabenese 250Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diamicron Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Diamox 250Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Dianofem", "descr": "", "catid": 35, "source": 83},
    {"name": "Diatebin 450Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Diazepam", "descr": "", "catid": 35, "source": 83},
    {"name": "Diazepam 10Mg Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Diazepam 10Mg/Amp Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Diazepam 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diazepam 5Mg (Swipha 50/Tab)", "descr": "", "catid": 35, "source": 83},
    {"name": "Diazepam 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Diazepam Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Diazepam Tablets 5Mg, 2Mg, 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclo Supp", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac 100Mg Suppository", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac 12.5 Suppository", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac 20G Gel", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac 50Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac 50Mg Suppository", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac 75Mg Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Gel 50G", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Gutt", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac K+ Tab 50Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Na+ Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Sodium + Misoprostol Tab Forte", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Sodium 100Mg (Bentren)", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Sodium 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Sodium 50G Gel (Olfen Gel)", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Sodium 50Mg (Diclomax)", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Sodium 50Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Sodium 75Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Sodium+B1+B6+B12Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Supp 100Mg (Voltaren)", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Supp. 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Supp.50Mg (Voltaren)", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac Suppository", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclofenac/Misoprostol", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclomol 500Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Diclomol Gel", "descr": "", "catid": 35, "source": 83},
    {"name": "Dicynone", "descr": "", "catid": 35, "source": 83},
    {"name": "Dicynone 250Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Dicynone 250Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Didrogesterone 10Mg (Duphaston)", "descr": "", "catid": 35, "source": 83},
    {"name": "Digoxin", "descr": "", "catid": 35, "source": 83},
    {"name": "Digoxin 0.0625Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Digoxin 0.25Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Digoxin 0.25Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Digoxin Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Dihydrocodein (Df118)", "descr": "", "catid": 35, "source": 83},
    {"name": "Dihydrocodeine 30Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Dihydrocodeine 30Mg(Df118)", "descr": "", "catid": 35, "source": 83},
    {"name": "Diloxanide Furoate 500Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Diovan 160Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Diovan 160Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Diovan 80 - Norvartis", "descr": "", "catid": 35, "source": 83},
    {"name": "Diovan 80Mg (Valsartan)", "descr": "", "catid": 35, "source": 83},
    {"name": "Diovan 80Mg Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Ditropan 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Dobutamine Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Dolometa B Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Doloneurobion (Dolometa - B)", "descr": "", "catid": 35, "source": 83},
    {"name": "Dolutegravir 50Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dolutegravir/Lamivudine/Tenofovir 50/200/300", "descr": "", "catid": 35, "source": 83},
    {"name": "Domperidon Tab 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Domperidone 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Donepezil 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dopamine 200Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Dot 4", "descr": "", "catid": 35, "source": 83},
    {"name": "Doxazosin (A.P.S) 1Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Doxazosin (A.P.S) 2Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Doxazosin 4Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Doxazosin 4Mg Tab (Cardura)", "descr": "", "catid": 35, "source": 83},
    {"name": "Doxycyclin 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Doxycycline 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Doxycycline 100Mg Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Doxycycline 100Mg Cap (Vibramycin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Drez Cream (Povidone Iodine + Metronidazole)", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugela", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugs - Chlorpromazine Hcl 25 MG Oral Chemo Anit", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugs - Cisplatin, Powder Or Solution, Per 10 MG", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugs - Digoxin", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugs - Gentamicin", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugs - Injection Betamethasone To 6 MG", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugs - Injection Hydrocortisone Sodium Succinate To 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugs - Injection Pentazocine Hcl To 30 MG", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugs - Injection Prednisolone Acetate To 1 ML", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugs - Injection Prednisolone Sodium Phosphate To 20 MG", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugs - Injection Tetanus Toxoid To 1 ML", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugs - Methylprednisolone Oral, Per 4 MG", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugs - Methylprednisone Oral 4 Gm", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugs - Prednisolone Oral 5 MG", "descr": "", "catid": 35, "source": 83},
    {"name": "Drugs - Prednisolone Oral, Per 5 MG", "descr": "", "catid": 35, "source": 83},
    {"name": "Ducolax Suppository", "descr": "", "catid": 35, "source": 83},
    {"name": "Ducolax Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Duodart 0.5/0.4Mg By 30", "descr": "", "catid": 35, "source": 83},
    {"name": "Duovir 650Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Duphaston 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Duphaston Tablet 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Dutasteride 0.5Mg Tab (Avodart )", "descr": "", "catid": 35, "source": 83},
    {"name": "Dydrogesterone 10Mg", "descr": "", "catid": 35, "source": 83},
])


nutritionals = np.array([
    {"name": "Doloneurobion Tab", "descr": "", "catid": 33, "source": 83},
    {"name": "Dynamogen Liquid 10Mls", "descr": "", "catid": 33, "source": 83},
])


others = np.array([
    {"name": "Day Observation (Less Than 6 Hours)", "descr": "", "catid": 48, "source": 83},
    {"name": "Day Observation (More Than 6 Hours)", "descr": "", "catid": 48, "source": 83},
    {"name": "Domestic Pre-Employment Test", "descr": "", "catid": 48, "source": 83},
    {"name": "Domestic Pre-Employment Test (Driver)", "descr": "", "catid": 48, "source": 83},
    {"name": "Double Bed", "descr": "", "catid": 48, "source": 83},
])


surgeries = np.array([
    {"name": "Daily Continuous Cardiac Monitoring", "descr": "", "catid": 37, "source": 83},
    {"name": "Decortications Of Lung", "descr": "", "catid": 37, "source": 83},
    {"name": "Dermabond Suturing", "descr": "", "catid": 37, "source": 83},
    {"name": "Diaphragmatic Hernia Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Direct Laryngoscopy", "descr": "", "catid": 37, "source": 83},
    {"name": "Drainage Of Anal Abscess", "descr": "", "catid": 37, "source": 83},
    {"name": "Drainage Of Ascities", "descr": "", "catid": 37, "source": 83},
    {"name": "Drainage Of Whitlow", "descr": "", "catid": 37, "source": 83},
    {"name": "Dressing &/Or Debridement Under Anaesthesia", "descr": "", "catid": 37, "source": 83},
    {"name": "Dressing &/Or Debridement Without Anaesthesia", "descr": "", "catid": 37, "source": 83},
    {"name": "Dressing-Minor", "descr": "", "catid": 37, "source": 83},
])


vaccines = np.array([
    {"name": "DPT", "descr": "", "catid": 46, "source": 83},
    {"name": "DPT Vaccine", "descr": "", "catid": 46, "source": 83},
])


# =============================================================================
# SHEET SUMMARY — Product D
# =============================================================================
# Total records on this sheet : 199
# Categories found            : consultations, diagnostic_imaging, infusions, laboratory_tests, medical_devices, medical_supplies, medications, nutritionals, others, surgeries, vaccines
# Duplicates removed          : 0
# Unmapped categories         : None
# =============================================================================
