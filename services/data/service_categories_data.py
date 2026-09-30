import numpy as np
"""
service_categories = np.array([
    {"name": "General Consultation", "descr": "A face-to-face visit with a general medical practitioner.", "parent": ""},
    {"name": "Prescribed Medications for Out patient covered care", "descr": "Medicines prescribed by a doctor during an outpatient visit, dispensed at a network pharmacy and covered under the outpatient benefit limit.", "parent": ""},
    {"name": "Basic Lab Investigations or Xrays and Ultrasound", "descr": "Routine diagnostic tests including blood counts, urinalysis, plain X-rays, and standard ultrasound examinations.", "parent": ""},
    {"name": "Out Patient care Limit", "descr": "The maximum coverage amount (financial or number of visits) for services delivered without hospital admission, including consultations, diagnostics, drugs, and minor procedures.", "parent": ""},
    {"name": "Treatment of basic outpatient and in-patient cases", "descr": "Medical and surgical management of common acute or chronic conditions at both ambulatory (OP) and admitted (IP) levels, following standard clinical protocols.", "parent": ""},
    {"name": "Specialist Consultation", "descr": "A visit to a medical doctor with advanced training in a specific branch of medicine for diagnosis, treatment planning, or follow-up of a complex condition.", "parent": ""},
    {"name": "Accident And Emergency Care Out Patient", "descr": "Immediate medical evaluation and treatment for acute injuries, sudden illness, or life-threatening conditions provided in a hospital emergency department, without requiring admission to an inpatient bed.", "parent": ""},
    {"name": "In Patient Care Limit", "descr": "Hospitalisation services where the patient is admitted for at least one overnight stay, including room, nursing care, routine medical procedures, and medications, subject to a predefined coverage limit.", "parent": ""},
    {"name": "Basic Diagnostic Imaging", "descr": "Standard imaging procedures  covered under outpatient (OPT) or inpatient (IPT) limits.", "parent": ""},
    {"name": "Advanced Diagnostic Imaging", "descr": "More complex imaging modalities.", "parent": ""},
    {"name": "Hematological Test", "descr": "Laboratory tests that assess blood cells and related parameters, and blood grouping.", "parent": ""},
    {"name": "Chemistry Investigations", "descr": "Blood and body fluid tests measuring metabolites, electrolytes, enzymes, hormones, and organ function markers.", "parent": ""},
    {"name": "Microbiology And Parasitology", "descr": "Laboratory identification of infectious agents.", "parent": ""},
    {"name": "Advanced Laboratory Investigations/Pathology", "descr": "Specialised tests such as immunohistochemistry, flow cytometry, cytogenetics, molecular diagnostics.", "parent": ""},
    {"name": "Eye/Optical Care", "descr": "Services provided by ophthalmologists or optometrists, and minor office procedures.", "parent": ""},
    {"name": "Dental Care", "descr": "Oral health services including routine check-ups, scaling and polishing, fillings, extractions, root canal treatment, and preventive care.", "parent": ""},
    {"name": "Physiotherapy Care", "descr": "Assessment and treatment of musculoskeletal, neurological, or cardiopulmonary conditions using physical methods.", "parent": ""},
    {"name": "Obstetrics  And Gynaecology Care (In Patient Limit Applies)", "descr": "Medical and surgical care related to pregnancy (antenatal, delivery, postnatal) and female reproductive health.", "parent": ""},
    {"name": "Infertility Care", "descr": "Evaluation and treatment of individuals or couples unable to conceive after one year of unprotected intercourse.", "parent": ""},
    {"name": "Npi Immunization (0-5 Years)", "descr": "Vaccinations provided to children from birth up to age 5 years under the National Programme on Immunization (NPI), covering standard antigens.", "parent": ""},
    {"name": "Additional Immunization (0-5 Years)", "descr": "Vaccines that are not part of the routine NPI schedule but recommended for children under 5 years.", "parent": ""},
    {"name": "Additional Immunization (6 Years And Above)", "descr": "Vaccinations for individuals aged 6 years and older beyond basic NPI schedules.", "parent": ""},
    {"name": "Family Planning Out Patient Limit", "descr": "Contraceptive services provided on an outpatient basis, including counselling, prescription of oral contraceptives, injectables, implants, intrauterine devices (IUDs), and barrier methods.", "parent": ""},
    {"name": "Gym(Discounted)", "descr": "Access to fitness centre facilities (gym equipment, group classes) at a reduced rate, typically through a network of partner gyms.", "parent": ""},
    {"name": "Routine Drugs", "descr": "Essential medications prescribed for common acute or chronic conditions that are included in a formulary.", "parent": ""},
    {"name": "Surgeries (All Inclusive)", "descr": "Comprehensive coverage for surgical procedures, including the surgeon's fee, anaesthesia, operating theatre, implants, inpatient stay, and post-operative care.", "parent": ""},
    {"name": "Cancer Screening/Care", "descr": "Services aimed at early detection of cancer and management after diagnosis and follow-up monitoring.", "parent": ""},
    {"name": "Renal Care (Dialysis)", "descr": "Treatment for end-stage renal disease, including haemodialysis (usually 2-3 sessions per week) or peritoneal dialysis, related laboratory tests (pre- and post-dialysis), and management of complications.", "parent": ""},
    {"name": "Wellness Checks", "descr": "A comprehensive preventive health assessment performed once per year at approved facilities.", "parent": ""},
    {"name": "Psychiatry Care", "descr": "Mental health services provided by psychiatrists, psychologists, or psychiatric nurses.", "parent": ""},
    {"name": "Hiv Care And Treatment At Designated Sites", "descr": "Comprehensive management of HIV/AIDS at accredited centres.", "parent": ""},
    {"name": "Seeking Second Opinion", "descr": "Consultation with another qualified physician to review a diagnosis, treatment plan, or surgical recommendation.", "parent": ""},
    {"name": "Mortuary Services", "descr": "Handling and storage of deceased bodies in a mortuary facility.", "parent": ""}
]) 
"""

