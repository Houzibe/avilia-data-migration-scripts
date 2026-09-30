#-------------------------------------------------------------
# DATA MIGRATION: CATEGORISE PRODUCTS
#-------------------------------------------------------------
import numpy as np
import pandas as pd
import requests as req
#from data.categorise_products_data import *
#from data.r3.s3__misc import *
#from data.r3.s3_A import *
#from data.r3.s3_B import *
#from data.r3.s3_C import *
#from data.r3.s3_D import *
#from data.r3.s3_E import *
#from data.r3.s3_F import *
#from data.r3.s3_G import *
#from data.r3.s3_H import *
#from data.r3.s3_I import *
#from data.r3.s3_J import *
#from data.r3.s3_K import *
#from data.r3.s3_L import *
#from data.r3.s3_M import *
#from data.r3.s3_N import *
from data.r3.s3_O import *
#from data.r2.s2_P import *
#from data.r2.s2_Q import *
#from data.r2.s2_R import *
#from data.r2.s2_S import *
#from data.r2.s2_T import *
#from data.r2.s2_U import *
#from data.r1.s1_V import *
#from data.r1.s1_W import *
#from data.r1.s1_X import *


print("\n")
print("="*50)
print("         SCRIPT TO LOAD PRODUCTS")
print("="*50)

#Load config file
config_f = pd.read_json("../config.json")

