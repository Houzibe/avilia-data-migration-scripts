import numpy as np


consultations = np.array([
    {"name": "Nephrologist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Neurologist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Neurologist Consultation Follow-Up", "descr": "", "catid": 36, "source": 83},
])


diagnostic_imaging = np.array([
    {"name": "Nuchal Scan", "descr": "", "catid": 27, "source": 83},
])


infusions = np.array([
    {"name": "Normal Saline (1 Ltr)", "descr": "", "catid": 47, "source": 83},
    {"name": "Normal Saline (500Ml)", "descr": "", "catid": 47, "source": 83},
    {"name": "Normal Saline 0.9% Infusion", "descr": "", "catid": 47, "source": 83},
    {"name": "Normal Saline 1000Mls Infusion", "descr": "", "catid": 47, "source": 83},
    {"name": "Normal Saline Infusion 0.5L", "descr": "", "catid": 47, "source": 83},
])


medical_devices = np.array([
    {"name": "Nebulizer Rental (Per Day)", "descr": "", "catid": 29, "source": 83},
    {"name": "Neck Collar", "descr": "", "catid": 29, "source": 83},
])


medical_supplies = np.array([
    {"name": "Nasogatric Tube", "descr": "", "catid": 34, "source": 83},
    {"name": "Needle 21G", "descr": "", "catid": 34, "source": 83},
    {"name": "Needle 23G", "descr": "", "catid": 34, "source": 83},
    {"name": "Needle And Syringe 10Ml", "descr": "", "catid": 34, "source": 83},
    {"name": "Needle And Syringe 2Ml", "descr": "", "catid": 34, "source": 83},
    {"name": "Needle And Syringe 5Ml", "descr": "", "catid": 34, "source": 83},
    {"name": "NG Tube -5", "descr": "", "catid": 34, "source": 83},
    {"name": "NG Tube-8", "descr": "", "catid": 34, "source": 83},
    {"name": "NG-Tube -6", "descr": "", "catid": 34, "source": 83},
    {"name": "NG-Tube-10", "descr": "", "catid": 34, "source": 83},
    {"name": "NG-Tube-12", "descr": "", "catid": 34, "source": 83},
    {"name": "NG-Tube-14", "descr": "", "catid": 34, "source": 83},
    {"name": "NG-Tube-16", "descr": "", "catid": 34, "source": 83},
    {"name": "NG-Tube-18", "descr": "", "catid": 34, "source": 83},
    {"name": "Novofine Needle", "descr": "", "catid": 34, "source": 83},
    {"name": "Novotwist Pin (8Mm)", "descr": "", "catid": 34, "source": 83},
    {"name": "Nurses’ Cap", "descr": "", "catid": 34, "source": 83},
    {"name": "Nylon -0", "descr": "", "catid": 34, "source": 83},
    {"name": "Nylon -1", "descr": "", "catid": 34, "source": 83},
    {"name": "Nylon -2", "descr": "", "catid": 34, "source": 83},
    {"name": "Nylon -2-0", "descr": "", "catid": 34, "source": 83},
    {"name": "Nylon 2/O", "descr": "", "catid": 34, "source": 83},
])


