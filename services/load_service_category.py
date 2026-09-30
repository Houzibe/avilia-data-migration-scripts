#-------------------------------------------------------------
# DATA MIGRATION: LOAD PRODUCT CATEGORIES
#-------------------------------------------------------------
import numpy as np
import pandas as pd
import requests as req
from data.service_categories_data import *

print("\n")
print("="*50)
print("         SCRIPT TO LOAD SERVICE CATEGORIES")
print("="*50)

#Load config file
config_f = pd.read_json("../config.json")

endpoint = "https://api.testing.lemunz.io/"
login_user = None
connID = None
error_creating_service_category = np.array([])
succeed_creating_service_category = np.array([])
service_categories_data = np.array([]) 
#service_categories_data = np.append(service_categories_data, service_categories)
#service_categories_data = np.append(service_categories_data, npi_immunization)
#service_categories_data = np.append(service_categories_data, physiotherapy_care)
#service_categories_data = np.append(service_categories_data, accident_emergency_care_out_patient)
#service_categories_data = np.append(service_categories_data, additional_immunization_0_5_Years)
#service_categories_data = np.append(service_categories_data, additional_immunization_6_Years_And_Above)
#service_categories_data = np.append(service_categories_data, advanced_diagnostic_imaging)
#service_categories_data = np.append(service_categories_data, basic_diagnostic_imaging)
#service_categories_data = np.append(service_categories_data, cancer_screening_care)
#service_categories_data = np.append(service_categories_data, chemistry_investigations)
#service_categories_data = np.append(service_categories_data, dental_care)
#service_categories_data = np.append(service_categories_data, eye_optical_care)
#service_categories_data = np.append(service_categories_data, family_planning_out_patient_limit)
#service_categories_data = np.append(service_categories_data, gym_discounted)
#service_categories_data = np.append(service_categories_data, hematological_test)
#service_categories_data = np.append(service_categories_data, hiv_care_and_treatment_at_designated_sites)
#service_categories_data = np.append(service_categories_data, in_patient_care_limit)
#service_categories_data = np.append(service_categories_data, incubator_care)
#service_categories_data = np.append(service_categories_data, infertility_care)
#service_categories_data = np.append(service_categories_data, microbiology_and_parasitology)
#service_categories_data = np.append(service_categories_data, mortuary_services)
#service_categories_data = np.append(service_categories_data, obstetrics_and_gynaecology_care)
#service_categories_data = np.append(service_categories_data, renal_care)
#service_categories_data = np.append(service_categories_data, routine_drugs)
#service_categories_data = np.append(service_categories_data, seeking_second_opinion)
#service_categories_data = np.append(service_categories_data, specialist_consultation)
#service_categories_data = np.append(service_categories_data, surgeries)
#service_categories_data = np.append(service_categories_data, wellness_checks)
#service_categories_data = np.append(service_categories_data, psychiatry_care)
#service_categories_data = np.append(service_categories_data, advanced_laboratory_investigations_pathology)


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


# Create Service Categories
for row in service_categories_data:
   params = {
        "_req": "n.asrvcat",
        "name": row["name"],
        "descr": row["descr"],
        "parent": row["parent"] if row["parent"] != "" else ""
    }

   print(params)
   
   new_service_category = post_request(endpoint, params, {"applicationid":connID})
   
   if new_service_category.status_code == 200:
        res = new_service_category.json()
        print(f"Service category params: {params}")
        print(f"Server response: {res}")

        if res["error"]:
            err = {
                "name": params["name"],
                "descr": params["descr"] if "descr" in params else "",
                "severity": res["error"]["severity"], 
                "error_message": res["error"]["msg"] 
            }
            print(f"Error: {err}")
            error_creating_service_category = np.append(error_creating_service_category, err)
        else:
            value = {
                "name": params["name"],
                "descr": params["descr"] if "descr" in params else "",
                "id": res["result"]["value"]["id"]   
            }
            succeed_creating_service_category = np.append(succeed_creating_service_category, value)

print(f"Error: {error_creating_service_category}")

#Write error to a file.
if error_creating_service_category.size > 0:
    error_f = pd.DataFrame(error_creating_service_category)
    error_f.to_csv("output/error_creating_service_categories.csv")

#Write return created classes to a file
if succeed_creating_service_category.size > 0:
    val_f = pd.DataFrame(succeed_creating_service_category)
    val_f.to_csv("output/created_service_categories.csv")

#logout
print("\n" + "-"*50)
logout_user = post_request(endpoint, {"_req":"logout"}, {"applicationid":connID})
if logout_user.status_code == 200:
    print("User logout successfull...")
    print(logout_user.json())

print("\n")