#26
specialist_consultation = np.array([
    {"name": "ENT Surgeon (Otorhinolaryngologist)", "descr": "A specialist who diagnoses and treats disorders of the ear, nose, throat, and related head-neck structures.", "parent": 26},
    {"name": "Urologist", "descr": "A surgeon managing diseases of the urinary tract (kidneys, ureters, bladder, urethra) in both sexes, and the male reproductive system (prostate, testes, penis).", "parent": 26},
    {"name": "Orthopedic Surgeon", "descr": "A specialist in the musculoskeletal system (bones, joints, ligaments, tendons) performing fracture fixation, joint replacement, arthroscopy, and spine surgery.", "parent": 26},
    {"name": "Obstetrician", "descr": "A doctor caring for women during pregnancy, labour, delivery, and the postpartum period, including high-risk pregnancies and caesarean sections.", "parent": 26},
    {"name": "Gynaecologist", "descr": "A specialist in female reproductive health: menstrual disorders, fibroids, endometriosis, pelvic organ prolapse, and gynaecological cancers.", "parent": 26},
    {"name": "Pediatrician or Pediatric Surgeon", "descr": "A child health specialist (0-18 years) for medical conditions.", "parent": 26},
    {"name": "Cardiothoracic Surgeon", "descr": "A surgeon specialising in the heart, lungs, oesophagus, and other thoracic organs, performing coronary bypass, valve repair, lung resections, etc.", "parent": 26},
    {"name": "Neurosurgeon", "descr": "A specialist in surgical treatment of brain, spinal cord, and peripheral nerve disorders.", "parent": 26},
    {"name": "Gastroenterologist", "descr": "A physician managing digestive tract diseases and performing endoscopy or colonoscopy.", "parent": 26},
    {"name": "Dietician or Nutritionist", "descr": "An expert in food and nutrition providing dietary counselling for weight management, diabetes, heart disease, food allergies, and enteral or parenteral support.", "parent": 26},
    {"name": "Pulmonologist or Respiratory Physician or Chest Physician", "descr": "A specialist in lung and airway diseases performing bronchoscopy and lung function tests.", "parent": 26},
    {"name": "Hematologist", "descr": "A physician specialising in blood disorders.", "parent": 26},
    {"name": "Oncologist", "descr": "A cancer specialist overseeing chemotherapy, targeted therapy, immunotherapy, and palliative care.", "parent": 26},
    {"name": "Pathologist", "descr": "A doctor who diagnoses disease by examining tissues, cells, and body fluids.", "parent": 26},
    {"name": "Endocrinologist", "descr": "A specialist in hormone-related disorders.", "parent": 26},
    {"name": "Cardiologist", "descr": "A physician managing heart and blood vessel diseases  performing ECG, echocardiography, stress tests.", "parent": 26},
    {"name": "Neurologist", "descr": "A specialist in disorders of the nervous system.", "parent": 26},
    {"name": "Nephrologist", "descr": "A physician specialising in kidney diseases, hypertension, electrolyte disorders, and dialysis.", "parent": 26},
    {"name": "Psychiatrist", "descr": "A medical doctor specialising in mental health disorders, prescribing medications and providing psychotherapy for depression, anxiety, bipolar disorder, schizophrenia.", "parent": 26},
    {"name": "Neonatologist", "descr": "A paediatric subspecialist caring for newborn infants, especially premature or ill babies in a neonatal intensive care unit (NICU).", "parent": 26},
    {"name": "Dermatologist", "descr": "A skin specialist managing acne, eczema, psoriasis, skin infections, hair and nail disorders, and performing skin biopsies or cryotherapy.", "parent": 26},
    {"name": "Family Physician", "descr": "A primary care doctor providing comprehensive, continuous care for individuals and families across all ages, genders, and diseases, first point of contact.", "parent": 26},
    {"name": "Oral and Maxillofacial Surgeon", "descr": "A dental specialist operating on the mouth, jaws, face, and skull, extracting wisdom teeth, corrective jaw surgery, facial trauma repair, dental implants.", "parent": 26},
    {"name": "Rheumatologist", "descr": "A physician specialising in autoimmune and inflammatory disorders affecting joints, muscles, and connective tissue.", "parent": 26}
]) 


#27
accident_emergency_care_out_patient = np.array([
    {"name": "Emergency Room Care", "descr": "Immediate evaluation and initial treatment of acute illness or injury in a hospital emergency department.", "parent": 27},
    {"name": "Resuscitative Care", "descr": "Resuscitative care for accident and emergency cases, including basic radiological and laboratory investigations needed to stabilize patient before being moved to the ICU if need be.", "parent": 27},
    {"name": "Emergency Transportation", "descr": "Emergency Transportation from hospital to hospital	Ambulance or medical transport service to transfer a patient from one facility to another for higher level of care or specialised treatment.", "parent": 27},
    {"name": "Intensive Care Unit", "descr": "Intensive Care Unit in Patient Care	Continuous monitoring and management of critically ill patients in an ICU.", "parent": 27}
])

#28
in_patient_care_limit = np.array([
    {"name": "Room Type", "descr": "Accommodation during hospital admission - categories include general ward, semi-private, private, or deluxe, each with different amenities and coverage limits.", "parent": 28},
    {"name": "Nursing Care and Consumables", "descr": "Daily nursing services (vital signs, wound care, medication administration) and disposable items (dressings, gloves, syringes, IV lines) used during admission.", "parent": 28},
    {"name": "Admission", "descr": "Formal acceptance of a patient into a hospital for at least one overnight stay, including bed, meals, routine nursing, and medical care per the treatment plan.", "parent": 28}
])

#29
basic_diagnostic_imaging = np.array([
    # {"name": "Abdominal X-Rays", "descr": "Plain radiograph of the abdomen to detect bowel obstruction, perforation, foreign bodies, calcifications, or abnormal gas patterns.", "parent": 29},
    # {"name": "Neck X-rays", "descr": "Radiograph of the cervical spine and soft tissues of the neck used for fractures, dislocations, airway obstruction, or foreign bodies.", "parent": 29},
    # {"name": "Chest X-Rays", "descr": "Standard posteroanterior (PA) and lateral views of the chest to assess lungs, heart size, ribs, and mediastinum.", "parent": 29},
     {"name": "Limbs X-rays", "descr": "Radiographs of upper and lower extremities to diagnose fractures, dislocations, arthritis, bone tumours, and foreign bodies.", "parent": 29},
    # {"name": "Thoracic Inlet X-rays", "descr": "Specialised view of the thoracic inlet (top of the chest) to assess clavicles, first ribs, lung apices, and subclavian vessels.", "parent": 29},
    # {"name": "Thoraco-Lumbar X-rays", "descr": "Radiograph of the lower thoracic and upper lumbar spine, used for trauma, degenerative changes, or scoliosis evaluation.", "parent": 29},
    # {"name": "Lumbosacral X-Rays", "descr": "X-ray of the lower back (lumbar vertebrae, sacrum, coccyx) for back pain, disc disease, fractures, or spondylolisthesis.", "parent": 29},
    # {"name": "Mandibles or Temporomandibular Joint X-Rays", "descr": "Radiographs of the lower jaw and TMJ, for fractures, dislocations, arthritis, or dental pathology.", "parent": 29},
    # {"name": "X-rays of All Body Joints", "descr": "Plain film imaging of any joint (shoulder, elbow, wrist, hip, knee, ankle) to detect arthritis, effusion, loose bodies, or traumatic injuries.", "parent": 29},
    # {"name": "Sinus X-rays", "descr": "Radiographs of the paranasal sinuses (frontal, maxillary, ethmoidal) to diagnose sinusitis, polyps, or fluid levels.", "parent": 29},
    # {"name": "Mastoid X-rays", "descr": "Imaging of the mastoid bone behind the ear, for chronic otitis media, cholesteatoma, or mastoiditis (largely replaced by CT).", "parent": 29},
    # {"name": "Cervical Spine X-rays", "descr": "Radiograph of the neck vertebrae (C1-C7) for trauma, neck pain, degenerative disease, or instability.", "parent": 29},
    # {"name": "Skull X-rays", "descr": "Plain radiograph of the skull for fractures, calcified intracranial lesions, or sinus abnormalities (largely superseded by CT).", "parent": 29},
    # {"name": "Pelvic X-rays", "descr": "Radiograph of the pelvic bones, hip joints, and sacrum-for fractures, arthritis, or after hip replacement.", "parent": 29},
     {"name": "Prescribed Routine Ultrasound Scans", "descr": "Non-invasive imaging using sound waves for obstetric (fetal growth, placental position), abdominal (liver, gallbladder, kidneys), pelvic (uterus, ovaries), breast, testicular, thyroid, prostate, and bladder examinations.", "parent": 29}

])

