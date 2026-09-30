import numpy as np

consultations = np.array([
    {"name": "Urinary Bladder Catheterization", "descr": "", "catid": 36, "source": 83},
    {"name": "Urologist", "descr": "", "catid": 36, "source": 83},
    {"name": "Urologist (Follow Up Consultation)", "descr": "", "catid": 36, "source": 83},
    {"name": "Urologist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Urologist Review", "descr": "", "catid": 36, "source": 83}
])

diagnostic_imaging = np.array([
    {"name": "Ultrasound Guided Aspiration", "descr": "", "catid": 27, "source": 83},
    {"name": "Ultrasound Guided Biopsy", "descr": "", "catid": 27, "source": 83},
    {"name": "Ultrasound Guided Biopsy And Histology/Cytology", "descr": "", "catid": 27, "source": 83},
    {"name": "Ultrasound Guided Fnac With A Surgeon", "descr": "", "catid": 27, "source": 83},
    {"name": "Upper Arm Ct", "descr": "", "catid": 27, "source": 83},
    {"name": "Upper Arm CT With Contrast", "descr": "", "catid": 27, "source": 83},
    {"name": "Upper Extremities CT Plain", "descr": "", "catid": 27, "source": 83},
    {"name": "Upper Extremities CT With Contrast", "descr": "", "catid": 27, "source": 83},
    {"name": "Upper Limb Arteriography", "descr": "", "catid": 27, "source": 83},
    {"name": "Urine Culture & Sensitivity", "descr": "", "catid": 27, "source": 83},
    {"name": "Urine Microscopy", "descr": "", "catid": 27, "source": 83},
    {"name": "Urine Urinalysis", "descr": "", "catid": 27, "source": 83},
    {"name": "Uroflowmetry", "descr": "", "catid": 27, "source": 83},
    {"name": "Urologic Scan", "descr": "", "catid": 27, "source": 83},
    {"name": "Urological", "descr": "", "catid": 27, "source": 83},
    {"name": "Urological Scan", "descr": "", "catid": 27, "source": 83},
    {"name": "USS", "descr": "", "catid": 27, "source": 83},
    {"name": "Uss Guilded Biopsy(With Needle)", "descr": "", "catid": 27, "source": 83},
    {"name": "Uss Guilded Biopsy(Without Needle)", "descr": "", "catid": 27, "source": 83},
    {"name": "Uterine Doppler", "descr": "", "catid": 27, "source": 83}
])

drugs = np.array([
    {"name": "Ubiquinol 100mg Tabs ( Co Enzyme Q10)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ulcertret 20Mg Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Ulgicid", "descr": "", "catid": 35, "source": 83},
    {"name": "Ulgicid 200Ml Antacid Suspension", "descr": "", "catid": 35, "source": 83},
    {"name": "Ulsakit (Omeprazole+Tinidazole+Clarithromycin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ulsakit Capsules", "descr": "", "catid": 35, "source": 83},
    {"name": "Ulsakit Tab 1Pack (Complete Dose)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ulsakit Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Ulsakit Tabs (Clarithromycin + Omeprazole + Tinidazole)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ultrasound Scan (Obstetrics)", "descr": "", "catid": 35, "source": 83},
    {"name": "Unaben 400Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Unasyn Injection (Ampicillin+ Sulbactam)", "descr": "", "catid": 35, "source": 83},
    {"name": "Uperio 100", "descr": "", "catid": 35, "source": 83},
    {"name": "Uperio 50", "descr": "", "catid": 35, "source": 83},
    {"name": "Uperio 50mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Urethral Swab M/C/ S", "descr": "", "catid": 35, "source": 83},
    {"name": "Urinary Bladder (B Scan)", "descr": "", "catid": 35, "source": 83},
    {"name": "Urine Bag Per 1", "descr": "", "catid": 35, "source": 83},
    {"name": "Ursodeoxycholic Acid (Ursoliv)", "descr": "", "catid": 35, "source": 83}
])

infusions = np.array([
    {"name": "Unidex-50 Infusion 100Ml 50% Glucose", "descr": "", "catid": 47, "source": 83}
])

