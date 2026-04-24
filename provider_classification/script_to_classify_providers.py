#-------------------------------------------------------------
# DATA MIGRATION: AFFILIATE WITH SPs
#-------------------------------------------------------------
import numpy as np
import pandas as pd
import requests as req
from data.classify_providers_data import *

print("\n")
print("="*50)
print("         SCRIPT TO AFFILIATE WITH PROVIDER")
print("="*50)

#Load config file
config_f = pd.read_json("../config.json")

endpoint = "https://api.testing.lemunz.io/"
login_user = None
connID = None
error_classifying_sps = np.array([])
succeed_classifying_sps = np.array([])
classify_sps = np.array([])
classify_sps = np.append(classify_sps, hospital_classes)
classify_sps = np.append(classify_sps, imaging_centers_classes)
classify_sps = np.append(classify_sps, pharmacy_classes)
classify_sps = np.append(classify_sps, laboratory_classes)
classify_sps = np.append(classify_sps, dental_classes)
classify_sps = np.append(classify_sps, eye_clinic_classes)
classify_sps = np.append(classify_sps, physiotherapy_classes)
classify_sps = np.append(classify_sps, band_A_Plus_providers)
classify_sps = np.append(classify_sps, band_A_providers)
classify_sps = np.append(classify_sps, band_B_providers)
classify_sps = np.append(classify_sps, band_C_providers)

#Load dataset from classify_providers_data.py
#hospital_classes_data = hospital_classes
#imaging_centers_classes_data = imaging_centers_classes
#pharmacy_classes_data = pharmacy_classes
#laboratory_classes_data = laboratory_classes
#dental_classes_data = dental_classes
#eye_clinic_classes_data = eye_clinic_classes
#physiotherapy_classes_data = physiotherapy_classes
#band_A_Plus_providers_data = band_A_Plus_providers
#band_A_providers_data = band_A_providers
#band_B_providers_data = band_B_providers
#band_C_providers_data = band_C_providers

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

#load dataset
#sps_f = pd.read_csv("datasets/avilia_providers_dataset.csv")
#print("\n classes loaded...")


#for i, row in sps_f.iterrows():
# Classify provider into the Hospital class
for row in classify_sps:
   params = {
        "_req": "n.aclahcp",
        "spcode": row["spcode"],
        "classid": row["classid"],
        "name": row["name"]
        }

   if row["descr"] != "":
        params["descr"] = row["descr"]
             
   print(params)
   
   new_classified_sp = post_request(endpoint, params, {"applicationid":connID})
   
   if new_classified_sp.status_code == 200:
        res = new_classified_sp.json()
        print(f"SP Classification params: {params}")
        print(f"Server response: {res}")

        if res["error"]:
            err = {
                "name": params["name"],
                "severity": res["error"]["severity"], 
                "error_message": res["error"]["msg"] 
            }
            print(f"Error: {err}")
            error_classifying_sps = np.append(error_classifying_sps, err)
        else:
            value = {
                "spcode": params["spcode"],
                "classid": params["classid"],
                "name": params["name"],
                "id": res["result"]["value"]["id"]   
            }
            succeed_classifying_sps = np.append(succeed_classifying_sps, value)

print(f"Error: {error_classifying_sps}")

#Write error to a file.
if error_classifying_sps.size > 0:
    error_f = pd.DataFrame(error_classifying_sps)
    error_f.to_csv("output/error_classifying_sps.csv")

#Write return created classes to a file
if succeed_classifying_sps.size > 0:
    val_f = pd.DataFrame(succeed_classifying_sps)
    val_f.to_csv("output/classified_sps.csv")

#logout
print("\n" + "-"*50)
logout_user = post_request(endpoint, {"_req":"logout"}, {"applicationid":connID})
if logout_user.status_code == 200:
    print("User logout successfull...")
    print(logout_user.json())

print("\n")

