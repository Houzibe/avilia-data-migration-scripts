import numpy as np

consultations = np.array([
    {"name": "Internal Medicine Physician Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Internal Medicine Physician Review", "descr": "", "catid": 36, "source": 83},
    {"name": "International Medical Report", "descr": "", "catid": 36, "source": 83},
])

dental_services = np.array([
    {"name": "Incision And Drainage Of Dental Abscesses", "descr": "", "catid": 50, "source": 83},
    {"name": "Intermaxillary Fixation", "descr": "", "catid": 50, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Image Reporting Only", "descr": "", "catid": 27, "source": 83},
    {"name": "Inter-Maxillary Fixation (For Weight Loss)", "descr": "", "catid": 27, "source": 83},
    {"name": "Intravenous Urograms (Ivu)", "descr": "", "catid": 27, "source": 83},
])

family_planning = np.array([
    {"name": "Implant Insertion (Excluding Drug)", "descr": "", "catid": 44, "source": 83},
    {"name": "Implant Insertion (Including Medication)", "descr": "", "catid": 44, "source": 83},
    {"name": "Implant Removal  (Uncomplicated)", "descr": "", "catid": 44, "source": 83},
    {"name": "Iucd Insertion (Excluding Drug)", "descr": "", "catid": 44, "source": 83},
    {"name": "Iucd Insertion Including Drugs - Copper T", "descr": "", "catid": 44, "source": 83},
])

infusions = np.array([
    {"name": "Infusion Tray", "descr": "", "catid": 47, "source": 83},
    {"name": "Intraosseous Infusion", "descr": "", "catid": 47, "source": 83},
])

laboratory_tests = np.array([
    {"name": "IgA", "descr": "", "catid": 39, "source": 83},
    {"name": "IgE", "descr": "", "catid": 39, "source": 83},
    {"name": "IgG", "descr": "", "catid": 39, "source": 83},
    {"name": "Igg, Igm, Iga", "descr": "", "catid": 39, "source": 83},
    {"name": "Igg, Igm, Iga , Ige (Each)", "descr": "", "catid": 39, "source": 83},
    {"name": "IgM", "descr": "", "catid": 39, "source": 83},
    {"name": "Immunohistochemistry", "descr": "", "catid": 39, "source": 83},
    {"name": "Immunohistochemistry per Stain", "descr": "", "catid": 39, "source": 83},
    {"name": "Influenza A & B", "descr": "", "catid": 39, "source": 83},
    {"name": "Inhibin A", "descr": "", "catid": 39, "source": 83},
    {"name": "Inhibin B", "descr": "", "catid": 39, "source": 83},
    {"name": "Inorganic Phosphate", "descr": "", "catid": 39, "source": 83},
    {"name": "Inorganic Phosphorus", "descr": "", "catid": 39, "source": 83},
    {"name": "Insulin", "descr": "", "catid": 39, "source": 83},
    {"name": "Insulin (F)", "descr": "", "catid": 39, "source": 83},
    {"name": "Insulin (PP)", "descr": "", "catid": 39, "source": 83},
    {"name": "Insulin Fasting", "descr": "", "catid": 39, "source": 83},
    {"name": "Insulin Resistance test", "descr": "", "catid": 39, "source": 83},
    {"name": "Insulin/ Glucose Ratio", "descr": "", "catid": 39, "source": 83},
    {"name": "Intact Pth", "descr": "", "catid": 39, "source": 83},
    {"name": "Intravenous Cholangiogram (Ptc)", "descr": "", "catid": 39, "source": 83},
    {"name": "Intravenous Pyelo-Urogram (Ivu)", "descr": "", "catid": 39, "source": 83},
    {"name": "Invertebral Disc", "descr": "", "catid": 39, "source": 83},
    {"name": "Iron", "descr": "", "catid": 39, "source": 83},
    {"name": "Iso Titre", "descr": "", "catid": 39, "source": 83},
    {"name": "Isolation Of Organism To Spp Level", "descr": "", "catid": 39, "source": 83},
    {"name": "Ivu For Bph", "descr": "", "catid": 39, "source": 83},
])

medical_devices = np.array([
    {"name": "Incubator", "descr": "", "catid": 29, "source": 83},
    {"name": "Infusion Pump", "descr": "", "catid": 29, "source": 83},
    {"name": "Inplanon", "descr": "", "catid": 29, "source": 83},
])

medications = np.array([
    {"name": "Ibuprofen 100Mg Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen 200Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen 200Mg Tab-Sachet", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen 400Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen Syrup 100Mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen Tab 400Mg (Sachet)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ikaclomin 50Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Imatinib 400Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Imipramine Hydrochloride 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Imipramine Hydrochloride 25Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Imipramine Hydrochloride 50Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Immunace", "descr": "", "catid": 35, "source": 83},
    {"name": "Immunace Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Imodium 4Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Imodium Cap 2Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Indapamide 1.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Inderal 40Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Inderal 40Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Indomethacin 25Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Indomethacine Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Injection Amikacin 500Mg/2Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Injection Pentazocine", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulatard Hm 100Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulatard Hm 40Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulatard Hm Penfil 100Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulatard Penfil", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulatard Vial 100Iu/Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulatard Vial 40Iu/Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin (Isophane) Injection 100 Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Lente 40Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Lente Inj 100Iu/Ml 10Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Lente Inj 40Iu/Ml 10Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Lentel 40I.U/Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Soluble Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Syringe 100 Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Syringe 40 Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Syringes 100Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Syringes 40Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Zinc Suspension (Izs) Inj 100 Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Zinc Suspension (Izs) Inj 40 Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Interflox 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Interflox Cap 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Intrasite Gel 15G", "descr": "", "catid": 35, "source": 83},
    {"name": "Irbesartan 150Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Irbesartan 300Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Iron Dextran", "descr": "", "catid": 35, "source": 83},
    {"name": "Iron Dextran Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Ironoglobin Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoniazid 300Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoniazid 300Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoniazid Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoniazid Syrup 120Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoplasma 500Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Isopto Carpine 4% Eye Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoptocarpine 4% Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Isordil 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Isordil 10Mg Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Isordil 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Isordil 5Mg Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Isordil Tab 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Itraconazole", "descr": "", "catid": 35, "source": 83},
    {"name": "Itraconazole 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Itraconazole Susp 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Itranox 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Itranox 100Mg Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Iv Chloramphenicol", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivermectin 3Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivf-C 5000Iu Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivf-M 75Iu Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivychrom Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivycrom Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivymiocelle Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivysine Eye Drop 10Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivytimol Eye Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivyzoxan Eye/Ear Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Ixime 400Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ixime Suspension 75Ml", "descr": "", "catid": 35, "source": 83},
])

others = np.array([
    {"name": "I & D (Minor)", "descr": "", "catid": 48, "source": 83},
    {"name": "I & D Major", "descr": "", "catid": 48, "source": 83},
    {"name": "Incubator care per", "descr": "", "catid": 48, "source": 83},
    {"name": "Infusion Giving Set", "descr": "", "catid": 48, "source": 83},
    {"name": "Insulin Needle", "descr": "", "catid": 48, "source": 83},
    {"name": "Iv Canula", "descr": "", "catid": 48, "source": 83},
])

reproductive_health = np.array([
    {"name": "Induction/Augmentation of Labour", "descr": "", "catid": 32, "source": 83},
])

surgeries = np.array([
    {"name": "I.M Injection Daily", "descr": "", "catid": 37, "source": 83},
    {"name": "Icu Care/ Day", "descr": "", "catid": 37, "source": 83},
    {"name": "Incision & Drainage For Big Abscess (For Procedure Only Under Ga)", "descr": "", "catid": 37, "source": 83},
    {"name": "Incision & Drainage For Big Abscess (For Procedure Only Under La)", "descr": "", "catid": 37, "source": 83},
    {"name": "Incision & Drainage For Small Abscess (For Procedure Only Under La)", "descr": "", "catid": 37, "source": 83},
    {"name": "Incision And Drainage", "descr": "", "catid": 37, "source": 83},
    {"name": "Incision And Drainage (Orthopaedics)", "descr": "", "catid": 37, "source": 83},
    {"name": "Incision And Drainage Of Abscess", "descr": "", "catid": 37, "source": 83},
    {"name": "Incisional Biopsy", "descr": "", "catid": 37, "source": 83},
    {"name": "Incisional Herniorrhaphy", "descr": "", "catid": 37, "source": 83},
    {"name": "Incubator Care/ Day", "descr": "", "catid": 37, "source": 83},
    {"name": "Indirect Laryngoscopy", "descr": "", "catid": 37, "source": 83},
    {"name": "Induction Of Labour (Where Applicable)", "descr": "", "catid": 37, "source": 83},
    {"name": "Induction Of Labour Package", "descr": "", "catid": 37, "source": 83},
    {"name": "Inguinal Hernia Repair Without Mesh (Bilateral)", "descr": "", "catid": 37, "source": 83},
    {"name": "Inguinal Hernia Repair Without Mesh (Unilateral)", "descr": "", "catid": 37, "source": 83},
    {"name": "Inguinal Herniorrhaphy", "descr": "", "catid": 37, "source": 83},
    {"name": "Inguinal Orchidectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Initial Acrylic Denture (Initial)", "descr": "", "catid": 37, "source": 83},
    {"name": "Initial Acrylic Denture Additional Tooth)", "descr": "", "catid": 37, "source": 83},
    {"name": "Intensive Care Unit (Icu)", "descr": "", "catid": 37, "source": 83},
    {"name": "Intensive Neonatal Resuscitation", "descr": "", "catid": 37, "source": 83},
    {"name": "Interlocked Intramedullary Nail", "descr": "", "catid": 37, "source": 83},
    {"name": "Intestinal Obstruction with Resection", "descr": "", "catid": 37, "source": 83},
    {"name": "Intestinal Obstruction without Resection", "descr": "", "catid": 37, "source": 83},
    {"name": "Intra-Abdominal Abscess, Drainage, Delayed Closure", "descr": "", "catid": 37, "source": 83},
    {"name": "Intra-Articular Injection", "descr": "", "catid": 37, "source": 83},
    {"name": "Intra-Lesional Injection", "descr": "", "catid": 37, "source": 83},
    {"name": "Intralesional Injection Of Steroids", "descr": "", "catid": 37, "source": 83},
    {"name": "Intralesional Injection Under Image Intensifier", "descr": "", "catid": 37, "source": 83},
    {"name": "Intraocular Lens Implantation", "descr": "", "catid": 37, "source": 83},
    {"name": "Iucd Removal", "descr": "", "catid": 37, "source": 83},
])

vaccines = np.array([
    {"name": "Immunization Certificate", "descr": "", "catid": 46, "source": 83},
    {"name": "IPV", "descr": "", "catid": 46, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — I
# =============================================================================
# Total records on this sheet : 163
# Categories found            : consultations, dental_services, diagnostic_imaging, family_planning, infusions, laboratory_tests, medical_devices, medications, others, reproductive_health, surgeries, vaccines
# Duplicates removed          : 4
# Unmapped categories         : None
# =============================================================================
