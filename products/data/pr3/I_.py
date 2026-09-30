import numpy as np

"""
consultations = np.array([
    {"name": "Infection Control Specialist Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Insertion Of Eliora + Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Insertion Of Mirena+Consultation", "descr": "", "catid": 36, "source": 83},
])


diagnostic_imaging = np.array([
    {"name": "Intravenous Cholangiogram (PTC)", "descr": "", "catid": 27, "source": 83},
    {"name": "Intravenous Pyelo-Urogram (IVU)", "descr": "", "catid": 27, "source": 83},
    {"name": "IV Cholangiogram", "descr": "", "catid": 27, "source": 83},
    {"name": "IVU", "descr": "", "catid": 27, "source": 83},
    {"name": "IVU For Bph", "descr": "", "catid": 27, "source": 83},
])


infusions = np.array([
    {"name": "Infusion - 5% Dextrose/Normal Saline 500 ML = 1 Unit", "descr": "", "catid": 47, "source": 83},
    {"name": "Infusion - Normal Saline Solution 1000 Cc", "descr": "", "catid": 47, "source": 83},
    {"name": "Infusion Set", "descr": "", "catid": 47, "source": 83},
    {"name": "Intralipid Infusion", "descr": "", "catid": 47, "source": 83},
    {"name": "Isoplasma", "descr": "", "catid": 47, "source": 83},
])


laboratory_tests = np.array([
    {"name": "Indirect Coomb'S Test", "descr": "", "catid": 39, "source": 83},
    {"name": "Inf. Mononucleosis", "descr": "", "catid": 39, "source": 83},
    {"name": "Influenza A & B", "descr": "", "catid": 39, "source": 83},
    {"name": "Inorganic Phosphorus", "descr": "", "catid": 39, "source": 83},
    {"name": "INR Test", "descr": "", "catid": 39, "source": 83},
    {"name": "Iron", "descr": "", "catid": 39, "source": 83},
])


medical_supplies = np.array([
    {"name": "Infusion Giving Set", "descr": "", "catid": 34, "source": 83},
    {"name": "Insulin Syringe", "descr": "", "catid": 34, "source": 83},
    {"name": "Insulin Syringe 100Iu", "descr": "", "catid": 34, "source": 83},
    {"name": "Insulin Syringe-40Iu", "descr": "", "catid": 34, "source": 83},
    {"name": "Intrasite Gel", "descr": "", "catid": 34, "source": 83},
    {"name": "IV Cannula Size14G,16G,18G,20G-23G,25G", "descr": "", "catid": 34, "source": 83},
    {"name": "IV Giving Set", "descr": "", "catid": 34, "source": 83},
])


medications = np.array([
    {"name": "Ibex", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen 100Mg Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen 200Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen 200Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen 400Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen 400Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen Syrup (Brustan – N)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen Syrup 100Mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen Tab 400Mg (Sachet)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ikaclomin 50Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Imodium 2Mg Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Imodium Cap 4Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Indapamide 1.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Indapamide 1.5Mg By 28", "descr": "", "catid": 35, "source": 83},
    {"name": "Indapamide 2.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Indapamide 2.5Mg Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Indapamide Sr 1.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Indapamide Sr Tab 1.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Indapamide Sr Tab 1.5Mg X 30", "descr": "", "catid": 35, "source": 83},
    {"name": "Indapamine Tabs 2.5Mg X 28", "descr": "", "catid": 35, "source": 83},
    {"name": "Inderal 40Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Indomethacine Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Inf Linezolid", "descr": "", "catid": 35, "source": 83},
    {"name": "Inf Moxifloxacin 400Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Infacol", "descr": "", "catid": 35, "source": 83},
    {"name": "Inj Polymycin 500000Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulatard", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulatard Penfill 100 IU/ML", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Lentel 40I.U/ML", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Mixtard 30/70 Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Soluble Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin; Free", "descr": "", "catid": 35, "source": 83},
    {"name": "Insuman Combo", "descr": "", "catid": 35, "source": 83},
    {"name": "Interflox Cap 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Iodine Solution", "descr": "", "catid": 35, "source": 83},
    {"name": "Ipratopium Bromide Nebules", "descr": "", "catid": 35, "source": 83},
    {"name": "Ipratropium 250Mcg Nebules", "descr": "", "catid": 35, "source": 83},
    {"name": "Ipratropium 500Mcg Nebules", "descr": "", "catid": 35, "source": 83},
    {"name": "Ipratropium Bromide Inhaler", "descr": "", "catid": 35, "source": 83},
    {"name": "Ipratropium Inhaler", "descr": "", "catid": 35, "source": 83},
    {"name": "Irbesartan 150Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Irbesartan 150Mg Tab (Aprovel)", "descr": "", "catid": 35, "source": 83},
    {"name": "Irbesartan 300Mg Tab (Aprovel)", "descr": "", "catid": 35, "source": 83},
    {"name": "Iron Sucrose 100Mg Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoniazid 150Mg Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoniazid 300Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoniazid 300Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoniazid Syrup 120Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoniazide", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoptocarpine 4% Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Isordil 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Isordil 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Isordil Tab 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Isorsobide Dinitrate Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Isosorbide Dinitratetablet10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Isosorbide Dinitratetabletoralsublingual 5 MG", "descr": "", "catid": 35, "source": 83},
"""
medications = np.array([    
    {"name": "Itraconazole 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Itraconazole 100Mg Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Itranox 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "IUCD", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivermectin 3Mg (Mectizan 3Mg)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivermectin 3Mg Tab (Mectizan)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivycrom Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivymectin 3Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivyzoxan Eye/Ear Drop 5Ml", "descr": "", "catid": 35, "source": 83},
])


