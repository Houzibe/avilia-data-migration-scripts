import numpy as np

consultations = np.array([
    {"name": "Radiologist Consulation", "descr": "", "catid": 36, "source": 83},
    {"name": "Radiologist Review", "descr": "", "catid": 36, "source": 83},
    {"name": "Registration", "descr": "", "catid": 36, "source": 83},
    {"name": "Registration (Adult)", "descr": "", "catid": 36, "source": 83},
    {"name": "Registration (Children)", "descr": "", "catid": 36, "source": 83},
    {"name": "Respiratory Physician Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Respiratory Physician Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "Rheumatologist (Visiting)", "descr": "", "catid": 36, "source": 83},
    {"name": "Rheumatology Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Rheumatology Follow Up", "descr": "", "catid": 36, "source": 83},
])

dental_services = np.array([
    {"name": "Root Canal Therapy  Anterior", "descr": "", "catid": 50, "source": 83},
    {"name": "Root Canal Therapy  Posterior", "descr": "", "catid": 50, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Radius & Ulna (L/R)", "descr": "", "catid": 27, "source": 83},
    {"name": "Refraction", "descr": "", "catid": 27, "source": 83},
    {"name": "Renal Scan", "descr": "", "catid": 27, "source": 83},
])

family_planning = np.array([
    {"name": "Repeat Caesarian Section (1 -2 Previous Cs) Plus Btl", "descr": "", "catid": 44, "source": 83},
])

laboratory_tests = np.array([
    {"name": "Random Blood Sugar (Glucometer)", "descr": "", "catid": 39, "source": 83},
    {"name": "Random Blood Sugar (RBS)", "descr": "", "catid": 39, "source": 83},
    {"name": "Rapid Strip Test for Dengue", "descr": "", "catid": 39, "source": 83},
    {"name": "Rbs", "descr": "", "catid": 39, "source": 83},
    {"name": "Rbs Check", "descr": "", "catid": 39, "source": 83},
    {"name": "Rectal Swab for Neisseria Gonorrhea", "descr": "", "catid": 39, "source": 83},
    {"name": "Red Cell Fragility", "descr": "", "catid": 39, "source": 83},
    {"name": "Renal Bipsy with Histochemical Stains", "descr": "", "catid": 39, "source": 83},
    {"name": "Resucitation Moderate (Ambu Bag)", "descr": "", "catid": 39, "source": 83},
    {"name": "Retics Count", "descr": "", "catid": 39, "source": 83},
    {"name": "Reticulocyte Count", "descr": "", "catid": 39, "source": 83},
    {"name": "Rheumatoid Factor", "descr": "", "catid": 39, "source": 83},
    {"name": "Rheumatoid Factor (Qualitative)", "descr": "", "catid": 39, "source": 83},
    {"name": "Rheumatoid Factor (Quantitative)", "descr": "", "catid": 39, "source": 83},
    {"name": "Rheumatoid Factor (Quantitative) Igm", "descr": "", "catid": 39, "source": 83},
    {"name": "Rheumatoid Factor (RF) - Latex", "descr": "", "catid": 39, "source": 83},
    {"name": "Rubella IgG Antibody (Quantitative)", "descr": "", "catid": 39, "source": 83},
    {"name": "Rubella IgM Antibody (Quantitative)", "descr": "", "catid": 39, "source": 83},
])

medical_devices = np.array([
    {"name": "Radiant Warmer", "descr": "", "catid": 29, "source": 83},
])

medications = np.array([
    {"name": "Rabeprazole 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 2.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 2.5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Random Blood Sugar", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranferon Blood Tonic", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranferon Blood Tonic 100Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranferon Blood Tonic 200Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranferon-12", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranferon-12 Capsule", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine 150Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine 300Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine 50Mg Inj (Zantac)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine Injection 50Mg/2Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Rapiclav 625Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rapiclav 625Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Rapidflox 500Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Refampicin Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Refolinon 30Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Refucil 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Refucil Suspension", "descr": "", "catid": 35, "source": 83},
    {"name": "Regroton", "descr": "", "catid": 35, "source": 83},
    {"name": "Regroton Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Reichamox Cap 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Reichlox Cap 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Reichlox Injection 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Relcer Suspension 180Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Rhinathiol", "descr": "", "catid": 35, "source": 83},
    {"name": "Rifampicin 150Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rifampicin 300Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rifampicin 300Mg Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Rifampicin Susp 100Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Rifampicin Susp 60Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Ringers Lactate", "descr": "", "catid": 35, "source": 83},
    {"name": "Ringers Lactate Infusion", "descr": "", "catid": 35, "source": 83},
    {"name": "Risperdal 3Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Rivaroxaban 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rocephin 1G Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Rocephin 500Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Rolux Susp", "descr": "", "catid": 35, "source": 83},
    {"name": "Rophex 1G Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosart 50Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosuvastatin 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosuvastatin 10Mg (Crestor)", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosuvastatin 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosuvastatin 20Mg (Crestor)", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosuvastatin 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rotypnol", "descr": "", "catid": 35, "source": 83},
    {"name": "Rovamycin 3Mu Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Rovigon", "descr": "", "catid": 35, "source": 83},
    {"name": "Rovigon Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Roxid 150Mg Tab", "descr": "", "catid": 35, "source": 83},
])

others = np.array([
    {"name": "Routine Care At Birth C/S (Vitamin K, Measurement, Receive And Clean The Baby)", "descr": "", "catid": 48, "source": 83},
    {"name": "Routine Care At Birth Svd   (Vitamin K, Measurement, Receive And Clean The Baby)", "descr": "", "catid": 48, "source": 83},
])

reproductive_health = np.array([
    {"name": "Repair Of Ruptured/Inverted Uterus", "descr": "", "catid": 32, "source": 83},
    {"name": "Rhogam", "descr": "", "catid": 32, "source": 83},
])

surgeries = np.array([
    {"name": "Radical Cystectomy And Urinary Diversion", "descr": "", "catid": 37, "source": 83},
    {"name": "Radical Nephrectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Radical Prostatectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Recto-Urethral Fistula Closure", "descr": "", "catid": 37, "source": 83},
    {"name": "Rectosigmoidectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Rectovesical Fistula Closure", "descr": "", "catid": 37, "source": 83},
    {"name": "Refraction", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Both Ovaries", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal of ingrown toe nail", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Intramedullary Nail", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of One Ovary", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Plate And Screws", "descr": "", "catid": 37, "source": 83},
    {"name": "Repeat Caesarian Section (1 -2 Previous Cs)", "descr": "", "catid": 37, "source": 83},
    {"name": "Repeat Myomectomy (20 Weeks Size Or Less)", "descr": "", "catid": 37, "source": 83},
    {"name": "Replacement Urethroplasy (Single Stage)", "descr": "", "catid": 37, "source": 83},
    {"name": "Retinal Detachment Surgery", "descr": "", "catid": 37, "source": 83},
    {"name": "Retrieval Of Lost Iucd", "descr": "", "catid": 37, "source": 83},
    {"name": "Retrograde Filling", "descr": "", "catid": 37, "source": 83},
    {"name": "Retrograde Intrarenal Surgery (Rirs) (Major Surgery)", "descr": "", "catid": 37, "source": 83},
    {"name": "Retrograde Pyelogram", "descr": "", "catid": 37, "source": 83},
    {"name": "Right Hemicolectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Root Canal Therapy (Anterior-Posterior", "descr": "", "catid": 37, "source": 83},
    {"name": "Root Canal Treatment  (Posteriors)", "descr": "", "catid": 37, "source": 83},
    {"name": "Root Canal Treatment (Anteriors)", "descr": "", "catid": 37, "source": 83},
    {"name": "Rubber Band Ligation (Haemorrhoids)", "descr": "", "catid": 37, "source": 83},
    {"name": "Ruptured Appendectomy", "descr": "", "catid": 37, "source": 83},
])

vaccines = np.array([
    {"name": "Rotarix Vaccine", "descr": "", "catid": 46, "source": 83},
    {"name": "Rotavirus", "descr": "", "catid": 46, "source": 83},
    {"name": "Rotavirus (Diarrhea & Vomiting) @6 Weeks", "descr": "", "catid": 46, "source": 83},
    {"name": "Rotavirus @10 Weeks", "descr": "", "catid": 46, "source": 83},
    {"name": "Rotavirus Vaccine", "descr": "", "catid": 46, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — R
# =============================================================================
# Total records on this sheet : 123
# Categories found            : consultations, dental_services, diagnostic_imaging, family_planning, laboratory_tests, medical_devices, medications, others, reproductive_health, surgeries, vaccines
# Duplicates removed          : 2
# Unmapped categories         : None
# =============================================================================
