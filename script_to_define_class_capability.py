#-------------------------------------------------------------
# DATA MIGRATION: DEFINE PROVIDER CLASS CAPABILITY
#-------------------------------------------------------------
import numpy as np
import pandas as pd
import requests as req

print("\n")
print("="*50)
print("         SCRIPT TO DEFINE PROVIDER CLASS CAPABILITY")
print("="*50)

#Load config file
config_f = pd.read_json("config.json")

endpoint = "https://api.testing.lemunz.io/"
login_user = None
connID = None
error_defining_class_capability = np.array([])
succeed_defining_class_capability = np.array([])

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
sps_f = pd.read_csv("datasets/avilia_class_capability_dataset.csv")
print("\n Providers class capability dataset is loaded...")


for i, row in sps_f.iterrows():
   params = {
        "_req": "n.aspcap",
        "catid": int(row["catid"]),
        "spclassid": int(row["spclassid"])
        }
   if not pd.isna(row["prescribe"]):
       params["prescribe"] = int(row["prescribe"])

   if not pd.isna(row["dispense"]):
       params["dispense"] = int(row["dispense"])

   if not pd.isna(row["active"]):
       params["active"] = row["active"]

   if not pd.isna(row["descr"]):
       params["descr"] = row["descr"]
             
   print(params)
   
   new_sp = post_request(endpoint, params, {"applicationid":connID})
   
   if new_sp.status_code == 200:
        res = new_sp.json()
        print(f"Define class capability: {params}")
        print(f"Server response: {res}")

        if res["error"]:
            err = {
                "catid": int(params["catid"]),
                "serverity": res["error"]["severity"], 
                "error_message": res["error"]["msg"] 
            }
            print(f"Error: {err}")
            error_defining_class_capability = np.append(error_defining_class_capability, err)
        else:
            value = {
                "catid": params["catid"],
                "capabilityid": res["result"]["value"]["id"],
            }
            succeed_defining_class_capability = np.append(succeed_defining_class_capability, value)

print(f"Error: {error_defining_class_capability}")

#Write error to a file.
if error_defining_class_capability.size > 0:
    error_f = pd.DataFrame(error_defining_class_capability)
    error_f.to_csv("output/error_defining_class_capability.csv")

#Write return created enrollees to a file
if succeed_defining_class_capability.size > 0:
    val_f = pd.DataFrame(succeed_defining_class_capability)
    val_f.to_csv("output/defined_class_capability.csv")

#logout
print("\n" + "-"*50)
logout_user = post_request(endpoint, {"_req":"logout"}, {"applicationid":connID})
if logout_user.status_code == 200:
    print("User logout successfull...")
    print(logout_user.json())

print("\n")

