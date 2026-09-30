import numpy as np

consultations = np.array([
    {"name": "In-Patient Endocrinologist Review - Initial", "descr": "", "catid": 36, "source": 83},
])

family_planning = np.array([
    {"name": "Implant Removal (Jadelle)", "descr": "", "catid": 44, "source": 83},
    {"name": "Iucd (Mirena) Removal Under G.A", "descr": "", "catid": 44, "source": 83},
    {"name": "Iucd - Copper T Insertion", "descr": "", "catid": 44, "source": 83},
    {"name": "Iucd Insertion (Copper T) Under GA", "descr": "", "catid": 44, "source": 83},
    {"name": "Iucd Insertion - Mirena", "descr": "", "catid": 44, "source": 83},
    {"name": "Iucd Mirena Insertion Under GA", "descr": "", "catid": 44, "source": 83},
    {"name": "Iucd Removal (Copper T)", "descr": "", "catid": 44, "source": 83},
    {"name": "Iucd Removal (Mirena)", "descr": "", "catid": 44, "source": 83},
    {"name": "Iucd Removal (Mirena) Under GA", "descr": "", "catid": 44, "source": 83},
    {"name": "Iucd Removal Copper T Under G.A", "descr": "", "catid": 44, "source": 83},
])

laboratory_tests = np.array([
    {"name": "Ihc-Alpha-Fetoprotein", "descr": "", "catid": 39, "source": 83},
    {"name": "Immunohistochemistry", "descr": "", "catid": 39, "source": 83},
    {"name": "Inhibin A", "descr": "", "catid": 39, "source": 83},
    {"name": "Inhibin B", "descr": "", "catid": 39, "source": 83},
    {"name": "Inorganic Phosphate", "descr": "", "catid": 39, "source": 83},
    {"name": "Insulin Fasting", "descr": "", "catid": 39, "source": 83},
    {"name": "Insulin Growth Factor Protein 3", "descr": "", "catid": 39, "source": 83},
    {"name": "International Normalized Ratio", "descr": "", "catid": 39, "source": 83},
    {"name": "Ionised Calcium", "descr": "", "catid": 39, "source": 83},
    {"name": "Iron Studies", "descr": "", "catid": 39, "source": 83},
])

medical_supplies = np.array([
    {"name": "Insulin Pen Needles (...) Item 1 Unit", "descr": "", "catid": 34, "source": 83},
    {"name": "Insulin Syringe (Promisemed 1Ml) Item 100 IU", "descr": "", "catid": 34, "source": 83},
])

