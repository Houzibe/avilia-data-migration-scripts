import numpy as np

consultations = np.array([
    {"name": "Gastroenterologist (Visiting)", "descr": "", "catid": 36, "source": 83},
    {"name": "Gastroenterology Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Gastroenterology Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "General Consultation Gp", "descr": "", "catid": 36, "source": 83},
    {"name": "General Surgeon (In-House)", "descr": "", "catid": 36, "source": 83},
    {"name": "General Surgeon Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "General Surgeon Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "Gp Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Gp Review \follow up", "descr": "", "catid": 36, "source": 83},
    {"name": "Gynaecology Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Gynaecology Follow Up", "descr": "", "catid": 36, "source": 83},
])

dental_services = np.array([
    {"name": "Gingivectomy", "descr": "", "catid": 50, "source": 83},
    {"name": "Glass Ionomer Cement Or Gic Restoration", "descr": "", "catid": 50, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Gynecological Scan", "descr": "", "catid": 27, "source": 83},
])

family_planning = np.array([
    {"name": "Genital Warts Cauterization", "descr": "", "catid": 44, "source": 83},
])

infusions = np.array([
    {"name": "Gastric Lavage", "descr": "", "catid": 47, "source": 83},
])

laboratory_tests = np.array([
    {"name": "G.I. Section", "descr": "", "catid": 39, "source": 83},
    {"name": "G6Pd", "descr": "", "catid": 39, "source": 83},
    {"name": "Gall Bladder", "descr": "", "catid": 39, "source": 83},
    {"name": "Gamma GT", "descr": "", "catid": 39, "source": 83},
    {"name": "Gastrectomy", "descr": "", "catid": 39, "source": 83},
    {"name": "Gastric Biopsy", "descr": "", "catid": 39, "source": 83},
    {"name": "Genotype Test", "descr": "", "catid": 39, "source": 83},
    {"name": "Genotype/Hb Electrophoresis", "descr": "", "catid": 39, "source": 83},
    {"name": "Glucose Tolerance Test (Gtt)", "descr": "", "catid": 39, "source": 83},
    {"name": "Glycated Haemoglobin (Hba1C)", "descr": "", "catid": 39, "source": 83},
    {"name": "Gram Staining", "descr": "", "catid": 39, "source": 83},
    {"name": "Grouping/Cross-Matching", "descr": "", "catid": 39, "source": 83},
    {"name": "Gxm Negative Blood", "descr": "", "catid": 39, "source": 83},
    {"name": "Gxm Positive Blood", "descr": "", "catid": 39, "source": 83},
])

medical_supplies = np.array([
    {"name": "General Suctioning", "descr": "", "catid": 34, "source": 83},
])

medications = np.array([
    {"name": "G Glutamine Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "G-6-Pd Screening", "descr": "", "catid": 35, "source": 83},
    {"name": "Gabapentin 300Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Gabapentin And Methylcobalamin", "descr": "", "catid": 35, "source": 83},
    {"name": "Gabapentin Cap 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gacrom", "descr": "", "catid": 35, "source": 83},
    {"name": "Galvus 50Mg (Vildagliptin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Galvus Met 50Mg/1000Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Galvus Met 50Mg/1G (Vildagliptin/Metformin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Gamma - Gt", "descr": "", "catid": 35, "source": 83},
    {"name": "Gascol Antacid Suspension", "descr": "", "catid": 35, "source": 83},
    {"name": "Gastric Lavage", "descr": "", "catid": 35, "source": 83},
    {"name": "Gaviscon 200Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Gebenclimide Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Gelusil Antacid", "descr": "", "catid": 35, "source": 83},
    {"name": "Gene Expert", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentamycin 280Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentamycin 280Mg/Amp Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentamycin 80Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentamycin 80Mg/Amp Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentamycin Cream 15G", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentamycin Ear Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentamycin Eye Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentian Violet Tincture", "descr": "", "catid": 35, "source": 83},
    {"name": "Gestid", "descr": "", "catid": 35, "source": 83},
    {"name": "Gestid Susp", "descr": "", "catid": 35, "source": 83},
    {"name": "Gestid Suspension 100Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Gestid Suspension 200Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Gestid Tab (Sachet)", "descr": "", "catid": 35, "source": 83},
    {"name": "Gestone 100Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Gestone 50Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Glass Ionomer Cement", "descr": "", "catid": 35, "source": 83},
    {"name": "Glibenclamide (Daonil) 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Glibenclamide 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Glibenclamide 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Gliclazide 30Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gliclazide 60Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Gliclazide 80Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Glimepiride 2Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Glimepiride 4Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Glimepiride 4Mg (Amaryl)", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucophage 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucophage 500Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucosamine Sulphate Cap", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucovance 500/2.5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Glycerine Borax", "descr": "", "catid": 35, "source": 83},
    {"name": "Glycerine Thymol Mouthwash", "descr": "", "catid": 35, "source": 83},
    {"name": "Glyceryl Trinirate 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Glyceryl Trinitrate 500Mcg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gonal-F 75Iu Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Griseofulvin 125Mg Susp", "descr": "", "catid": 35, "source": 83},
    {"name": "Griseofulvin 125Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Griseofulvin 125Mg/5Ml Suspension", "descr": "", "catid": 35, "source": 83},
    {"name": "Griseofulvin 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Griseofulvin 500Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Gsunate 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gsunate 100Mg Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Gutt Effemoline", "descr": "", "catid": 35, "source": 83},
    {"name": "Gvither", "descr": "", "catid": 35, "source": 83},
    {"name": "Gvither Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Gyno-Trosyd Ovule 300Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gyno-Trosyd Vag Tablet 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gynodaktarin 200Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gynodaktarin 400Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gynodaktarin 400Mg Ovule", "descr": "", "catid": 35, "source": 83},
    {"name": "Gynotrosid 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gynotrosid 300Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gypsona Pop 4", "descr": "", "catid": 35, "source": 83},
    {"name": "Gypsona Pop 6", "descr": "", "catid": 35, "source": 83},
])

others = np.array([
    {"name": "Gastric Lavage", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "Ganglion excision", "descr": "", "catid": 37, "source": 83},
    {"name": "Gastrectomy (Cancer)", "descr": "", "catid": 37, "source": 83},
    {"name": "Gastro-Jejunostomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Gastroduodenoscopy", "descr": "", "catid": 37, "source": 83},
    {"name": "Girdle-Stone Excision Arthroplasty", "descr": "", "catid": 37, "source": 83},
    {"name": "Glaucoma Trabeculectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Granuloma Excision", "descr": "", "catid": 37, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — G
# =============================================================================
# Total records on this sheet : 108
# Categories found            : consultations, dental_services, diagnostic_imaging, family_planning, infusions, laboratory_tests, medical_supplies, medications, others, surgeries
# Duplicates removed          : 5
# Unmapped categories         : None
# =============================================================================
