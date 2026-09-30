import numpy as np


biologics = np.array([
    {"name": "Erythropoetin 2000 Unit Inj", "descr": "", "catid": 31, "source": 83},
    {"name": "Erythropoietin 40000I.U", "descr": "", "catid": 31, "source": 83},
])


consultations = np.array([
    {"name": "Emergency Specialist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Endocinologist Consultataion", "descr": "", "catid": 36, "source": 83},
    {"name": "Endocrinologist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Endocrinologist Consultation Follow-Up", "descr": "", "catid": 36, "source": 83},
    {"name": "ENT Consultation", "descr": "", "catid": 36, "source": 83},
])


diagnostic_imaging = np.array([
    {"name": "ECG (Pre-Exercise And Stress Test)", "descr": "", "catid": 27, "source": 83},
    {"name": "ECG For ≤4Years Old", "descr": "", "catid": 27, "source": 83},
    {"name": "Echocardiography (TTE)", "descr": "", "catid": 27, "source": 83},
    {"name": "EEG", "descr": "", "catid": 27, "source": 83},
    {"name": "Elbow", "descr": "", "catid": 27, "source": 83},
    {"name": "Elbow Joint", "descr": "", "catid": 27, "source": 83},
    {"name": "EMG", "descr": "", "catid": 27, "source": 83},
])


laboratory_tests = np.array([
    {"name": "E/U/Cr", "descr": "", "catid": 39, "source": 83},
    {"name": "E/U/Crt", "descr": "", "catid": 39, "source": 83},
    {"name": "Ear Swab M/C/S", "descr": "", "catid": 39, "source": 83},
    {"name": "Egfr", "descr": "", "catid": 39, "source": 83},
    {"name": "Electrolytes", "descr": "", "catid": 39, "source": 83},
    {"name": "Electrolytes & Urea", "descr": "", "catid": 39, "source": 83},
    {"name": "Eosinophil Count", "descr": "", "catid": 39, "source": 83},
    {"name": "ESR", "descr": "", "catid": 39, "source": 83},
    {"name": "Esr (Sedimentation Rate)", "descr": "", "catid": 39, "source": 83},
    {"name": "ESR Only", "descr": "", "catid": 39, "source": 83},
    {"name": "ESR+FBC", "descr": "", "catid": 39, "source": 83},
])


medical_supplies = np.array([
    {"name": "Elbow Length Glove", "descr": "", "catid": 34, "source": 83},
    {"name": "Endotracheal Tube 4.0Mm", "descr": "", "catid": 34, "source": 83},
    {"name": "Examination Glove", "descr": "", "catid": 34, "source": 83},
    {"name": "Exchange Blood Giving Set", "descr": "", "catid": 34, "source": 83},
    {"name": "Exchange Blood Trans Set", "descr": "", "catid": 34, "source": 83},
    {"name": "Eye Pad", "descr": "", "catid": 34, "source": 83},
])