#30
advanced_diagnostic_imaging = np.array([
    {"name":"MRI", "descr":"Advanced imaging using a strong magnetic field and radio waves to produce detailed cross-sectional images of soft tissues, brain, spine, joints, and internal organs.","parent":30},
    {"name":"Echocardiography", "descr":"Ultrasound of the heart assessing chamber sizes, wall motion, valve function, and ejection fraction - for heart failure, valvular disease, congenital anomalies.","parent":30},
    {"name":"Proctoscopy", "descr":"Visual examination of the anal canal and lower rectum using a rigid or flexible proctoscope - for haemorrhoids, fissures, polyps, and rectal bleeding.","parent":30},
    {"name":"Sigmoidoscopy", "descr":"Flexible endoscopy of the rectum and sigmoid colon (up to 60 cm) for evaluation of lower GI symptoms (bleeding, diarrhoea, polyps, cancer screening).","parent":30},
    {"name":"Upper GI Endoscopy", "descr":"Endoscopic examination of the oesophagus, stomach, and duodenum - diagnoses ulcers, gastritis, tumours, coeliac disease, and can biopsy or treat bleeding.","parent":30},
    {"name":"Endoscopic retrograde cholangiopancreatography (ERCP)", "descr":"Combined endoscopy and fluoroscopy to visualise the bile and pancreatic ducts, used to remove stones, stent strictures, or biopsy tumours.","parent":30},
    {"name":"Laryngoscopy (Direct and Indirect)", "descr":"Visualisation of the larynx (voice box) and vocal cords. Indirect uses a mirror; direct uses a rigid or flexible laryngoscope - for hoarseness, stridor, or biopsy.", "parent":30},
    {"name":"Bronchoscopy", "descr":"Flexible or rigid endoscopy of the trachea and bronchi - to diagnose lung masses, infections, or airway obstruction, and to lavage or biopsy.","parent":30},
    {"name":"Thoracoscopy", "descr":"Endoscopic examination of the pleural space and lung surfaces, under general anaesthesia for pleural biopsy, talc poudrage, or drainage of empyema.","parent":30},
    {"name":"Hysteroscopy", "descr":"Endoscopic inspection of the uterine cavity, diagnoses polyps, fibroids, adhesions, and septum; can also perform operative procedures (resection, ablation).","parent":30},
    {"name":"Enteroscopy", "descr":"Endoscopic examination of the small intestine (jejunum and ileum) for obscure GI bleeding, polyps, Crohn's disease, or capsule endoscopy with deep enteroscopy.","parent":30},
    {"name":"ECG (PRE AND POST EXERCISE)", "descr":"Electrocardiogram at rest and after physical stress, evaluates heart rhythm and detects coronary artery disease (stress test).","parent":30},
    {"name":"CT Scan", "descr":"Cross-sectional X-ray imaging that creates detailed 3D images of bones, blood vessels, and soft tissues.","parent":30},
    {"name":"Gastroscopy", "descr":"Same as Upper GI Endoscopy, visual examination of the oesophagus, stomach, and duodenum.","parent":30},
    {"name":"Colonoscopy", "descr":"Complete endoscopic examination of the large bowel (caecum to rectum) for colorectal cancer screening, polypectomy, biopsy, and management of inflammatory bowel disease.","parent":30},
    {"name":"Cystoscopy", "descr":"Endoscopic inspection of the urinary bladder and urethra - diagnoses stones, tumours, strictures, or prostatic obstruction; can obtain biopsies or remove stents.","parent":30},
    {"name":"Laparoscopy", "descr":"Minimally invasive surgery of the abdominal cavity using a laparoscope  for cholecystectomy, appendicectomy, hernia repair, and diagnostic exploration.","parent":30}
])

#31
hematological_test = np.array([
    {"name": "Full Blood Count and differentials (FBC)", "descr": "Automated blood test measuring red cells, white cells, platelets, haemoglobin, haematocrit, and white cell differential (neutrophils, lymphocytes, monocytes, eosinophils, basophils).", "parent": 31},
    {"name": "White Blood Cell count", "descr": "Specific count of leukocytes; elevated in infection or inflammation, decreased in bone marrow disorders or certain drugs.", "parent": 31},
    {"name": "Red Blood Cell or Reticulocyte count", "descr": "RBC count (total number of red cells); reticulocyte count assesses bone marrow response to anaemia.", "parent": 31},
    {"name": "Grouping and Cross Matching", "descr": "Determines ABO and Rh blood group and tests compatibility between donor blood and recipient's serum before transfusion.", "parent": 31},
    {"name": "Hemoglobin (HB)", "descr": "Concentration of oxygen-carrying protein in red blood cells; low in anaemia, high in polycythaemia.", "parent": 31},
    {"name": "Packed Cell Volume (PCV)", "descr": "Proportion of blood volume occupied by red cells (haematocrit); used to diagnose anaemia or polycythaemia.", "parent": 31},
    {"name": "MCH", "descr": "Mean corpuscular haemoglobin: average mass of haemoglobin per red cell (normal = 27-31 pg).", "parent": 31},
    {"name": "MCV", "descr": "Mean corpuscular volume: average size of red cells (microcytic, normocytic, macrocytic) helps classify anaemia.", "parent": 31},
    {"name": "Blood Film", "descr": "Microscopic examination of stained blood smear, detects abnormal cell shapes, inclusions, parasites (malaria), and immature cells.", "parent": 31},
    {"name": "Blood Pregnancy (Beta HCG) Test", "descr": "Quantitative or qualitative detection of human chorionic gonadotropin in blood, confirms pregnancy and monitors ectopic or molar pregnancy.", "parent": 31},
    {"name": "White cell count (Total and Differential)", "descr": "Same as white blood cell count with differential, enumerates each leukocyte type.", "parent": 31},
    {"name": "Genotype (on request by clinician)", "descr": "Usually refers to haemoglobin genotype (AA, AS, SS) for sickle cell trait or disease testing.", "parent": 31},
    {"name": "Blood group (on request by clinician)", "descr": "ABO and RhD typing.", "parent": 31},
    {"name": "Erythrocyte Sedimentation Rate (ESR)", "descr": "Non-specific marker of inflammation; elevated in infection, autoimmune disease, malignancy.", "parent": 31},
    {"name": "MCHC", "descr": "Mean corpuscular haemoglobin concentration: average concentration of haemoglobin in a given volume of red cells.", "parent": 31}

])

