import numpy as np

"""
diagnostic_imaging = np.array([
    {"name": "Babygram", "descr": "", "catid": 27, "source": 83},
    {"name": "Barium Enema", "descr": "", "catid": 27, "source": 83},
    {"name": "Barium Meal & Follow Through", "descr": "", "catid": 27, "source": 83},
    {"name": "Barium Sulphate Meal", "descr": "", "catid": 27, "source": 83},
    {"name": "Barium Swallow", "descr": "", "catid": 27, "source": 83},
    {"name": "Brain Scan Contrast(Angio)", "descr": "", "catid": 27, "source": 83},
    {"name": "Brain Scan Plain(MRI)", "descr": "", "catid": 27, "source": 83},
])

laboratory_tests = np.array([
    {"name": "B-Type Natriuretic Peptide", "descr": "", "catid": 39, "source": 83},
    {"name": "Base Excess", "descr": "", "catid": 39, "source": 83},
    {"name": "Bcl2", "descr": "", "catid": 39, "source": 83},
    {"name": "Bcl6", "descr": "", "catid": 39, "source": 83},
    {"name": "Bedside Blood Glucose", "descr": "", "catid": 39, "source": 83},
    {"name": "Beta-Human Chorionic Gonadotrophin", "descr": "", "catid": 39, "source": 83},
    {"name": "Bicarbonate(Hco3)", "descr": "", "catid": 39, "source": 83},
    {"name": "Bilirubin, Direct", "descr": "", "catid": 39, "source": 83},
    {"name": "Bilirubin, Total", "descr": "", "catid": 39, "source": 83},
    {"name": "Bleeding Tendency (1,7,11,13,15)", "descr": "", "catid": 39, "source": 83},
    {"name": "Bleeding Time", "descr": "", "catid": 39, "source": 83},
    {"name": "Blood Crossmatch", "descr": "", "catid": 39, "source": 83},
    {"name": "Blood Group & Rhesus Type", "descr": "", "catid": 39, "source": 83},
    {"name": "Blood Sugar Series", "descr": "", "catid": 39, "source": 83},
    {"name": "Blood Transfusion", "descr": "", "catid": 39, "source": 83},
    {"name": "Blood Urea Nitrogen", "descr": "", "catid": 39, "source": 83},
])

medical_supplies = np.array([
    {"name": "Braided Absorbable Suture (Vicryl 0-Mh1 Plus) Item 75 Cm", "descr": "", "catid": 34, "source": 83},
    {"name": "Braided Absorbable Suture (Vicryl 2-0) Roll 75 Cm", "descr": "", "catid": 34, "source": 83},
    {"name": "Braided Absorbable Suture (Vicryl 3-0 Fs) Item 45 Cm", "descr": "", "catid": 34, "source": 83},
"""
medical_supplies = np.array([    
    {"name": "Braided Absorbable Suture (Vicryl 3-0 Sh Plus) Item 75 Cm", "descr": "", "catid": 34, "source": 83},
    {"name": "Braided Absorbable Suture (Vicryl-1 Cpx) Item 75 Cm", "descr": "", "catid": 34, "source": 83},
])