laboratory_tests = np.array([
    {"name": "U/Cr/E", "descr": "", "catid": 39, "source": 83},
    {"name": "Unit Of Blood (Screened) Rh Negative", "descr": "", "catid": 39, "source": 83},
    {"name": "Unit Of Blood (Screened) Rh Positive", "descr": "", "catid": 39, "source": 83},
    {"name": "Urea", "descr": "", "catid": 39, "source": 83},
    {"name": "Urea (24Hrs) Urine", "descr": "", "catid": 39, "source": 83},
    {"name": "Urea (Serum)", "descr": "", "catid": 39, "source": 83},
    {"name": "Urea - [Serum]", "descr": "", "catid": 39, "source": 83},
    {"name": "Urea - [Urine, 24hrs]", "descr": "", "catid": 39, "source": 83},
    {"name": "Urea any fluid", "descr": "", "catid": 39, "source": 83},
    {"name": "Urea Clearance", "descr": "", "catid": 39, "source": 83},
    {"name": "Urethra Swabs Mcs", "descr": "", "catid": 39, "source": 83},
    {"name": "Urethral Swab", "descr": "", "catid": 39, "source": 83},
    {"name": "Urethral Swab (Us) M/C/S", "descr": "", "catid": 39, "source": 83},
    {"name": "Urethral Swab Culture", "descr": "", "catid": 39, "source": 83},
    {"name": "Uric Acid", "descr": "", "catid": 39, "source": 83},
    {"name": "Uric Acid - [Urine]", "descr": "", "catid": 39, "source": 83},
    {"name": "Uric Acid(24Hr Urine)", "descr": "", "catid": 39, "source": 83},
    {"name": "Uric Acid(Serum)", "descr": "", "catid": 39, "source": 83},
    {"name": "Urinalysis", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine 24Hr Total Protein", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Albumin", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Albumin/Creatinine Ratio", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Calcium", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Culture", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Culture And Sensitivity", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Drug Analysis", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Drug Test", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine M/C/S", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Microscopy", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Preg. Test", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Pregancy Test", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Pregnancy Test", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Protein Creatinine Ratio (Upcr)", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Schistosomes", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Sodium (Random)", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Sugar", "descr": "", "catid": 39, "source": 83}
])

medical_supplies = np.array([
    {"name": "Under Pad", "descr": "", "catid": 34, "source": 83},
    {"name": "Urine / Drainage Bag", "descr": "", "catid": 34, "source": 83},
    {"name": "Urine Bag", "descr": "", "catid": 34, "source": 83},
    {"name": "Urine Bag (All Sizes)", "descr": "", "catid": 34, "source": 83},
    {"name": "Urine Bags", "descr": "", "catid": 34, "source": 83}
])

others = np.array([
    {"name": "Ulnar Tunnel Decompression", "descr": "", "catid": 48, "source": 83},
    {"name": "Umbilical Hernia Repair", "descr": "", "catid": 48, "source": 83},
    {"name": "Umbilical Hernia, Child", "descr": "", "catid": 48, "source": 83},
    {"name": "Umbilical Herniorrhaphy, Adult", "descr": "", "catid": 48, "source": 83},
    {"name": "Umbilical Vein Catheterization", "descr": "", "catid": 48, "source": 83},
    {"name": "Umblical Veinous Cannulation", "descr": "", "catid": 48, "source": 83},
    {"name": "Uncomplicated", "descr": "", "catid": 48, "source": 83},
    {"name": "Uncomplicated Caeserian Section - (Elective/Emergency)", "descr": "", "catid": 48, "source": 83},
    {"name": "Unilateral", "descr": "", "catid": 48, "source": 83},
    {"name": "Unilateral Breast (L)", "descr": "", "catid": 48, "source": 83},
    {"name": "Unilateral Breast (R)", "descr": "", "catid": 48, "source": 83},
    {"name": "Ureteral Reinplantation Into The Bladder", "descr": "", "catid": 48, "source": 83},
    {"name": "Uretero-renoscopy and Laser Lithotripsy for ureteric stones", "descr": "", "catid": 48, "source": 83},
    {"name": "Uretero-renoscopy for ureteric stones", "descr": "", "catid": 48, "source": 83},
    {"name": "Ureterolithotomy", "descr": "", "catid": 48, "source": 83},
    {"name": "Ureteroscopy", "descr": "", "catid": 48, "source": 83},
    {"name": "Ureterosigmoidostomywith Rectal Bladder/Colostomy", "descr": "", "catid": 48, "source": 83},
    {"name": "Uretherectomy", "descr": "", "catid": 48, "source": 83},
    {"name": "Urethral Catherization (Procedure Only)", "descr": "", "catid": 48, "source": 83},
    {"name": "Urethro-cystoscopy", "descr": "", "catid": 48, "source": 83},
    {"name": "Urethro-Vesicopexy,Combined Abdominal And Vaginal Approach", "descr": "", "catid": 48, "source": 83},
    {"name": "Urethroplasty", "descr": "", "catid": 48, "source": 83},
    {"name": "Urethroplasty (plastic reconstruction of the urethra)", "descr": "", "catid": 48, "source": 83},
    {"name": "Urethrotomy", "descr": "", "catid": 48, "source": 83},
    {"name": "Uretro Vaginal Fistula Repair", "descr": "", "catid": 48, "source": 83},
    {"name": "Uretro Vesical Fistula Repair", "descr": "", "catid": 48, "source": 83},
    {"name": "Urinary bladder catheterization in theatre(failed outpatient catheterization)", "descr": "", "catid": 48, "source": 83},
    {"name": "Urology", "descr": "", "catid": 48, "source": 83},
    {"name": "USS Guided Prostate biopsy", "descr": "", "catid": 48, "source": 83},
    {"name": "Uterine Adhesiolysis (Hysteroscopy)", "descr": "", "catid": 48, "source": 83},
    {"name": "Uterine Fibroid Embolization", "descr": "", "catid": 48, "source": 83},
    {"name": "Uterine polypectomy", "descr": "", "catid": 48, "source": 83},
    {"name": "Uterine Prolapse", "descr": "", "catid": 48, "source": 83},
    {"name": "Uvulectomy", "descr": "", "catid": 48, "source": 83}
])

surgeries = np.array([
    {"name": "Upper  Arm", "descr": "", "catid": 37, "source": 83},
    {"name": "Uppp- Uvulopalatopharyngoplasty", "descr": "", "catid": 37, "source": 83},
    {"name": "Ureterovaginal Fistula Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Uterovesical Fistula Repair", "descr": "", "catid": 37, "source": 83}
])

# =============================================================================
# SHEET SUMMARY — Product U
# =============================================================================
# Total records on this sheet : 124
# Categories found            : consultations, diagnostic_imaging, drugs, infusions, laboratory_tests, medical_supplies, others, surgeries
# Unmapped categories         : None
# =============================================================================
