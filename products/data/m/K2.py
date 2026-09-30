import numpy as np

cancer_care = np.array([
    {"name": "Kytril 3Mg/3Ml", "descr": "", "catid": 42, "source": 83}
])

diagnostic_imaging = np.array([
    {"name": "Knee (Ap Lateral)", "descr": "", "catid": 27, "source": 83},
    {"name": "Knee (Ap Standing) Xray", "descr": "", "catid": 27, "source": 83},
    {"name": "Knee (Both) +Sunrise View", "descr": "", "catid": 27, "source": 83},
    {"name": "Knee (Rosenburg View)", "descr": "", "catid": 27, "source": 83},
    {"name": "Knee (Rosenburg) Xray", "descr": "", "catid": 27, "source": 83},
    {"name": "Knee (Skyline View)", "descr": "", "catid": 27, "source": 83},
    {"name": "Knee (Skyline) Xray", "descr": "", "catid": 27, "source": 83},
    {"name": "Knee CT Plain", "descr": "", "catid": 27, "source": 83},
    {"name": "Knee Joint - Ap & Lat", "descr": "", "catid": 27, "source": 83},
    {"name": "Knee Scan", "descr": "", "catid": 27, "source": 83},
    {"name": "Knee X-Ray", "descr": "", "catid": 27, "source": 83}
])

drugs = np.array([
    {"name": "Kaolin And Morphine Mixture 200mL Susp (Mist Kaolin And Morphine)", "descr": "", "catid": 35, "source": 83},
    {"name": "Kapdap 80 Adult", "descr": "", "catid": 35, "source": 83},
    {"name": "Kemodipine 10mg (Amlodipine)", "descr": "", "catid": 35, "source": 83},
    {"name": "Kenalog", "descr": "", "catid": 35, "source": 83},
    {"name": "Kenalog 40Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Keppra", "descr": "", "catid": 35, "source": 83},
    {"name": "Kerob", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketamine 50mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketamine Inj 10Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketamine Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketesse", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketesse 25mg Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoanalogues/Essential Amino Acids 600mg Tab  (Ketosteril)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoconazole", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoconazole (Drugfield) 2%", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoconazole (Greenzoral)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoconazole (Hovid)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoconazole (Ketazol) Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoconazole (Ketofung)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoconazole (Ketovid) Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoconazole 200Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoconazole 20Mg Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoconazole Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoconazole Shampoo (1 Tube) /Refer", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoconazole Shampoo (Nizoral)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoconazole Tablet 200Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoconazole+Clobetasol+Neomycin G", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketofung Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketonazole Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoprofen", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoprofen (Fastum) Gel", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoprofen (Ketovail)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoprofen 100Mg Cap (Oruvail)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoprofen 100Mg Inj  (Oruvail)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoprofen 100Mg Inj (Oruvail)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoprofen 2.5% (Fastum)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoprofen 200Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoprofen 200Mg (Ketovail)/Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoprofen 200Mg Cap (Oruvail)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoprofen Gel 100G", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoprofen Gel 50G", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketoprofen Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketorolac (Acular)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketotifen (Zaditen)1mg/5mL Syr X300Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketotifen Eye Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketotifen/Gutt", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketotifen1mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketotifen2mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ketotifeneye Drops250mcg/Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Kinbrex Celecoxib Capsules 200Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Klean Prep (Laxative)", "descr": "", "catid": 35, "source": 83},
    {"name": "Klinfast (Clindamycin 100mg And Clotrimazole 200mg Ovule)", "descr": "", "catid": 35, "source": 83},
    {"name": "Klovinal", "descr": "", "catid": 35, "source": 83},
    {"name": "Klovinal  1 X 6 Vaginal Pessaries", "descr": "", "catid": 35, "source": 83},
    {"name": "Klovinal Pessaries", "descr": "", "catid": 35, "source": 83},
    {"name": "Klovinal Pessary", "descr": "", "catid": 35, "source": 83},
    {"name": "Klovinal V Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Klovinal(Metronidazole +Clotrimazole+Lactobacillus Spores Pessaries)", "descr": "", "catid": 35, "source": 83},
    {"name": "Knee Brace", "descr": "", "catid": 35, "source": 83},
    {"name": "Kolestran Toz 4G/9G(Kolestramin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Kombiglyze Tabs 2.5mg/1000Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Kombiglyze Tabs 5mg/1000Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Kombiglyze Xr 5mg/1000Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Kombiglyze Xr 5mg/1000mg (Metformin And Saxagliptin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Kotase", "descr": "", "catid": 35, "source": 83},
    {"name": "Kotase Tab (Bromelin  Crystalline Trypsin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ky Gel", "descr": "", "catid": 35, "source": 83},
    {"name": "Ky Jelly", "descr": "", "catid": 35, "source": 83}
])

laboratory_tests = np.array([
    {"name": "Kappa Free Light Chain", "descr": "", "catid": 39, "source": 83},
    {"name": "Kappa Light Chain", "descr": "", "catid": 39, "source": 83},
    {"name": "Ketamine", "descr": "", "catid": 39, "source": 83},
    {"name": "Kidney Function Test", "descr": "", "catid": 39, "source": 83},
    {"name": "Kidney Stone Analysis", "descr": "", "catid": 39, "source": 83},
    {"name": "KOH", "descr": "", "catid": 39, "source": 83}
])

medical_supplies = np.array([
    {"name": "K-Y Jelly", "descr": "", "catid": 34, "source": 83}
])

others = np.array([
    {"name": "Keloid Excision (Major)", "descr": "", "catid": 48, "source": 83},
    {"name": "Keloid Excision (Minor)", "descr": "", "catid": 48, "source": 83},
    {"name": "Keloid Excision (Moderate)", "descr": "", "catid": 48, "source": 83},
    {"name": "Keloid Excision I", "descr": "", "catid": 48, "source": 83},
    {"name": "Keloid Excision Ii", "descr": "", "catid": 48, "source": 83},
    {"name": "KELOID EXCISION Ill", "descr": "", "catid": 48, "source": 83},
    {"name": "Kinesio-Taping", "descr": "", "catid": 48, "source": 83},
    {"name": "Knee Arthrotomy", "descr": "", "catid": 48, "source": 83},
    {"name": "Knee Surgery (Arthrotomy)", "descr": "", "catid": 48, "source": 83},
    {"name": "Kyphoplasty", "descr": "", "catid": 48, "source": 83}
])

physiotherapy = np.array([
    {"name": "Knee Ligament Sprains", "descr": "", "catid": 40, "source": 83},
    {"name": "Kyphosis", "descr": "", "catid": 40, "source": 83}
])

surgeries = np.array([
    {"name": "Kelloid Excision", "descr": "", "catid": 37, "source": 83},
    {"name": "Knee Effusion Tap", "descr": "", "catid": 37, "source": 83}
])

# =============================================================================
# SHEET SUMMARY — Product K
# =============================================================================
# Total records on this sheet : 101
# Categories found            : cancer_care, diagnostic_imaging, drugs, laboratory_tests, medical_supplies, others, physiotherapy, surgeries
# Unmapped categories         : None
# =============================================================================
