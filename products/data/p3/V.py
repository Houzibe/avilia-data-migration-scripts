import numpy as np

consultations = np.array([
    {"name": "Vascular Surgeon Consulation", "descr": "", "catid": 36, "source": 83},
    {"name": "Vascular Surgeon Review", "descr": "", "catid": 36, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "2 View X-Ray", "descr": "", "catid": 27, "source": 83},
    {"name": "Venogram", "descr": "", "catid": 27, "source": 83},
    {"name": "Venogram - One Leg", "descr": "", "catid": 27, "source": 83},
    {"name": "Venous /Carotid/Tissue(Eg Renal) Doppler", "descr": "", "catid": 27, "source": 83},
    {"name": "Visual Field Assessment", "descr": "", "catid": 27, "source": 83},
])

laboratory_tests = np.array([
    {"name": "Vanilyl Mandellic Acid (VMA)", "descr": "", "catid": 39, "source": 83},
    {"name": "VDRL", "descr": "", "catid": 39, "source": 83},
    {"name": "VDRL, Serum/CSF", "descr": "", "catid": 39, "source": 83},
])

medical_devices = np.array([
    {"name": "Varilux", "descr": "", "catid": 29, "source": 83},
    {"name": "Varilux Bluecut", "descr": "", "catid": 29, "source": 83},
    {"name": "Varilux Photo/ARC", "descr": "", "catid": 29, "source": 83},
    {"name": "Varilux Photo/ARC Special Order", "descr": "", "catid": 29, "source": 83},
    {"name": "Varilux White", "descr": "", "catid": 29, "source": 83},
    {"name": "Varilux White Special Order", "descr": "", "catid": 29, "source": 83},
])

medications = np.array([
    {"name": "Valium (Diazepam)", "descr": "", "catid": 35, "source": 83},
    {"name": "Valium (Diazepam) 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Valium Inj 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan 160Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan 160Mg Tabs(Diovan)", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan 320Mg (Diovan)", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan/ Hydrochlorothiazide 160/12.5Mg(Co-Diovan)", "descr": "", "catid": 35, "source": 83},
    {"name": "Vasoprin", "descr": "", "catid": 35, "source": 83},
    {"name": "Vasoprin Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Vecuten Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Veltrex Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ventolin (Sabutamol)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ventolin 2Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ventolin Inhaler", "descr": "", "catid": 35, "source": 83},
    {"name": "Ventolin Nebules 2.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ventolin Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Vermox 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Vermox Suspension 3Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Viarex Inhaler", "descr": "", "catid": 35, "source": 83},
    {"name": "Vioplex Spray(Neomycin+ Bacitracin Antibiotic Spray", "descr": "", "catid": 35, "source": 83},
    {"name": "Virest Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Visine Eye Drops (Big)", "descr": "", "catid": 35, "source": 83},
    {"name": "Visine Eye Drops (Small)", "descr": "", "catid": 35, "source": 83},
    {"name": "Vision Plus Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin A", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin A 1000Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin B Complex", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin B-Co Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin Bco Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin Bco Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin C (Ascobic Acid)", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin C 1000Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin C 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin C 100Mg/5Mls Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin C 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin C Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin E ( Togopheryl)", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin E 1000Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin E 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin K", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin K Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamins B1+B6+B12", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitrincine Eye Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Voltaren 75Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Voltaren Emulgel (20G) Small Size", "descr": "", "catid": 35, "source": 83},
    {"name": "Voltaren Emulgel (Big Size) 50G", "descr": "", "catid": 35, "source": 83},
    {"name": "Voltaren Emulgel 20G", "descr": "", "catid": 35, "source": 83},
    {"name": "Voltaren Emulgel 50G", "descr": "", "catid": 35, "source": 83},
    {"name": "Voltaren Eye Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Voltaren Retard 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Voltaren Retard Sr 75Mg Tab", "descr": "", "catid": 35, "source": 83},
])

surgeries = np.array([
    {"name": "Vacuum Devilery", "descr": "", "catid": 37, "source": 83},
    {"name": "Vaginal Cyst Enucleation", "descr": "", "catid": 37, "source": 83},
    {"name": "Vaginoclesis", "descr": "", "catid": 37, "source": 83},
    {"name": "Vagoplasty", "descr": "", "catid": 37, "source": 83},
    {"name": "Vagotomy/Pyloroplasty", "descr": "", "catid": 37, "source": 83},
    {"name": "Varicocoelectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Vasectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Vasoplasty", "descr": "", "catid": 37, "source": 83},
    {"name": "Vein Patch Angioplasty", "descr": "", "catid": 37, "source": 83},
    {"name": "Ventrosuspension Of The Bladder", "descr": "", "catid": 37, "source": 83},
    {"name": "Ventrosuspension Procedures Of Correction Of Uterine Prolapse", "descr": "", "catid": 37, "source": 83},
    {"name": "Vesical Diverticulectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Vesicovaginal Fistula Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Vidian Neurectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Volvous Of Large Bowel", "descr": "", "catid": 37, "source": 83},
    {"name": "Vulvectomy", "descr": "", "catid": 37, "source": 83},
])

vaccines = np.array([
    {"name": "Varicella", "descr": "", "catid": 46, "source": 83},
    {"name": "Varilrix (Chicken Pox)", "descr": "", "catid": 46, "source": 83},
    {"name": "Verorab + Syringe", "descr": "", "catid": 46, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — Product V
# =============================================================================
# Total records on this sheet : 86
# Categories found            : consultations, diagnostic_imaging, laboratory_tests, medical_devices, medications, surgeries, vaccines
# Unmapped categories         : None
# Duplicates removed          : medications:"Ventolin (Sabutamol)"; medications:"Vitamin A"; medications:"Vitamin B Complex"; medications:"Vitamin C (Ascobic Acid)"; medications:"Vitamins B1+B6+B12"
# =============================================================================
