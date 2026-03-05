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

endpoint = "https://api.testing.lemunz.io/"
login_user = None
connID = None
error_creating_subscriber = np.array([])
succeed_creating_subscriber = np.array([])

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
subcribers_f = pd.read_csv("datasets/avilia_subscribers_dataset.csv")
print("\n Subscribers dataset is loaded...")

for i, row in subcribers_f.iterrows():
    params = {
        "_req": "c.asub",
        "code": row["Code"],
        "alias": row["Alias"],
        "name": row["Name"],
        "email": row["Email"],
        "phone": row["Phone"],
        "city": row["City"],
        "exdate": row["Expiry_Date"]
    }
    print(params)
    new_subscribers = post_request(endpoint, params, {"applicationid":connID})

    if new_subscribers.status_code == 200:
        res = new_subscribers.json()
        print(f"Adding subscriber: {params}")
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
            print(f"Error: {err}")
            error_creating_subscriber = np.append(error_creating_subscriber, err)
        else:
            value = {
                "Code": params["code"], 
                "Name": params["name"], 
                "Email": params["email"], 
                "Phone": params["phone"],
                "Wheel": res["result"]["value"]["wheel"],
                "Pass": res["result"]["value"]["pass"]
            }
            succeed_creating_subscriber = np.append(succeed_creating_subscriber, value)

print(f"Error: {error_creating_subscriber}")

#Write error to a file.
if error_creating_subscriber.size > 0:
    error_f = pd.DataFrame(error_creating_subscriber)
    error_f.to_csv("output/error_creating_subscribers.csv")

#Write return subscribers logins to a file
if succeed_creating_subscriber.size > 0:
    val_f = pd.DataFrame(succeed_creating_subscriber)
    val_f.to_csv("output/created_subscribers_logins.csv")

#logout
print("\n" + "-"*50)
logout_user = post_request(endpoint, {"_req":"logout"}, {"applicationid":connID})
if logout_user.status_code == 200:
    print("User logout successfull...")
    print(logout_user.json())

print("\n")

