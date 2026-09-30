import numpy as np

consultations = np.array([
    {"name": "Gastroenterology Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Gastroenterology Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "General Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "General Consultation Follow-Up", "descr": "", "catid": 36, "source": 83},
    {"name": "General Surgeon Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "General Surgeon Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "GP Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "GP Initial Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "GP Review \Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "Gynaecology Consultation", "descr": "", "catid": 36, "source": 83},
    {"name": "Gynaecology Follow Up", "descr": "", "catid": 36, "source": 83},
])

infusions = np.array([
    {"name": "Glucose (Dextrose)", "descr": "", "catid": 47, "source": 83},
    {"name": "Glucose + Sodium Chloride (Paediatric)", "descr": "", "catid": 47, "source": 83},
])

laboratory_tests = np.array([
    {"name": "G-6-PD Deficiency", "descr": "", "catid": 39, "source": 83},
    {"name": "G-6-Pd Screening", "descr": "", "catid": 39, "source": 83},
    {"name": "Gamma Gt", "descr": "", "catid": 39, "source": 83},
    {"name": "Genotype", "descr": "", "catid": 39, "source": 83},
    {"name": "Globulin", "descr": "", "catid": 39, "source": 83},
    {"name": "Glucose Tolerance Test", "descr": "", "catid": 39, "source": 83},
    {"name": "Glycated Hb", "descr": "", "catid": 39, "source": 83},
    {"name": "Glycocylated Heamoglobin", "descr": "", "catid": 39, "source": 83},
    {"name": "Grouping & Cross Matching", "descr": "", "catid": 39, "source": 83},
])

medical_devices = np.array([
    {"name": "Glasses ( Lenses & Frames) Note (Provision Of Lenses Once In Two Years)", "descr": "", "catid": 29, "source": 83},
])

medical_supplies = np.array([
    {"name": "Giving Set", "descr": "", "catid": 34, "source": 83},
])

medications = np.array([
    {"name": "Gabapentin + Methylcobalamin", "descr": "", "catid": 35, "source": 83},
    {"name": "Gabapentin 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gabapentin 300Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gabapentin 300Mg & Methylcobalamin 500Mg(Biopentin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Galvus 50Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Galvus Met 1000/50Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Galvus Met 850/50Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gascol Susp", "descr": "", "catid": 35, "source": 83},
    {"name": "Gaviscon Sspension", "descr": "", "catid": 35, "source": 83},
    {"name": "Gelusil", "descr": "", "catid": 35, "source": 83},
    {"name": "Gelusil Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentamicin", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentamycin", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentamycin 280Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentamycin 80Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentamycin Cream 15G", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentamycin Ear/Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Gentian Violet", "descr": "", "catid": 35, "source": 83},
    {"name": "Genticin 160Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Genticin 80Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Genticin Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Gestid 100Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Gestid 200Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Gestid Suspension 100Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Gestid Suspension 200Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Gestid Tab (Satchet)", "descr": "", "catid": 35, "source": 83},
    {"name": "Gestone 100Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Gestone 50Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Glanil (Daoni I.) 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Glemax 3Mg (Glimepiride)", "descr": "", "catid": 35, "source": 83},
    {"name": "Glemax 4Mg (Glimepiride)", "descr": "", "catid": 35, "source": 83},
    {"name": "Glibenclamide", "descr": "", "catid": 35, "source": 83},
    {"name": "Glibenclamide 5Mgtabs (Daonil)", "descr": "", "catid": 35, "source": 83},
    {"name": "Gliclazide", "descr": "", "catid": 35, "source": 83},
    {"name": "Glimepiride", "descr": "", "catid": 35, "source": 83},
    {"name": "Glimepiride 1Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Glimepiride 2Mg Tabs(Amaryl)", "descr": "", "catid": 35, "source": 83},
    {"name": "Glimepiride 4Mg(Amaryl)", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucobay (Acarbose )100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucobay (Acarbose) 50Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucobay 100Mg (Acarbose)", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucobay 50Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucophage", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucophage 500Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucophage 850Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucophage Sr 500Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucophage Tablet 1G", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucophage Tabs 500Mg (Branded)", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucovance 500/2.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucovance 500/5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Glucovance(Glucophage500Mg +Gibenclamide5Mgtab", "descr": "", "catid": 35, "source": 83},
    {"name": "Glycerin Supp. Adult", "descr": "", "catid": 35, "source": 83},
    {"name": "Glycerin Supp. Infant", "descr": "", "catid": 35, "source": 83},
    {"name": "Glycerin Thymol", "descr": "", "catid": 35, "source": 83},
    {"name": "Glycerine Borax", "descr": "", "catid": 35, "source": 83},
    {"name": "Glycerine Trinitrate 5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Glyceryl Trinitrate", "descr": "", "catid": 35, "source": 83},
    {"name": "Glyceryl Trinitrate Spray N-Glysol", "descr": "", "catid": 35, "source": 83},
    {"name": "Glyceryl Trinitrate Tab 500Mcg(0.5Mg)", "descr": "", "catid": 35, "source": 83},
    {"name": "Granisetron (Branded) Kytril", "descr": "", "catid": 35, "source": 83},
    {"name": "Griseofulvin", "descr": "", "catid": 35, "source": 83},
    {"name": "Griseofulvin (Fulcin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Griseofulvin 125Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Griseofulvin 500Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Gvither Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Gynamead (Canesteen) Vag Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Gynastatum", "descr": "", "catid": 35, "source": 83},
    {"name": "Gyno- Tiocosid Vaginal Tablet(Tioconazole100Mg)", "descr": "", "catid": 35, "source": 83},
    {"name": "Gyno-Betnosil Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Gyno-Betnosil Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Gyno-Trosyd 300Mg Ovule", "descr": "", "catid": 35, "source": 83},
    {"name": "Gynocare Pessary", "descr": "", "catid": 35, "source": 83},
    {"name": "Gynodactarin 40G Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Gynodactarin Vaginal Tab 200Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gynodactarin Vaginal Tab 400Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Gynoral Kit", "descr": "", "catid": 35, "source": 83},
    {"name": "Gynotrosyd 100Mg Ovule", "descr": "", "catid": 35, "source": 83},
])

others = np.array([
    {"name": "General Feeding/Day", "descr": "", "catid": 48, "source": 83},
    {"name": "General Room", "descr": "", "catid": 48, "source": 83},
    {"name": "General Room Feeding", "descr": "", "catid": 48, "source": 83},
    {"name": "Gonioscopy", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "Ganglion (Dorsum Of Both Wrist) - Excision", "descr": "", "catid": 37, "source": 83},
    {"name": "Ganglion - Excision", "descr": "", "catid": 37, "source": 83},
    {"name": "Ganglion - Small - Excision D ,", "descr": "", "catid": 37, "source": 83},
    {"name": "Ganglion Excision (Block Fee)", "descr": "", "catid": 37, "source": 83},
    {"name": "Ganglionectectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Gastrectomy- Partial/Total", "descr": "", "catid": 37, "source": 83},
    {"name": "Gastric Lavage", "descr": "", "catid": 37, "source": 83},
    {"name": "Gastroduodenoscopy", "descr": "", "catid": 37, "source": 83},
    {"name": "Gastroduodenoscopy/ Endoscopies", "descr": "", "catid": 37, "source": 83},
    {"name": "Gastroenterostomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Gastrojejunostomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Gastrostomy", "descr": "", "catid": 37, "source": 83},
    {"name": "General Major", "descr": "", "catid": 37, "source": 83},
    {"name": "General Major Plus (Two Major Surgeries In One Sitting)", "descr": "", "catid": 37, "source": 83},
    {"name": "General Medium", "descr": "", "catid": 37, "source": 83},
    {"name": "General Ward", "descr": "", "catid": 37, "source": 83},
    {"name": "Gingivectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Glass Ionomer Cerment (GIC) Restoration", "descr": "", "catid": 37, "source": 83},
    {"name": "Glass Ionomer Filling", "descr": "", "catid": 37, "source": 83},
    {"name": "Glaucoma Phasing", "descr": "", "catid": 37, "source": 83},
    {"name": "Glossectomy-Partial/Total", "descr": "", "catid": 37, "source": 83},
    {"name": "Grahams Operation", "descr": "", "catid": 37, "source": 83},
    {"name": "Granuloma - Excision", "descr": "", "catid": 37, "source": 83},
    {"name": "Gypsum", "descr": "", "catid": 37, "source": 83},
])

vaccines = np.array([
    {"name": "Genevac B Paed (Hepatitis B)", "descr": "", "catid": 46, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — Product G
# =============================================================================
# Total records on this sheet : 130
# Categories found            : consultations, infusions, laboratory_tests, medical_devices, medical_supplies, medications, others, surgeries, vaccines
# Unmapped categories         : None
# Duplicates removed          : medications:"Gentamycin"; medications:"Gliclazide"; medications:"Glimepiride"; medications:"Griseofulvin"
# =============================================================================
