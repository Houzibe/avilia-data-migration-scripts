import numpy as np

laboratory_tests = np.array([
    {"name": "Zn Afb X1", "descr": "", "catid": 39, "source": 83},
])

medical_supplies = np.array([
    {"name": "Zetgel 35G Cre", "descr": "", "catid": 34, "source": 83},
    {"name": "Zimmer Biomet Dermatome Blade", "descr": "", "catid": 34, "source": 83},
])

medications = np.array([
    {"name": "Z Cristin Vincristine Sulfate 1Mg In 1Ml Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Zaditen Eye Drops", "descr": "", "catid": 35, "source": 83},
    {"name": "Zaditen Syrup 100Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Zaditen(Ketotifen) Suspension", "descr": "", "catid": 35, "source": 83},
    {"name": "Zaditen[Ketotifen]Tab 1Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zafirlukast 20Mg/Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zantac 150Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zantac 300Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zantac [Ranitidine]", "descr": "", "catid": 35, "source": 83},
    {"name": "Zantac Inj[Ranitidine]", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestoretic 20Mg (Lisinopril+Hct", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestril 10Mg(Lisinopril)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zestril 5Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zetgel Cream", "descr": "", "catid": 35, "source": 83},
    {"name": "Zetiheal Ezetimibe 10Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zetro 200Mg In 5Ml Syr", "descr": "", "catid": 35, "source": 83},
    {"name": "Zetro 250Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zetro 500Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zidovudine Syrup 50Mg/5Mls", "descr": "", "catid": 35, "source": 83},
    {"name": "Zifam Probio 282 Point 5Mg Granules", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinacef 750Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Zincofer 200Ml Syrup", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat 125Mg/5Mls Syrups", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat 250", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat 250Mg(Cefuroxime)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat 500", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat 500Mg Tabs (Gsk)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat 750Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat Cefuroxime Suspension 100Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat Inj 750Mg (Gsk)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat Injection. 750 Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat Suspension 100Ml(Cefuroxime)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat Suspension 50Ml", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinnat Tabs 500Mg(Cefuroxime)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zinncaef Inj 750Mg (Branded) Cefuroxime", "descr": "", "catid": 35, "source": 83},
    {"name": "Zista Amiodarone 100Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zithromax 250Mg ( Pfizer)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zithromax Caps", "descr": "", "catid": 35, "source": 83},
    {"name": "Zithromax Syp", "descr": "", "catid": 35, "source": 83},
    {"name": "Zithromax Tabs(Azithromycin)", "descr": "", "catid": 35, "source": 83},
    {"name": "Zithromax, Cap, 250Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zofixime 100Mg In 5Ml Syr", "descr": "", "catid": 35, "source": 83},
    {"name": "Zoladex 10 Point 8Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Zoladex 10.8Mg Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Zoladex 3 Point 6Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Zoladex 3.6 Mg Injection", "descr": "", "catid": 35, "source": 83},
    {"name": "Zolamid 5Mg In 1Ml Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Zolamox, Tab, 250Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zolat 20Ml Sus", "descr": "", "catid": 35, "source": 83},
    {"name": "Zolat 400Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zoldric Zolendronic Acid 4Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Zoloft, Tab, 50Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zolon Azithromycin 500Mg Caps", "descr": "", "catid": 35, "source": 83},
    {"name": "Zolon Pentazocine 30Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Zometa 4Mg In 100Ml Inf", "descr": "", "catid": 35, "source": 83},
    {"name": "Zonason Benzylpenicillin 600Mg Inj", "descr": "", "catid": 35, "source": 83},
    {"name": "Zopiclone 7.5Mg Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zortemib, Inj, 2Mg", "descr": "", "catid": 35, "source": 83},
    {"name": "Zovirox ( Acyclovir) Oc", "descr": "", "catid": 35, "source": 83},
    {"name": "Zyncet Cetirizine Hydrochloride Tab", "descr": "", "catid": 35, "source": 83},
    {"name": "Zyncet Syrup 100Ml", "descr": "", "catid": 35, "source": 83},
])

nutritionals = np.array([
    {"name": "Zinc Adult/Tab", "descr": "", "catid": 33, "source": 83},
    {"name": "Zinc Baby/Tab", "descr": "", "catid": 33, "source": 83},
    {"name": "Zinc Chloride Plus Zinc Sulphate", "descr": "", "catid": 33, "source": 83},
    {"name": "Zinc Sulphate 20Mg Tab Archy", "descr": "", "catid": 33, "source": 83},
    {"name": "Zinc Tab:", "descr": "", "catid": 33, "source": 83},
    {"name": "Zinc Tablet", "descr": "", "catid": 33, "source": 83},
])

surgeries = np.array([
    {"name": "Zirconium / Bruxir", "descr": "", "catid": 37, "source": 83},
    {"name": "Zoom Whitening", "descr": "", "catid": 37, "source": 83},
])

# =============================================================================
# SHEET SUMMARY — Z
# =============================================================================
# Total records on this sheet : 72
# Categories found            : laboratory_tests, medical_supplies, medications, nutritionals, surgeries
# Duplicates removed          : None
# Unmapped categories         : None
# =============================================================================
