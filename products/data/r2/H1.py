import numpy as np

biologics = np.array([
    {"name": "Hepatitis B Immunoglobulin (...) Injection 100 IU", "descr": "", "catid": 31, "source": 83},
    {"name": "Human Immunoglobulin G (Human Immunoglobulin G) Injection 10 G", "descr": "", "catid": 31, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Holter ECG", "descr": "", "catid": 27, "source": 83},
    {"name": "Holter ECG For 48Hrs", "descr": "", "catid": 27, "source": 83},
])

laboratory_tests = np.array([
    {"name": "H. Pylori(Blood)", "descr": "", "catid": 39, "source": 83},
    {"name": "H.Pylori(Stool)", "descr": "", "catid": 39, "source": 83},
    {"name": "Haemoglobin", "descr": "", "catid": 39, "source": 83},
    {"name": "Hbsag, HIV 1 And 2, VDRL And Hcv", "descr": "", "catid": 39, "source": 83},
    {"name": "Hepatitis A Antibodies", "descr": "", "catid": 39, "source": 83},
    {"name": "Hepatitis A IgM", "descr": "", "catid": 39, "source": 83},
    {"name": "Hepatitis B 5-Test Panel", "descr": "", "catid": 39, "source": 83},
    {"name": "Hepatitis B Core Antibodies", "descr": "", "catid": 39, "source": 83},
    {"name": "Hepatitis B Envelope Antibodies", "descr": "", "catid": 39, "source": 83},
    {"name": "Hepatitis B Envelope Antigen", "descr": "", "catid": 39, "source": 83},
    {"name": "Hepatitis B Surface Antibodies", "descr": "", "catid": 39, "source": 83},
    {"name": "Hepatitis B Surface Antigen", "descr": "", "catid": 39, "source": 83},
    {"name": "Hepatitis C", "descr": "", "catid": 39, "source": 83},
    {"name": "Herpes Simplex (1 And 2) IgG", "descr": "", "catid": 39, "source": 83},
    {"name": "Herpes Simplex (1 And 2) IgM", "descr": "", "catid": 39, "source": 83},
    {"name": "Herpes Simplex PCR", "descr": "", "catid": 39, "source": 83},
    {"name": "High Density Lipoprotien Cholesterol", "descr": "", "catid": 39, "source": 83},
    {"name": "Histology", "descr": "", "catid": 39, "source": 83},
    {"name": "Histopathology", "descr": "", "catid": 39, "source": 83},
    {"name": "HIV Confirmatory(Elisa Method)", "descr": "", "catid": 39, "source": 83},
    {"name": "HIV I & Ii Screen", "descr": "", "catid": 39, "source": 83},
    {"name": "HIV PCR", "descr": "", "catid": 39, "source": 83},
    {"name": "Hiv(Viral Load)", "descr": "", "catid": 39, "source": 83},
    {"name": "HPV PCR", "descr": "", "catid": 39, "source": 83},
])

medical_supplies = np.array([
    {"name": "Hypoject Syringe (...) Item 10 ml", "descr": "", "catid": 34, "source": 83},
    {"name": "Hypoject Syringe (...) Item 50 ml", "descr": "", "catid": 34, "source": 83},
])

medications = np.array([
    {"name": "Haloperidol (...) Injection 5 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Haloperidol (...) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Halothane (...) Inhalation 250 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Hand Sanitizer (Smartans) Gel 70 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Hand Sanitizer (Spaceclean) Solution 62 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Heparin Sodium (...) Injection 5000 IU", "descr": "", "catid": 35, "source": 83},
    {"name": "Hexaxim (Dtap/Ipv/Hb/Hib) Injection 20 IU", "descr": "", "catid": 35, "source": 83},
    {"name": "Hexedene 0.1% (Hexedene Mouth Wash) Solution 300 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Hexetidine (Oraldene) Solution 200 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Homatropine Methylbromide (Nospamin) Drops 2 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Honey (Forever) Syrup 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Human Albumin (Alburex) Injection 2 G/10Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Human Chorionic Gonadotropin (Coriosurge) Injection 5000 IU", "descr": "", "catid": 35, "source": 83},
    {"name": "Human Chorionic Gonadotropin (Hucog) Injection 5000 IU", "descr": "", "catid": 35, "source": 83},
    {"name": "Human Chorionic Gonadotropin (I V F-C) Injection 5000 IU", "descr": "", "catid": 35, "source": 83},
    {"name": "Human Chorionic Gonadotropin (Pregnyl) Injection 5000 IU", "descr": "", "catid": 35, "source": 83},
    {"name": "Human Insulin (Actrapid) Injection 100 IU", "descr": "", "catid": 35, "source": 83},
    {"name": "Human Papillomavirus Type 16 And 18 (Cervarix) Injection 0.5 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Human Papillomavirus Type 6, 11, 16 And 18 (Gardasil) Injection 0.5 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Hydralazine (...) Injection 20 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Hydralazine (Apresoline) Tablet 25 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Hydrochlorothiazide (Esidrex) Tablet 25 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Hydrochlorothiazide (Hydrex) Tablet 25 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Hydrochlorothiazide 50Mg + Amiloride Hydrochloride 5Mg (Normoretic) Tablet 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Hydrocortisone (...) Injection 100 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Hydrocortisone (Hydrocortisone) Cream 15 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Hydrogen Peroxide 6% (...) Solution 100 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Hydroxychloroquine Sulfate (Plaquenil) Tablet 200 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Hydroxymagnessium Aluminate Complex + Simethicone (Gascol) Suspension 150 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Hydroxyurea (Hydrine) Capsule 500 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Hyoscine Butylbromide (...) Injection 10 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Hyoscine Butylbromide (Buscopan) Tablet 10 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Hyoscine Butylbromide (Colipan) Syrup 5 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Hyoscine Butylbromide (Hyomide) Tablet 10 mg", "descr": "", "catid": 35, "source": 83},
])

others = np.array([
    {"name": "Hfnc-High Flow Nasal Cannula", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "Haemorrhoidectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Hearing Screening For Newborn", "descr": "", "catid": 37, "source": 83},
    {"name": "Herniorrhaphy", "descr": "", "catid": 37, "source": 83},
    {"name": "Herniotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Herniotomy -Bilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Hypospadias Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Hysterectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Hysterotomy", "descr": "", "catid": 37, "source": 83},
])

vaccines = np.array([
    {"name": "Hepatitis B Vaccine (Engerix B Adult) Injection 1 ml", "descr": "", "catid": 46, "source": 83},
    {"name": "Hepatitis B Vaccine (Engerix B Child) Injection 0.5 ml", "descr": "", "catid": 46, "source": 83},
    {"name": "Hepatitis B Vaccine (Euvax Multi Dose) Injection 0.5 ml", "descr": "", "catid": 46, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — H
# =============================================================================
# Total records on this sheet : 77
# Categories found            : biologics, diagnostic_imaging, laboratory_tests, medical_supplies, medications, others, surgeries, vaccines
# Unmapped categories         : None
# Duplicates removed          : 1
# =============================================================================