medications = np.array([
    {"name": "Ibuprofen (...) Tablet 200 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen (Brustan-N) Syrup 100 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen (Brustan-N) Tablet 400 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen (Buprol) Tablet 400 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen (Emprofen) Capsule 400 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen (Emprofen) Syrup 100 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen (Nurofen) Syrup 100 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen (Rexifen) Capsule 400 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen (Swifen) Syrup 100 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen/Paracetamol/Caffeine (200/325/30Mg) (Brusta Extra) Capsule 200 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ibuprofen/Paracetamol/Caffeine (200/325/30Mg) (Ibex) Capsule 200 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Imipenem/Cilastatine (Bacquire) Injection 500 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Imipramine (Tofranil) Tablet 25 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Inactivated Rabies Virus (Rabipur) Injection 2 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Indapamide 1.5 + Amlodipine 5Mg (Natrixam) Tablet 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Indapamide 1.5Mg (Natrilix Sr) Tablet 1.5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Indapamide 2.5Mg (Indapamide) Tablet 2.5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Aspart (Novorapid Flexpen) Injection 100 IU/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Degludec (Tresiba Flexpen) Injection 100 IU/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Determir (Levemir Flex Pen) Injection 100 IU/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Glargine (Lantus Solostar) Injection 100 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Glulisine (Apidra Solostar) Injection 100 IU/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Lispro (Humalog) Injection 100 IU/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Insulin Lispro 25% + Insulin Lispro Protamine 75% (Humalog Mix 25) Injection 100 IU/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Intrauterine Copper Device (Copper T) Item 176 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Iodinated - Povidone + Metronidazole (Drez) Ointment 10 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Iodine 2.5% (Iodine Tincture) Solution 15 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ipatropium Bromide 20Mcg + Fenoterol Hydrobromide 50Mcg (Duovent) Spray 50 μg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ipecacuanha + Glycerin + Honey + Lemon (Beehive Balsam) Syrup 100 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ipecacuanha + Glycerin + Honey + Lemon (Novalyn Cough Lintus) Syrup 100 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Ipratropium (Steri-Neb) Inhalation 500 μg", "descr": "", "catid": 35, "source": 83},
    {"name": "Irbesartan (Aprovel) Tablet 150 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Irbesartan (Aprovel) Tablet 300 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Irbesartan 150Mg + Amlodipine 10Mg (Aprovasc) Tablet 10 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Irbesartan 150Mg +Amlodipine 5Mg (Aprovasc) Tablet 150 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Irbesartan 150Mg +Hydrochlorthiazide 12.5Mg (Coaprovel) Tablet 162.5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Irbesartan 300Mg + Amlodipine 10Mg (Aprovasc) Tablet 300 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Irbesartan 300Mg + Amlodipine 5Mg (Aprovasc) Tablet 300 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Irbesartan 300Mg + Hydrochlorthiazide 12.5Mg (Coaprovel) Tablet 312.5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Iron + Folic Acid + Cyanocobalamin + Zinc Sulphate (Hemoforce Plus) Capsule 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Iron + Folic Acid + Zinc Sulphate + Ascorbic Acid (Hemoforce Forte) Syrup 5 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Iron Dextran (...) Injection 250 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Iron Polymaltose (Zegem) Syrup 5 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Iron(Iii) - Hydroxide Polymaltose Complex (Glamife) Syrup 50 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoconazole (Gyno-Travogen) Pessary 600 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoconazole 10Mg + Hydrocortisone 1Mg (Travocort) Cream 15 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoconazole Nitrate 1% (Travogen) Cream 20 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoflurane (...) Solution 250 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoniazid (...) Tablet 150 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Isoniazid (Spenazid) Syrup 100 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Isopropyl Alcohol (Methylated Spirit) Solution 2 L", "descr": "", "catid": 35, "source": 83},
    {"name": "Isopropyl Alcohol (Methylated Spirit) Solution 200 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Isosorbide Dinitrate (Isordil) Tablet 10 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Ispaghula (Fybogel) Powder 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Ivermectin 3Mg (Mectizan) Tablet 3 mg", "descr": "", "catid": 35, "source": 83},
])

nutritionals = np.array([
    {"name": "Iron + Folic Acid + Vitamin B12 (Feroglobin) Syrup 5 ml", "descr": "", "catid": 33, "source": 83},
    {"name": "Iron 53.25Mg + Folic Acid 0.75Mg + Vitamin B12 7.5Ug (Ferrotone) Capsule 1 Unit", "descr": "", "catid": 33, "source": 83},
])

others = np.array([
    {"name": "In-Patient Reviews", "descr": "", "catid": 48, "source": 83},
    {"name": "Incubator Care", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "Incision And Drainage (Minor)", "descr": "", "catid": 37, "source": 83},
    {"name": "Incision And Drainage (Theatre)", "descr": "", "catid": 37, "source": 83},
    {"name": "Incision And Drainage(Major)", "descr": "", "catid": 37, "source": 83},
    {"name": "Incision And Drainage(Moderate)", "descr": "", "catid": 37, "source": 83},
    {"name": "Indirect Laryngoscopy", "descr": "", "catid": 37, "source": 83},
    {"name": "Induction Of Labour", "descr": "", "catid": 37, "source": 83},
    {"name": "Inguinal Exploratory", "descr": "", "catid": 37, "source": 83},
    {"name": "Inguinal Hernioplasty + Mesh", "descr": "", "catid": 37, "source": 83},
    {"name": "Inguinal Herniotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Internal Fixation", "descr": "", "catid": 37, "source": 83},
    {"name": "Intracervical Adhesiolysis", "descr": "", "catid": 37, "source": 83},
    {"name": "Intrauterine Adhesiolysis", "descr": "", "catid": 37, "source": 83},
    {"name": "Iop", "descr": "", "catid": 37, "source": 83},
])

vaccines = np.array([
    {"name": "Inactivated Influenza Vaccine (Hiberix) Injection 0.5 ml", "descr": "", "catid": 46, "source": 83},
    {"name": "Inactivated Poliomyelitis Vaccine (Ipv) Injection 0.5 %", "descr": "", "catid": 46, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — I
# =============================================================================
# Total records on this sheet : 98
# Categories found            : consultations, family_planning, laboratory_tests, medical_supplies, medications, nutritionals, others, surgeries, vaccines
# Unmapped categories         : None
# Duplicates removed          : 1
# =============================================================================
