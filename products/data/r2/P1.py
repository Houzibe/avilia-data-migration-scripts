import numpy as np

consultations = np.array([
    {"name": "Paediatric Doctor", "descr": "", "catid": 36, "source": 83},
    {"name": "Physician Geriatrician", "descr": "", "catid": 36, "source": 83},
    {"name": "Physician Geriatrician- Initial", "descr": "", "catid": 36, "source": 83},
    {"name": "Physiotherapist - Follow Up", "descr": "", "catid": 36, "source": 83},
    {"name": "Physiotherapist - Initial", "descr": "", "catid": 36, "source": 83},
])

diagnostic_imaging = np.array([
    {"name": "Pelvi", "descr": "", "catid": 27, "source": 83},
    {"name": "Pelvic MRI", "descr": "", "catid": 27, "source": 83},
    {"name": "Pelvic Scan Single Contrast", "descr": "", "catid": 27, "source": 83},
    {"name": "Print Extra Cd", "descr": "", "catid": 27, "source": 83},
    {"name": "Print Extra View", "descr": "", "catid": 27, "source": 83},
    {"name": "Print Lasser Hard Copy", "descr": "", "catid": 27, "source": 83},
    {"name": "Prostate And Bladder With Contrast", "descr": "", "catid": 27, "source": 83},
])

laboratory_tests = np.array([
    {"name": "Packed Cell Volume", "descr": "", "catid": 39, "source": 83},
    {"name": "Packed Cells - Rh Negative", "descr": "", "catid": 39, "source": 83},
    {"name": "Packed Cells - Rh Positive", "descr": "", "catid": 39, "source": 83},
    {"name": "Paediatric Food Screen", "descr": "", "catid": 39, "source": 83},
    {"name": "Pap Smear", "descr": "", "catid": 39, "source": 83},
    {"name": "Parathyroid Hormone", "descr": "", "catid": 39, "source": 83},
    {"name": "Parvovirus IgG", "descr": "", "catid": 39, "source": 83},
    {"name": "Peanuts", "descr": "", "catid": 39, "source": 83},
    {"name": "Ph", "descr": "", "catid": 39, "source": 83},
    {"name": "Phadiatop", "descr": "", "catid": 39, "source": 83},
    {"name": "Phadiatop(Inhalative Mix Allergens)", "descr": "", "catid": 39, "source": 83},
    {"name": "Phosphate", "descr": "", "catid": 39, "source": 83},
    {"name": "Platelet Antibodies", "descr": "", "catid": 39, "source": 83},
    {"name": "Platelet Concentrates", "descr": "", "catid": 39, "source": 83},
    {"name": "Point Of Care Pcv", "descr": "", "catid": 39, "source": 83},
    {"name": "Pollen Grain", "descr": "", "catid": 39, "source": 83},
    {"name": "Potassium", "descr": "", "catid": 39, "source": 83},
    {"name": "Pressure Of Oxygen(Po2)", "descr": "", "catid": 39, "source": 83},
    {"name": "Procalcitonin", "descr": "", "catid": 39, "source": 83},
    {"name": "Progesterone(D21)", "descr": "", "catid": 39, "source": 83},
    {"name": "Prolactin", "descr": "", "catid": 39, "source": 83},
    {"name": "Prostate Specific Antigen", "descr": "", "catid": 39, "source": 83},
    {"name": "Protein - Quantitative", "descr": "", "catid": 39, "source": 83},
    {"name": "Prothrombin Time Test", "descr": "", "catid": 39, "source": 83},
])

medical_supplies = np.array([
    {"name": "Plaster Of Paris Bandage (Pop) Roll 6 Inch", "descr": "", "catid": 34, "source": 83},
])