endpoint = "https://api.testing.lemunz.io/"
login_user = None
connID = None
error_categorising_products = np.array([])
succeed_categorising_products = np.array([])
categorise_products_data = np.array([])
"""
#categorise_products_data = np.append(categorise_products_data, Prescribed_Medications_for_Out_patient_covered_care)
categorise_products_data = np.append(categorise_products_data, hours_Post_prandial_Blood_Sugar)
categorise_products_data = np.append(categorise_products_data, hour_Creatinine_Clearance)
categorise_products_data = np.append(categorise_products_data, Abdominal_X_Rays)
categorise_products_data = np.append(categorise_products_data, Accident_And_Emergency_Care_Out_Patient)
#categorise_products_data = np.append(categorise_products_data, Access_To_Prescribed_Drugs)
#categorise_products_data = np.append(categorise_products_data, Accident_And_Emergency_Care_Out_Patient)
categorise_products_data = np.append(categorise_products_data, Additional_Immunization_0_5_Years)
categorise_products_data = np.append(categorise_products_data, Additional_Immunization_6_Years_And_Above)
#categorise_products_data = np.append(categorise_products_data, Admission)
categorise_products_data = np.append(categorise_products_data, Advanced_Diagnostic_Imaging) 
categorise_products_data = np.append(categorise_products_data, Advanced_Laboratory_Investigations_Pathology)
categorise_products_data = np.append(categorise_products_data, Advanced_Ocular_tests)
#categorise_products_data = np.append(categorise_products_data, After_Demise_Compensation)
categorise_products_data = np.append(categorise_products_data, Amalgam_Filling)
categorise_products_data = np.append(categorise_products_data, Antenatal_Care_Including_all_specialist_care_and_anc_drugs)
#categorise_products_data = np.append(categorise_products_data, Annual_Visual_Acuity_Check)
#categorise_products_data = np.append(categorise_products_data, Aspirates_M_C_S)
categorise_products_data = np.append(categorise_products_data, Assisted_Delivery)
categorise_products_data = np.append(categorise_products_data, Basic_Diagnostic_Imaging)
categorise_products_data = np.append(categorise_products_data, Basic_Lab_Investigations_or_Xrays_and_Ultrasound)
categorise_products_data = np.append(categorise_products_data, Basic_ocular_tests)
categorise_products_data = np.append(categorise_products_data, Bcg)
#categorise_products_data = np.append(categorise_products_data, Biennial_Lenses_And_Frames)
categorise_products_data = np.append(categorise_products_data, Bleeding_Time)
#categorise_products_data = np.append(categorise_products_data, Blood_Culture)
categorise_products_data = np.append(categorise_products_data, Blood_Film)
#categorise_products_data = np.append(categorise_products_data, Blood_group_on_request_by_clinician)
categorise_products_data = np.append(categorise_products_data, Blood_Pregnancy_Beta_HCG_Test)
#categorise_products_data = np.append(categorise_products_data, Blood_Pressure_Check_Hypertension_Screening)
#categorise_products_data = np.append(categorise_products_data, Blood_Sugar_Check_Diabetes_Screening)
categorise_products_data = np.append(categorise_products_data, Blood_urea_Nitrogen)
#categorise_products_data = np.append(categorise_products_data, bmi_check)
categorise_products_data = np.append(categorise_products_data, Body_Massage)
categorise_products_data = np.append(categorise_products_data, Bronchoscopy)
categorise_products_data = np.append(categorise_products_data, Caesarian_Section_Emergency_covered_to_surgical_limit)
categorise_products_data = np.append(categorise_products_data, Cancer_Screening_Care)
categorise_products_data = np.append(categorise_products_data, Cancer_Related_Radiological_Investigations)
categorise_products_data = np.append(categorise_products_data, Cardiologist)
categorise_products_data = np.append(categorise_products_data, Cardiothoracic_Surgeon)
categorise_products_data = np.append(categorise_products_data, Cervical_Collar_and_Crutches)
#categorise_products_data = np.append(categorise_products_data, Cervical_Spine_X_rays)
categorise_products_data = np.append(categorise_products_data, Chemistry_Investigations)
categorise_products_data = np.append(categorise_products_data, Chemotherapy)
categorise_products_data = np.append(categorise_products_data, Chest_X_Ray)
#categorise_products_data = np.append(categorise_products_data, Chest_X_Rays)
categorise_products_data = np.append(categorise_products_data, Chicken_Pox)
#categorise_products_data = np.append(categorise_products_data, Chlamydia_Screening)
categorise_products_data = np.append(categorise_products_data, Clotting_Time)
categorise_products_data = np.append(categorise_products_data, Colonoscopy)
#categorise_products_data = np.append(categorise_products_data, Composite_Filling)
categorise_products_data = np.append(categorise_products_data, Contraceptive_Pills)
categorise_products_data = np.append(categorise_products_data, Coomb_s_Test_Direct)
categorise_products_data = np.append(categorise_products_data, Coomb_s_Test_Indirect)
#categorise_products_data = np.append(categorise_products_data, Copper_T_Intrauterine_Device)
#categorise_products_data = np.append(categorise_products_data, Counselling_Sessions)
#categorise_products_data = np.append(categorise_products_data, creatinine_phosphokinase)
categorise_products_data = np.append(categorise_products_data, CSF_M_C_S_CSF_Analysis)
categorise_products_data = np.append(categorise_products_data, CT_Scan)
categorise_products_data = np.append(categorise_products_data, Cystoscopy)
categorise_products_data = np.append(categorise_products_data, D_Dimer)
categorise_products_data = np.append(categorise_products_data, Delivery_Multiple)
categorise_products_data = np.append(categorise_products_data, Delivery_SVD_or_Normal_and_Complicated)
categorise_products_data = np.append(categorise_products_data, Dental_Care)
#categorise_products_data = np.append(categorise_products_data, Dental_consultation)
categorise_products_data = np.append(categorise_products_data, Dental_pain_therapy)
categorise_products_data = np.append(categorise_products_data, Dermatologist)
categorise_products_data = np.append(categorise_products_data, Diagnosis_Confirmation_From_Secondary_And_Tertiary_Care_Centres)
categorise_products_data = np.append(categorise_products_data, Dialysis_And_All_Related_Care)
#categorise_products_data = np.append(categorise_products_data, Dietician_or_Nutritionist)
#categorise_products_data = np.append(categorise_products_data, Dpt)
#categorise_products_data = np.append(categorise_products_data, ECG_PRE_AND_POST_EXERCISE)
#categorise_products_data = np.append(categorise_products_data, ear_swab_m_c_s)
#categorise_products_data = np.append(categorise_products_data, ecg_pre_and_post_exercise)
categorise_products_data = np.append(categorise_products_data, Echocardiography)
categorise_products_data = np.append(categorise_products_data, Electrolytes_Urea_and_Creatinine)
#categorise_products_data = np.append(categorise_products_data, Emergency_Room_Care)
categorise_products_data = np.append(categorise_products_data, Emergency_Transportation)
categorise_products_data = np.append(categorise_products_data, Endocervical_Swab_ECS_M_or_C_or_S)
#categorise_products_data = np.append(categorise_products_data, Endocrinologist)
categorise_products_data = np.append(categorise_products_data, Endoscopic_retrograde_cholangiopancreatography_ERCP)
#categorise_products_data = np.append(categorise_products_data, ent_surgeon_otorhinolaryngologist)
categorise_products_data = np.append(categorise_products_data, Enteroscopy)
#categorise_products_data = np.append(categorise_products_data, Erythrocyte_Sedimentation_Rate_ESR)
categorise_products_data = np.append(categorise_products_data, Eye_Swab_M_C_S)
categorise_products_data = np.append(categorise_products_data, Eye_Optical_Care)
categorise_products_data = np.append(categorise_products_data, Facials)
categorise_products_data = np.append(categorise_products_data, Family_Physician)
categorise_products_data = np.append(categorise_products_data, Family_Planning_Out_Patient_Limit)
#categorise_products_data = np.append(categorise_products_data, Fasting_Blood_Sugar)
categorise_products_data = np.append(categorise_products_data, Fertility_Investigations)
categorise_products_data = np.append(categorise_products_data, Fertility_Specialist_Consultation_and_Counselling)
categorise_products_data = np.append(categorise_products_data, Full_Blood_Count_and_differentials_FBC)
categorise_products_data = np.append(categorise_products_data, G_6PD_Screening)
categorise_products_data = np.append(categorise_products_data, Gastroenterologist)
categorise_products_data = np.append(categorise_products_data, Gastroscopy)
categorise_products_data = np.append(categorise_products_data, General_Consultation)
categorise_products_data = np.append(categorise_products_data, General_Physical_Examination)
categorise_products_data = np.append(categorise_products_data, General_Surgeon)
#categorise_products_data = np.append(categorise_products_data, Genotype_on_request_by_clinician)
#categorise_products_data = np.append(categorise_products_data, genotype)
categorise_products_data = np.append(categorise_products_data, Gingival_Curettage)
#categorise_products_data = np.append(categorise_products_data, Glucose_Challenge_Test)
categorise_products_data = np.append(categorise_products_data, Grouping_and_Cross_Matching)
categorise_products_data = np.append(categorise_products_data, Gym_Services_At_Network_Gym_Centres)
#categorise_products_data = np.append(categorise_products_data, Gym_Discounted)
categorise_products_data = np.append(categorise_products_data, Gynaecologist)
categorise_products_data = np.append(categorise_products_data, H_Pylori)
categorise_products_data = np.append(categorise_products_data, HBA1C)
categorise_products_data = np.append(categorise_products_data, Hematological_Test)
categorise_products_data = np.append(categorise_products_data, Hematologist)
categorise_products_data = np.append(categorise_products_data, Hemoglobin_HB)
categorise_products_data = np.append(categorise_products_data, Hepatitis_B)
categorise_products_data = np.append(categorise_products_data, Hepatitis_B_Screening)
categorise_products_data = np.append(categorise_products_data, Hepatitis_B_Surface_Antigen_HBSAg)
categorise_products_data = np.append(categorise_products_data, Hepatitis_C_Screening)
#categorise_products_data = np.append(categorise_products_data, High_Vaginal_Swab_HVS_M_or_C_or_S)
categorise_products_data = np.append(categorise_products_data, Hiv_Care_And_Treatment_At_Designated_Sites)
#categorise_products_data = np.append(categorise_products_data, HIV_Confirmatory_Test)
categorise_products_data = np.append(categorise_products_data, HIV_Screening)
categorise_products_data = np.append(categorise_products_data, Hysteroscopy)
#categorise_products_data = np.append(categorise_products_data, Implanon)
categorise_products_data = np.append(categorise_products_data, In_Patient_Care_Limit)
categorise_products_data = np.append(categorise_products_data, Incision_and_Drainage)
categorise_products_data = np.append(categorise_products_data, Incubator_Care)
categorise_products_data = np.append(categorise_products_data, Infertility_Care)
categorise_products_data = np.append(categorise_products_data, Injectibles)
#categorise_products_data = np.append(categorise_products_data, intensive_care_unit)
categorise_products_data = np.append(categorise_products_data, Intermediate_Surgeries)
categorise_products_data = np.append(categorise_products_data, Jadelle_Implant)
categorise_products_data = np.append(categorise_products_data, Kidney_Function_Tests)
categorise_products_data = np.append(categorise_products_data, Laparoscopy)
categorise_products_data = np.append(categorise_products_data, Laryngoscopy_Direct_and_Indirect)
categorise_products_data = np.append(categorise_products_data, Leishmania_Screening)
categorise_products_data = np.append(categorise_products_data, Limbs_X_rays)
categorise_products_data = np.append(categorise_products_data, Line_Of_Treatment_Confirmation_From_Secondary_And_Tertiary_Care_Centres)
categorise_products_data = np.append(categorise_products_data, Lipid_Profile_Fasting)
categorise_products_data = np.append(categorise_products_data, Liver_Function_Test)
categorise_products_data = np.append(categorise_products_data, Liver_Function_Test_LFT)
categorise_products_data = np.append(categorise_products_data, Lumbosacral_X_Rays)
categorise_products_data = np.append(categorise_products_data, Major_Surgeries)
categorise_products_data = np.append(categorise_products_data, Malaria_Parasite)
#categorise_products_data = np.append(categorise_products_data, Male_Circumcision_and_Ear_piercing_within_first_6_wks)
#categorise_products_data = np.append(categorise_products_data, Mammography_For_Women_40_Years_Of_Age)
categorise_products_data = np.append(categorise_products_data, Mandibles_or_Temporomandibular_Joint_X_Rays)
categorise_products_data = np.append(categorise_products_data, Mantoux_Heaf_s_Test)
categorise_products_data = np.append(categorise_products_data, Mastoid_X_rays)
#categorise_products_data = np.append(categorise_products_data, MCH)
categorise_products_data = np.append(categorise_products_data, MCHC)
#categorise_products_data = np.append(categorise_products_data, MCV)
#categorise_products_data = np.append(categorise_products_data, Measles)
categorise_products_data = np.append(categorise_products_data, Meningitis)
categorise_products_data = np.append(categorise_products_data, Mental_Illness_Care_With_Certified_Psychiatrists_Outpatient_Care_Only)
categorise_products_data = np.append(categorise_products_data, Microbiology_And_Parasitology)
categorise_products_data = np.append(categorise_products_data, Minor_Surgeries)
categorise_products_data = np.append(categorise_products_data, Mmr)
categorise_products_data = np.append(categorise_products_data, Mortuary_Services)
categorise_products_data = np.append(categorise_products_data, MRI)
categorise_products_data = np.append(categorise_products_data, Neck_X_rays)
categorise_products_data = np.append(categorise_products_data, Neonatologist)
#categorise_products_data = np.append(categorise_products_data, Nephrologist)
categorise_products_data = np.append(categorise_products_data, Neurologist)
categorise_products_data = np.append(categorise_products_data, Neurosurgeon)
categorise_products_data = np.append(categorise_products_data, Non_surgical_extraction)
categorise_products_data = np.append(categorise_products_data, Norplant)
categorise_products_data = np.append(categorise_products_data, Npi_Immunization_0_5_Years)
categorise_products_data = np.append(categorise_products_data, Number_of_Sessions_Covered)
categorise_products_data = np.append(categorise_products_data, Nursing_Care_and_Consumables)
"""
categorise_products_data = np.append(categorise_products_data, Obstetrician)
categorise_products_data = np.append(categorise_products_data, Obstetrics_And_Gynaecology_Care_In_Patient_Limit_Applies)
categorise_products_data = np.append(categorise_products_data, Oncological_Investigations)
#categorise_products_data = np.append(categorise_products_data, oncologist)
categorise_products_data = np.append(categorise_products_data, Oncologist_Or_Cancer_Specialist_Visits)
categorise_products_data = np.append(categorise_products_data, Operculectomy)
categorise_products_data = np.append(categorise_products_data, Opv_Or_Ipv)
#categorise_products_data = np.append(categorise_products_data, Oral_and_Maxillofacial_Surgeon)
#categorise_products_data = np.append(categorise_products_data, Oral_Glucose_Tolerance_Test_OGTT)
categorise_products_data = np.append(categorise_products_data, Orthopedic_Surgeon)
categorise_products_data = np.append(categorise_products_data, Osmotic_Fragility_Test)
categorise_products_data = np.append(categorise_products_data, Out_Patient_care_Limit)
"""
#categorise_products_data = np.append(categorise_products_data, pa)
#categorise_products_data = np.append(categorise_products_data, Packed_Cell_Volume_PCV)
categorise_products_data = np.append(categorise_products_data, Pain_therapy)
categorise_products_data = np.append(categorise_products_data, Pap_Smear_and_Cytology)
categorise_products_data = np.append(categorise_products_data, Pap_Smear_Every_2Years_For_Women_Above_35_Years)
categorise_products_data = np.append(categorise_products_data, Pathologist)
#categorise_products_data = np.append(categorise_products_data, pediatrician_or_pediatric_surgeon)
categorise_products_data = np.append(categorise_products_data, Pelvic_X_rays)
categorise_products_data = np.append(categorise_products_data, Pentavalent)
#categorise_products_data = np.append(categorise_products_data, Pharmacological_treatment_of_acute_and_chronic_ocular_infections)
categorise_products_data = np.append(categorise_products_data, Physical_Examination)
categorise_products_data = np.append(categorise_products_data, Physiotherapy_Care)
categorise_products_data = np.append(categorise_products_data, Pneumococcal)
categorise_products_data = np.append(categorise_products_data, Prescribed_Drugs_At_Designated_Pharmacies)
categorise_products_data = np.append(categorise_products_data, Prescribed_Medications_for_Out_patient_covered_care)
categorise_products_data = np.append(categorise_products_data, Prescribed_Routine_Ultrasound_Scans)
categorise_products_data = np.append(categorise_products_data, Preventive_Counselling_on_referral)
categorise_products_data = np.append(categorise_products_data, Preventive_dental_care_and_counselling)
categorise_products_data = np.append(categorise_products_data, Private)
categorise_products_data = np.append(categorise_products_data, Proctoscopy)
categorise_products_data = np.append(categorise_products_data, Prostate_Specific_Antigen)
categorise_products_data = np.append(categorise_products_data, Protein_Electrophoresis)
categorise_products_data = np.append(categorise_products_data, Prothrombin_time_PT_or_INR)

categorise_products_data = np.append(categorise_products_data, Psa_Check_For_Men_40_Years_Of_Age)

categorise_products_data = np.append(categorise_products_data, Psychiatrist)
categorise_products_data = np.append(categorise_products_data, Psychiatry_Care)
categorise_products_data = np.append(categorise_products_data, Pulmonologist_or_Respiratory_Physician_or_Chest_Physician)
categorise_products_data = np.append(categorise_products_data, Random_Blood_Sugar)
categorise_products_data = np.append(categorise_products_data, Red_Blood_Cell_or_Reticulocyte_count)
categorise_products_data = np.append(categorise_products_data, Renal_Care_Dialysis)
categorise_products_data = np.append(categorise_products_data, Resuscitative_Care)
#categorise_products_data = np.append(categorise_products_data, Rheumatologist)
categorise_products_data = np.append(categorise_products_data, Room_Type)
categorise_products_data = np.append(categorise_products_data, Root_Canal_Therapy)
#categorise_products_data = np.append(categorise_products_data, Rotavirus)
categorise_products_data = np.append(categorise_products_data, Routine_dental_examination)
categorise_products_data = np.append(categorise_products_data, Routine_Drugs)
categorise_products_data = np.append(categorise_products_data, Scaling_and_Polishing)
categorise_products_data = np.append(categorise_products_data, Seeking_Second_Opinion)
#categorise_products_data = np.append(categorise_products_data, semen_m_c_s)
categorise_products_data = np.append(categorise_products_data, Seminal_Fluid_Analysis_SFA)
categorise_products_data = np.append(categorise_products_data, Semi_Private_Room)
categorise_products_data = np.append(categorise_products_data, Serum_Acid_Phosphate)
categorise_products_data = np.append(categorise_products_data, Serum_Albumin)
#categorise_products_data = np.append(categorise_products_data, Serum_Alkaline_Phosphate)
#categorise_products_data = np.append(categorise_products_data, Serum_Bicarbonate)
categorise_products_data = np.append(categorise_products_data, Serum_Bilirubin_Total_and_Direct)
#categorise_products_data = np.append(categorise_products_data, Serum_Calcium)
categorise_products_data = np.append(categorise_products_data, Serum_Chloride)
categorise_products_data = np.append(categorise_products_data, Serum_Cholesterol)
categorise_products_data = np.append(categorise_products_data, Serum_Gamma_Glutamyl_Transferase)
categorise_products_data = np.append(categorise_products_data, Serum_Inorganic_Phosphate)
#categorise_products_data = np.append(categorise_products_data, serum_iron)
categorise_products_data = np.append(categorise_products_data, Serum_Lactate_Dehydrogenase)
categorise_products_data = np.append(categorise_products_data, Serum_Lithium)
categorise_products_data = np.append(categorise_products_data, Serum_Magnesium)
categorise_products_data = np.append(categorise_products_data, Serum_Potasium)
#categorise_products_data = np.append(categorise_products_data, Serum_Sodium)
#categorise_products_data = np.append(categorise_products_data, serum_uric_acid)
categorise_products_data = np.append(categorise_products_data, Sigmoidoscopy)
categorise_products_data = np.append(categorise_products_data, Sinus_X_rays)
categorise_products_data = np.append(categorise_products_data, Skin_Scraping_for_Fungi)
categorise_products_data = np.append(categorise_products_data, Skin_Snip_for_Microfilaria)
categorise_products_data = np.append(categorise_products_data, Skull_X_rays)
categorise_products_data = np.append(categorise_products_data, Special_Care_baby_Unit)
#categorise_products_data = np.append(categorise_products_data, Specialist_Consultation)
categorise_products_data = np.append(categorise_products_data, Specialist_Drug_Therapy)
categorise_products_data = np.append(categorise_products_data, Specialist_Opthalmologist_Consultation)
categorise_products_data = np.append(categorise_products_data, Sputum_Acid_Fast_Bacilli_AFB_Test)
#categorise_products_data = np.append(categorise_products_data, sputum_m_c_s)
categorise_products_data = np.append(categorise_products_data, Standard_Room)
#categorise_products_data = np.append(categorise_products_data, Stool_M_C_S)
categorise_products_data = np.append(categorise_products_data, Stool_Occult_Blood)
categorise_products_data = np.append(categorise_products_data, Stress_Management)
categorise_products_data = np.append(categorise_products_data, Surgeries_All_Inclusive)
categorise_products_data = np.append(categorise_products_data, Surgical_Cancer_Care)
categorise_products_data = np.append(categorise_products_data, Surgical_extraction)
#categorise_products_data = np.append(categorise_products_data, Syphilis_Screening)
categorise_products_data = np.append(categorise_products_data, Therapeutic_Abortion_Manual_Vacuum_Aspiration)
categorise_products_data = np.append(categorise_products_data, Thoracic_Inlet_X_rays)
categorise_products_data = np.append(categorise_products_data, Thoraco_Lumbar_X_rays)
categorise_products_data = np.append(categorise_products_data, Thoracoscopy)
#categorise_products_data = np.append(categorise_products_data, throat_swab_m_c_s)
categorise_products_data = np.append(categorise_products_data, Thyroid_Function_Tests)
categorise_products_data = np.append(categorise_products_data, Toxoplasma_Screening)
categorise_products_data = np.append(categorise_products_data, Treatment_of_basic_outpatient_and_in_patient_cases )
categorise_products_data = np.append(categorise_products_data, Trypanosomes_Screening)
categorise_products_data = np.append(categorise_products_data, Upper_GI_Endoscopy)
categorise_products_data = np.append(categorise_products_data, Urethral_Swab_M_C_S)
categorise_products_data = np.append(categorise_products_data, Urinalysis)
categorise_products_data = np.append(categorise_products_data, Urine_M_C_S)
categorise_products_data = np.append(categorise_products_data, Urine_Pregnancy_Test)
categorise_products_data = np.append(categorise_products_data, Urologist)
categorise_products_data = np.append(categorise_products_data, VDRL_Veneral_Disease_Research_Laboratory_Test_unless_where_disallowed_by_diagnosis)
categorise_products_data = np.append(categorise_products_data, Vitamin_A)
categorise_products_data = np.append(categorise_products_data, Wellness_Checks)
#categorise_products_data = np.append(categorise_products_data, white_blood_cell_count)
categorise_products_data = np.append(categorise_products_data, White_cell_count_Total_and_Differential)
categorise_products_data = np.append(categorise_products_data, wound_swab_m_c_s)
categorise_products_data = np.append(categorise_products_data, X_rays_of_All_Body_Joints)
categorise_products_data = np.append(categorise_products_data, yellow_fever)
"""