#32
chemistry_investigations = np.array([
    {"name":"Electrolytes/Urea and Creatinine", "descr":"Basic renal function and electrolyte panel (Na, K, Cl, HCO₃, urea, creatinine) for kidney disease, dehydration, acid-base disorders.", "parent":32},
    {"name":"Lipid Profile (Fasting)", "descr":"Measures total cholesterol, HDL, LDL (calculated), and triglycerides, assesses cardiovascular risk and monitors lipid-lowering therapy.", "parent":32},
    {"name":"Liver Function Test (LFT)", "descr":"Panel including ALT, AST, ALP, GGT, bilirubin, albumin, evaluates hepatocellular injury, cholestasis, and synthetic function.", "parent":32},
    {"name":"Serum Sodium", "descr":"Measures blood sodium level; deranged in dehydration, renal failure, SIADH, adrenal insufficiency.", "parent":32},
    {"name":"Glucose Challenge Test", "descr":"Screening test for gestational diabetes, measures blood glucose 1 hour after 50g glucose load.", "parent":32},
    {"name":"Serum Calcium", "descr":"Total calcium (bound + ionised); abnormal in hyperparathyroidism, bone metastases, renal failure.", "parent":32},
    {"name":"Fasting Blood Sugar", "descr":"Blood glucose after 8-12 hours fasting - diagnostic for diabetes mellitus (≥7.0 mmol/L) and prediabetes.", "parent":32},
    {"name":"Random Blood Sugar", "descr":"Any time glucose measurement; useful for hyperglycaemic or hypoglycaemic symptoms.", "parent":32},
    {"name":"2 Hours Post-prandial Blood Sugar", "descr":"Glucose measured 2 hours after a meal, assesses glycaemic control in diabetes.", "parent":32},
    {"name":"Oral Glucose Tolerance Test (OGTT)", "descr":"Standard 75g glucose load with fasting and 2-hour glucose, gold standard for diagnosis of diabetes and gestational diabetes.", "parent":32},
    {"name":"Serum Alkaline Phosphate", "descr":"Enzyme elevated in liver disease (cholestasis) or bone disease (Paget's, metastases).", "parent":32},
    {"name":"Serum Acid Phosphate", "descr":"Used in past for prostate cancer (now replaced by PSA); also elevated in bone disease.", "parent":32},
    {"name":"Serum Inorganic Phosphate", "descr":"Measures phosphate level, abnormal in renal failure, hyperparathyroidism, vitamin D disorders.", "parent":32},
    {"name":"Serum Bilirubin (Total and Direct)", "descr":"Total bilirubin and conjugated (direct) fraction for jaundice, haemolysis, or hepatobiliary obstruction.", "parent":32},
    {"name":"Serum Albumin", "descr":"Major plasma protein; low in malnutrition, liver disease, nephrotic syndrome, or protein-losing enteropathy.", "parent":32},
    {"name":"Serum Magnesium", "descr":"Magnesium level, low in malnutrition, alcoholism, diuretics; high in renal failure.", "parent":32},
    {"name":"Serum Potasium", "descr":"Key electrolyte for nerve and muscle function; abnormal in renal disease, diuretics, acidosis.", "parent":32},
    {"name":"Serum Lithium", "descr":"Therapeutic drug monitoring for patients on lithium carbonate (bipolar disorder) to avoid toxicity.", "parent":32},
    {"name":"Serum Chloride", "descr":"Electrolyte, often mirrors sodium changes; also used in acid-base evaluation.", "parent":32},
    {"name":"Serum Bicarbonate", "descr":"Measures carbon dioxide content (HCO₃⁻) in blood, low in metabolic acidosis, high in metabolic alkalosis.", "parent":32},
    {"name":"Serum Lactate Dehydrogenase", "descr":"Non-specific marker of cell damage; elevated in haemolysis, myocardial infarction, liver disease, some cancers.", "parent":32},
    {"name":"Serum Gamma Glutamyl Transferase", "descr":"Sensitive indicator of hepatobiliary disease and alcohol use.", "parent":32},
    {"name":"Prothrombin time (PT or INR)", "descr":"Measures extrinsic clotting pathway; used to monitor warfarin therapy and assess liver synthetic function.", "parent":32},
    {"name":"Urine Pregnancy Test", "descr":"Qualitative dipstick or lateral flow test for hCG in urine, rapid confirmation of pregnancy.", "parent":32}
])