medications = np.array([
    {"name": "Pancuronium (...) Injection 4 mg/2Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Pantoprazole 20Mg (...) Tablet 20 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (...) Syrup 120 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (...) Tablet 500 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (Acepol) Syrup 120 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (Avipol) Syrup 120 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (Calpol Infant 2Mnths Sugar Free) Syrup 120 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (Calpol Infant 2Mths+ 100Mls) Suspension 120 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (Calpol Infant 2Mths+ 200Mls) Suspension 120 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (Drugamol) Injection 300 mg/2Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (Easadol) Syrup 120 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (Easadol) Tablet 500 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (Emcap) Syrup 120 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (Emcap) Tablet 500 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (Moxie) Suspension 120 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (Panadol) Tablet 500 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol (Panda) Suspension 125 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol + Caffiene (Panadol Extra) Tablet 500 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol 1000Mg (Paraconica) Infusion 10 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol 500Mg+Pseudoephedrine30Mg + Pholcodeine 5Mg (Day Nurse) Capsule 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol 500Mg/Codeine Phosphate 30Mg (Co-Codamol) Tablet 530 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol 500Mg/Codeine Phosphate 8Mg (Co-Codamol) Efferv Tab 508 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Paracetamol/Codeine/Caffeine (500/8/30Mg) (Solpadeine) Capsule 500 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Paraldehyde (Paraldehyde) Injection 0.01 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Paroxetine (Paroxetine 20Mg) Tablet 20 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Paroxetine (Paroxetine 20Mg) Tablet 30 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Paroxetine (Seroxat) Tablet 20 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Pefloxacin (Loxapef) Tablet 400 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Pefloxacin (Peflacine) Tablet 400 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Penicillin (...) Ointment 20 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Penicillin (...) Ointment 5000 IU", "descr": "", "catid": 35, "source": 83},
    {"name": "Penicillin Vk (...) Tablet 250 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Pentazocine (Pilat) Injection 30 mg/2Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Perindopril 10Mg/Amlodipine 10Mg (Coveram 10Mg/10Mg) Tablet 10 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Perindopril 10Mg/Amlodipine 5Mg (Coveram 10Mg/5Mg) Tablet 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Perindopril 10Mg/Amlodipine 5Mg/Indapamide 2.5Mg (Coveram Plus 10Mg/5Mg/2.5Mg) Tablet 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Perindopril 5Mg/Amlodipine 5Mg (Coveram 5Mg/5Mg) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Perineal Pad (Dr Brown) Item 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Permethrin (Permin) Cream 30 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Pethidine (...) Injection 100 mg/2Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Phenobarbitone (...) Injection 100 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Phenobarbitone (...) Tablet 15 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Phenobarbitone (Pitrofin) Syrup 15 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Phenytoin (Epanutin) Syrup 30 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Phenytoin Sodium (...) Injection 250 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Phototherapy Eye Protector (Argyle) Item 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Pilocarpine (...) Drops 4 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Pioglitazone (Pionorm - 30) Tablet 15 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Pioglitazone (Pionorm - 30) Tablet 30 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Piperacillin/Tazobactam (Tazpen) Injection 4.5 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Piroxicam (...) Injection 20 mg/2Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Piroxicam (Felxicam) Capsule 20 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Plaster (Durapore) Item 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Plastibel (...) Item 1.1 Cm", "descr": "", "catid": 35, "source": 83},
    {"name": "Podophyllotoxin (Podophyllin) Cream 15 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Podophyllum Resin (Podofin Paint) Solution 50 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Podophyllum Resin (Podophyllin Paint) Solution 100 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Podophyllum Resin (Podowart Paint) Solution 15 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Polyamide 6 Monofilament (Ethilon 2-0) Item 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Polyenylphosphatidylcholine (Livolin Forte) Capsule 300 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Potassium Chloride (...) Injection 1.5 G/10Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Potassium Chloride (Sando K) Tablet 600 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Potassium Chloride (Slow-K) Tablet 600 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Potassium Citrate (Mist Pot. Citrate) Solution 200 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Potassium Citrate (Uropocit) Solution 200 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Potassium Iodide + Sodium Iodide (Vitreolent) Drops 0.3 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Povidone Iodine (Braunol) Solution 10 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Povidone Iodine (Wosan) Ointment 20 G", "descr": "", "catid": 35, "source": 83},
    {"name": "Povidone Iodine (Wosan) Solution 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Praziquantel (...) Tablet 600 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Prednisolone (Perilon) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Prednisolone Eye Drop (Ivysolone) Suspension 1 Unit", "descr": "", "catid": 35, "source": 83},
    {"name": "Pregabalin (Ligaba) Capsule 75 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Pregabalin (Lyrica) Capsule 25 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Pregabalin (Lyrica) Capsule 75 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Primaquine Phosphate 15Mg (Primaquine) Tablet 15 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Primidone (Mysoline) Tablet 250 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Procaine Penicillin (...) Injection 1000000 IU", "descr": "", "catid": 35, "source": 83},
    {"name": "Prochlorperazine Maleate (Stemetil) Tablet 5 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Progesterone (Cyclogest) Pessary 400 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Progesterone (Gestone) Injection 100 mg/ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Progesterone (Progestan 200Mg) Ovule 200 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Proguanil (Cedrine) Tablet 100 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Proguanil (Reludrine) Tablet 100 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Promethazine (...) Syrup 5 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Promethazine (Rophegan) Syrup 5 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Promethazine Theoclate (...) Injection 50 mg/2Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Promethazine Theoclate (Avomine) Tablet 25 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Propofol 1% (...) Injection 10 ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Propranolol (...) Tablet 40 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Purified Soybean Oil (Intralipid 20%W/V) Solution 20 %", "descr": "", "catid": 35, "source": 83},
    {"name": "Pyrantel Pamoate (Pyrantrin) Tablet 125 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Pyrazinamide (...) Tablet 500 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Pyridostigmine 60Mg (Mestinon) Tablet 60 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Pyridoxine (...) Tablet 50 mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Pyritinol Dihcl Monohydrate (Encephabol) Syrup 80.5 mg/5Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Pyronaridine Tetraphosphate 180Mg + Artesunate 60Mg (Pyramax) Tablet 1 Tab", "descr": "", "catid": 35, "source": 83},
])

