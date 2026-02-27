#-----------------------------------------------------------
# DATA MIGRATION: LOAD HEALTHCARE PROVIDERS
#-----------------------------------------------------------
import pandas as pd
import requests as req
 
print("=" * 50)
print("     SCRIPT TO LOAD HEALTHCARE PROVIDERS")
print("=" * 50)

#Load Config
config = pd.read_json("config.json")
print(f"{config}")
#Load dataset
hcps = pd.read_csv("datasets/avilia_hcps_datasets.csv")
print("Length:", len(hcps))


#Define endPoints
endpoint = "https://api.testing.melone.io"

