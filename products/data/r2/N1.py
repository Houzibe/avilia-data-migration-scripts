import numpy as np

consultations = np.array([
    {"name": "Neurosurgeon", "descr": "", "catid": 36, "source": 83},
    {"name": "Neurosurgeon - Initial", "descr": "", "catid": 36, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Nuchal Translucency Scan", "descr": "", "catid": 27, "source": 83},
])

laboratory_tests = np.array([
    {"name": "Neutrophils", "descr": "", "catid": 39, "source": 83},
    {"name": "Non-Invasive Prenatal Test", "descr": "", "catid": 39, "source": 83},
])

medications = np.array([
    {"name": "N Acetylcysteine (Nac) Capsule 600 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nalidixic Acid (...) Tablet 500 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Naloxone (...) Injection 0.4 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Naproxen (...) Tablet 500 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Naproxen (Relev) Tablet 500 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Naproxen Sodium (Relev Rapid) Tablet 550 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Neck Collar (Hard) Item 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Neck Collar (Soft) Item 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Neofylin (Neofylin) Syrup 50 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Neomycin + Beclomethasone +Clotrimazole +Lignocaine Hcl (Clozotic Ear) Drops 1 Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Neomycin 50.2Mg + Polymyxin 35I.U + Nystatin 100Iu. (Gynocare) Ovule 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Neomycin 50.2Mg + Polymyxin 35I.U + Nystatin 100Iu. (Polygynax) Ovule 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Neomycin Sulphate + Bacitracin Zinc (Bivacyn) Spray 20 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Neomycin Sulphate + Bacitracin Zinc (Cicatrin) Powder 20 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Neonatal ECG Probe (...) Item 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Neostigmine (...) Injection 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Nepafenac (Nekatap) Solution 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Nevirapine (...) Suspension 50 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Nevirapine (...) Tablet 200 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nicotinic Acid 50Mg (Pharmatinic Acid) Tablet 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine (Cardovasc) Tablet 20 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine (Cardovasc) Tablet 30 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine (Nifecard) Tablet 30 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine (Nifegem) Tablet 20 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine (Nifendal) Tablet 20 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimodipine (Nmotop) Tablet 30 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrazepam (Swidon) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrofurantoin (...) Tablet 100 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Noradrenaline (Veraline) Injection 0.2 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Norethisterone (Noristerat) Injection 200 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Norethisterone (Primolut-N Depot) Injection 250 mg/2Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Norethisterone (Primolut-N) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nurses Cap (Dgl) Item 100 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin (Biomestatin) Syrup 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin (Biomestatin) Tablet 500000 IU", "descr": "", "catid": 35, "source": 83},
])

others = np.array([
    {"name": "Nebulization", "descr": "", "catid": 48, "source": 83},
    {"name": "Neonatal Care", "descr": "", "catid": 48, "source": 83},
    {"name": "Nursing Care", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "Nasal Endoscopy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nasal Polypectomy (Under GA)", "descr": "", "catid": 37, "source": 83},
    {"name": "Nasal Polypectomy + Bina Under GA", "descr": "", "catid": 37, "source": 83},
    {"name": "Nebulisation With Normal Saline", "descr": "", "catid": 37, "source": 83},
    {"name": "Nebulisation With Salbutamol 3Mg Or More", "descr": "", "catid": 37, "source": 83},
    {"name": "Nebulization With Salbutamol 2.5Mg Or Less", "descr": "", "catid": 37, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — N
# =============================================================================
# Total records on this sheet : 49
# Categories found            : consultations, diagnostic_imaging, laboratory_tests, medications, others, surgeries
# Unmapped categories         : None
# =============================================================================