#33
microbiology_and_parasitology = np.array([
    {"name":"Skin Snip for Microfilaria", "descr":"Removal of a small skin sample to detect microfilariae (e.g., Onchocerca volvulus causing river blindness).", "parent":33},
    {"name":"Skin Scraping for Fungi", "descr":"Scraping of skin scales or nails for KOH preparation and microscopy, diagnoses dermatophyte or yeast infections.", "parent":33},
    {"name":"Malaria Parasite", "descr":"Microscopic or rapid diagnostic test (RDT) for Plasmodium species in blood.", "parent":33},
    {"name":"Trypanosomes Screening", "descr":"Blood smear or serology for Trypanosoma (African sleeping sickness or Chagas disease).", "parent":33},
    {"name":"Toxoplasma Screening", "descr":"Serological detection of IgG or IgM antibodies for Toxoplasma gondii, important in pregnancy and immunocompromised.", "parent":33},
    {"name":"Leishmania Screening", "descr":"Serology or microscopy for Leishmania parasites causing cutaneous or visceral leishmaniasis.", "parent":33},
    {"name": "Urine M/C/S", "descr": "Microscopy, culture, and sensitivity of urine, diagnoses urinary tract infection and identifies antibiotic susceptibilities.", "parent":33},
    {"name": "Endocervical Swab (ECS) M or C or S", "descr": "Swab from cervix for culture, used for sexually transmitted infections (Chlamydia, Gonorrhoea).", "parent":33},
    {"name": "High Vaginal Swab (HVS) M or C or S", "descr": "Vaginal swab for bacterial vaginosis, candidiasis, or trichomoniasis.", "parent":33},
    {"name": "Urethral Swab M/C/S", "descr": "Male urethral swab for STIs (Neisseria gonorrhoeae, Chlamydia trachomatis).", "parent":33},
    {"name": "Throat Swab M/C/S", "descr": "Swab from oropharynx, for Streptococcus pyogenes (sore throat), diphtheria, or candida.", "parent":33},
    {"name": "Ear Swab M/C/S", "descr": "Swab from external ear canal for otitis externa (bacterial or fungal).", "parent":33},
    {"name": "Wound Swab M/C/S", "descr":"Pus or swab from a wound, identifies pathogens causing soft tissue infection.", "parent":33},
    {"name": "Eye Swab M/C/S", "descr": "Conjunctival or corneal swab for bacterial, viral, or fungal keratitis or conjunctivitis.", "parent":33},
    {"name": "Sputum M/C/S", "descr": "Expectorated sputum, diagnoses pneumonia, bronchitis, or tuberculosis (also AFB smear).", "parent":33},
    {"name": "Aspirates M/C/S", "descr": "Fluid aspirated from abscess, joint, pleural, or peritoneal cavity for culture.", "parent":33},
    {"name": "Stool M/C/S", "descr": "Stool culture for enteric pathogens (Salmonella, Shigella, Campylobacter, E. coli O157).", "parent":33},
    {"name": "VDRL (Veneral Disease Research Laboratory) Test (unless where disallowed by diagnosis)", "descr": "Screening test for syphilis (non-treponemal); reactive requires confirmatory TPHA.", "parent":33},
    {"name": "H.Pylori", "descr": "Urea breath test, stool antigen, or biopsy, diagnoses Helicobacter pylori infection (peptic ulcer disease).", "parent":33},
    {"name": "Mantoux/Heaf's Test", "descr": "Intradermal tuberculin test for latent tuberculosis infection (not diagnostic of active TB).", "parent":33},
    {"name": "Blood Culture", "descr": "Collection of blood into culture bottles to detect bacteraemia or fungaemia, identifies pathogen and susceptibilities.", "parent":33},
    {"name": "Stool Occult Blood", "descr": "Detects hidden blood in stool - screening for colorectal cancer or gastrointestinal bleeding.", "parent":33}
])

#34
advanced_laboratory_investigations_pathology = np.array([
    {"name": "Blood urea Nitrogen", "descr":"Measures urea nitrogen - part of renal function panel.", "parent": 34},
    {"name": "Hepatitis B Surface Antigen (HBSAg)", "descr": "Marker of active hepatitis B infection (acute or chronic).", "parent": 34},
    {"name": "HIV Screening", "descr": "ELISA or rapid test for antibodies to HIV (or p24 antigen), screening for HIV infection.", "parent": 34},
    {"name": "HIV Confirmatory Test", "descr": "Western blot or PCR to confirm a positive screening test.", "parent": 34},
    {"name": "G-6PD Screening", "descr": "Detects glucose-6-phosphate dehydrogenase deficiency - important before certain drugs (e.g., primaquine, dapsone).", "parent": 34},
    {"name": "Thyroid Function Tests", "descr": "TSH, free T4, and sometimes free T3, evaluates thyroid status (hypo or hyperthyroidism).", "parent": 34},
    {"name": "Serum Uric Acid", "descr": "Measures uric acid, elevated in gout, renal insufficiency, or leukaemia.", "parent": 34},
    {"name": "HBA1C", "descr": "Glycated haemoglobin, reflects average blood glucose over 2-3 months; used for diabetes diagnosis and monitoring.", "parent": 34},
    {"name": "Hepatitis C Screening", "descr": "Anti-HCV antibody test; positive requires confirmatory HCV RNA.", "parent": 34},
    {"name": "Hepatitis B Screening", "descr": "Panel to diagnose HBV infection, immunity (post-vaccine), or past infection.", "parent": 34},
    {"name": "Creatinine phosphokinase", "descr": "Enzyme elevated in muscle damage (myocardial infarction, rhabdomyolysis, muscular dystrophy).", "parent": 34},
    {"name": "Syphilis Screening", "descr": "RPR/VDRL or TPHA; part of antenatal and STI screening.", "parent": 34},
    {"name": "CSF M/C/S (CSF Analysis)", "descr": "Cerebrospinal fluid examination, cell count, protein, glucose, culture for meningitis.", "parent": 34},
    {"name": "Semen M/C/S", "descr": "Semen culture, diagnoses prostatitis or epididymitis.", "parent": 34},
    {"name": "Serum Iron", "descr": "Measures circulating iron, used in evaluation of anaemia and iron overload.", "parent": 34},
    {"name": "24 Hour Creatinine Clearance", "descr": "Urine and blood creatinine to estimate glomerular filtration rate.", "parent": 34},
    {"name": "Coomb's Test (Indirect)", "descr": "Detects free antibodies in serum, used for crossmatching, antenatal screening, or diagnosing immune haemolysis.", "parent": 34},
    {"name": "Coomb's Test (Direct)", "descr": "Detects antibodies or complement attached to red cells, positive in autoimmune haemolytic anaemia or haemolytic disease of the newborn.", "parent": 34},
    {"name": "Osmotic Fragility Test", "descr": "Detects spherocytosis (hereditary or acquired) by measuring red cell resistance to hypotonic solution.", "parent": 34},
    {"name": "Pap Smear and Cytology", "descr": "Cervical cytology screening for precancerous or cancerous changes.", "parent": 34},
    {"name": "Prostate Specific Antigen", "descr": "PSA blood test for prostate cancer screening.", "parent": 34},
    {"name": "Protein Electrophoresis", "descr": "Serum or urine electrophoresis, detects monoclonal gammopathy (multiple myeloma) or other protein abnormalities.", "parent": 34},
    {"name": "Chlamydia Screening", "descr": "NAAT (nucleic acid amplification test) on urine or swab for Chlamydia trachomatis.", "parent": 34},
    {"name": "Seminal Fluid Analysis (SFA)", "descr": "Sperm count, motility, morphology, for male infertility investigation.", "parent": 34},
    {"name": "Clotting Time", "descr": "Time taken for blood to clot, used to assess coagulation disorders (often replaced by PT/APTT).", "parent": 34},
    {"name": "Bleeding Time", "descr": "Measures platelet function and vascular integrity, prolonged in platelet disorders or von Willebrand disease.", "parent": 34},
    {"name": "D-Dimer", "descr": "Blood test for fibrin degradation products; elevated in deep vein thrombosis, pulmonary embolism, DIC.", "parent": 34},
    {"name": "Sputum Acid Fast Bacilli (AFB) Test", "descr": "Ziehl-Neelsen stain or GeneXpert for Mycobacterium tuberculosis (pulmonary TB).", "parent": 34},

])

