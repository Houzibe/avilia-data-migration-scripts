import numpy as np

biologics = np.array([
    {"name": "Ebt (Rh +Ve Blood +Ebt Kit)", "descr": "", "catid": 31, "source": 83},
    {"name": "Ebt (Rh -Ve Blood +Ebt Kit)", "descr": "", "catid": 31, "source": 83},
])

consultations = np.array([
    {"name": "Endocrinology Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Endocrinology Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "ENT Specialist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "ENT Specialst Follow Up", "descr": "", "catid": 36, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Ear View - Middle & Int.Aud.Meatus", "descr": "", "catid": 27, "source": 83},
    {"name": "Echocardiography", "descr": "", "catid": 27, "source": 83},
    {"name": "Echocardiography-Transthoracic (2D, M-Mode, & Doppler) + Consultant Cardiologist Report", "descr": "", "catid": 27, "source": 83},
    {"name": "Elbow", "descr": "", "catid": 27, "source": 83},
    {"name": "Elbow Joint - Ap & Lat", "descr": "", "catid": 27, "source": 83},
    {"name": "Elbow X-Ray", "descr": "", "catid": 27, "source": 83},
])

laboratory_tests = np.array([
    {"name": "E/U/Cr", "descr": "", "catid": 39, "source": 83},
    {"name": "Electrocardiography ( ECG) + Consultant Cardiologist Report", "descr": "", "catid": 39, "source": 83},
    {"name": "Electrolytes", "descr": "", "catid": 39, "source": 83},
    {"name": "ELISA - Retroviral Screening", "descr": "", "catid": 39, "source": 83},
    {"name": "Ers Only", "descr": "", "catid": 39, "source": 83},
    {"name": "Erythrocyte Sedimentation Rate (ESR)", "descr": "", "catid": 39, "source": 83},
    {"name": "ESR", "descr": "", "catid": 39, "source": 83},
    {"name": "ESR + FBC", "descr": "", "catid": 39, "source": 83},
])

medications = np.array([
    {"name": "E-45 Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "E-Mal", "descr": "", "catid": 35, "source": 83},
    {"name": "Edrophonium", "descr": "", "catid": 35, "source": 83},
    {"name": "Efemoline Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Elicorid (Rabeprazole20Mg+Clarithromycin 500Mg+Amoxicillin1000Mg )", "descr": "", "catid": 35, "source": 83},
    {"name": "Ellamuselle[Libido Women]", "descr": "", "catid": 35, "source": 83},
    {"name": "Emal I Njection(Arthemeter)", "descr": "", "catid": 35, "source": 83},
    {"name": "Emvite Super Multivitamin Capsules", "descr": "", "catid": 35, "source": 83},
    {"name": "Emzolyn Expectorant", "descr": "", "catid": 35, "source": 83},
    {"name": "Emzolyn Syrup Children", "descr": "", "catid": 35, "source": 83},
    {"name": "Emzolyn With Codeine", "descr": "", "catid": 35, "source": 83},
    {"name": "Enalapril Maleate 10Mg(Teva)", "descr": "", "catid": 35, "source": 83},
    {"name": "Enalapril Maleate 20Mg (Alumus)", "descr": "", "catid": 35, "source": 83},
    {"name": "Enalapril Tab 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Enalapril Tab 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Encephabol", "descr": "", "catid": 35, "source": 83},
    {"name": "Encephabol Syrup 120Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Encephabol Syrup 200Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Endix G Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Enoxaparin", "descr": "", "catid": 35, "source": 83},
    {"name": "Epanutin Caps (100Mg)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ephedrine + Theophyline", "descr": "", "catid": 35, "source": 83},
    {"name": "Ephedrine Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Epilim Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Epilim Tab 200Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Epinephrine (Adrenaline)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ergometrine", "descr": "", "catid": 35, "source": 83},
    {"name": "Ergot Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Ergot Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Ergotamine", "descr": "", "catid": 35, "source": 83},
    {"name": "Ergotamine Tartrate + Caffeine", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin 125Mg/5Ml Susp", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin 250Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythromycin 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythropoeitin", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythropoetin 2000 Unit Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Erythropoietin-A 10000 Unit Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Esidrex 25Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Esomeprazole", "descr": "", "catid": 35, "source": 83},
    {"name": "Esomeprazole 40Mg Branded (Nexium)", "descr": "", "catid": 35, "source": 83},
    {"name": "Essential Forte Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Essential Forte/Liver Forte", "descr": "", "catid": 35, "source": 83},
    {"name": "Ethambutol 400Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ethosuximide", "descr": "", "catid": 35, "source": 83},
    {"name": "Etovit Capgel 200Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Eucalyptus Oil", "descr": "", "catid": 35, "source": 83},
    {"name": "Eurax Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Evadine 200Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Evening Primrose Oil 500Mg Supplement", "descr": "", "catid": 35, "source": 83},
    {"name": "Evitol 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Exforge (Amlodipine/Valsartan) 10Mg/12.5Mg/160Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Exforge Hct 10/160/12.5(Amlodipine/Valsartan/Hct)", "descr": "", "catid": 35, "source": 83},
    {"name": "Exoforg Hct 10/160/25Mg Tab(Amlodipine/Valsartan/Hct)", "descr": "", "catid": 35, "source": 83},
])

others = np.array([
    {"name": "ECG (Pre-Exercise And Street Test)", "descr": "", "catid": 48, "source": 83},
    {"name": "ECG (Pre-Exercise/Resting)", "descr": "", "catid": 48, "source": 83},
    {"name": "ECG (Stress Test Only)", "descr": "", "catid": 48, "source": 83},
    {"name": "ECG For ≤4Years Old", "descr": "", "catid": 48, "source": 83},
    {"name": "EEG", "descr": "", "catid": 48, "source": 83},
    {"name": "Electrocardiography [ECG]", "descr": "", "catid": 48, "source": 83},
    {"name": "Electrocardiography [ECG] - Pre And Post Exercise", "descr": "", "catid": 48, "source": 83},
    {"name": "Electroencephalography [Eeg]", "descr": "", "catid": 48, "source": 83},
    {"name": "EMG", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "Ear", "descr": "", "catid": 37, "source": 83},
    {"name": "Ear Piercing", "descr": "", "catid": 37, "source": 83},
    {"name": "Ear Syringing", "descr": "", "catid": 37, "source": 83},
    {"name": "Ear Syringing – Bilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Ear Syringing – Unilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Echocardiography-Transthoracic (2D, M-Mode, & Doppler) + Consultant Cardiologist Report", "descr": "", "catid": 37, "source": 83},
    {"name": "Ectopic Parathyroidectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Ectopic Pregnancy", "descr": "", "catid": 37, "source": 83},
    {"name": "Edge Resection Of The Ovary", "descr": "", "catid": 37, "source": 83},
    {"name": "Electrofulgaration Of Condylomata Acuminata", "descr": "", "catid": 37, "source": 83},
    {"name": "Encephalocoele Excision", "descr": "", "catid": 37, "source": 83},
    {"name": "Endoscopy", "descr": "", "catid": 37, "source": 83},
    {"name": "Enema Saponis", "descr": "", "catid": 37, "source": 83},
    {"name": "Enterocele Or Vault Prolapse Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Enterostomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Epidedectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Epidural/Spinal", "descr": "", "catid": 37, "source": 83},
    {"name": "Epiostomy And Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Erbs Palsy Per Visit", "descr": "", "catid": 37, "source": 83},
    {"name": "Ethmoidectomy; Fronto, External", "descr": "", "catid": 37, "source": 83},
    {"name": "EUA", "descr": "", "catid": 37, "source": 83},
    {"name": "Eua Nasopharynx + Biopsy", "descr": "", "catid": 37, "source": 83},
    {"name": "Evacuation Of Impacted Faeces", "descr": "", "catid": 37, "source": 83},
    {"name": "Evacuation Of Scrotal Hematoma", "descr": "", "catid": 37, "source": 83},
    {"name": "Examination Under Anaesthesia", "descr": "", "catid": 37, "source": 83},
    {"name": "Exchange Blood Transfusion", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision / Diathermy Of Warts", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Biopsy", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Biopsy (Block Fee Excluding Histology)", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Bronchial Sinus", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Mammary Fistula", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Meckel’S Diverticulum", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Breast Lump", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Intrascrostal Mass", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Liver Abscess", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Lymphoedematous Lymph Tissues", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Nasomaxillary Mass", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Neurofibroma", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Pelvi-Rectal Fistula", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Salivary Gland", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Tophi", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Urethral Carbuncle", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Of Vaginal Septum", "descr": "", "catid": 37, "source": 83},
    {"name": "Excision Pilonidal Sinus", "descr": "", "catid": 37, "source": 83},
    {"name": "Excission Of Haemangiomas", "descr": "", "catid": 37, "source": 83},
    {"name": "Exostectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Exploratory Laparatomy/Lysis Of Adhesions", "descr": "", "catid": 37, "source": 83},
    {"name": "Exploratory Laparotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Extensive (Small And Large) Bowel Resection And Anastomoses", "descr": "", "catid": 37, "source": 83},
    {"name": "External Fixation", "descr": "", "catid": 37, "source": 83},
])

vaccines = np.array([
    {"name": "Eng B 10Mcg (Hepatitis B)", "descr": "", "catid": 46, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — Product E
# =============================================================================
# Total records on this sheet : 134
# Categories found            : biologics, consultations, diagnostic_imaging, laboratory_tests, medications, others, surgeries, vaccines
# Unmapped categories         : None
# Duplicates removed          : medications:"Enoxaparin"; medications:"Ergometrine"; medications:"Erythromycin"; medications:"Erythromycin"; medications:"Erythropoeitin"; medications:"Esomeprazole"
# =============================================================================
