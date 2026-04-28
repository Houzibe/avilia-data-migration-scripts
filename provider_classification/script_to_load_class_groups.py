#-------------------------------------------------------------
# DATA MIGRATION: AFFILIATE WITH SPs
#-------------------------------------------------------------
import numpy as np
import pandas as pd
import requests as req
from data.class_groups_data import class_groups

print("\n")
print("="*50)
print("         SCRIPT TO AFFILIATE WITH PROVIDER")
print("="*50)

#Load config file
config_f = pd.read_json("../config.json")

endpoint = "https://api.testing.lemunz.io/"
login_user = None
connID = None
error_creating_class_group = np.array([])
succeed_creating_class_group = np.array([])
class_groups_data = class_groups


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


# Create Class groups
for row in class_groups_data:
   params = {
        "_req": "n.aspclg",
        "name": row["name"],
        }

   if row["descr"] != "":
        params["descr"] = row["descr"]
    
   if row["status_id"] != "":
        params["status_id"] = row["status_id"]
             
   print(params)
   
   new_class_group = post_request(endpoint, params, {"applicationid":connID})
   
   if new_class_group.status_code == 200:
        res = new_class_group.json()
        print(f"Class group params: {params}")
        print(f"Server response: {res}")

        if res["error"]:
            err = {
                "name": params["name"],
                "descr": params["descr"] if "descr" in params else "",
                "severity": res["error"]["severity"], 
                "error_message": res["error"]["msg"] 
            }
            print(f"Error: {err}")
            error_creating_class_group = np.append(error_creating_class_group, err)
        else:
            value = {
                "name": params["name"],
                "descr": params["descr"] if "descr" in params else "",
                "id": res["result"]["value"]["id"]   
            }
            succeed_creating_class_group = np.append(succeed_creating_class_group, value)

print(f"Error: {error_creating_class_group}")

#Write error to a file.
if error_creating_class_group.size > 0:
    error_f = pd.DataFrame(error_creating_class_group)
    error_f.to_csv("output/error_creating_class_groups.csv")

#Write return created classes to a file
if succeed_creating_class_group.size > 0:
    val_f = pd.DataFrame(succeed_creating_class_group)
    val_f.to_csv("output/created_class_groups.csv")

#logout
print("\n" + "-"*50)
logout_user = post_request(endpoint, {"_req":"logout"}, {"applicationid":connID})
if logout_user.status_code == 200:
    print("User logout successfull...")
    print(logout_user.json())

print("\n")

