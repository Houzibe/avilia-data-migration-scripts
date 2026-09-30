import numpy as np

cancer_care = np.array([
    {"name": "Zoladex 10.8Mg", "descr": "", "catid": 42, "source": 83}
])

drugs = np.array([
    {"name": "Zaditen 0.2mg/mL Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Zaditen 1Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zaditen 1Mg Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Zaditen 2Mg Tablet", "descr": "", "catid": 35, "source": 83},
    {"name": "Zaditen Eye Drop", "descr": "", "catid": 35, "source": 83},
    {"name": "Zaditen Eye Drop (Kitotifen) 0.025%", "descr": "", "catid": 35, "source": 83},
    {"name": "Zaditen Syr", "descr": "", "catid": 35, "source": 83},
    {"name": "Zaditen(Ketotifen) Suspension", "descr": "", "catid": 35, "source": 83},
    {"name": "Zaditen[Ketotifen]Tab 1mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zadol (Aceclofenac/ PCM/ Chlorzaxazone)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zafirlukast 20mg Tab (Accolate )", "descr": "", "catid": 35, "source": 83},
    {"name": "Zantac 150Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zantac [Ranitidine]", "descr": "", "catid": 35, "source": 83},
    {"name": "Zantac Inj[Ranitidine]", "descr": "", "catid": 35, "source": 83},
    {"name": "Zedex Cold", "descr": "", "catid": 35, "source": 83},
    {"name": "Zedex Cough Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Zedex D", "descr": "", "catid": 35, "source": 83},
    {"name": "Zeep Balm", "descr": "", "catid": 35, "source": 83},
    {"name": "Zentel", "descr": "", "catid": 35, "source": 83},
    {"name": "Zentel 200Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zentel Susp", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestoretic 20mg (Lisinopril+Hct", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestoretic Tab 10mg/12.5mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestoretic Tabs", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestoretic-20 20mg  [Uk]", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestril", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestril 10Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestril 10mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestril 10mg(Lisinopril)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestril 20Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestril 20mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestril 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestril 5mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zet Gel Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Zetgel", "descr": "", "catid": 35, "source": 83},
    {"name": "Zetgel (Diclofenac) 1% Gel", "descr": "", "catid": 35, "source": 83},
    {"name": "Zidovudine 100mg Tab (Retrovir)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zifam Probio (Probiotics)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinacef 750Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinc (Pead)/Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinc 10Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinc 20Mg Per Tab (Paediatric)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinc 20mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinc 50Mg (X50) Per Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinc Chloride Plus Zinc Sulphate", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinc Gluconate", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinc Oxide 20Mg Cream (1 Tube)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinc Oxide Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinchlor Eyedrop", "descr": "", "catid": 35, "source": 83},
    {"name": "Zing C 500", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat 125Mg Susp", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat 250Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat 250Mg Per Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat 250mg(Cefuroxime)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat 500Mg Per Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat Susp 100Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat Suspension", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat Suspension 100ml(Cefuroxime)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat Suspension 50ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat Tabs 250Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat Tabs 500Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat Tabs 500mg(Cefuroxime)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinncaef Inj 750mg (Branded) Cefuroxime", "descr": "", "catid": 35, "source": 83},
    {"name": "Zirtek Allergy", "descr": "", "catid": 35, "source": 83},
    {"name": "Zithromax", "descr": "", "catid": 35, "source": 83},
    {"name": "Zithromax Tabs(Azithromycin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zoladex", "descr": "", "catid": 35, "source": 83},
    {"name": "Zoladex 10.8Mg Implant", "descr": "", "catid": 35, "source": 83},
    {"name": "Zolat", "descr": "", "catid": 35, "source": 83},
    {"name": "Zoledronic Acid 4Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Zoloft", "descr": "", "catid": 35, "source": 83},
    {"name": "Zolpidem 10mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zonisamide (Endo)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zopiclone 7.5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zopiclone Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zoretic", "descr": "", "catid": 35, "source": 83},
    {"name": "Zosinamide", "descr": "", "catid": 35, "source": 83},
    {"name": "Zovirax Cold Sore", "descr": "", "catid": 35, "source": 83},
    {"name": "Zukoren Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Zumenon (Estradiol)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zylocaine", "descr": "", "catid": 35, "source": 83},
    {"name": "Zyloric ( Allopuranol) 100Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zyloric 100Mg", "descr": "", "catid": 35, "source": 83}
])

laboratory_tests = np.array([
    {"name": "Zinc (Serum)", "descr": "", "catid": 39, "source": 83},
    {"name": "Zn Smear(Acid Fast Bacilli) Afb", "descr": "", "catid": 39, "source": 83}
])

nutritionals = np.array([
    {"name": "Zedex Cough Syrup 100Ml", "descr": "", "catid": 33, "source": 83},
    {"name": "Zinc Sulphate Dispesible 20Mg Tab", "descr": "", "catid": 33, "source": 83}
])

others = np.array([
    {"name": "Zygomatic Fracture (Fillies Operation)", "descr": "", "catid": 48, "source": 83}
])

surgeries = np.array([
    {"name": "Zirconium Crown", "descr": "", "catid": 37, "source": 83}
])

# =============================================================================
# SHEET SUMMARY — Product Z
# =============================================================================
# Total records on this sheet : 92
# Categories found            : cancer_care, drugs, laboratory_tests, nutritionals, others, surgeries
# Unmapped categories         : None
# =============================================================================