medications = np.array([
    {"name": "E-Mal 150Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "E-Mal 75Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ear - Ear Syringing", "descr": "", "catid": 35, "source": 83},
    {"name": "Efavirenz 600Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Efavirenz 600Mg/Emtricitabine 200Mg/Tenofivir 300Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Efemoline Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Electrolyte Profile", "descr": "", "catid": 35, "source": 83},
    {"name": "Empagliflozin 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Emtricitabine/Tenofovir 200/300Mg Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Emzolyn Cough Syr", "descr": "", "catid": 35, "source": 83},
    {"name": "Emzolyn Expectorant Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Emzolyn Expectorant Syrup Paed", "descr": "", "catid": 35, "source": 83},
    {"name": "Enalapril 10Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Enalapril 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Enalapril Maleate Tabs 10Mg X 28 [England]", "descr": "", "catid": 35, "source": 83},
    {"name": "Enalapril Maleate Tabs 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Enalapril Maleate Tabs 20Mg X 28", "descr": "", "catid": 35, "source": 83},
    {"name": "Enaretic Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Enaretic Tabs X 30", "descr": "", "catid": 35, "source": 83},
    {"name": "Encephabol Syr 100Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Encephabol Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Endix G Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Enhancin 312Mg/5Ml Susp", "descr": "", "catid": 35, "source": 83},
    {"name": "Enhancin 375Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Enhancin 625Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Enoxaparin 40", "descr": "", "catid": 35, "source": 83},
    {"name": "Enoxaparin 40Mg Injection (Clexane)", "descr": "", "catid": 35, "source": 83},
    {"name": "Enterogermina", "descr": "", "catid": 35, "source": 83},
    {"name": "Ephedrine Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Epipen(Adrenaline)0.3Mg/0.3Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Epsom Salt", "descr": "", "catid": 35, "source": 83},
    {"name": "Ergometrine Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Ergotamine Tartrate 100Mg Tab (Cafergot)", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin 125Mg/5Ml Susp", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin 125Mg/5Ml Susp. 100Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin 125Mg/5Ml Susp. 60Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin 250Mg Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin 250Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin 500Mg Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin 500Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin 500Mg Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin Suspension", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin Tab (250Mg)", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin Tab (500Mg)", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythropoietin 4000Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Escitalopram 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Esidrex 25Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Esomeprazole 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Esomeprazole 20Mg (Nexium )", "descr": "", "catid": 35, "source": 83},
    {"name": "Esomeprazole 20Mg Tab (Nexium)", "descr": "", "catid": 35, "source": 83},
    {"name": "Esomeprazole 40Mg Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Esomeprazole 40Mg Tab (Nexium)", "descr": "", "catid": 35, "source": 83},
    {"name": "Esomeprazole Nexium 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Esomeprazole Nexium 40Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "ESR (Erythocyte Sedimentation Rate)", "descr": "", "catid": 35, "source": 83},
    {"name": "Essential Forte", "descr": "", "catid": 35, "source": 83},
    {"name": "Essential Forte Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Ethambutol", "descr": "", "catid": 35, "source": 83},
    {"name": "Ethambutol 400Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Eucalyptus Oil", "descr": "", "catid": 35, "source": 83},
    {"name": "Eucardic 12.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Eucardic 25Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Eucardic 3.125Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Eurax Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Evadine 200Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Eviol 100Mg Capgel", "descr": "", "catid": 35, "source": 83},
    {"name": "Evitol 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Exacef 1.25Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Exforge 5/12.5/160Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Eye Antioxidant Cap", "descr": "", "catid": 35, "source": 83},
])


nutritionals = np.array([
    {"name": "Etovit Capgel 200Mg", "descr": "", "catid": 33, "source": 83},
    {"name": "Evening Prime Rose Cap", "descr": "", "catid": 33, "source": 83},
])


others = np.array([
    {"name": "EBT (Rh+Ve Blood + EBT Kit)(Minus Blood)", "descr": "", "catid": 48, "source": 83},
    {"name": "ECG ( Stress Test Only)", "descr": "", "catid": 48, "source": 83},
    {"name": "ECG(Pre-Exercise/Resting)", "descr": "", "catid": 48, "source": 83},
    {"name": "Echocardiogram", "descr": "", "catid": 48, "source": 83},
    {"name": "Emergency Call-Out Fee (Radiographer)", "descr": "", "catid": 48, "source": 83},
])


surgeries = np.array([
    {"name": "Ear Lobe Reconstruction", "descr": "", "catid": 37, "source": 83},
    {"name": "Ear Piercing", "descr": "", "catid": 37, "source": 83},
    {"name": "Ear Syringing", "descr": "", "catid": 37, "source": 83},
    {"name": "Ear Syringing - Bilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Ear Syringing - Unilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Ear Toileting", "descr": "", "catid": 37, "source": 83},
    {"name": "EBT (Central Line+Insertion Of Central Line+ Procedure) Does Not Include Blood", "descr": "", "catid": 37, "source": 83},
    {"name": "EBT (Rh -Ve + Blood + EBT Kit + Procedure)", "descr": "", "catid": 37, "source": 83},
    {"name": "EBT (Rh+Ve Blood + EBT + Procedure Kit) (For Neonates)", "descr": "", "catid": 37, "source": 83},
    {"name": "Electrocautery Of The Nose", "descr": "", "catid": 37, "source": 83},
    {"name": "Electrocautery Per Quadrant", "descr": "", "catid": 37, "source": 83},
    {"name": "Emergency Blood Transfusion (Per Pint)", "descr": "", "catid": 37, "source": 83},
    {"name": "Emergency Caesn Section", "descr": "", "catid": 37, "source": 83},
    {"name": "Emergency Pap Smear", "descr": "", "catid": 37, "source": 83},
    {"name": "Emphysematous Cyst, Excision, Bilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Emphysematous Cyst, Excision, Unilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Endometrial Biopsy", "descr": "", "catid": 37, "source": 83},
    {"name": "Endoscopy", "descr": "", "catid": 37, "source": 83},
    {"name": "Enema Saponis", "descr": "", "catid": 37, "source": 83},
    {"name": "Enterocele Or Vault Prolapse Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Entropion Or Ectropion Free Skin,", "descr": "", "catid": 37, "source": 83},
    {"name": "Epidural During Labour", "descr": "", "catid": 37, "source": 83},
    {"name": "Epidural/Spinal", "descr": "", "catid": 37, "source": 83},
    {"name": "Eua", "descr": "", "catid": 37, "source": 83},
    {"name": "Evacuation Of Impacted Faeces", "descr": "", "catid": 37, "source": 83},
    {"name": "Evisceration Or Enucleation With Or Without Hydroxyapatite Implantation", "descr": "", "catid": 37, "source": 83},
    {"name": "Exchange Blood Transfusion (+ Set)", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Biopsy (Block Fee Excluding Histology)", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Biopsy (Exclude Histology)", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Biopsy (With Histology)", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Intrascrotal Mass", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Overgranulated Tissue + Skin Graft <10%", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Pelvi-Rectal Fistula", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Salivary Gland", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Soft Tissue Mass", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Vaginal Septum", "descr": "", "catid": 37, "source": 83},
    {"name": "Exenteration", "descr": "", "catid": 37, "source": 83},
    {"name": "Exenteration, Anterior", "descr": "", "catid": 37, "source": 83},
    {"name": "Exenteration, Posterior", "descr": "", "catid": 37, "source": 83},
    {"name": "Exenteration, Total", "descr": "", "catid": 37, "source": 83},
    {"name": "Exploratory Laparotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "External Fixation", "descr": "", "catid": 37, "source": 83},
    {"name": "Extirpation Per Quadrant", "descr": "", "catid": 37, "source": 83},
])


vaccines = np.array([
    {"name": "Engerix-B Vaccine", "descr": "", "catid": 46, "source": 83},
])


# =============================================================================
# SHEET SUMMARY — Product E
# =============================================================================
# Total records on this sheet : 153
# Categories found            : biologics, consultations, diagnostic_imaging, laboratory_tests, medical_supplies, medications, nutritionals, others, surgeries, vaccines
# Duplicates removed          : 0
# Unmapped categories         : None
# =============================================================================