medications = np.array([
    {"name": "Naloxone 400Mcg", "descr": "", "catid": 35, "source": 83},
    {"name": "Naloxone Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Naproxen 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Natrilix Sr 1.5Mg X 30", "descr": "", "catid": 35, "source": 83},
    {"name": "Natrixam 1.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Naxen 250Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Naxen 500Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nebivolol 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nebivolol 5Mg (Nebicard)", "descr": "", "catid": 35, "source": 83},
    {"name": "Neo-Healer Ointment 30G", "descr": "", "catid": 35, "source": 83},
    {"name": "Neo-Healer Suppository", "descr": "", "catid": 35, "source": 83},
    {"name": "Neofylin 100Ml Cough Syr", "descr": "", "catid": 35, "source": 83},
    {"name": "Neofylin Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Neomercazole 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Neomycin 15G Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Neomycin Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Neomycin Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Neopresol Lotion", "descr": "", "catid": 35, "source": 83},
    {"name": "Neostigmin", "descr": "", "catid": 35, "source": 83},
    {"name": "Neostigmine Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Neurobion / Neurovit Forte", "descr": "", "catid": 35, "source": 83},
    {"name": "Neurogesic / Powergesic", "descr": "", "catid": 35, "source": 83},
    {"name": "Neurogesic Gel 35G", "descr": "", "catid": 35, "source": 83},
    {"name": "Nevirapine 200Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nevirapine Susp 50Mg/5Ml 240Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Nevirapine Suspension", "descr": "", "catid": 35, "source": 83},
    {"name": "Nevirapine Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nexium 20Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nexium 40Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nicotinic Acid Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedine De", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedine Dexcel Tabs X 30", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine 20Mg Retard", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine 20Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine 30Mg Tab (Nifecard )", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine Sr 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine Sr 30Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifegem 20Mg X 10 [Blister]", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifegem Retard Tab 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nilgar M-15 Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Nilgar M-15 Tabs X 20", "descr": "", "catid": 35, "source": 83},
    {"name": "Nilgar M-30 Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Nilgar M-30 Tabs X 20", "descr": "", "catid": 35, "source": 83},
    {"name": "Nilgar Tabs 15Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nilgar Tabs 15Mg X 30", "descr": "", "catid": 35, "source": 83},
    {"name": "Nilgar Tabs 30Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nilgar Tabs 30Mg X 30", "descr": "", "catid": 35, "source": 83},
    {"name": "Nilide 100Mg Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimesulide 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimica 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimica Susp -60Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimodipine 30Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimulid Susp 30Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimulid Tab 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrazepam 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrazepam 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrilix 1.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrofurantoin", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrofurantoin 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrofurantoin 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitroglycerine 0.4Mg Sublingual Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nivaquine Forte Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Nizoral 200Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nizoral Cream 15G", "descr": "", "catid": 35, "source": 83},
    {"name": "Nizoral Shampoo", "descr": "", "catid": 35, "source": 83},
    {"name": "No-Spa Inj 40Mg/Amp", "descr": "", "catid": 35, "source": 83},
    {"name": "Nocof Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Nor Adrenaline Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Norflex", "descr": "", "catid": 35, "source": 83},
    {"name": "Norflex 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Norgesic", "descr": "", "catid": 35, "source": 83},
    {"name": "Norgesic 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Noristerat", "descr": "", "catid": 35, "source": 83},
    {"name": "Normal Saline Nasal Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Normoretic", "descr": "", "catid": 35, "source": 83},
    {"name": "Normoretic Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Normoretic Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Normoretic Tabs Blister", "descr": "", "catid": 35, "source": 83},
    {"name": "Normoretic Tabs X 100", "descr": "", "catid": 35, "source": 83},
    {"name": "Norplant", "descr": "", "catid": 35, "source": 83},
    {"name": "Norvasc 10Mg * 10 Strips", "descr": "", "catid": 35, "source": 83},
    {"name": "Norvasc 10Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Norvasc 10Mg X 10 Pack", "descr": "", "catid": 35, "source": 83},
    {"name": "Norvasc 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Norvasc Tabs 5Mg X 100", "descr": "", "catid": 35, "source": 83},
    {"name": "Nose -Nasal Packing/Control Of Epistaxis", "descr": "", "catid": 35, "source": 83},
    {"name": "Nospa 40Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Novalgin Tab 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Novomix Pen", "descr": "", "catid": 35, "source": 83},
    {"name": "Novorapid Pen", "descr": "", "catid": 35, "source": 83},
    {"name": "Nugel-O", "descr": "", "catid": 35, "source": 83},
    {"name": "Nugel-O Antacid", "descr": "", "catid": 35, "source": 83},
    {"name": "Nyolol 0.5% Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Nyolol Opthalmic Gel 0.1% 5G", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin 500000 IU Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin Drops 100,000Iu/Generic", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin Oral 500 000 I.U", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin Oral Drops 30Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin Pess.100,000Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin Pessary", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin Suspension", "descr": "", "catid": 35, "source": 83},
])


nutritionals = np.array([
    {"name": "Neurobion Tab", "descr": "", "catid": 33, "source": 83},
    {"name": "Neurovit Forte (Vitamin B1,B6,B12)", "descr": "", "catid": 33, "source": 83},
    {"name": "Neurovit Forte Tabs", "descr": "", "catid": 33, "source": 83},
])


others = np.array([
    {"name": "Nebulization + Drugs", "descr": "", "catid": 48, "source": 83},
    {"name": "Nebulization+Nebules (Per Session)", "descr": "", "catid": 48, "source": 83},
])


surgeries = np.array([
    {"name": "Nasal And Aural Washout", "descr": "", "catid": 37, "source": 83},
    {"name": "Nasal Packing", "descr": "", "catid": 37, "source": 83},
    {"name": "Nebulization+Drug (In-Patient/Day)", "descr": "", "catid": 37, "source": 83},
    {"name": "Nebulization+Drug (Out-Patient/Session)", "descr": "", "catid": 37, "source": 83},
    {"name": "Nebulizing / Mdi Using A Spacer", "descr": "", "catid": 37, "source": 83},
    {"name": "Neonatal ICU", "descr": "", "catid": 37, "source": 83},
    {"name": "Nephrectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nephrectomy With Drainage Nephrostomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nephrectomy, Partial", "descr": "", "catid": 37, "source": 83},
    {"name": "Nephro-Ureterectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nephrolithotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nephrolithotomy/Ureterolithotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Normal Delivery (Cervical Ripening/Lnduction)", "descr": "", "catid": 37, "source": 83},
    {"name": "Normal Delivery (Including Episiotomy/Induction)", "descr": "", "catid": 37, "source": 83},
    {"name": "Normal Delivery (Without Episiotomy/Induction)", "descr": "", "catid": 37, "source": 83},
    {"name": "Normal Delivery + Perineal Laceration Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Normal Delivery With Or Without Episiotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Norplant Application", "descr": "", "catid": 37, "source": 83},
])


# =============================================================================
# SHEET SUMMARY — Product N
# =============================================================================
# Total records on this sheet : 158
# Categories found            : consultations, diagnostic_imaging, infusions, medical_devices, medical_supplies, medications, nutritionals, others, surgeries
# Duplicates removed          : 0
# Unmapped categories         : None
# =============================================================================
