import numpy as np

consultations = np.array([
    {"name": "Ophthalmologist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Opthamologist Consultion", "descr": "", "catid": 36, "source": 83},
    {"name": "Opthamologist Review", "descr": "", "catid": 36, "source": 83},
    {"name": "Optometrist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Optometrist Review", "descr": "", "catid": 36, "source": 83},
    {"name": "Orthodontist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Orthodontist Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "Orthopaedic Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Orthopaedic Follow Up", "descr": "", "catid": 36, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Obstetric", "descr": "", "catid": 27, "source": 83},
    {"name": "Obstetric Scan", "descr": "", "catid": 27, "source": 83},
    {"name": "Obstetric Scan (Extra)", "descr": "", "catid": 27, "source": 83},
    {"name": "Occipito-Mental (Om) X-Ray", "descr": "", "catid": 27, "source": 83},
    {"name": "OCT (Both Eyes)", "descr": "", "catid": 27, "source": 83},
    {"name": "One Hip Joint - Ap & Lat", "descr": "", "catid": 27, "source": 83},
    {"name": "OPG (Panoramic View X-Ray)", "descr": "", "catid": 27, "source": 83},
    {"name": "Oral Cholecystogram", "descr": "", "catid": 27, "source": 83},
    {"name": "Ovulometry/Tv Scan", "descr": "", "catid": 27, "source": 83},
])

laboratory_tests = np.array([
    {"name": "Observation", "descr": "", "catid": 39, "source": 83},
    {"name": "Occult Blood, Stool/Urine", "descr": "", "catid": 39, "source": 83},
    {"name": "Occult Blood-Fecal", "descr": "", "catid": 39, "source": 83},
    {"name": "Occult Fecal Blood", "descr": "", "catid": 39, "source": 83},
    {"name": "Oestradiol", "descr": "", "catid": 39, "source": 83},
    {"name": "OGTT", "descr": "", "catid": 39, "source": 83},
    {"name": "Oral Glucose Tolerence Test ( Gtt)", "descr": "", "catid": 39, "source": 83},
    {"name": "Orbital CT", "descr": "", "catid": 39, "source": 83},
    {"name": "Osmotic Fragility", "descr": "", "catid": 39, "source": 83},
])

medications = np.array([
    {"name": "Obron 6 Capsules", "descr": "", "catid": 35, "source": 83},
    {"name": "Ofloxacin", "descr": "", "catid": 35, "source": 83},
    {"name": "Ofloxacin (Other Brands) Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Okacin (Lomefloxacin) Eyedrop", "descr": "", "catid": 35, "source": 83},
    {"name": "Olanpazine 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Olanzapine 10Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Olanzepine", "descr": "", "catid": 35, "source": 83},
    {"name": "Olive Oil", "descr": "", "catid": 35, "source": 83},
    {"name": "Olopatadine Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Omeprazole", "descr": "", "catid": 35, "source": 83},
    {"name": "Omeprazole 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Omnglyza 5Mg (Saxaplitin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Omron Automatic Blood Pressure Monitor", "descr": "", "catid": 35, "source": 83},
    {"name": "Ondasteron", "descr": "", "catid": 35, "source": 83},
    {"name": "Ondasteroninj 4Mg/2Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Onglyza 2.5Mg (Saxagliptin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ophenadrine", "descr": "", "catid": 35, "source": 83},
    {"name": "Optalidon", "descr": "", "catid": 35, "source": 83},
    {"name": "Optrex Eye Dros", "descr": "", "catid": 35, "source": 83},
    {"name": "Oraasel Granules(Ors Solution)", "descr": "", "catid": 35, "source": 83},
    {"name": "Oral Polio", "descr": "", "catid": 35, "source": 83},
    {"name": "Oral Rehydration Salt", "descr": "", "catid": 35, "source": 83},
    {"name": "Orelox (Cefpodoxime) 100Mg Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Orelox (Cefpodoxime) 100Ml Suspension", "descr": "", "catid": 35, "source": 83},
    {"name": "Orelox (Cefpodoxime) 50Ml Susp", "descr": "", "catid": 35, "source": 83},
    {"name": "Orelox 200Mg (Branded)", "descr": "", "catid": 35, "source": 83},
    {"name": "Orphenadrine + Paracetamol", "descr": "", "catid": 35, "source": 83},
    {"name": "Ors", "descr": "", "catid": 35, "source": 83},
    {"name": "Osteocare Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Otomed Ear Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Otrivin Nasal Drop (Adult)", "descr": "", "catid": 35, "source": 83},
    {"name": "Otrivin Nasal Drop (Infant)", "descr": "", "catid": 35, "source": 83},
    {"name": "Oxybutynin", "descr": "", "catid": 35, "source": 83},
    {"name": "Oxytocin", "descr": "", "catid": 35, "source": 83},
    {"name": "Oxytocin Inj 10 Unit", "descr": "", "catid": 35, "source": 83},
])

