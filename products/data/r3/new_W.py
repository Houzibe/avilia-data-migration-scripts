import numpy as np


consultations = np.array([
    {"name": "Well Child Clinic", "descr": "", "catid": 36, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Wrist Joint (Ap +Lat) X-Ray", "descr": "", "catid": 27, "source": 83},
    {"name": "Wrist X-Ray", "descr": "", "catid": 27, "source": 83},
])

infusions = np.array([
    {"name": "Water For Injection Injection 10Ml, Per Amp/Vial", "descr": "", "catid": 47, "source": 83},
])

laboratory_tests = np.array([
    {"name": "Wbc Count", "descr": "", "catid": 39, "source": 83},
    {"name": "Western Blot/Confirmatory", "descr": "", "catid": 39, "source": 83},
    {"name": "White Cell Count", "descr": "", "catid": 39, "source": 83},
    {"name": "White Cell Count (Total & Differential)", "descr": "", "catid": 39, "source": 83},
    {"name": "Widal Test", "descr": "", "catid": 39, "source": 83},
    {"name": "Wound Swab M/C/S", "descr": "", "catid": 39, "source": 83},
    {"name": "Wound Swab/Mcs", "descr": "", "catid": 39, "source": 83},
])

medical_devices = np.array([
    {"name": "Wheelchair (Without Bowl)", "descr": "", "catid": 29, "source": 83},
])

medications = np.array([
    {"name": "Waipa Tabs X12", "descr": "", "catid": 35, "source": 83},
    {"name": "Walking Clutches(Metallic Frame)", "descr": "", "catid": 35, "source": 83},
    {"name": "Walking Clutches(Wooden)", "descr": "", "catid": 35, "source": 83},
    {"name": "Warfarin 1Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Warfarin 2.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Warfarin 3Mg Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Warfarin 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Warfarin Sodium Tablets (As Sodium) 3Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Warfarin Tabs 1mg X28", "descr": "", "catid": 35, "source": 83},
    {"name": "Warfarin Tabs 3mg X28", "descr": "", "catid": 35, "source": 83},
    {"name": "Warfarin Tabs 5mg X28", "descr": "", "catid": 35, "source": 83},
    {"name": "Water For Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Water For Injection (Aquadee) X50", "descr": "", "catid": 35, "source": 83},
    {"name": "Water For Injection (Aquapress) 50X10Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Wellkid Baby & Infant Syrup 150ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Wellkid Baby Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Wellman 50 Plus Tabs X30", "descr": "", "catid": 35, "source": 83},
    {"name": "Wellman 70 Plus Tabs X30", "descr": "", "catid": 35, "source": 83},
    {"name": "Wellman Caps X30", "descr": "", "catid": 35, "source": 83},
    {"name": "Wellwoman 50 Plus Tabs X30", "descr": "", "catid": 35, "source": 83},
    {"name": "Wellwoman 70 Plus Caps X30", "descr": "", "catid": 35, "source": 83},
    {"name": "Wellwoman Caps X30", "descr": "", "catid": 35, "source": 83},
    {"name": "Wellwoman Max Caps", "descr": "", "catid": 35, "source": 83},
    {"name": "White Field Ointment 20G", "descr": "", "catid": 35, "source": 83},
    {"name": "Whitefield Ointment", "descr": "", "catid": 35, "source": 83},
    {"name": "Whitfield Ointment 20G (Drugfield)", "descr": "", "catid": 35, "source": 83},
    {"name": "Wosan Lotion", "descr": "", "catid": 35, "source": 83},
])

nutritionals = np.array([
    {"name": "Wate On Tonic Emulsion", "descr": "", "catid": 33, "source": 83},
    {"name": "Well Woman(50+) Multivitamin Capsules Caps", "descr": "", "catid": 33, "source": 83},
    {"name": "Wellman Capsule", "descr": "", "catid": 33, "source": 83},
    {"name": "Wellwoman Capsule", "descr": "", "catid": 33, "source": 83},
])

others = np.array([
    {"name": "Water For Injection (Aquadee)", "descr": "", "catid": 48, "source": 83},
    {"name": "Woodwards Gripe Water Small", "descr": "", "catid": 48, "source": 83},
    {"name": "Wound Debridement", "descr": "", "catid": 48, "source": 83},
    {"name": "Wound Debridement - Major", "descr": "", "catid": 48, "source": 83},
    {"name": "Wound Debridement Minor", "descr": "", "catid": 48, "source": 83},
    {"name": "Wound Dressings Large", "descr": "", "catid": 48, "source": 83},
    {"name": "Wound Dressings Medium", "descr": "", "catid": 48, "source": 83},
    {"name": "Wound Dressings Small", "descr": "", "catid": 48, "source": 83},
    {"name": "Wrist Brace", "descr": "", "catid": 48, "source": 83},
    {"name": "Wrist Splint", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "Warrens Shunt", "descr": "", "catid": 37, "source": 83},
    {"name": "Wedge Resection -Ovary - Global Fee", "descr": "", "catid": 37, "source": 83},
    {"name": "Wedge Resection Of The Stomach", "descr": "", "catid": 37, "source": 83},
    {"name": "Wedge Resection Or Biopsy Of Malign Lip Tumors", "descr": "", "catid": 37, "source": 83},
    {"name": "Wedge-Shaped Tissue Resection From Lips, Or Tongue And Primary Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Wertheim Operation (Radical Hysterectomy)", "descr": "", "catid": 37, "source": 83},
    {"name": "Whipple Procedure", "descr": "", "catid": 37, "source": 83},
    {"name": "Wide Or Radical Resection Of Malignant Tumor Of Large Bones", "descr": "", "catid": 37, "source": 83},
    {"name": "Wide Or Radical Resection Of Malignant Tumor Of Medium Bones", "descr": "", "catid": 37, "source": 83},
    {"name": "Wide Or Radical Resection Of Malignant Tumor Of Small Bones", "descr": "", "catid": 37, "source": 83},
    {"name": "Wide Or Radical Resection Of Malignant Tumor Of Vertebral Bones", "descr": "", "catid": 37, "source": 83},
    {"name": "Wilm'S Tumor Excision", "descr": "", "catid": 37, "source": 83},
    {"name": "Wisdom Tooth Extraction", "descr": "", "catid": 37, "source": 83},
    {"name": "Wisdom Tooth Extraction (In Theater)", "descr": "", "catid": 37, "source": 83},
    {"name": "Wisdom Tooth Partial Impacted Surgical Extraction", "descr": "", "catid": 37, "source": 83},
    {"name": "Wisdom Tooth Surgical Extraction", "descr": "", "catid": 37, "source": 83},
    {"name": "Wisdom Tooth Surgical Extraction (In Theater)", "descr": "", "catid": 37, "source": 83},
    {"name": "Wound Debridement ( Under Ga )", "descr": "", "catid": 37, "source": 83},
    {"name": "Wound Dressing Intermediate (Per Day)", "descr": "", "catid": 37, "source": 83},
    {"name": "Wound Dressing Major (Per Day)", "descr": "", "catid": 37, "source": 83},
    {"name": "Wound Dressing Minor (Per Day)", "descr": "", "catid": 37, "source": 83},
    {"name": "Wound Exploration - Intermediate", "descr": "", "catid": 37, "source": 83},
    {"name": "Wound Exploration - Major", "descr": "", "catid": 37, "source": 83},
    {"name": "Wound Exploration - Minor", "descr": "", "catid": 37, "source": 83},
])


# =============================================================================
# SHEET SUMMARY — Product W
# =============================================================================
# Total records on this sheet : 77
# Categories found            : consultations, diagnostic_imaging, infusions, laboratory_tests, medical_devices, medications, nutritionals, others, surgeries
# Unmapped categories         : None
# =============================================================================
