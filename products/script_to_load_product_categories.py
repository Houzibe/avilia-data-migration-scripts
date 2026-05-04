#-------------------------------------------------------------
# DATA MIGRATION: LOAD PRODUCT CATEGORIES
#-------------------------------------------------------------
import numpy as np
import pandas as pd
import requests as req
from data.product_categories_data import *

print("\n")
print("="*50)
print("         SCRIPT TO LOAD PRODUCT CATEGORIES")
print("="*50)

#Load config file
config_f = pd.read_json("../config.json")

endpoint = "https://api.testing.lemunz.io/"
login_user = None
connID = None
error_creating_product_category = np.array([])
succeed_creating_product_category = np.array([])
product_categories_data = product_categories


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


# Create Product Categories
for row in product_categories_data:
   params = {
        "_req": "aprodcat",
        "name": row["name"],
        "descr": row["descr"] if row["descr"] != "" else "",
        "parent": row["parent"] if row["parent"] != "" else ""
    }

   print(params)
   
   new_product_category = post_request(endpoint, params, {"applicationid":connID})
   
   if new_product_category.status_code == 200:
        res = new_product_category.json()
        print(f"Product category params: {params}")
        print(f"Server response: {res}")

        if res["error"]:
            err = {
                "name": params["name"],
                "descr": params["descr"] if "descr" in params else "",
                "severity": res["error"]["severity"], 
                "error_message": res["error"]["msg"] 
            }
            print(f"Error: {err}")
            error_creating_product_category = np.append(error_creating_product_category, err)
        else:
            value = {
                "name": params["name"],
                "descr": params["descr"] if "descr" in params else "",
                "id": res["result"]["value"]["id"]   
            }
            succeed_creating_product_category = np.append(succeed_creating_product_category, value)

print(f"Error: {error_creating_product_category}")

#Write error to a file.
if error_creating_product_category.size > 0:
    error_f = pd.DataFrame(error_creating_product_category)
    error_f.to_csv("output/error_creating_product_categories.csv")

#Write return created classes to a file
if succeed_creating_product_category.size > 0:
    val_f = pd.DataFrame(succeed_creating_product_category)
    val_f.to_csv("output/created_product_categories.csv")

#logout
print("\n" + "-"*50)
logout_user = post_request(endpoint, {"_req":"logout"}, {"applicationid":connID})
if logout_user.status_code == 200:
    print("User logout successfull...")
    print(logout_user.json())

print("\n")