#API CALL
#Function to post api request
def post_request(url, params, header = None):
    return req.post(url, params, headers = header)

#Function to logout
def logout(url, params, header):
    return req.post(url, params, headers = header)

#Login to connect to the database
print("Login to connect to the database.")
username = input("Enter username: ")
password = input("Enter password: ")

print("\nConnecting to the database...")
login = post_request(
    endpoint,
    params = {
        "_req":"login",
        "org" : config_f["payer"]["org"],
        "mid" : config_f["payer"]["mid"],
        "midtype" : config_f["payer"]["midtype"],
        "magik" : config_f["payer"]["magik"],
        "user" : username,
        "pass" : password
    }
)

if login.status_code == 200:
    response = login.json()
    login_user = response["result"]["value"]
    connID = login_user[0][0]["APPID"]
    print("Login successfully...")
else:
    print("Login failed. Error has occured! Try again later.")

if login_user:
    print("\nLoging User")
    print("-"*50)
    print(f"User:  {login_user[0][0]["SURNAME"]} {login_user[0][0]["OTHERNAMES"]}")
    print(f"Last Login: {login_user[0][0]["LASTLOGIN"]}")
    print("-"*50)


# Create Products
for row in categorise_products_data:
   params = {
        "_req": "n.acatprod",
        "catid": row["catid"],
        "prodcode": row["prodcode"],
        "descr": row["descr"] if row["descr"] != "" else "",
    }

   print(params)
   
   new_product_category = post_request(endpoint, params, {"applicationid":connID})
   
   if new_product_category.status_code == 200:
        res = new_product_category.json()
        print(f"Product Category params: {params}")
        print(f"Server response: {res}")

        if res["error"]:
            err = {
                "catid": params["catid"],
                "prodcode": params["prodcode"],
                "descr": params["descr"] if "descr" in params else "",
                "severity": res["error"]["severity"], 
                "error_message": res["error"]["msg"] 
            }
            print(f"Error: {err}")
            error_categorising_products = np.append(error_categorising_products, err)
        else:
            value = {
                "catid": params["catid"],
                "prodcode":params["prodcode"],
                "descr": params["descr"] if "descr" in params else "",
                "id": res["result"]["value"]["id"]   
            }
            succeed_categorising_products = np.append(succeed_categorising_products, value)

print(f"Error: {error_categorising_products}")

#Write error to a file.
if error_categorising_products.size > 0:
    error_f = pd.DataFrame(error_categorising_products)
    error_f.to_csv("output/error_categorising_products.csv")

#Write return created classes to a file
if succeed_categorising_products.size > 0:
    val_f = pd.DataFrame(succeed_categorising_products)
    val_f.to_csv("output/categorised_products.csv")

#logout
print("\n" + "-"*50)
logout_user = post_request(endpoint, {"_req":"logout"}, {"applicationid":connID})
if logout_user.status_code == 200:
    print("User logout successfull...")
    print(logout_user.json())

print("\n")

