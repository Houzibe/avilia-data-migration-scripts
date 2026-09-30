import numpy as np

"""
diagnostic_imaging = np.array([
    {"name": 'Whole Body Ct {Rta}', "descr": "", "catid": 27, "source": 83},
    {"name": 'Whole Spine Ct', "descr": "", "catid": 27, "source": 83},
    {"name": 'Wrist (Both) Ap&Lat', "descr": "", "catid": 27, "source": 83},
    {"name": 'Wrist (Left) Ap&Lat', "descr": "", "catid": 27, "source": 83},
    {"name": 'Wrist (Right) Ap&Lat', "descr": "", "catid": 27, "source": 83},
    {"name": 'Wrist Joibnt (Ap/Oblique/Lat) (Left Or Right)', "descr": "", "catid": 27, "source": 83},
    {"name": 'Wrist X-Ray', "descr": "", "catid": 27, "source": 83},
])

infusions = np.array([
    {"name": 'Water For Injection Injection 10Ml, Per Amp/Vial', "descr": "", "catid": 47, "source": 83},
])

laboratory_tests = np.array([
    {"name": 'WBC Count', "descr": "", "catid": 39, "source": 83},
    {"name": 'Wbc Differential', "descr": "", "catid": 39, "source": 83},
    {"name": 'Wbc Total', "descr": "", "catid": 39, "source": 83},
    {"name": 'Western Blot/Confirmatory', "descr": "", "catid": 39, "source": 83},
    {"name": 'White Blood Count', "descr": "", "catid": 39, "source": 83},
    {"name": 'White Cell Count (Wcc)', "descr": "", "catid": 39, "source": 83},
    {"name": 'White Cell Count, Total & Differential', "descr": "", "catid": 39, "source": 83},
    {"name": 'Widal Reaction', "descr": "", "catid": 39, "source": 83},
    {"name": 'Widal Reaction (Widal)', "descr": "", "catid": 39, "source": 83},
    {"name": 'Widal Test', "descr": "", "catid": 39, "source": 83},
    {"name": 'Wound Swab M/C/S', "descr": "", "catid": 39, "source": 83},
    {"name": 'Wound, M/C/S', "descr": "", "catid": 39, "source": 83},
])

medications = np.array([
    {"name": 'Walking Clutches(Metallic Frame)', "descr": "", "catid": 35, "source": 83},
    {"name": 'Walking Clutches(Wooden)', "descr": "", "catid": 35, "source": 83},
    {"name": 'Warfarin 1Mg', "descr": "", "catid": 35, "source": 83},
"""
medications = np.array([    
    {"name": 'Warfarin 2.5Mg', "descr": "", "catid": 35, "source": 83},
    {"name": 'Warfarin 3Mg Tabs', "descr": "", "catid": 35, "source": 83},
    {"name": 'Warfarin 5Mg', "descr": "", "catid": 35, "source": 83},
    {"name": 'Warfarin Sodium Tablets (As Sodium) 3Mg', "descr": "", "catid": 35, "source": 83},
    {"name": 'Water For Injection', "descr": "", "catid": 35, "source": 83},
    {"name": 'Water For Injection 10Mls 1 Vial', "descr": "", "catid": 35, "source": 83},
    {"name": 'Wellman Capsule', "descr": "", "catid": 35, "source": 83},
    {"name": 'Wellwoman Capsule', "descr": "", "catid": 35, "source": 83},
    {"name": 'Wellwoman Plus Omega 3-6-9', "descr": "", "catid": 35, "source": 83},
    {"name": 'White Plaster 6Inch', "descr": "", "catid": 35, "source": 83},
    {"name": 'Whitefield Ointment', "descr": "", "catid": 35, "source": 83},
    {"name": 'Whitfield Ointment 20G 1 Tube', "descr": "", "catid": 35, "source": 83},
    {"name": 'Winart', "descr": "", "catid": 35, "source": 83},
    {"name": 'Wosan 10%', "descr": "", "catid": 35, "source": 83},
    {"name": 'Wosan Lotion', "descr": "", "catid": 35, "source": 83},
    {"name": 'Wrist Brace', "descr": "", "catid": 35, "source": 83},
    {"name": 'Wrist Splint', "descr": "", "catid": 35, "source": 83},
])

nutritionals = np.array([
    {"name": 'Well Woman(50+) Multivitamin Capsules Caps', "descr": "", "catid": 33, "source": 83},
])

surgeries = np.array([
    {"name": 'Warrens Shunt', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wedge Resection -Ovary - Global Fee', "descr": "", "catid": 37, "source": 83},
    {"name": 'Whole Lower Limb (Including Reduction)', "descr": "", "catid": 37, "source": 83},
    {"name": 'Whole Upper Limb (Including Reduction|)', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wide Tumor Excision', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wound Closure', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wound Closure (Orthopaedics)', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wound Debridement ( Under GA )', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wound Debridement - Major', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wound Debridement Minor', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wound Dressing     Intermediate (Per Day)', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wound Dressing     Major (Per Day)', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wound Dressing     Minor (Per Day)', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wound Exploration - Intermediate', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wound Exploration - Major', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wound Exploration - Minor', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wound Revision (Orthopaedics)', "descr": "", "catid": 37, "source": 83},
    {"name": 'Wound Suturing Debridement/Mass Excision', "descr": "", "catid": 37, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — Product W
# =============================================================================
# Total records on this sheet : 59
# Categories found            : diagnostic_imaging, infusions, laboratory_tests, medications, nutritionals, surgeries
# Unmapped categories         : None
# =============================================================================