#35
eye_optical_care = np.array([
    {"name":"Specialist Opthalmologist Consultation", "descr":"An eye examination performed by an ophthalmologist (medical eye specialist) to diagnose and manage diseases of the eye.", "parent": 35},
    {"name":"Basic ocular tests", "descr":"Standard eye assessments: intraocular pressure measurement, refractive error, fundus (retina) exam, corneal thickness, and anterior segment examination.", "parent": 35},
    {"name":"Pharmacological treatment of acute and chronic ocular infections", "descr":"Prescription of topical or systemic antibiotics, antivirals, antifungals, or anti-inflammatory agents for conditions such as conjunctivitis, keratitis, uveitis.", "parent": 35},
    {"name":"Advanced Ocular tests", "descr":"Specialised diagnostic tests: visual field perimetry, peripheral retina view, stereopsis, dry eye assessment, macular function, retinal imaging, optical coherence tomography, biometry (A-scan), and ultrasound (B-scan) for posterior segment.", "parent": 35},
    {"name":"Biennial Lenses and Frames", "descr":"Provision of prescription spectacles or contact lenses every two years.", "parent": 35},
])

#36
dental_care = np.array([
    {"name": "Scaling and Polishing", "descr": "Professional removal of plaque, calculus (tartar), and stain from tooth surfaces, prevents gingivitis and periodontitis.", "parent": 36},
    {"name": "Routine dental examination", "descr": "Visual and radiographic assessment of teeth, gums, and oral mucosa, detects caries, periodontal disease, oral cancer.", "parent": 36},
    {"name": "Preventive dental care and counselling", "descr": "Fluoride application, fissure sealants, oral hygiene instruction, dietary advice, and smoking cessation counselling.", "parent": 36},
    {"name": "Dental pain therapy", "descr": "Management of acute dental pain using analgesics, antibiotics (for abscess), and local anaesthesia with temporary filling if needed.", "parent": 36},
    {"name": "Surgical extraction", "descr": "Removal of a tooth that requires incision of the gum tissue, elevation of a flap, and possible bone removal.", "parent": 36},
    {"name": "Non-surgical extraction", "descr": "Simple extraction of a mobile or fully erupted tooth using forceps without raising a surgical flap; usually performed under local anaesthesia.", "parent": 36},
    {"name": "Root Canal Therapy", "descr": "Endodontic procedure involving removal of infected or necrotic pulp from the root canal system, followed by cleaning, shaping, disinfection, and obturation (filling) to save a tooth that would otherwise require extraction.", "parent": 36},
    {"name": "Pharmacological treatment of acute and chronic dental infections", "descr": "Use of antibiotics, analgesics, anti-inflammatory agents, and antiseptic mouth rinses to manage conditions.", "parent": 36},
    {"name": "Operculectomy", "descr": "Excision of the operculum (the flap of gum tissue) overlying a partially erupted tooth, usually a third molar, to relieve pain, inflammation, and food trapping (pericoronitis).", "parent": 36},
    {"name": "Gingival Curettage", "descr": "Deep scaling and root planing of the gingival sulcus to remove inflamed soft tissue, subgingival calculus, and bacterial biofilm; part of non-surgical periodontal therapy.", "parent": 36},
    {"name": "Composite Filling", "descr": "Tooth-coloured resin material used to restore dental caries, chipped teeth, or close diastemas; bonded directly to the tooth structure for a natural appearance.", "parent": 36},
    {"name": "Amalgam Filling", "descr": "Durable silver-mercury alloy filling used primarily for posterior teeth; provides high compressive strength and resistance to wear.", "parent": 36},
    {"name": "Incision and Drainage", "descr": "Minor surgical procedure to open and drain pus from a dental abscess (periapical, periodontal, or pericoronal), relieving pressure, pain, and preventing spread of infection.", "parent": 36}
])

#37
physiotherapy_care = np.array([
    #{"name": "Specialist Consultation", "descr": "A visit to a physician or dentist with advanced training in a specific field for diagnosis, treatment planning, or management of complex cases.", "parent": 37},
    {"name": "Preventive Counselling on referral", "descr": "Advice provided by a healthcare professional after a medical referral, focusing on lifestyle modifications, posture, ergonomics, nutrition, or oral hygiene to prevent disease or injury recurrence.", "parent": 37},
    {"name": "Cervical Collar and Crutches", "descr": "Orthopaedic devices: cervical collars (soft or rigid) for neck support and immobilisation; crutches (axillary or forearm) to assist mobility in lower limb injuries or surgeries.", "parent": 37},
    {"name": "Pain therapy", "descr": "Non-pharmacological and pharmacological management of acute or chronic pain using modalities such as electrotherapy (TENS, ultrasound), heat or cold packs, manual therapy, therapeutic exercises, and prescribed analgesics.", "parent": 37},
    {"name": "Access to prescribed drugs", "descr": "Provision of medications from a formulary list, dispensed at network pharmacies under a doctor's prescription, often within a health insurance benefit.", "parent": 37},
    {"name": "Number of Sessions Covered", "descr": "Predefined limit (e.g., 6-12 sessions per year) for a specific service such as physiotherapy, counselling, or gym attendance, beyond which additional sessions may require re-authorisation or out-of-pocket payment.", "parent": 37}

])

#38
obstetrics_and_gynaecology_care = np.array([
    {"name": "Antenatal Care (Including all specialist care and anc drugs)", "descr": "Comprehensive pregnancy care: regular check-ups, blood pressure monitoring, urine testing, ultrasound scans, screening for anaemia, diabetes, infections, and prescribed medications.", "parent": 38},
    {"name": "Delivery (SVD or Normal and Complicated)", "descr": "Spontaneous vaginal delivery without (normal) or with complications such as shoulder dystocia, postpartum haemorrhage, retained placenta, or perineal tears requiring active medical or surgical intervention.", "parent": 38},
    {"name": "Delivery (Multiple)", "descr": "Vaginal or caesarean delivery of twins, triplets, or higher-order multiples; requires additional personnel, monitoring, equipment, and often longer hospital stay.", "parent": 38},
    {"name": "Assisted Delivery", "descr": "Use of forceps or vacuum extractor to facilitate vaginal delivery when maternal pushing is ineffective, fetal distress occurs, or to shorten the second stage of labour.", "parent": 38},
    {"name": "Therapeutic Abortion (Manual Vacuum Aspiration)", "descr": "First-trimester termination of pregnancy using a handheld aspirator to remove uterine contents; performed under local anaesthesia or conscious sedation.", "parent": 38},
    {"name": "Caesarian Section (Emergency covered to surgical limit)", "descr": "Surgical delivery of the fetus through abdominal and uterine incisions due to fetal distress, failed labour, placental abruption, or maternal complications; coverage is provided up to the surgical limit defined in the health plan.", "parent": 38}
])

