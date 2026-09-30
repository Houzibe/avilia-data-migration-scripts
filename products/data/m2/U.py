import numpy as np

consultations = np.array([
    {"name": "Urologist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Urologist Review", "descr": "", "catid": 36, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Ultrasound Of The Brain Including Doppler", "descr": "", "catid": 27, "source": 83},
    {"name": "Ultrasound Of The Brain –Neonatal", "descr": "", "catid": 27, "source": 83},
    {"name": "Unilateral Breast (L)", "descr": "", "catid": 27, "source": 83},
    {"name": "Unilateral Breast (R)", "descr": "", "catid": 27, "source": 83},
    {"name": "Upper Arm Ct With Contrast", "descr": "", "catid": 27, "source": 83},
    {"name": "Upper Extremities Ct Plain", "descr": "", "catid": 27, "source": 83},
    {"name": "Upper Extremities Ct With Contrast", "descr": "", "catid": 27, "source": 83},
    {"name": "Upper Limb Arteriography", "descr": "", "catid": 27, "source": 83},
])

laboratory_tests = np.array([
    {"name": "Unit Of Screened  Rh-Positive Blood", "descr": "", "catid": 39, "source": 83},
    {"name": "Unit Of Screened Rh- Negative Blood", "descr": "", "catid": 39, "source": 83},
    {"name": "Urea Breath Test", "descr": "", "catid": 39, "source": 83},
    {"name": "Urea Clearance*", "descr": "", "catid": 39, "source": 83},
    {"name": "Urea Reflotron", "descr": "", "catid": 39, "source": 83},
    {"name": "Urea, Fluid", "descr": "", "catid": 39, "source": 83},
    {"name": "Urea, Random Urine", "descr": "", "catid": 39, "source": 83},
    {"name": "Urethra Swab M/C/S", "descr": "", "catid": 39, "source": 83},
    {"name": "Urethral Smear M/C/S", "descr": "", "catid": 39, "source": 83},
    {"name": "Urethral Swab", "descr": "", "catid": 39, "source": 83},
    {"name": "Uric Acid Reflotron", "descr": "", "catid": 39, "source": 83},
    {"name": "Urinalysis", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine 24Hr Total Protein", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Analysis", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Analysis (Urinalysis)", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Culture & Sensitivity", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Drug Panel (Cocaine, Amphetamines, Barbiturates, Benzodiazepine, Cannabis, Methamphetamine, Opiates)", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine M/C/S", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Microscopy", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Pgt", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Pt (2 Weeks After Missing Menses)", "descr": "", "catid": 39, "source": 83},
    {"name": "Urine Urinalysis", "descr": "", "catid": 39, "source": 83},
])

medications = np.array([
    {"name": "Ulgicid Susp", "descr": "", "catid": 35, "source": 83},
    {"name": "Ulsakit", "descr": "", "catid": 35, "source": 83},
    {"name": "Ulsakit Caps", "descr": "", "catid": 35, "source": 83},
    {"name": "Ulsakit Tabs (Clarithromycin + Omeprazole + Tinidazole)", "descr": "", "catid": 35, "source": 83},
    {"name": "Unaben Tab 400Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Unasyn Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Unasyn Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Unasyn Injection (Ampicillin+ Sulbactam)", "descr": "", "catid": 35, "source": 83},
    {"name": "Unasyn Tabs 375Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Unasyna 250Mg/5Ml(Pfizer)", "descr": "", "catid": 35, "source": 83},
    {"name": "Unihart Sodium Lactate Infusion", "descr": "", "catid": 35, "source": 83},
    {"name": "Urine Bag", "descr": "", "catid": 35, "source": 83},
    {"name": "Ursodeoxycholic Acid 250Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Utrogestan 200Mg Pessaries", "descr": "", "catid": 35, "source": 83},
])

others = np.array([
    {"name": "Urea", "descr": "", "catid": 48, "source": 83},
    {"name": "Uric Acid", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "U- Shaped Pop Back Slap", "descr": "", "catid": 37, "source": 83},
    {"name": "U- Shaped Pop Cast", "descr": "", "catid": 37, "source": 83},
    {"name": "Ultrasound Scan (Obstetric)", "descr": "", "catid": 37, "source": 83},
    {"name": "Umbilical Sinus - Excision", "descr": "", "catid": 37, "source": 83},
    {"name": "Unbooked Multiple Delivery (Uncomplicated)", "descr": "", "catid": 37, "source": 83},
    {"name": "Unbooked Normal Delivery (Singleton)", "descr": "", "catid": 37, "source": 83},
    {"name": "Uncomplicated Caeserian Section - (Elective/Emergency)", "descr": "", "catid": 37, "source": 83},
    {"name": "Upper Arm", "descr": "", "catid": 37, "source": 83},
    {"name": "Upper Arm Cast (Excluding Reduction)(Global Fee)", "descr": "", "catid": 37, "source": 83},
    {"name": "Urerthra-Reconstruction/ Repair Of Prostatic/Membraneous Urethra", "descr": "", "catid": 37, "source": 83},
    {"name": "Ureteral Reinplantation Into The Bladder", "descr": "", "catid": 37, "source": 83},
    {"name": "Ureterolithotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Ureterosigmoidostomywith Rectal Bladder/Colostomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Ureterovaginal Fistula Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Uretherectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Urethral Catherization(Global Fee)", "descr": "", "catid": 37, "source": 83},
    {"name": "Urethro-Vesicopexy,Combined Abdominal And Vaginal Approach", "descr": "", "catid": 37, "source": 83},
    {"name": "Urethroplasty(Global Fee)", "descr": "", "catid": 37, "source": 83},
    {"name": "Urethrotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Uretro Vaginal Fistula Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Uretro Vesical Fistula Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Abdomen (2D)", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Abdomen With Doppler Flow", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Abdomino-Pelvic", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Adrenal Scan", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Breast (Bilateral)", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Chest", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Doppler Scanning Per Limb", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Follicular Abd", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Follicular Tvs", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Gall Bladder Scanning", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Maxillary", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Micturating Cysto-Urethrogram", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Obs.Scan For Biophy.Profile", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Obs.Scan For Fetal Anomaly", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Obstetric Scan", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Occular Scan", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Pelvic Scan", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Pelvic Scan Wt Doppler Flow", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Pleural Scan", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Prostate Scan (Trans Rectal)", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Prostate Scan(Trans Abdominal)", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Renal Scan", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Scrotal Scan", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Soft Tissue Neck", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Sonohysterography", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Subcut/Deep Soft Tissue Scan", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Thyroid Scan", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Transfrontenelle Scan", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Transvaginal Scan", "descr": "", "catid": 37, "source": 83},
    {"name": "Uss-Uss Guided Aspiration", "descr": "", "catid": 37, "source": 83},
    {"name": "Uterine Prolapse", "descr": "", "catid": 37, "source": 83},
    {"name": "Uterine Rupture Repair(Global Fee)", "descr": "", "catid": 37, "source": 83},
    {"name": "Uterovesical Fistula Repair", "descr": "", "catid": 37, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — Product U
# =============================================================================
# Total records on this sheet : 103
# Categories found            : consultations, diagnostic_imaging, laboratory_tests, medications, others, surgeries
# Duplicates removed          : None
# Unmapped categories         : None
# =============================================================================
