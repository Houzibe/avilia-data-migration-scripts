#-----------------------------------------------------------
# DATA MIGRATION: LOAD HEALTHCARE PROVIDERS
#-----------------------------------------------------------
import pandas as pd
import requests as req
 
print("=" * 50)
print("     SCRIPT TO LOAD HEALTHCARE PROVIDERS")
print("=" * 50)

#Load dataset
hcps = pd.read_csv("datasets/avilia_hcps_datasets.csv")


