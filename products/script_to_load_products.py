#-------------------------------------------------------------
# DATA MIGRATION: LOAD PRODUCTS
#-------------------------------------------------------------
import numpy as np
import pandas as pd
import requests as req
from data.products_data import *
#from data.m2.A import *
#from data.m2.B import *
#from data.m2.C import *
#from data.m2.D import *
#from data.m2.E import *
#from data.m2.F import *
#from data.m2.G import *
#from data.m2.H import *
#from data.m2.I import *
#from data.m2.J import *
#from data.m2.K import * 
#from data.m2.L import *
#from data.m2.M import *
#from data.m2.N import *
#from data.m2.O import *
#from data.m2.P import *
#from data.m2.Q import *
#from data.m2.R import *
#from data.m2.S import *
#from data.m2.T import *
#from data.m2.U import *
#from data.m2.V import *
#from data.m2.W import *
#from data.m2.X import *
#from data.m2.Y import *
from data.m2.Z import *
#from data.r3._hash import *

print("\n")
print("="*50)
print("         SCRIPT TO LOAD PRODUCTS")
print("="*50)

#Load config file
config_f = pd.read_json("../config.json")

endpoint = "https://api.testing.lemunz.io/"
login_user = None
connID = None
error_creating_products = np.array([])
succeed_creating_products = np.array([])
products_data = np.array([])

# diagnostic_imaging, medications, surgeries

#products_data = np.append(products_data, biologics)
#products_data = np.append(products_data,cancer_care)
#products_data = np.append(products_data,cosmetics_personal_care)
#products_data = np.append(products_data, consultations)
#products_data = np.append(products_data,dental_services)
#products_data = np.append(products_data,diagnostic_imaging)
#products_data = np.append(products_data,dialysis)
#products_data = np.append(products_data,family_planning)
#products_data = np.append(products_data,infusions)
products_data = np.append(products_data,laboratory_tests)
#products_data = np.append(products_data,medical_devices)
#products_data = np.append(products_data,medical_supplies)
products_data = np.append(products_data,medications)
#products_data = np.append(products_data,mental_health_services)
#products_data = np.append(products_data,nutritionals)
#products_data = np.append(products_data,others)
#products_data = np.append(products_data,physiotherapy)
#products_data = np.append(products_data,reproductive_health)
#products_data = np.append(products_data,public_health_vector_control)
#products_data = np.append(products_data,surgeries)
#products_data = np.append(products_data,vaccines)

#API CALL:
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


# Create Products
for row in products_data:
   params = {
        "_req": "aprod",
        "name": row["name"],
        "descr": row["descr"] if row["descr"] != "" else "",
        "catid": row["catid"],
        "source": row["source"]
    }

   print(params)
   
   new_product = post_request(endpoint, params, {"applicationid":connID})
   
   if new_product.status_code == 200:
        res = new_product.json()
        print(f"Product params: {params}")
        print(f"Server response: {res}")

        if res["error"]:
            err = {
                "name": params["name"],
                "descr": params["descr"] if "descr" in params else "",
                "severity": res["error"]["severity"], 
                "error_message": res["error"]["msg"] 
            }
            print(f"Error: {err}")
            error_creating_products = np.append(error_creating_products, err)
        else:
            value = {
                "name": params["name"],
                "descr": params["descr"] if "descr" in params else "",
                "id": res["result"]["value"]["id"]   
            }
            succeed_creating_products = np.append(succeed_creating_products, value)

print(f"Error: {error_creating_products}")

#Write error to a file.
if error_creating_products.size > 0:
    error_f = pd.DataFrame(error_creating_products)
    error_f.to_csv("output/error_creating_products.csv")

#Write return created classes to a file
if succeed_creating_products.size > 0:
    val_f = pd.DataFrame(succeed_creating_products)
    val_f.to_csv("output/created_products.csv")

#logout
print("\n" + "-"*50)
logout_user = post_request(endpoint, {"_req":"logout"}, {"applicationid":connID})
if logout_user.status_code == 200:
    print("User logout successfull...")
    print(logout_user.json())

print("\n")

