#-------------------------------------------------------------
# DATA MIGRATION: LOAD BENEFICIARIES
#-------------------------------------------------------------
import numpy as np
import pandas as pd
import requests as req

print("\n")
print("="*50)
print("         SCRIPT TO LOAD BENEFICIARIES")
print("="*50)

#Load config file
config_f = pd.read_json("config.json")

endpoint = "https://api.testing.lemunz.io/"
login_user = None
connID = None
error_creating_beneficiary = np.array([])
succeed_creating_beneficiary = np.array([])

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
beneficiary_f = pd.read_csv("datasets/avilia_beneficiaries_dataset.csv")
print("\n Beneficiaries dataset is loaded...")


for i, row in beneficiary_f.iterrows():
   params = {
        "_req": "c.aben",
        "enrolleeId": int(row["enrollee_id"])
        }
   
   if not pd.isna(row["subscriber_id_org_id"]):
       params["subscriberId"] = int(row["subscriber_id_org_id"]),
   
   if not pd.isna(row["principal"]):
       params["principal"] = int(row["principal"])
    
   if not pd.isna(row["principal_rel"]):
       params["principal_rel"] = int(row["principal_rel"])

   if not pd.isna(row["honorific"]):
       params["honorific"] = int(row["honorific"])

   if not pd.isna(row["comments"]):
       params["comments"] = row["comments"]           
   print(params)
   
   new_beneficiary = post_request(endpoint, params, {"applicationid":connID})
   
   if new_beneficiary.status_code == 200:
        res = new_beneficiary.json()
        print(f"Adding Beneficiary: {params}")
        print(f"Server response: {res}")

        if res["error"]:
            err = {
                "enrolleeId": params["enrolleeId"],
                "serverity": res["error"]["severity"], 
                "error_message": res["error"]["msg"] 
            }
            print(f"Error: {err}")
            error_creating_beneficiary = np.append(error_creating_beneficiary, err)
        else:
            value = {
                "beneficiary_id": res["result"]["value"]["id"],
            }
            succeed_creating_beneficiary = np.append(succeed_creating_beneficiary, value)

print(f"Error: {error_creating_beneficiary}")

#Write error to a file.
if error_creating_beneficiary.size > 0:
    error_f = pd.DataFrame(error_creating_beneficiary)
    error_f.to_csv("output/error_creating_beneficiaries.csv")

#Write return created enrollees to a file
if succeed_creating_beneficiary.size > 0:
    val_f = pd.DataFrame(succeed_creating_beneficiary)
    val_f.to_csv("output/created_beneficiaries.csv")

#logout
print("\n" + "-"*50)
logout_user = post_request(endpoint, {"_req":"logout"}, {"applicationid":connID})
if logout_user.status_code == 200:
    print("User logout successfull...")
    print(logout_user.json())

print("\n")

