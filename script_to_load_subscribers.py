#-------------------------------------------------------------
# DATA MIGRATION: LOAD SUBSCRIBERS
#-------------------------------------------------------------
import numpy as np
import pandas as pd
import requests as req

print("\n")
print("="*50)
print("         SCRIPT TO LOAD SUBSCRIBERS")
print("="*50)

#Load config file
config_f = pd.read_json("config.json")
print(config_f["config"].to_string)
print(config_f["config"]["magik"])