nutritionals = np.array([
    {"name": "Preconception Supplement (Conceive Plus) Tablet 200 mg", "descr": "", "catid": 33, "source": 83},
])

others = np.array([
    {"name": "Phototherapy", "descr": "", "catid": 48, "source": 83},
])

surgeries = np.array([
    {"name": "Polypectomy Under Local Anaesthesia", "descr": "", "catid": 37, "source": 83},
    {"name": "Pothole Of The 5Th Metartarsals", "descr": "", "catid": 37, "source": 83},
    {"name": "Pre-Auricular Sinus Excision (Unilateral)", "descr": "", "catid": 37, "source": 83},
    {"name": "Prostatectomy", "descr": "", "catid": 37, "source": 83},
    {"name": "Pta", "descr": "", "catid": 37, "source": 83},
    {"name": "Pull Through", "descr": "", "catid": 37, "source": 83},
    {"name": "Pure Tone Audiometry", "descr": "", "catid": 37, "source": 83},
])

vaccines = np.array([
    {"name": "Pneumococcus Polysaccharide Capsular 1 Vaccine (Synflorix) Injection 0.5 ml", "descr": "", "catid": 46, "source": 83},
    {"name": "Pneumococcus Polysaccharide Capsular 13 Vaccine (Prevenar) Injection 0.5 ml", "descr": "", "catid": 46, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — P
# =============================================================================
# Total records on this sheet : 146
# Categories found            : consultations, diagnostic_imaging, laboratory_tests, medical_supplies, medications, nutritionals, others, surgeries, vaccines
# Unmapped categories         : None
# Duplicates removed          : 1
# =============================================================================