nutritionals = np.array([
    {"name": "Immunace Capsule", "descr": "", "catid": 33, "source": 83},
])


others = np.array([
    {"name": "ICU Care/Day Neonate", "descr": "", "catid": 48, "source": 83},
    {"name": "Incubator Care", "descr": "", "catid": 48, "source": 83},
    {"name": "Initial Speech Assessment", "descr": "", "catid": 48, "source": 83},
    {"name": "Intensive Care (ICU)", "descr": "", "catid": 48, "source": 83},
])


surgeries = np.array([
    {"name": "Ileostomy Pouch Revision", "descr": "", "catid": 37, "source": 83},
    {"name": "Implanon", "descr": "", "catid": 37, "source": 83},
    {"name": "In-Growing Toe Nail Excision", "descr": "", "catid": 37, "source": 83},
    {"name": "Incision And Drainage", "descr": "", "catid": 37, "source": 83},
    {"name": "Incision And Drainage (I & D)", "descr": "", "catid": 37, "source": 83},
    {"name": "Incubator Care/Day", "descr": "", "catid": 37, "source": 83},
    {"name": "Indirect Laryngoscopy", "descr": "", "catid": 37, "source": 83},
    {"name": "Induction Of Labour", "descr": "", "catid": 37, "source": 83},
    {"name": "Ingrown Toe Nail", "descr": "", "catid": 37, "source": 83},
    {"name": "Initial Resuscitation", "descr": "", "catid": 37, "source": 83},
    {"name": "Injection Sclerotherapy", "descr": "", "catid": 37, "source": 83},
    {"name": "Insertion Of Pessaries", "descr": "", "catid": 37, "source": 83},
    {"name": "Intenal Iliac Vessel Ligation", "descr": "", "catid": 37, "source": 83},
    {"name": "Intercostal Drainage Insertion", "descr": "", "catid": 37, "source": 83},
    {"name": "Intercostal Drainage Insertion (Thoracostomy)", "descr": "", "catid": 37, "source": 83},
    {"name": "Intermediate", "descr": "", "catid": 37, "source": 83},
    {"name": "Internal Auditory Meatus Surgery", "descr": "", "catid": 37, "source": 83},
    {"name": "Internal Drainage Of Pancreatic Cyst", "descr": "", "catid": 37, "source": 83},
    {"name": "Intestinal Obstruction", "descr": "", "catid": 37, "source": 83},
    {"name": "Intestinal Obstruction Repair With Resection", "descr": "", "catid": 37, "source": 83},
    {"name": "Intestinal Obstruction Repair Without Resection", "descr": "", "catid": 37, "source": 83},
    {"name": "Intestinal Obstruction With Resection", "descr": "", "catid": 37, "source": 83},
    {"name": "Intestinal Obstruction Without Resection", "descr": "", "catid": 37, "source": 83},
    {"name": "Intra-Abdominal Abscess, Drainage, Delayed Closure", "descr": "", "catid": 37, "source": 83},
    {"name": "Intra-Articular Injection Excluding The Drug", "descr": "", "catid": 37, "source": 83},
    {"name": "Intraleisonal Infiltration Of Kenalog", "descr": "", "catid": 37, "source": 83},
    {"name": "IUCD Insertion", "descr": "", "catid": 37, "source": 83},
    {"name": "IUCD Insertion + Device", "descr": "", "catid": 37, "source": 83},
    {"name": "IUCD Removal", "descr": "", "catid": 37, "source": 83},
])


vaccines = np.array([
    {"name": "Influenza - Vaxigrip Tetra (1 Dose Syringe)", "descr": "", "catid": 46, "source": 83},
    {"name": "IPV", "descr": "", "catid": 46, "source": 83},
])


# =============================================================================
# SHEET SUMMARY — Product I
# =============================================================================
# Total records on this sheet : 127
# Categories found            : consultations, diagnostic_imaging, infusions, laboratory_tests, medical_supplies, medications, nutritionals, others, surgeries, vaccines
# Duplicates removed          : 0
# Unmapped categories         : None
# =============================================================================
