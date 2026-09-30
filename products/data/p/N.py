import numpy as np

consultations = np.array([
    {"name": "Neonatologist (In-House)", "descr": "", "catid": 36, "source": 83},
    {"name": "Neonatologist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Neonatologist Review", "descr": "", "catid": 36, "source": 83},
    {"name": "Neonatologist Senior Consultant Care", "descr": "", "catid": 36, "source": 83},
    {"name": "Nephrologist (In-House)", "descr": "", "catid": 36, "source": 83},
    {"name": "Nephrologist (Visiting)", "descr": "", "catid": 36, "source": 83},
    {"name": "Nephrology Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Nephrology Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "Neurologist", "descr": "", "catid": 36, "source": 83},
    {"name": "Neurologist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Neurologist Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "Neurology Review", "descr": "", "catid": 36, "source": 83},
    {"name": "Neurosurgeon Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Neurosurgeon Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "Nurse (Home Care Package)/Hour", "descr": "", "catid": 36, "source": 83},
    {"name": "Nurse Care /Out Born", "descr": "", "catid": 36, "source": 83},
    {"name": "Nurse Care/ Nicu", "descr": "", "catid": 36, "source": 83},
    {"name": "Nursing care", "descr": "", "catid": 36, "source": 83},
])

dental_services = np.array([
    {"name": "Non Surgical Extraction", "descr": "", "catid": 50, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Nuchal Translucency", "descr": "", "catid": 27, "source": 83},
    {"name": "Nuchal Translucency (Triplets)", "descr": "", "catid": 27, "source": 83},
    {"name": "Nuchal Translucency (Twins)", "descr": "", "catid": 27, "source": 83},
])

laboratory_tests = np.array([
    {"name": "Nail Clippings", "descr": "", "catid": 39, "source": 83},
    {"name": "Nail Scrapping Microscopy", "descr": "", "catid": 39, "source": 83},
    {"name": "Nail Snipping Microscopy", "descr": "", "catid": 39, "source": 83},
    {"name": "Nasal Screen for Methicillin resistant Staphylococcus Aureus", "descr": "", "catid": 39, "source": 83},
    {"name": "Nasal/Swab Mcs", "descr": "", "catid": 39, "source": 83},
    {"name": "Nasal: Microscopy, Culture & Sensitivity", "descr": "", "catid": 39, "source": 83},
    {"name": "Non Gynaecological Cytology", "descr": "", "catid": 39, "source": 83},
])

medical_devices = np.array([
    {"name": "Nebulization (Between One To Three Cycles)", "descr": "", "catid": 29, "source": 83},
    {"name": "Nebulization (Procedure) For 1-3 Cycles", "descr": "", "catid": 29, "source": 83},
    {"name": "Nebulization (Procedure) With Patient Kits", "descr": "", "catid": 29, "source": 83},
    {"name": "Nebulization More Than Three Cycles", "descr": "", "catid": 29, "source": 83},
])

medical_supplies = np.array([
    {"name": "Ng  Tube Insertion", "descr": "", "catid": 34, "source": 83},
    {"name": "Ng Tube Insertion Adult", "descr": "", "catid": 34, "source": 83},
    {"name": "Ngt Feeding", "descr": "", "catid": 34, "source": 83},
    {"name": "Ngt/Ogt Feeding", "descr": "", "catid": 34, "source": 83},
])

medications = np.array([
    {"name": "Nalidixic Acid 500Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Naproxen 250Mg  (Naxen)", "descr": "", "catid": 35, "source": 83},
    {"name": "Naproxen 500Mg  (Naxen)", "descr": "", "catid": 35, "source": 83},
    {"name": "Naproxen Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Natrilix 1.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Natrilix 1.5Mg Sr Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Natrilix Sr 1.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Natulan 50Mg Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Nebulization - Drug", "descr": "", "catid": 35, "source": 83},
    {"name": "Needle And Syringe 10Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Needle And Syringe 20Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Needle And Syringe 2Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Needle And Syringe 50Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Needle And Syringe 5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Neofylin Cough Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Neomercazole 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Neopresol Lotion", "descr": "", "catid": 35, "source": 83},
    {"name": "Neoral 25Mg Capsule", "descr": "", "catid": 35, "source": 83},
    {"name": "Neoral 50Mg Capsule", "descr": "", "catid": 35, "source": 83},
    {"name": "Neostigmine 2.5Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Neostigmine Bromide 15Mg (Prostigmin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Nepafenac", "descr": "", "catid": 35, "source": 83},
    {"name": "Nerve And Bone Liniment", "descr": "", "catid": 35, "source": 83},
    {"name": "Neurobion", "descr": "", "catid": 35, "source": 83},
    {"name": "Neurobion Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Neuroderm", "descr": "", "catid": 35, "source": 83},
    {"name": "Neurogesic Gel", "descr": "", "catid": 35, "source": 83},
    {"name": "Neurogesic Gel 35G", "descr": "", "catid": 35, "source": 83},
    {"name": "Neurovite", "descr": "", "catid": 35, "source": 83},
    {"name": "Neurovite Forte", "descr": "", "catid": 35, "source": 83},
    {"name": "Neurovite Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Nevimune Susp", "descr": "", "catid": 35, "source": 83},
    {"name": "Nevirapine 200Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nevirapine 200Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nevirapine 50Mg Susp - 240Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Nexfort 10/160Mg (Amlodipine/Valsartan)", "descr": "", "catid": 35, "source": 83},
    {"name": "Nexium Tab 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nexium Tab 40Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ng Tube (All Sizes)", "descr": "", "catid": 35, "source": 83},
    {"name": "Nicotinic Acid", "descr": "", "catid": 35, "source": 83},
    {"name": "Nicotinic Acid Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifecard Xl 30Mg Tablets", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine 20Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifedipine 30Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifegem 20Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nifegem Retard 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nilide 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimenrix", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimesulide 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimica 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimica Suspension", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimulid 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nimulid Suspension", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrazepam 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrazepam 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrofurantoin 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrofurantoin 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nitrofurantoin 50Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nivaquine Forte", "descr": "", "catid": 35, "source": 83},
    {"name": "Nizoral 200Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Nizoral Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Nizoral Shampoo", "descr": "", "catid": 35, "source": 83},
    {"name": "Norethisterone Enantate 200Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Norethisterone Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Norflex 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Norgesic", "descr": "", "catid": 35, "source": 83},
    {"name": "Norgesic Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Normal Saline Infusion 0.5L", "descr": "", "catid": 35, "source": 83},
    {"name": "Normoretic", "descr": "", "catid": 35, "source": 83},
    {"name": "Normoretic Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Norodexa", "descr": "", "catid": 35, "source": 83},
    {"name": "Norvasc 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Norvasc 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nospa 40Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nospa Inj 40Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Nospamin", "descr": "", "catid": 35, "source": 83},
    {"name": "Nospamin Oral Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Novalgin 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Novapime 1G Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Novapime 500Mg Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Novofine Needle", "descr": "", "catid": 35, "source": 83},
    {"name": "Novomix", "descr": "", "catid": 35, "source": 83},
    {"name": "Nyolol Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Nyolol Opthalmic Gel 0.1% - 5G", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin 100000Iu Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin Lozenges 100000 Units", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin Oral Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Nystatin Tab 500,000Iu", "descr": "", "catid": 35, "source": 83},
])

mental_health_services = np.array([
    {"name": "Neuro Developmental Clinic (Follow Up)", "descr": "", "catid": 43, "source": 83},
    {"name": "Neuro Developmental Clinic (Initial Consult)", "descr": "", "catid": 43, "source": 83},
])

others = np.array([
    {"name": "Nasogastric Tube All Sizes", "descr": "", "catid": 48, "source": 83},
    {"name": "Nebulisation With Drugs", "descr": "", "catid": 48, "source": 83},
    {"name": "Nebulisation With Saline", "descr": "", "catid": 48, "source": 83},
    {"name": "Nurse", "descr": "", "catid": 48, "source": 83},
    {"name": "Nursing Care (One On One)", "descr": "", "catid": 48, "source": 83},
])

physiotherapy = np.array([
    {"name": "Nerve Conduction Test", "descr": "", "catid": 40, "source": 83},
])

reproductive_health = np.array([
    {"name": "Normal Delivery", "descr": "", "catid": 32, "source": 83},
])

surgeries = np.array([
    {"name": "Nasal Packing", "descr": "", "catid": 37, "source": 83},
    {"name": "Nasal Polypectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nasal Sinus Surgery E.G Caldwell Luc", "descr": "", "catid": 37, "source": 83},
    {"name": "Neck Collar ( Hard)", "descr": "", "catid": 37, "source": 83},
    {"name": "Neck Collar (Soft)", "descr": "", "catid": 37, "source": 83},
    {"name": "Neonatal Resuscitation + Endotracheal Intubation", "descr": "", "catid": 37, "source": 83},
    {"name": "Nephrectomy With Drainage Nephrostomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nephrectomy/ Nephrolithotomy/ Pyelolithotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nephro-Ureterectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nephrolithotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Nerve Blockage (One Ankle)", "descr": "", "catid": 37, "source": 83},
    {"name": "Nerve Blockage (One Hand)", "descr": "", "catid": 37, "source": 83},
    {"name": "Normal Delivery Package", "descr": "", "catid": 37, "source": 83},
])

vaccines = np.array([
    {"name": "Nimenrix @2 Years", "descr": "", "catid": 46, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — N
# =============================================================================
# Total records on this sheet : 149
# Categories found            : consultations, dental_services, diagnostic_imaging, laboratory_tests, medical_devices, medical_supplies, medications, mental_health_services, others, physiotherapy, reproductive_health, surgeries, vaccines
# Duplicates removed          : 1
# Unmapped categories         : None
# =============================================================================
