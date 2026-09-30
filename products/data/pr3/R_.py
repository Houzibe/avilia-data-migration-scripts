import numpy as np


consultations = np.array([
    {"name": "Radiology Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Rare Specialist Consultation(Paed Cardio, Endocrinologist, Nephrologist, Cardiothoracic Surgeon)", "descr": "", "catid": 36, "source": 83},
    {"name": "Rare Specialist Review", "descr": "", "catid": 36, "source": 83},
    {"name": "Registration Fee", "descr": "", "catid": 36, "source": 83},
    {"name": "Rheumatologist Consultation", "descr": "", "catid": 36, "source": 83},
])


diagnostic_imaging = np.array([
    {"name": "Retrograde Urethrogram", "descr": "", "catid": 27, "source": 83},
    {"name": "Routine Obs Scan (Inhouse)", "descr": "", "catid": 27, "source": 83},
])


infusions = np.array([
    {"name": "Ringers Lactate Solution (500Ml)", "descr": "", "catid": 47, "source": 83},
    {"name": "Ringers Solution", "descr": "", "catid": 47, "source": 83},
])


laboratory_tests = np.array([
    {"name": "Random Blood Sugar", "descr": "", "catid": 39, "source": 83},
    {"name": "Random Blood Sugar (Rbs)", "descr": "", "catid": 39, "source": 83},
    {"name": "RBC", "descr": "", "catid": 39, "source": 83},
    {"name": "Red Cell Count", "descr": "", "catid": 39, "source": 83},
    {"name": "Retics Count", "descr": "", "catid": 39, "source": 83},
    {"name": "Reticulocyte", "descr": "", "catid": 39, "source": 83},
    {"name": "Rheumatoid Factor", "descr": "", "catid": 39, "source": 83},
    {"name": "Rhumatoid Factor (Quant.)", "descr": "", "catid": 39, "source": 83},
    {"name": "Rsv (Respiratory Syncytial Virus)", "descr": "", "catid": 39, "source": 83},
    {"name": "Rubella Igg/Igm", "descr": "", "catid": 39, "source": 83},
])


medical_devices = np.array([
    {"name": "Rental Of Infusion Pump", "descr": "", "catid": 29, "source": 83},
    {"name": "Rental Of Monitor", "descr": "", "catid": 29, "source": 83},
])


