import numpy as np

biologics = np.array([
    {"name": "Rabies Immunoglobin 150 Unit In Ml", "descr": "", "catid": 31, "source": 83},
    {"name": "Rh +Ve", "descr": "", "catid": 31, "source": 83},
    {"name": "Rh –Ve", "descr": "", "catid": 31, "source": 83},
])

consultations = np.array([
    {"name": "Radiologist Consulation", "descr": "", "catid": 36, "source": 83},
    {"name": "Radiologist Review", "descr": "", "catid": 36, "source": 83},
    {"name": "Rare Specialist Con (1St) ENT, Orthopedic, Paed Cardiologist, Endocrinologist, Neurologist, Nephrologist", "descr": "", "catid": 36, "source": 83},
    {"name": "Rare Specialist Review", "descr": "", "catid": 36, "source": 83},
    {"name": "Registration", "descr": "", "catid": 36, "source": 83},
    {"name": "Respiratory Physician Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Respiratory Physician Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "Review", "descr": "", "catid": 36, "source": 83},
    {"name": "Rheumatology Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Rheumatology Follow Up", "descr": "", "catid": 36, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Refraction", "descr": "", "catid": 27, "source": 83},
])

laboratory_tests = np.array([
    {"name": "Random Blood Sugar", "descr": "", "catid": 39, "source": 83},
    {"name": "Red Cell Count", "descr": "", "catid": 39, "source": 83},
    {"name": "Reticulocyte", "descr": "", "catid": 39, "source": 83},
    {"name": "Reticulocyte Count", "descr": "", "catid": 39, "source": 83},
    {"name": "Rhesus Factor Determination", "descr": "", "catid": 39, "source": 83},
    {"name": "Rheumatoid Factor", "descr": "", "catid": 39, "source": 83},
    {"name": "Rubella", "descr": "", "catid": 39, "source": 83},
])

medications = np.array([
    {"name": "Rabeprazole", "descr": "", "catid": 35, "source": 83},
    {"name": "Rabeprazole 200Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 2.5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ramipril 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranferon 12 Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranferon Tonic", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine 150Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine 300Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine Inj 50Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ranitidine IV", "descr": "", "catid": 35, "source": 83},
    {"name": "Regen D Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Regroton Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Resperpine + Dihydroergocristine + Clopamide", "descr": "", "catid": 35, "source": 83},
    {"name": "Resperpine + Dihydroergocristine +Hydrochlorothiazide", "descr": "", "catid": 35, "source": 83},
    {"name": "Retapen 0.5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Retin A Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Retinol (Vitamin A)", "descr": "", "catid": 35, "source": 83},
    {"name": "Rhinathiol Cough Syrup (Adult)", "descr": "", "catid": 35, "source": 83},
    {"name": "Rhinathiol Coughsyrup(Children)", "descr": "", "catid": 35, "source": 83},
    {"name": "Rhinathiol With Promethazine", "descr": "", "catid": 35, "source": 83},
    {"name": "Rhogam (Anti—Rh D Immunoglobulin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Riboflavine (Vitamin B2)", "descr": "", "catid": 35, "source": 83},
    {"name": "Rifampicin", "descr": "", "catid": 35, "source": 83},
    {"name": "Rifampicin 100Mls Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Rifampicin 150M", "descr": "", "catid": 35, "source": 83},
    {"name": "Rifampicin 300Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ringers Lactate IV", "descr": "", "catid": 35, "source": 83},
    {"name": "Risperdal 3Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Risperidone 2Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Robinax500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rocephin Inj Ig", "descr": "", "catid": 35, "source": 83},
    {"name": "Rocephine", "descr": "", "catid": 35, "source": 83},
    {"name": "Rocephine 1G Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Rohypnol Tab 1Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosuvastatin (Crestor)10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Rosuvastatin 20Mg (Crestor)", "descr": "", "catid": 35, "source": 83},
    {"name": "Rovamycin 3Mu Tab", "descr": "", "catid": 35, "source": 83},
])

others = np.array([
    {"name": "Refraction/Auto-Refraction", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "Rabies", "descr": "", "catid": 37, "source": 83},
    {"name": "Radical Cystectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Radical Neck Dissection - Excision", "descr": "", "catid": 37, "source": 83},
    {"name": "Radical Pancreatectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Radical Prostatectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Reconstruction Of The Ureter", "descr": "", "catid": 37, "source": 83},
    {"name": "Reconstruction Of Vagina (E.G. Secondary To Vaginal Atresia)", "descr": "", "catid": 37, "source": 83},
    {"name": "Reconstruction Surgeries: Acromium, Head Of Femur Etc", "descr": "", "catid": 37, "source": 83},
    {"name": "Reconstruction Surgery E.G Straussman Operation", "descr": "", "catid": 37, "source": 83},
    {"name": "Rectal Dilation", "descr": "", "catid": 37, "source": 83},
    {"name": "Rectal Polyp", "descr": "", "catid": 37, "source": 83},
    {"name": "Recto-Urethral Fistula Closure", "descr": "", "catid": 37, "source": 83},
    {"name": "Rectopexy", "descr": "", "catid": 37, "source": 83},
    {"name": "Rectovaginal Fistula Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Rectovesical Fistula Closure", "descr": "", "catid": 37, "source": 83},
    {"name": "Reduction And Fixation Of Maxillary Fractures", "descr": "", "catid": 37, "source": 83},
    {"name": "Regional GA (Intermediate) + Theatre Fee", "descr": "", "catid": 37, "source": 83},
    {"name": "Release Of Chordae", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Foreign Body (Ear-Bilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Foreign Body (Ear-Unilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Foreign Body (Nose-Bilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Foreign Body (Nose-Unilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Foreign Body (Throat)", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Implant", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Ovaries", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Wax From Ear – Bilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Removal Of Wax From Ear – Unilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Renal Aneurysmectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Renal Cystectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Renal Decapsulation", "descr": "", "catid": 37, "source": 83},
    {"name": "Renopelvic Lymphatectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of 3Rd Degree Tear", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Bochidalek Diaphragmatic Congenital Defect", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Bowel Perforations", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Cervical Laceration", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Cervical Laceration (1St And 2Nd Degree)", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Common Bile Duct", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Gastric Lacerations", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Inverted Uterus", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Minor Vaginal Laceration", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Oesophageal Lacerations", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Perforated Uterus", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Ruptured Uterus", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Splenic Laceration", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Third Degree Perineal Tear", "descr": "", "catid": 37, "source": 83},
    {"name": "Repair Of Vaginal Laceration (2Nd Degree)", "descr": "", "catid": 37, "source": 83},
    {"name": "Resection Anastomosis (Large Intestine)", "descr": "", "catid": 37, "source": 83},
    {"name": "Resection Of Median Bar Obstruction", "descr": "", "catid": 37, "source": 83},
    {"name": "Retroperitoneal Drainage Of Perinephric Abscess", "descr": "", "catid": 37, "source": 83},
    {"name": "Retroperitoneal Tumor - Excision", "descr": "", "catid": 37, "source": 83},
    {"name": "Rhinoplasty", "descr": "", "catid": 37, "source": 83},
    {"name": "Ribs", "descr": "", "catid": 37, "source": 83},
    {"name": "Rigid Direct Larngoscopy", "descr": "", "catid": 37, "source": 83},
    {"name": "Root Canal Anterior", "descr": "", "catid": 37, "source": 83},
    {"name": "Root Canal Posterior", "descr": "", "catid": 37, "source": 83},
    {"name": "Root Canal Therapy Anterior", "descr": "", "catid": 37, "source": 83},
    {"name": "Root Canal Therapy Posterior", "descr": "", "catid": 37, "source": 83},
    {"name": "Root Extraction", "descr": "", "catid": 37, "source": 83},
    {"name": "Rotavirus", "descr": "", "catid": 37, "source": 83},
    {"name": "Roux-En-Y Pancreatic Jejunostomy", "descr": "", "catid": 37, "source": 83},
])

vaccines = np.array([
    {"name": "Rotarix (Rotavirus Vaccine)", "descr": "", "catid": 46, "source": 83},
    {"name": "Rotarix Vaccine", "descr": "", "catid": 46, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — Product R
# =============================================================================
# Total records on this sheet : 122
# Categories found            : biologics, consultations, diagnostic_imaging, laboratory_tests, medications, others, surgeries, vaccines
# Unmapped categories         : None
# Duplicates removed          : surgeries:"Rectal Polyp"; surgeries:"Release Of Chordae"; medications:"Retinol (Vitamin A)"; medications:"Retinol (Vitamin A)"; medications:"Rifampicin"
# =============================================================================
