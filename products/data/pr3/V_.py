import numpy as np


consultations = np.array([
    {"name": "Visiting Consultation", "descr": "", "catid": 36, "source": 83},
])


diagnostic_imaging = np.array([
    {"name": "Venogram", "descr": "", "catid": 27, "source": 83},
    {"name": "Venogram - One Leg", "descr": "", "catid": 27, "source": 83},
])


laboratory_tests = np.array([
    {"name": "VDRL", "descr": "", "catid": 39, "source": 83},
    {"name": "VDRL, Serum/CSF", "descr": "", "catid": 39, "source": 83},
    {"name": "Viral Screen", "descr": "", "catid": 39, "source": 83},
    {"name": "Viral Screen For Blood Pint", "descr": "", "catid": 39, "source": 83},
])


medical_devices = np.array([
    {"name": "Ventilator", "descr": "", "catid": 29, "source": 83},
    {"name": "Volumatic Spacer (Paediatric)", "descr": "", "catid": 29, "source": 83},
])


medical_supplies = np.array([
    {"name": "Vicryl 2-0", "descr": "", "catid": 34, "source": 83},
    {"name": "Vicryl 3/0", "descr": "", "catid": 34, "source": 83},
    {"name": "Vicryl-2", "descr": "", "catid": 34, "source": 83},
])


medications = np.array([
    {"name": "Valium 10Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan 160/12.5 Co-Diovan", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan 160/25 Co-Diovan", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan 160Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan 80Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan Caps[Teva] 160Mg X 28", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan Htcz[Teva] 80/12.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan Htcz[Teva] 80/12.5Mg X 28", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan Htcz[Teva] 80/12.5Mg X 28 (Valsartan + Hydrochlorothiazide)", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan Htcz[Teva] Caplet 80/12.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan Htcz[Teva] Caplet 80/12.5Mg X 28", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan(Eng) 160Mg (Joltan)", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan(Eng) 80Mg (Joltan)", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan/Hct 160/12.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan/Hct 160/25Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsartan/Hct 80/12.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsatan /Hydrochlothiazide Tab 80/12.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsatan /Hydrochlothiazidetab160/12.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsatan /Hydrochlothiazidetab160/25Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsatan Tab 160Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Valsatantab 80Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Vancomycin 1G Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Vancomycin 500Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Vasopressin", "descr": "", "catid": 35, "source": 83},
    {"name": "Vasopressin Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Vasoprin 75Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Vasoprin 75Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Vasoprin Tab 75Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Vasoprin Tab 75Mg (Coated/Micropirin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Vecuten Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Ventolin 2Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ventolin Inhaler", "descr": "", "catid": 35, "source": 83},
    {"name": "Ventolin Inhaler (Salbutamol)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ventolin Nebules 2.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ventolin Nebules 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ventolin Nebules 5Mg/Vial", "descr": "", "catid": 35, "source": 83},
    {"name": "Ventolin Salbutamol Inhaler", "descr": "", "catid": 35, "source": 83},
    {"name": "Ventolin Syrup 2Mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Viarex Inhaler", "descr": "", "catid": 35, "source": 83},
    {"name": "Vidagliptin + Metformintablet50Mg/1000Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Vildagliptin 50Mg Galvus", "descr": "", "catid": 35, "source": 83},
    {"name": "Vildagliptin/Metformin 50/1000", "descr": "", "catid": 35, "source": 83},
    {"name": "Vildagliptin/Metformin 50/500", "descr": "", "catid": 35, "source": 83},
    {"name": "Vildagliptintablet50Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Villicin Balm 25G", "descr": "", "catid": 35, "source": 83},
    {"name": "Visine Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit A + Vitamin E (Rovigon Tab)", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit A 10,000 IU Softgel", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit A Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit C 1000Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit C 500Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit C Syr", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit C Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit D Oral Drops 400 IU/ML", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit D(Cholecalciferol) Syr", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit E", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit E 100Mg (Eviol)", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit E 200Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit K Inj.", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit Tab (Neurobion)", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit Tab (Neurovit)", "descr": "", "catid": 35, "source": 83},
    {"name": "Vit. K", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin A. Cap 25,000", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin B6", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin C Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin C Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin E 1000 I.U", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin E Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamin K Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Vitamins B1+B6+B12Tablet100Mg+200Mg+200Mcg", "descr": "", "catid": 35, "source": 83},
    {"name": "Voltaren Emugel 50G Tube", "descr": "", "catid": 35, "source": 83},
    {"name": "Voltaren Emulgel 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Voltaren Retard 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Voltaren Sr 100Mg", "descr": "", "catid": 35, "source": 83},
])


nutritionals = np.array([
    {"name": "Vit B-Complex Inj", "descr": "", "catid": 33, "source": 83},
    {"name": "Vit B-Complex Syrup", "descr": "", "catid": 33, "source": 83},
    {"name": "Vit B-Complex Tab", "descr": "", "catid": 33, "source": 83},
    {"name": "Vit C 1500Mg Tab-H/Craft", "descr": "", "catid": 33, "source": 83},
    {"name": "Vit. B-Complex Tab H/Craft", "descr": "", "catid": 33, "source": 83},
    {"name": "Vit. C 1000Mg Tab-H/Craft", "descr": "", "catid": 33, "source": 83},
    {"name": "Vit. C 100Mg Tab", "descr": "", "catid": 33, "source": 83},
    {"name": "Vit. C 100Mg/5Ml Syrup", "descr": "", "catid": 33, "source": 83},
    {"name": "Vitamin A", "descr": "", "catid": 33, "source": 83},
    {"name": "Vitamin B Complex", "descr": "", "catid": 33, "source": 83},
    {"name": "Vitamin B Complex Syrup", "descr": "", "catid": 33, "source": 83},
    {"name": "Vitamin Bco Inj", "descr": "", "catid": 33, "source": 83},
    {"name": "Vitamin C 500Mg H/C", "descr": "", "catid": 33, "source": 83},
    {"name": "Vitamin C Syrup", "descr": "", "catid": 33, "source": 83},
    {"name": "Vitamin C Tabs 100Mg", "descr": "", "catid": 33, "source": 83},
    {"name": "Vitamin D", "descr": "", "catid": 33, "source": 83},
    {"name": "Vitamin D 400Iu", "descr": "", "catid": 33, "source": 83},
    {"name": "Vitamin D Spec D", "descr": "", "catid": 33, "source": 83},
    {"name": "Vitamin D3 50000", "descr": "", "catid": 33, "source": 83},
])


others = np.array([
    {"name": "Visual Acuity(Paelon)", "descr": "", "catid": 48, "source": 83},
])


surgeries = np.array([
    {"name": "Vacuum Delivery", "descr": "", "catid": 37, "source": 83},
    {"name": "Vaginal Hysterectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Vagotomy And Antrectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Vagotomy, Selective", "descr": "", "catid": 37, "source": 83},
    {"name": "Vagotomy, Truncal", "descr": "", "catid": 37, "source": 83},
    {"name": "Varilux Ellipse", "descr": "", "catid": 37, "source": 83},
    {"name": "Vasectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Viral Screening For Blood Transfusion", "descr": "", "catid": 37, "source": 83},
])


# =============================================================================
# SHEET SUMMARY — Product V
# =============================================================================
# Total records on this sheet : 114
# Categories found            : consultations, diagnostic_imaging, laboratory_tests, medical_devices, medical_supplies, medications, nutritionals, others, surgeries
# Duplicates removed          : 0
# Unmapped categories         : None
# =============================================================================