medications = np.array([
    {"name": "Rabeprazole (Pariet)", "descr": "", "catid": 35, "source": 83},
    {"name": "Rabeprazole 10Mg Tab (Pariet)", "descr": "", "catid": 35, "source": 83},
    {"name": "Rabeprazole 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rabeprazole 20Mg Tab (Pariet)", "descr": "", "catid": 35, "source": 83},
    {"name": "Rabeprazole/Clarithromycin/Amoxicillin", "descr": "", "catid": 35, "source": 83},
    {"name": "Rabeprazole/Domperidone 20/30Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril (Teva) Caps 2.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril (Teva) Caps 2.5Mg X 28", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 1.25Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 1.25Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 10Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 10Mg/Hydrochlorothiazide 12.5Mg Tab (Tritazide)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 10Mg/Hydrochlorothiazide 25Mg Tab (Tritazide)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 2.5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 5Mg/Hydrochlorothiazide 12.5Mg Tab (Tritazide)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril Caps 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril Caps 5Mg X 28", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramitace Tabs 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramitace Tabs 10Mg X 30", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramitace Tabs 2.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramitace Tabs 2.5Mg X 30", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramitace Tabs 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramitace Tabs 5Mg X 30", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine 150Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine 150Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine 50Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine 50Mg/2Ml Inj (Zantac)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine Tab 150Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine Tab 150Mg (Zantac)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine Tab 300Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine Tab 300Mg (Zantac)", "descr": "", "catid": 35, "source": 83},
    {"name": "Rapiclav 625Mg Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Regroton Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Remdesivir 100Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Retin-A", "descr": "", "catid": 35, "source": 83},
    {"name": "Rhinathiol", "descr": "", "catid": 35, "source": 83},
    {"name": "Rhinathiol + Promethazine", "descr": "", "catid": 35, "source": 83},
    {"name": "Rhinathiol Adult", "descr": "", "catid": 35, "source": 83},
    {"name": "Rhinathiol Children", "descr": "", "catid": 35, "source": 83},
    {"name": "Rhogam (Anti-D)", "descr": "", "catid": 35, "source": 83},
    {"name": "Rifampicin 300Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rifampicin 300Mg Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Rifampicin Susp 100Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Rifampicin Susp-60Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Rifampicin Syrup 100Mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Risperdal 3Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Risperidone 2Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rivaroxaban 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rivaroxaban 15Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rivaroxaban 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rohypnol Tab 1Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosiglitazone4Mg Tab (Avandia)", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosuvastatin 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosuvastatin 10Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosuvastatin 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosuvastatin 20Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosuvastatin 40Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosuvastatin 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Rovamycin 3Mu Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Rovigon Tablet", "descr": "", "catid": 35, "source": 83},
])


nutritionals = np.array([
    {"name": "Ranferon Blood Tonic 100Ml", "descr": "", "catid": 33, "source": 83},
    {"name": "Ranferon Blood Tonic 200Ml", "descr": "", "catid": 33, "source": 83},
    {"name": "Ranferon-12 Capsule", "descr": "", "catid": 33, "source": 83},
    {"name": "Redoxon 1G Tab", "descr": "", "catid": 33, "source": 83},
])


others = np.array([
    {"name": "Referral (International)", "descr": "", "catid": 48, "source": 83},
    {"name": "Referral (Local)", "descr": "", "catid": 48, "source": 83},
    {"name": "Registration", "descr": "", "catid": 48, "source": 83},
    {"name": "Removal Of Mortal Remains", "descr": "", "catid": 48, "source": 83},
    {"name": "Removal Of Mortal Remains/Embalment", "descr": "", "catid": 48, "source": 83},
    {"name": "Repair Of Achilles Tendon Tear (Excluding Investigations And Admission)", "descr": "", "catid": 48, "source": 83},
    {"name": "Rh +Ve", "descr": "", "catid": 48, "source": 83},
])


surgeries = np.array([
    {"name": "Reconstruction/Repair Of Prostatic/Membranous Urethra", "descr": "", "catid": 37, "source": 83},
    {"name": "Recto-Urethral Fistula Closure", "descr": "", "catid": 37, "source": 83},
    {"name": "Rectovesical Fistula Closure", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Both Ovaries", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Cerumol (Ear Wax)", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Foreign Body (Ear)", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Foreign Body (Ear-Bilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Foreign Body (Ear-Unilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Foreign Body (Nose)", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Foreign Body (Nose- Bilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Foreign Body (Nose- Unilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Foreign Body (Throat)", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of IUCD With Forceps I", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of IUCD With Forceps Ii", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of One Ovary", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of 3Rd Deg Tear", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Cervical Laceration", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Minor Vaginal Laceration", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Vag Inal Laceration (2Nd Degree)", "descr": "", "catid": 37, "source": 83},
    {"name": "Retrieval Of Missing IUCD", "descr": "", "catid": 37, "source": 83},
    {"name": "Retroperitoneal Drainage Of Perinephric Abscess", "descr": "", "catid": 37, "source": 83},
    {"name": "Rhogam Injection", "descr": "", "catid": 37, "source": 83},
    {"name": "Ring Pessary", "descr": "", "catid": 37, "source": 83},
    {"name": "Root Canal Therapy Anterior", "descr": "", "catid": 37, "source": 83},
    {"name": "Root Canal Therapy Posterior", "descr": "", "catid": 37, "source": 83},
])


vaccines = np.array([
    {"name": "Rabies Vaccine", "descr": "", "catid": 46, "source": 83},
    {"name": "Rota Virus Vacc.", "descr": "", "catid": 46, "source": 83},
    {"name": "Rotavirus Vaccine - Rotarix (1 Dose Syringe)", "descr": "", "catid": 46, "source": 83},
    {"name": "Rotavirus Vaccine - Rotasil (1 Dose Syringe)", "descr": "", "catid": 46, "source": 83},
])


# =============================================================================
# SHEET SUMMARY — Product R
# =============================================================================
# Total records on this sheet : 124
# Categories found            : consultations, diagnostic_imaging, infusions, laboratory_tests, medical_devices, medications, nutritionals, others, surgeries, vaccines
# Duplicates removed          : 0
# Unmapped categories         : None
# =============================================================================