medications = np.array([
    {"name": "Baby Wipes (Pampers) Item 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Bacillus Clausii (Enterogermina) Syrup 5 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Bendroflumethiazide (...) Tablet 2.5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Benylin Children Paediatric (Benylin) Syrup 100 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Benzathine Penicillin (...) Injection 24000 IU", "descr": "", "catid": 35, "source": 83},
    {"name": "Benzathine Penicillin (Retarpen) Injection 24000 IU", "descr": "", "catid": 35, "source": 83},
    {"name": "Benzoyl Peroxide 10%W/W (Oxy 10) Gel 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Benzyl Benzoate 25% (Benzyl Benzoate) Solution 100 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Betahistine (Serc) Tablet 16 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Betahistine (Serc) Tablet 8 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Betamethasone (...) Cream 20 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Betamethasone 0.05%+ Salicylic Acid 3% (Diprosalic) Ointment 30 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Betamethasone 0.1% + Neomycin 0.5% (Aristobet N) Drops 1 Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Betamethasone 0.1% + Neomycin 0.5% (Betadrone-N) Drops 1 Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Betamethasone 0.1% + Neomycin 0.5% (Betadrone-N) Ointment 0.1 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Betamethasone 0.1% + Neomycin 0.5% (Betnovate N) Cream 25 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Betaxolol Hydrochloride (Betoptic) Drops 5.6 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Betaxolol Hydrochloride (Betoptic) Ointment 5 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Bicalutamide (Casodex) Tablet 50 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Bilaxten (Bilaxten) Tablet 20 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Biopentinnt (Gabapentin) Tablet 400 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Bisacodyl (Dulcolax) Suppository 10 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Bisacodyl (Dulcolax) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Bisacodyl 5Mg (Bisamed) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Bismuth Subsalicylate (Peptol-Bismol) Suspension 525 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Bisoprolol Fumarate (Teva) Tablet 2.5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Bisoprolol Fumarate (Teva) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Blood Giving Set (...) Item 100 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Bovine Lipid Extract Surfactant (Bles) Injection 5 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Braided Non Absorbable Surgical Sucture (Cervix Set) Item 75 Cm", "descr": "", "catid": 35, "source": 83},
    {"name": "Braided Non Absorbable Surgical Sucture (Mersilene Tape) Item 75 Cm", "descr": "", "catid": 35, "source": 83},
    {"name": "Breast Milk Fortifier (Similac) Powder 0.9 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Breast Milk Substitute (Aptamil) Powder 800 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Breast Milk Substitute (Nan 1 Comfortis) Powder 400 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Breast Milk Substitute (Nan 1) Powder 400 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Breast Milk Substitute (Peak) Item 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Breast Milk Substitute (Pre Nan) Powder 400 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Breast Milk Substitute (Pre Nutriprem) Powder 400 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Breast Milk Substitute (Sma 1 Gold) Powder 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Breast Pump (...) Item 150 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Bromazepam (Lexotan) Tablet 1.5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Bromhexine Hydrochloride (Broncholyte) Syrup 4 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Bromocriptine (Bromergon) Tablet 2.5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Bromocriptine (Bromodel) Tablet 2.5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Bromocriptine (Parlodel) Tablet 2.5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Budesonide (Pulmicrot) Inhalation 0.25 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Budesonide (Pulmicrot) Inhalation 0.5 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Budesonide 160Mcg +Formoterol 4.5Mcg (Symbicort) Powder 164.5 μg", "descr": "", "catid": 35, "source": 83},
    {"name": "Budesonide 80Mcg +Formoterol 4.5Mcg (Symbicort) Powder 84.5 μg", "descr": "", "catid": 35, "source": 83},
    {"name": "Bupivacaine (Duracaine) Injection 2.5 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Bupivacaine (Heavy Marcaine) Injection 0.5 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Bupropion (...) Tablet 150 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Bupropion (Wellbutrin) Tablet 150 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Buserelin (Busarlin) Injection 0.5 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Buserelin (Suprefact) Injection 0.5 ml", "descr": "", "catid": 35, "source": 83},
])

others = np.array([
    {"name": "Breast Milk Bank", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "Bilateral Aural Toileting", "descr": "", "catid": 37, "source": 83},
    {"name": "Bilateral Herniotomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Bilateral Inguinal Exploratory", "descr": "", "catid": 37, "source": 83},
    {"name": "Bilateral Intranasal Anstrostomy Under GA", "descr": "", "catid": 37, "source": 83},
    {"name": "Bilateral Scrotal Exploratory", "descr": "", "catid": 37, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — B
# =============================================================================
# Total records on this sheet : 89
# Categories found            : diagnostic_imaging, laboratory_tests, medical_supplies, medications, others, surgeries
# Unmapped categories         : None
# =============================================================================