others = np.array([
    {"name": "Observation", "descr": "", "catid": 48, "source": 83},
    {"name": "Oto-Accousticemessions (OAE)", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "Obstetrics Trauma/Paresis/Paralysis", "descr": "", "catid": 37, "source": 83},
    {"name": "Oddis Sphincteroplasty", "descr": "", "catid": 37, "source": 83},
    {"name": "Oeshophagoscopy For Foreign Body Removal", "descr": "", "catid": 37, "source": 83},
    {"name": "Oesophageal ,2 & 3 Stage, Thoraco-Abdominal, Fistula Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Oesophageal Atresia (Fistula)", "descr": "", "catid": 37, "source": 83},
    {"name": "Oesophageal Atresia And Tracheo-Oesophageal Fistula Repair", "descr": "", "catid": 37, "source": 83},
    {"name": "Oesophageal Transection", "descr": "", "catid": 37, "source": 83},
    {"name": "Oesophagealsubstitution, Diverticulum Excision", "descr": "", "catid": 37, "source": 83},
    {"name": "Oesophagectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Oesophagogastrectomy With Interposition Of Colonic/Jejunal Segment", "descr": "", "catid": 37, "source": 83},
    {"name": "Oesophagoscopy", "descr": "", "catid": 37, "source": 83},
    {"name": "Oesophagoscopy (Interventional)", "descr": "", "catid": 37, "source": 83},
    {"name": "Oophorectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Open Reduction & Internal Fixation Of Fractures (+Locked Plate Implant)", "descr": "", "catid": 37, "source": 83},
    {"name": "Open Reduction & Internal Fixation Of Fractures–Femur (+Dynamic Compression Plate Implant)", "descr": "", "catid": 37, "source": 83},
    {"name": "Open Reduction & Internal Fixation Of Fractures–Hand (+Dynamic Compression Plate Implant)", "descr": "", "catid": 37, "source": 83},
    {"name": "Open Reduction And Internal Fixation Of Fractures Of :", "descr": "", "catid": 37, "source": 83},
    {"name": "Operculectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Opv", "descr": "", "catid": 37, "source": 83},
    {"name": "Orchidectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Orchidectomy + Herniorraphy", "descr": "", "catid": 37, "source": 83},
    {"name": "Orchidopexy", "descr": "", "catid": 37, "source": 83},
    {"name": "Orchidopexy - Bilateral", "descr": "", "catid": 37, "source": 83},
    {"name": "Orchidopexy - Unilateral)", "descr": "", "catid": 37, "source": 83},
    {"name": "Orchidopexy, With Circumsion, With Eversion Of Sac, With Herniotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Osteoclasis, Internal Fixation Of Mal-Union", "descr": "", "catid": 37, "source": 83},
    {"name": "Ovarectomy/Oophrectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Ovarian Biopsy", "descr": "", "catid": 37, "source": 83},
    {"name": "Oxygen Therapy (Continuous/Day)", "descr": "", "catid": 37, "source": 83},
    {"name": "Oxygen Therapy (Intermittent/Day)", "descr": "", "catid": 37, "source": 83},
    {"name": "Oxygen Therapy (Per Day)", "descr": "", "catid": 37, "source": 83},
])

vaccines = np.array([
    {"name": "Opv (Oral Polio Vaccine)", "descr": "", "catid": 46, "source": 83},
    {"name": "Oral Polio Vaccine", "descr": "", "catid": 46, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — Product O
# =============================================================================
# Total records on this sheet : 97
# Categories found            : consultations, diagnostic_imaging, laboratory_tests, medications, others, surgeries, vaccines
# Unmapped categories         : None
# Duplicates removed          : surgeries:"Oesophagoscopy"; medications:"Ofloxacin"; medications:"Omeprazole"; surgeries:"Open Reduction & Internal Fixation Of Fractures–Femur (+Dynamic Compression Plate Implant)"; consultations:"Optometrist Consultation"; consultations:"Optometrist Review"; medications:"Oral Rehydration Salt"; surgeries:"Oxygen Therapy (Per Day)"
# =============================================================================