#39
infertility_care = np.array([
    {"name": "Fertility  Specialist Consultation and Counselling", "descr": "Evaluation by a reproductive endocrinologist/infertility specialist, including medical history, physical examination, and discussion of treatment options (ovulation induction, intrauterine insemination, IVF, etc.).", "parent": 39},
    {"name": "Fertility  Investigations", "descr": "Diagnostic tests for infertility: hormonal assays (FSH, LH, oestradiol, progesterone, AMH), semen analysis, hysterosalpingography (tubal patency), ultrasound follicular tracking, and genetic screening.", "parent": 39}
])

#40
npi_immunization = np.array([
    {"name": "Vitamin A", "descr": "High-dose vitamin A supplements given every 6 months to children aged 6-59 months to prevent childhood blindness, reduce infection-related mortality, and support immune function.", "parent": 40},
    {"name": "Measles", "descr": "Live attenuated measles vaccine, administered at 9 months (and sometimes a second dose at 18 months) as part of routine immunisation.", "parent": 40},
    {"name": "Bcg", "descr": "Bacillus Calmette-Guérin vaccine against tuberculosis; given at birth or first contact to prevent severe forms of TB (miliary, meningitis) in children.", "parent": 40},
    {"name": "Opv Or Ipv", "descr": "Oral polio vaccine (OPV - live attenuated) or inactivated polio vaccine (IPV) used to eradicate poliomyelitis; given at birth and subsequent doses.", "parent": 40},
    {"name": "Pentavalent", "descr": "Combined vaccine protecting against diphtheria, tetanus, pertussis, hepatitis B, and Haemophilus influenzae type b (Hib); given at 6, 10, and 14 weeks.", "parent": 40},
    {"name": "Hepatitis B", "descr": "Vaccine against hepatitis B virus; birth dose within 24 hours, then as part of pentavalent or hexavalent schedule.", "parent": 40},
    {"name": "Dpt", "descr": "Diphtheria, tetanus, pertussis (whole cell or acellular) vaccine; given at 6, 10, 14 weeks and booster doses later.", "parent": 40},
    {"name": "Yellow Fever", "descr": "Live attenuated yellow fever vaccine for travel to endemic areas or as part of routine immunisation in endemic countries; given at 9 months and every 10 years thereafter.", "parent": 40}
])

#41
additional_immunization_0_5_Years = np.array([
    {"name": "Chicken Pox", "descr": "Varicella vaccine, administered in two doses (first at 12-15 months, second at 4-6 years) to prevent chickenpox.", "parent": 41},
    {"name": "Mmr", "descr": "Measles, mumps, rubella vaccine; first dose at 12-15 months, second dose at 4-6 years.", "parent": 41},
    {"name": "Pneumococcal", "descr": "Pneumococcal conjugate vaccine (PCV10 or PCV13) against Streptococcus pneumoniae; prevents pneumonia, meningitis, and otitis media in children.", "parent": 41},
    {"name": "Meningitis", "descr": "Meningococcal conjugate vaccine (MenACWY or MenC) for prevention of meningitis and septicaemia caused by Neisseria meningitidis.", "parent": 41},
    {"name": "Rotavirus", "descr": "Oral live attenuated vaccine given in 2-3 doses (usually at 6, 10, and 14 weeks) to prevent severe diarrhoea and vomiting from rotavirus infection.", "parent": 41}
])

#42
additional_immunization_6_Years_And_Above = np.array([
    {"name": "Yellow Fever", "descr": "Live attenuated yellow fever vaccine for travel to endemic areas or as part of routine immunisation in endemic countries; given at 9 months and every 10 years thereafter.", "parent": 42}
])

#43
family_planning_out_patient_limit = np.array([
    {"name": "Contraceptive Pills", "descr": "Oral hormonal contraceptives (combined oestrogen-progestin or progestin-only) taken daily to prevent ovulation and pregnancy.", "parent": 43},
    {"name": "Jadelle Implant", "descr": "Two-rod levonorgestrel implant inserted subdermally in the upper arm, effective for up to 5 years for long-term reversible contraception.", "parent": 43},
    {"name": "Implanon", "descr": "Single-rod etonogestrel implant inserted subdermally, effective for 3 years.", "parent": 43},
    {"name": "Copper T Intrauterine Device", "descr": "Non-hormonal T-shaped intrauterine device (IUD) containing copper, effective for 5-10 years; acts by inhibiting sperm motility and fertilisation.", "parent": 43},
    {"name": "Injectibles", "descr": "Progestin-only injectable contraceptives: Depo-Provera (medroxyprogesterone acetate) every 3 months; Noristerat (norethisterone enanthate) every 2 months.", "parent": 43},
    {"name": "Norplant", "descr": "Six-capsule levonorgestrel subdermal implant (older system, largely replaced by Jadelle or Implanon), effective for up to 5 years.", "parent": 43}
])

#44
gym_discounted = np.array([
    {"name":"Gym Services At Network Gym Centres", "descr":"Access to physical fitness facilities (treadmills, weight machines, group classes) at partner gyms, often with a discounted or limited number of sessions per month under a wellness benefit.", "parent":44},
    {"name":"PA", "descr":"Personal Assistant: non-medical administrative support to help beneficiaries with claims filing, appointment scheduling, and other plan-related tasks.", "parent":44},
    {"name":"Facials", "descr":"Cosmetic skin treatment including cleansing, exfoliation, extraction, and mask application; non-medical, may be offered as a discounted wellness add-on.", "parent":44},
    {"name":"Body Massage", "descr":"Therapeutic manipulation of soft tissues for relaxation, stress reduction, or muscle pain relief; non-medical, limited sessions may be covered under wellness benefits.", "parent":44}
])

#45
routine_drugs = np.array([
    {"name": "Prescribed Drugs At Designated Pharmacies", "descr": "Dispensing of medications from an approved formulary at network pharmacies, covered under the outpatient drug benefit, with possible copayment.", "parent": 45}
])

#46
surgeries = np.array([
    {"name": "Minor Surgeries",	"descr": "Low-risk, short-duration (<30 minutes) procedures often under local anaesthesia, e.g., excision of skin lesion, incision & drainage, nail bed repair, simple circumcision.","parent": 46},
    {"name": "Intermediate Surgeries", "descr": "Moderate-risk procedures lasting 30-120 minutes, usually under regional or general anaesthesia, e.g., hernia repair, tonsillectomy, laparoscopic appendicectomy, varicose vein surgery, arthroscopy.", "parent": 46},
    {"name": "Major Surgeries", "descr": "High-complexity, prolonged (>120 minutes) or life-threatening procedures requiring ICU care, e.g., coronary artery bypass, craniotomy, joint replacement, major cancer resections (colectomy, nephrectomy).", "parent": 46}
])

