import numpy as np

diagnostic_imaging = np.array([
    {"name": "Follicular Tracking Session", "descr": "", "catid": 27, "source": 83},
    {"name": "Functional Mri(Fmri)", "descr": "", "catid": 27, "source": 83},
])

laboratory_tests = np.array([
    {"name": "Factor V111", "descr": "", "catid": 39, "source": 83},
    {"name": "Family Donor Processing", "descr": "", "catid": 39, "source": 83},
    {"name": "Ferritin", "descr": "", "catid": 39, "source": 83},
    {"name": "Fibrinogen", "descr": "", "catid": 39, "source": 83},
    {"name": "FNAC", "descr": "", "catid": 39, "source": 83},
    {"name": "Follicule Stimulating Hormone (D2-D5)", "descr": "", "catid": 39, "source": 83},
    {"name": "Food Screening", "descr": "", "catid": 39, "source": 83},
    {"name": "Free Thyroxine(FT4)", "descr": "", "catid": 39, "source": 83},
    {"name": "Free Triiodothyronine(FT3)", "descr": "", "catid": 39, "source": 83},
    {"name": "Fresh Frozen Plasma", "descr": "", "catid": 39, "source": 83},
    {"name": "Full Blood Count", "descr": "", "catid": 39, "source": 83},
    {"name": "Fungi Skin Scrapping", "descr": "", "catid": 39, "source": 83},
])

medical_supplies = np.array([
    {"name": "Face Mask (...) Item 1 Unit", "descr": "", "catid": 34, "source": 83},
    {"name": "Face Mask With Visor (...) Item 1 Unit", "descr": "", "catid": 34, "source": 83},
    {"name": "Foley Catheter (Foleys 2 Way Catheter) Item 10 Cm", "descr": "", "catid": 34, "source": 83},
    {"name": "Foley Catheter (Silicone Catheter (All Sizes)) Item 1 Unit", "descr": "", "catid": 34, "source": 83},
])

medications = np.array([
    {"name": "Febuxostat (Febo - G) Tablet 40 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Feeding Tube(Ng Tube) (...) Item 10 Cm", "descr": "", "catid": 35, "source": 83},
    {"name": "Fenofibrate (...) Tablet 160 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Fentanyl (...) Injection 100 μg", "descr": "", "catid": 35, "source": 83},
    {"name": "Fenugreek 610Mg (Fenugreek) Capsule 610 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ferrous Gluconate (Chemiron) Syrup 16 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ferrous Sulfate (Ferrous Sulphate) Tablet 200 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Fexofenadine Hcl (Fexet) Tablet 180 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Filgrastim (Religrast) Injection 300 μg", "descr": "", "catid": 35, "source": 83},
    {"name": "Flexpen (Mixtard 30) Injection 100 IU/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Flucloxacillin (Floxapen) Syrup 100 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Fluconazole (Diflucan) Capsule 50 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Fluconazole (Flucamed) Capsule 50 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Fluconazole (Flucamed) Drops 3 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Fluconazole (Flucamed) Syrup 50 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Fluconazole (Juconazole) Infusion 2 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Flucor Day (Flucor Day) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Fludrocortisone + Neomycin + Polymyxin + Lidocaine Hcl (Oto- Med) Drops 10 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Fluorometholone (Efemoline) Drops 1 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Flupentixol Decanoate (Depixol) Solution 20 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Fluticasone Furoate (Avamys) Spray 0.1 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Fluticasone Propionate (Flixonase) Spray 0.1 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Folic Acid (...) Syrup 2.5 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Folic Acid (...) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Follitropin Alpha (Folisurge) Injection 75 IU", "descr": "", "catid": 35, "source": 83},
    {"name": "Framycetin 5Mg Dexamethasone 0.5Mg + Gramicidine 0.05Mg (Framoptic-D) Drops 10 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Framycetin Sulphate (Steritin Tulle) Item 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Frusemide (...) Injection 20 mg/2Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Frusemide (...) Tablet 20 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Frusemide (...) Tablet 40 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Full Strength Darrows Solution (...) Infusion 500 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Furosemide (...) Tablet 20 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Furosemide (...) Tablet 40 mg", "descr": "", "catid": 35, "source": 83},
])

surgeries = np.array([
    {"name": "Fetal Lung Maturation", "descr": "", "catid": 37, "source": 83},
    {"name": "Fetal Reduction", "descr": "", "catid": 37, "source": 83},
    {"name": "Fistulectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Foreign Body Removal (Nose, Ear, Throat) (Under GA)", "descr": "", "catid": 37, "source": 83},
    {"name": "Foreign Body Removal (Underla)", "descr": "", "catid": 37, "source": 83},
    {"name": "Foreign Body Removal From Ear/Nose/Throat", "descr": "", "catid": 37, "source": 83},
    {"name": "Foreign Body Removal From Nose(Without General Anaesthesia)", "descr": "", "catid": 37, "source": 83},
    {"name": "Frenulectomy Under GA", "descr": "", "catid": 37, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — F
# =============================================================================
# Total records on this sheet : 59
# Categories found            : diagnostic_imaging, laboratory_tests, medical_supplies, medications, surgeries
# Unmapped categories         : None
# =============================================================================
