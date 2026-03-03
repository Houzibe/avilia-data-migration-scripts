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
print(f"{config["config"]["org"]}")

#Define endPoints
endpoint = "https://api.testing.melone.io"
login_user = None
connID = None

#Api call
def post_request(url, params):
    print(f"url: {url}")
    print(f"params: {params}")
    return req.post(url, params)

def logout(url,params,header):
    print("login out...")
    print(f"Params: {params}")
    return req.post(url, params, headers=header)


#login
username = input("Enter username: ")
password = input("Enter password: ")

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
    print("login feedback...")
    print(response["result"]["value"])
else:
    print("Error has occured")

print("\nLoging User")
print("-"*50)
print(f"Login user: {login_user}")
print(login_user[0][0])
print(f"ConnID: {connID}")
#Load dataset
hcps = pd.read_csv("datasets/avilia_hcps_datasets.csv")
print("Length:", len(hcps))



#login
logout_user = logout(endpoint, {"_req":"logout"}, {"applicationid":connID})
if logout_user.status_code == 200:
    print("\n" + "-"*50)
    print("User logout successfully...")
    print(logout_user.json())
