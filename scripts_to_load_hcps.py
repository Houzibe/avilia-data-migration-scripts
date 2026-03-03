#-----------------------------------------------------------
# DATA MIGRATION: LOAD HEALTHCARE PROVIDERS
#-----------------------------------------------------------
import numpy as np
import pandas as pd
import requests as req

print("\n") 
print("=" * 50)
print("     SCRIPT TO LOAD HEALTHCARE PROVIDERS DATASET")
print("=" * 50)

#Load Config
config = pd.read_json("config.json")
#print(f"{config["config"]["org"]}")

#Define endPoints
endpoint = "https://api.testing.melone.io"
login_user = None
connID = None
error_creating_hcp = np.array([])
succeed_creating_hcp = np.array([])

#Api call
#function for post request
def post_request(url, params, header=None):
    return req.post(url, params, headers=header)

#logout function
def logout(url,params,header):
    return req.post(url, params, headers=header)


#login
print("Login to connect to the database.")
username = input("Enter username: ")
password = input("Enter password: ")

print("\nConnecting to the database...")

login = post_request(
    endpoint,
    params={
        "_req" : "login",
        "org" : config["config"]["org"],
        "mid" : config["config"]["mid"],
        "midtype" : config["config"]["midtype"],
        "magik" : config["config"]["magik"],
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

print()
print("Loading dataset...")

#Load dataset
hcps = pd.read_csv("datasets/avilia_hcps_datasets.csv")
print("Dataset loaded successfully...")

print("\nDataset info:")
#print(f"Size: {hcps.shape()}")

for i, row in hcps.iterrows():
    params = {
        "_req": "v.ah",
        "code": int(row["Code"]),
        "alias": row["Alias"],
        "name": row["Name"],
        "email": row["Email"],
        "phone": int(row["Phone"]),
        "city": int(row["City"])
    }

    new_hcp = post_request(endpoint,params, {"applicationid":connID})

    if new_hcp.status_code == 200:
        res = new_hcp.json()
        print(f"Added HCP: {params}")
        print(f"Server response: {res}")
        if res["error"]:
            err = {
                "Code": params["code"], 
                "Name": params["name"], 
                "Email": params["email"], 
                "Phone": params["phone"],
                "Serverity": res["error"]["severity"], 
                "Error Message": res["error"]["msg"]
                }
            print(f"Err: {err}")
            error_creating_hcp = np.append(error_creating_hcp, err)\
        


print(f"\nError: {error_creating_hcp}")

#Writing the errors to the output file. 
error_f = pd.DataFrame(error_creating_hcp) 
error_f.to_csv("output/error_creating_hcps.csv")

#logout
print("\n" + "-"*50)
logout_user = logout(endpoint, {"_req":"logout"}, {"applicationid":connID})
if logout_user.status_code == 200:
    print("User logout successfull...")
    print(logout_user.json())

print("\n")