#47
cancer_screening_care = np.array([
    {"name": "Oncologist Or Cancer Specialist Visits", "descr": "Consultations with medical, radiation, or surgical oncologists for diagnosis, staging, treatment planning, and follow-up care of cancer patients.", "parent": 47},
    {"name": "Oncological Investigations", "descr": "Laboratory tests to diagnose or monitor cancer: tumour markers (CEA, CA-125, PSA), immunohistochemistry, flow cytometry, cytogenetics, molecular profiling, and histopathology review.", "parent": 47},
    {"name": "Cancer-Related Radiological Investigations", "descr": "Imaging studies for detection, staging, and treatment monitoring: CT, MRI, PET-CT, mammography, ultrasound, bone scan, and plain X-rays.", "parent": 47},
    {"name": "Surgical Cancer Care", "descr": "Operative procedures for cancer, including tumour resection (e.g., mastectomy, lobectomy, colectomy), lymph node dissection, and debulking of metastatic disease.", "parent": 47},
    {"name": "Chemotherapy", "descr": "Systemic treatment of cancer using cytotoxic drugs, targeted therapy, immunotherapy, or hormonal agents, often given intravenously or orally, with supportive medications (antiemetics, growth factors).", "parent": 47}
])

#48
renal_care = np.array([
    {"name": "Dialysis And All Related Care", "descr": "Renal replacement therapy (haemodialysis 3x per week or peritoneal dialysis), including vascular access creation/maintenance (fistula, catheter), dialysate supplies, laboratory monitoring, and management of complications (anaemia, bone disease, hyperkalaemia).", "parent": 48}
])

#49
wellness_checks = np.array([
    #{"name": "Blood Sugar Check (Diabetes Screening)", "descr": "Capillary or venous glucose measurement (fasting or random) to screen for hyperglycaemia or monitor diabetes control.", "parent": 49},
    #{"name": "Serum Cholesterol", "descr": "Laboratory measurement of total cholesterol, HDL cholesterol, LDL cholesterol (calculated), and triglycerides for cardiovascular risk assessment.", "parent": 49},
    #{"name": "Annual Visual Acuity Check (Using Snellen Chart)", "descr": "Standard eye chart test to measure distance vision and detect refractive errors; performed annually as a screening tool.", "parent": 49},
    #{"name": "Mammography (For Women ≥ 40 Years Of Age)", "descr": "Low-dose X-ray of the breast recommended every 1-2 years for early detection of breast cancer in women aged 40 and above.", "parent": 49},
    #{"name": "Bmi Check", "descr": "Calculation of body mass index (weight in kg divided by height in m²) to classify underweight, normal weight, overweight, or obesity.", "parent": 49},
    #{"name": "Physical Examination", "descr": "General medical assessment including vital signs (temperature, pulse, respiration, blood pressure), inspection, palpation, percussion, auscultation, and basic neurological evaluation.", "parent": 49},
    #{"name": "General Physical Examination", "descr": "Comprehensive head-to-toe examination covering all major body systems (cardiovascular, respiratory, abdominal, musculoskeletal, neurological, skin, etc.).", "parent": 49},
    #{"name": "Blood Pressure Check (Hypertension Screening)", "descr": "Non-invasive measurement of systolic and diastolic blood pressure using an oscillometric or auscultatory device to screen for hypertension.", "parent": 49},
    #{"name": "Pap Smear Every 2Years For Women Above 35 Years", "descr": "Cervical cytology screening (Papanicolaou test) performed every two years for women aged over 35 years to detect precancerous or cancerous changes of the cervix.", "parent": 49},
    #{"name": "Psa Check (For Men ≥ 40 Years Of Age)", "descr": "Prostate-specific antigen blood test for early detection of prostate cancer in men aged 40 years and older.", "parent": 49},
    #{"name": "Liver Function Test", "descr": "Panel of blood tests (ALT, AST, ALP, GGT, bilirubin, albumin) to assess hepatocellular injury, cholestasis, and synthetic function of the liver.", "parent": 49},
    {"name": "Kidney Function Tests", "descr": "Measurement of electrolytes (sodium, potassium, chloride, bicarbonate), urea, and creatinine to evaluate renal function and acid-base balance.", "parent": 49},
   # {"name": "Urinalysis", "descr": "Dipstick and microscopic examination of urine for glucose, protein, blood, leukocytes, nitrites, ketones, and casts; used in screening for urinary tract infections, kidney disease, and diabetes.", "parent": 49},
    #{"name": "Chest X-Ray", "descr": "Plain radiograph of the chest (posteroanterior and lateral views) to evaluate lungs, heart, mediastinum, ribs, and pleura for conditions such as pneumonia, heart failure, tuberculosis, or masses.", "parent": 49}
])

#217
incubator_care = np.array([
  {"name": "Special Care baby Unit", "descr": "Neonatal intensive care for premature or critically ill newborns, including incubators, respiratory support (ventilators, ICU,Life support,phototherapy), haemodynamic monitoring, life support, and phototherapy for neonatal jaundice.", "parent": 217},
 # {"name": "Male Circumcision and Ear piercing within first 6 wks", "descr": "Newborn circumcision (often for cultural or religious reasons) and ear piercing performed during the first six weeks of life; covered under the inpatient (IPT) limit of the health plan.", "parent": 217}
])

#50
psychiatry_care = np.array([
     {"name": "Mental Illness Care With Certified Psychiatrists(Outpatient Care Only)", "descr": "Outpatient psychiatric care including diagnosis, medication management, and follow-up for conditions such as depression, anxiety, bipolar disorder, schizophrenia, and substance use disorders.", "parent": 50},
    {"name": "Stress Management", "descr": "Non-pharmacological interventions (counselling, relaxation techniques, mindfulness, breathing exercises, lifestyle modification) to reduce perceived stress and improve coping.", "parent": 50}
])

#51
hiv_care_and_treatment_at_designated_sites = np.array([
    {"name": "Specialist Drug Therapy", "descr": "Prescription of specialised medications (e.g., antipsychotics, immunosuppressants, chemotherapy agents, biologics) typically managed by a specialist rather than a general practitioner.", "parent": 51},
    {"name": "Counselling Sessions", "descr": "Structured talk therapy (e.g., cognitive behavioural therapy, interpersonal therapy, family counselling) provided by a psychologist or trained counsellor to address mental health concerns.", "parent": 51}
])

#52
seeking_second_opinion = np.array([
    {"name": "Diagnosis Confirmation From Secondary And Tertiary Care Centres", "descr": "Referral of a patient to a higher-level facility (secondary or tertiary hospital) to obtain a definitive diagnosis through advanced investigations or specialist review.", "parent": 52},
    {"name": "Line Of Treatment Confirmation From Secondary And Tertiary Care Centres", "descr": "Validation of a proposed treatment plan by a second consultant or a multidisciplinary team at a secondary or tertiary care centre to ensure appropriateness before proceeding.", "parent": 52}
])
#53
mortuary_services = np.array([
    {"name": "After-Demise Compensation", "descr": "A fixed monetary benefit paid to the nominee or beneficiary of a health insurance plan member upon the death of the member; unrelated to specific healthcare service costs.", "parent": 53}
])
