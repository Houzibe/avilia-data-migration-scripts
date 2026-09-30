import numpy as np

consultations = np.array([
    {"name": "Internal Medicine Physician Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Internal Medicine Physician Review", "descr": "", "catid": 36, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Intravenous Cholangiogram", "descr": "", "catid": 27, "source": 83},
    {"name": "Intravenous Urography [Ivu]", "descr": "", "catid": 27, "source": 83},
    {"name": "IV Cholangiogram", "descr": "", "catid": 27, "source": 83},
    {"name": "IVU", "descr": "", "catid": 27, "source": 83},
])

infusions = np.array([
    {"name": "Induction Drip", "descr": "", "catid": 47, "source": 83},
])

laboratory_tests = np.array([
    {"name": "Indirect Comb’S Test", "descr": "", "catid": 39, "source": 83},
    {"name": "Inorganic Phosphate", "descr": "", "catid": 39, "source": 83},
    {"name": "Inorganic Phosphorus", "descr": "", "catid": 39, "source": 83},
    {"name": "INR Test", "descr": "", "catid": 39, "source": 83},
    {"name": "Iron*", "descr": "", "catid": 39, "source": 83},
    {"name": "IV Contrast (Additional)", "descr": "", "catid": 39, "source": 83},
])

medical_devices = np.array([
    {"name": "Invincible Bifocal", "descr": "", "catid": 29, "source": 83},
    {"name": "Invisible Bifocal Photo/ARC", "descr": "", "catid": 29, "source": 83},
    {"name": "Invisible Bifocal White", "descr": "", "catid": 29, "source": 83},
])

medical_supplies = np.array([
    {"name": "Insulin Pen Needle", "descr": "", "catid": 34, "source": 83},
    {"name": "Insulin Syringe 100Iu", "descr": "", "catid": 34, "source": 83},
    {"name": "IV Canular", "descr": "", "catid": 34, "source": 83},
])

medications = np.array([
    {"name": "Ibuporfen", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen 200Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen 400Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen Syrup 100Ml/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Imipramine", "descr": "", "catid": 35, "source": 83},
    {"name": "Immodium (Loperamide)", "descr": "", "catid": 35, "source": 83},
    {"name": "Immunace Capsules", "descr": "", "catid": 35, "source": 83},
    {"name": "Imodium", "descr": "", "catid": 35, "source": 83},
    {"name": "Imodium Cap 4Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Indapamide 2.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Inderal 40Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Inderal Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Indomethacin Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Infacol Suspension", "descr": "", "catid": 35, "source": 83},
    {"name": "Infusion Set", "descr": "", "catid": 35, "source": 83},
    {"name": "Instaclop", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulatard Hm 100Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulatard Hm 40Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulatard Hm Penfil 100Iu", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulatard Penfill", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulatard Vial 100Iu/Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulatard Vial 40Iu/Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin (Humulin) 70/30 (10Ml)", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Glargine (Lantus)", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Human]Actrapid Soluble For IV Use", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Lente (Soluble)", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Lente Inj 100Iu/Ml 10Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Lente Inj 40Iu/Ml 10Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Novomix Penfill", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Penfill 70/30 (Insuman Comb3)", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Soluble", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Solule(Insuman Rapid)", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Zinc Suspension (I.Z.S)", "descr": "", "catid": 35, "source": 83},
    {"name": "Ipratropium Bromide", "descr": "", "catid": 35, "source": 83},
    {"name": "Iron Dextran 2Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Iron Sucrose", "descr": "", "catid": 35, "source": 83},
    {"name": "Ironoglobin Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoniazid (Inh)", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoniazid 300Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoniazid Syrup 120Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Isophane Insulin", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoplasma", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoptocarpine 4% Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Isordil 10Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Isordil 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Isosorbide Mononitrate Xl- 60Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Itraconazole", "descr": "", "catid": 35, "source": 83},
    {"name": "Itraconazole Capsule", "descr": "", "catid": 35, "source": 83},
    {"name": "Itranox 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivermectin", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivycrom", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivyflur", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivysine Eyedrop", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivysolone Opthalmic Susp", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivytimol Eye Drop 0.5% 5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivyzinc", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivyzozan Eye/Ear Drop 5Ml", "descr": "", "catid": 35, "source": 83},
])

others = np.array([
    {"name": "Indirect Ophthalmoscopy", "descr": "", "catid": 48, "source": 83},
    {"name": "Intra Ocular Pressure (IOP)/ Tonometry", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "I &D Of Mastoid Abscess", "descr": "", "catid": 37, "source": 83},
    {"name": "I.D.", "descr": "", "catid": 37, "source": 83},
    {"name": "ICU Care/Day", "descr": "", "catid": 37, "source": 83},
    {"name": "Ileostomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Ileostomy Pouch Revison", "descr": "", "catid": 37, "source": 83},
    {"name": "Ilieo Sigmoidostomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Immunization", "descr": "", "catid": 37, "source": 83},
    {"name": "Implanon (Insertion)", "descr": "", "catid": 37, "source": 83},
    {"name": "In-Growing Toe Nail ( Excision )", "descr": "", "catid": 37, "source": 83},
    {"name": "In-Growing Toe Nail Removal", "descr": "", "catid": 37, "source": 83},
    {"name": "Incision And Drainage", "descr": "", "catid": 37, "source": 83},
    {"name": "Incision And Drainage Of Abscess", "descr": "", "catid": 37, "source": 83},
    {"name": "Incontinence", "descr": "", "catid": 37, "source": 83},
    {"name": "Incubator Care (Per Day)", "descr": "", "catid": 37, "source": 83},
    {"name": "Indirect", "descr": "", "catid": 37, "source": 83},
    {"name": "Indirect Laryngonoscopy", "descr": "", "catid": 37, "source": 83},
    {"name": "Induction Of Labor/Augmentation", "descr": "", "catid": 37, "source": 83},
    {"name": "Induction Of Labour [Including Medications]", "descr": "", "catid": 37, "source": 83},
    {"name": "Infected Bunion Foot - Excision", "descr": "", "catid": 37, "source": 83},
    {"name": "Ingrown Toe Nail (Block Fee)", "descr": "", "catid": 37, "source": 83},
    {"name": "Inguinal Node (Bulk Dissection) Axial", "descr": "", "catid": 37, "source": 83},
    {"name": "Injection Sclerotherapy", "descr": "", "catid": 37, "source": 83},
    {"name": "Injection Sclerotherapy Of Varicose Veins (Minor)", "descr": "", "catid": 37, "source": 83},
    {"name": "Injection Trauma/Palsy Per Visit", "descr": "", "catid": 37, "source": 83},
    {"name": "Instestinal Perforation", "descr": "", "catid": 37, "source": 83},
    {"name": "Instrumental Delivery [Vacuum Extraction,Forceps]", "descr": "", "catid": 37, "source": 83},
    {"name": "Intercostals Drainage Insertion", "descr": "", "catid": 37, "source": 83},
    {"name": "Intercostalsdrainage Insertion (Thorascostomy)", "descr": "", "catid": 37, "source": 83},
    {"name": "Intermediate", "descr": "", "catid": 37, "source": 83},
    {"name": "Intermediate Anesthetist Fee", "descr": "", "catid": 37, "source": 83},
    {"name": "Intermediate Theatre Use", "descr": "", "catid": 37, "source": 83},
    {"name": "Internal Auditory Meatus Surgery", "descr": "", "catid": 37, "source": 83},
    {"name": "Intestinal Obstruction", "descr": "", "catid": 37, "source": 83},
    {"name": "Intestinal Obstruction With Resection", "descr": "", "catid": 37, "source": 83},
    {"name": "Intestinal Obstruction Without Resection", "descr": "", "catid": 37, "source": 83},
    {"name": "Intestinal Perforation (Resection Anastomosis)", "descr": "", "catid": 37, "source": 83},
    {"name": "Intra –Articular Injection Excluding The Drug", "descr": "", "catid": 37, "source": 83},
    {"name": "Intra-Articular Injection Procedure", "descr": "", "catid": 37, "source": 83},
    {"name": "Intranasal Anthrosmy", "descr": "", "catid": 37, "source": 83},
    {"name": "Intranasal Ethmoidectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Intraocular Foreign Body Removal", "descr": "", "catid": 37, "source": 83},
    {"name": "Intussusception Operation", "descr": "", "catid": 37, "source": 83},
    {"name": "IUCD Insertion [Includes Device]", "descr": "", "catid": 37, "source": 83},
    {"name": "IUCD Removal", "descr": "", "catid": 37, "source": 83},
    {"name": "IUD (Insertion)", "descr": "", "catid": 37, "source": 83},
    {"name": "IUD Removal", "descr": "", "catid": 37, "source": 83},
])

vaccines = np.array([
    {"name": "Injectable Poliomyelitis Vaccine (IPV)", "descr": "", "catid": 46, "source": 83},
    {"name": "Ipv (Injectable Polio Vaccine)", "descr": "", "catid": 46, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — Product I
# =============================================================================
# Total records on this sheet : 127
# Categories found            : consultations, diagnostic_imaging, infusions, laboratory_tests, medical_devices, medical_supplies, medications, others, surgeries, vaccines
# Unmapped categories         : None
# Duplicates removed          : medications:"Itraconazole"
# =============================================================================
