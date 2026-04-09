#-------------------------------------------------------------
# DATA MIGRATION: CREATE PACKAGE
#-------------------------------------------------------------
import numpy as np
import pandas as pd
import requests as req

print("\n")
print("="*50)
print("         SCRIPT TO CREATE PACKAGE")
print("="*50)

#Load config file
config_f = pd.read_json("config.json")

endpoint = "https://api.testing.lemunz.io/"
login_user = None
connID = None
error_creating_package = np.array([])
succeed_creating_package = np.array([])

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
sps_f = pd.read_csv("datasets/avilia_package_dataset.csv")
print("\n Package dataset is loaded...")


for i, row in sps_f.iterrows():
   params = {
        "_req": "n.apkg",
        "name": row["name"],
        "descr": row["descr"]
        }
   if not pd.isna(row["allow_oon"]):
       params["allow_oon"] = row["allow_oon"]

   if not pd.isna(row["active"]):
       params["active"] = row["active"]
             
   print(params)
   
   new_package= post_request(endpoint, params, {"applicationid":connID})
   
   if new_package.status_code == 200:
        res = new_package.json()
        print(f"Create package: {params}")
        print(f"Server response: {res}")

        if res["error"]:
            err = {
                "name": int(params["name"]),
                "descr": params["descr"],
                "severity": res["error"]["severity"], 
                "error_message": res["error"]["msg"] 
            }
            print(f"Error: {err}")
            error_creating_package = np.append(error_creating_package, err)
        else:
            value = {
                "name": params["name"],
                "descr": params["descr"],
                "packageid": res["result"]["value"]["id"],
            }
            succeed_creating_package = np.append(succeed_creating_package, value)

print(f"Error: {error_creating_package}")

#Write error to a file.
if error_creating_package.size > 0:
    error_f = pd.DataFrame(error_creating_package)
    error_f.to_csv("output/error_creating_package.csv")

#Write return created enrollees to a file
if succeed_creating_package.size > 0:
    val_f = pd.DataFrame(succeed_creating_package)
    val_f.to_csv("output/created_packages.csv")

#logout
print("\n" + "-"*50)
logout_user = post_request(endpoint, {"_req":"logout"}, {"applicationid":connID})
if logout_user.status_code == 200:
    print("User logout successfull...")
    print(logout_user.json())

print("\n")

