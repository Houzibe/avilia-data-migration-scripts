import numpy as np

consultations = np.array([
    {"name": "Neonatologist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Neonatologist Review", "descr": "", "catid": 36, "source": 83},
    {"name": "Nephrology Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Nephrology Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "Neurologist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Neurologist Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "Neurosurgeon Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Neurosurgeon Follow Up", "descr": "", "catid": 36, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Neck Computed Tomography (CT) Scan", "descr": "", "catid": 27, "source": 83},
    {"name": "Neck/Thyroid Scan", "descr": "", "catid": 27, "source": 83},
])

infusions = np.array([
    {"name": "Normal Saline Infusion", "descr": "", "catid": 47, "source": 83},
])

medical_supplies = np.array([
    {"name": "Needle", "descr": "", "catid": 34, "source": 83},
])

medications = np.array([
    {"name": "Naloxone", "descr": "", "catid": 35, "source": 83},
    {"name": "Naproxen", "descr": "", "catid": 35, "source": 83},
    {"name": "Naproxen (Other Brands) 250Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Naproxen (Other Brands) 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Naproxen 250Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Naproxen 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Natrilix Tab 1.5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Natrilix Tab 2.5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Navidoxine", "descr": "", "catid": 35, "source": 83},
    {"name": "Naxen 250Mg Tab (Naproxen)", "descr": "", "catid": 35, "source": 83},
    {"name": "Naxen 500Mg Tab (Naproxen)", "descr": "", "catid": 35, "source": 83},
    {"name": "Neomercazole 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Neomycin", "descr": "", "catid": 35, "source": 83},
    {"name": "Neomycin Powder", "descr": "", "catid": 35, "source": 83},
    {"name": "Neopreson Lotion", "descr": "", "catid": 35, "source": 83},
    {"name": "Neoskin", "descr": "", "catid": 35, "source": 83},
    {"name": "Neostigmine Bromide 25Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Neostigmine Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Neuracalm 150Mg ( Pregabalin & Methylcobalamin) Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Neuracalm(Pregabalin 75Mg& Methylcobalamin 750Ug)", "descr": "", "catid": 35, "source": 83},
    {"name": "Neurobion", "descr": "", "catid": 35, "source": 83},
    {"name": "Neurogesic Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Neurovite", "descr": "", "catid": 35, "source": 83},
    {"name": "Neurovite Forte", "descr": "", "catid": 35, "source": 83},
    {"name": "Nevirapine 200Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nevirapine Syrup 240Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Nexium (Esomeprazole 20Mg)", "descr": "", "catid": 35, "source": 83},
    {"name": "Nexium 20Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nexium 40Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nexium Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Ng Tube", "descr": "", "catid": 35, "source": 83},
    {"name": "Nicotinic Acid Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nidof 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nife Card 30Mg (Nefidipine)", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine 30Mg 30Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifegem Retard 20Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nilide 100Mg Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimesulide 100 Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimica 100 Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimica Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrazepam", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrazepam 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrofurantoin", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrofurantoin 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitroglycerine Lingual", "descr": "", "catid": 35, "source": 83},
    {"name": "Nivaquine Fortye Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Nivaquine Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Nizoral", "descr": "", "catid": 35, "source": 83},
    {"name": "Nizoral Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Nizoral Shampoo", "descr": "", "catid": 35, "source": 83},
    {"name": "Nizoral Tab 200Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "No-Spa Inj40Mg/Qmop", "descr": "", "catid": 35, "source": 83},
    {"name": "No-Spa Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Norflex", "descr": "", "catid": 35, "source": 83},
    {"name": "Norflex Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Norgesic Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Noristherat", "descr": "", "catid": 35, "source": 83},
    {"name": "Normoretic Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Norvasc", "descr": "", "catid": 35, "source": 83},
    {"name": "Norvasc Tab 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nospa", "descr": "", "catid": 35, "source": 83},
    {"name": "Nospamin", "descr": "", "catid": 35, "source": 83},
    {"name": "Novalgin", "descr": "", "catid": 35, "source": 83},
    {"name": "Nylon", "descr": "", "catid": 35, "source": 83},
    {"name": "Nyolo Gel", "descr": "", "catid": 35, "source": 83},
    {"name": "Nyolol.5% Eye Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Nysatin Oral", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin 500, 000Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin Oral Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin Oral Drops 30Mls", "descr": "", "catid": 35, "source": 83},
])

others = np.array([
    {"name": "Nasal Packing", "descr": "", "catid": 48, "source": 83},
    {"name": "Nasogastric Tube Passage+Feeding Per Diem", "descr": "", "catid": 48, "source": 83},
    {"name": "NICU", "descr": "", "catid": 48, "source": 83},
    {"name": "Nursing Care/Day", "descr": "", "catid": 48, "source": 83},
    {"name": "Nursing Services", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "Nasal Polypectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nebulisation", "descr": "", "catid": 37, "source": 83},
    {"name": "Nebulisation (Per Day)", "descr": "", "catid": 37, "source": 83},
    {"name": "Nebulization + Drug (In-Patient/Session)", "descr": "", "catid": 37, "source": 83},
    {"name": "Nebulization+Drug (Out-Patient/Session)", "descr": "", "catid": 37, "source": 83},
    {"name": "Neck Exploration For Penetrating Neck Injury", "descr": "", "catid": 37, "source": 83},
    {"name": "Nephrectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nephrolithotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nephrolithotomy/ Ureterolithotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nerve Root Compression", "descr": "", "catid": 37, "source": 83},
    {"name": "Ngtube Insertion", "descr": "", "catid": 37, "source": 83},
    {"name": "Normal Delivery [Plus 1 Postnatal Visit]", "descr": "", "catid": 37, "source": 83},
    {"name": "Normal Vaginal Delivery", "descr": "", "catid": 37, "source": 83},
    {"name": "Normal Vaginal Delivery +/- Episiotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nose", "descr": "", "catid": 37, "source": 83},
    {"name": "Nursing Care Per Diem", "descr": "", "catid": 37, "source": 83},
])

vaccines = np.array([
    {"name": "Nimenrix (Meningitis)", "descr": "", "catid": 46, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — Product N
# =============================================================================
# Total records on this sheet : 107
# Categories found            : consultations, diagnostic_imaging, infusions, medical_supplies, medications, others, surgeries, vaccines
# Unmapped categories         : None
# Duplicates removed          : medications:"Naproxen"; medications:"Nifedipine"; medications:"Nystatin"; medications:"Nystatin"
# =============================================================================
