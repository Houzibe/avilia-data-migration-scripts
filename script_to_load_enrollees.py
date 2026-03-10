#-------------------------------------------------------------
# DATA MIGRATION: LOAD ENROLLEES
#-------------------------------------------------------------
import numpy as np
import pandas as pd
import requests as req

print("\n")
print("="*50)
print("         SCRIPT TO LOAD ENROLLEES")
print("="*50)

#Load config file
config_f = pd.read_json("config.json")

endpoint = "https://api.testing.lemunz.io/"
login_user = None
connID = None
error_creating_enrollee = np.array([])
succeed_creating_enrollee = np.array([])

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
enrollee_f = pd.read_csv("datasets/avilia_enrollees_dataset.csv")
print("\n Subscribers dataset is loaded...")

""" params = {
        
    }"""

for i, row in enrollee_f.iterrows():
   params = {
        "_req": "en.aenrol",
        "sn": row["Surname"],
        "sex": row["Gender"],
        "dob": row["Date_of_birth"],
        "city": row["City"]
        }
   if not pd.isna(row["Middle_name"]):
       params["mn"] = row["Middle_name"]

   if not pd.isna(row["Last_name"]):
       params["ln"] = row["Last_name"]

   if not pd.isna(row["Marital_status"]):
       params["maritstatus"] = row["Marital_status"]

   if not pd.isna(row["Occupation"]):
       params["occupation"] = row["Occupation"]

   if not pd.isna(row["Honorific"]):
       params["honorific"] = row["Honorific"]

   if not pd.isna(row["Blood_group"]):
       params["blgroup"] = row["Blood_group"]

   if not pd.isna(row["Religion"]):
       params["religion"] = row["Religion"]

   if not pd.isna(row["Nationality"]):
       params["nationality"] =  row["Nationality"]

   if not pd.isna(row["Comments"]):
       params["comments"] = row["Comments"]
       
   print(params)
   
   new_enrollee = post_request(endpoint, params, {"applicationid":connID})
   
   if new_enrollee.status_code == 200:
        res = new_enrollee.json()
        print(f"Adding enrollee: {params}")
        print(f"Server response: {res}")

        if res["error"]:
            err = {
                "surname": params["sn"],
                "sex": params["sex"],
                "dob": params["dob"],
                "serverity": res["error"]["severity"], 
                "error_message": res["error"]["msg"] 
            }
            print(f"Error: {err}")
            error_creating_enrollee = np.append(error_creating_enrollee, err)
        else:
            value = {
                "surname": params["sn"],
                "sex": params["sex"],
                "dob": params["dob"],
            }
            succeed_creating_enrollee = np.append(succeed_creating_enrollee, value)

print(f"Error: {error_creating_enrollee}")

#Write error to a file.
if error_creating_enrollee.size > 0:
    error_f = pd.DataFrame(error_creating_enrollee)
    error_f.to_csv("output/error_creating_enrollees.csv")

#Write return created enrollees to a file
if succeed_creating_enrollee.size > 0:
    val_f = pd.DataFrame(succeed_creating_enrollee)
    val_f.to_csv("output/created_enrollees.csv")

#logout
print("\n" + "-"*50)
logout_user = post_request(endpoint, {"_req":"logout"}, {"applicationid":connID})
if logout_user.status_code == 200:
    print("User logout successfull...")
    print(logout_user.json())

print("\n")

