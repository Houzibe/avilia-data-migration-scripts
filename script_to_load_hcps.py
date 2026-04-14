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
        "org" : config["vendor"]["org"],
        "mid" : config["vendor"]["mid"],
        "midtype" : config["vendor"]["midtype"],
        "magik" : config["vendor"]["magik"],
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
hcps = pd.read_csv("datasets/avilia_hcps_dataset.csv")
print("Dataset loaded successfully...")

print("\nDataset info:")
#print(f"Size: {hcps.shape()}")

for i, row in hcps.iterrows():
    params = {
        "_req": "v.ah",
        "code": row["code"],
        "alias": row["alias"],
        "name": row["name"],
        "email": row["email"],
        "phone": int(row["phone"]),
        "city": int(row["city"])
    }
    print(f"Params: {params}")
    new_hcp = post_request(endpoint,params, {"applicationid":connID})

    if new_hcp.status_code == 200:
        res = new_hcp.json()
        print(f"Added HCP: {params}")
        print(f"Server response: {res}")
        print("^"*50)
        print(res)
        print("^"*50)
        if res["error"]:
            err = {
                "code": params["code"], 
                "name": params["name"], 
                "email": params["email"], 
                "phone": params["phone"],
                "serverity": res["error"]["severity"], 
                "error Message": res["error"]["msg"]
                }
            print(f"Err: {err}")
            error_creating_hcp = np.append(error_creating_hcp, err)
        else:
            value = {
                "code": params["code"], 
                "name": params["name"], 
                "email": params["email"], 
                "phone": params["phone"],
                "wheel": res["result"]["value"]["wheel"],
                "pass": res["result"]["value"]["pass"]
            }
            succeed_creating_hcp = np.append(succeed_creating_hcp,value)
        


print(f"\nError: {error_creating_hcp}")

#Writing the errors to the output file. 
if error_creating_hcp.size > 0:
    error_f = pd.DataFrame(error_creating_hcp) 
    error_f.to_csv("output/error_creating_hcps.csv")

if succeed_creating_hcp.size > 0:
    val_f = pd.DataFrame(succeed_creating_hcp)
    val_f.to_csv("output/created_hcps_logins.csv")

#logout
print("\n" + "-"*50)
logout_user = logout(endpoint, {"_req":"logout"}, {"applicationid":connID})
if logout_user.status_code == 200:
    print("User logout successfull...")
    print(logout_user.json())

print("\n")