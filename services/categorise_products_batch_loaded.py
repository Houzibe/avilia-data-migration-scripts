#-------------------------------------------------------------
# DATA MIGRATION: CATEGORISE PRODUCTS (JSON BATCH LOADER)
#-------------------------------------------------------------
import numpy as np
import pandas as pd
import requests as req
import importlib
import sys

# ------------------------------------------------------------------
# 1. Configuration & paths
# ------------------------------------------------------------------
print("\n")
print("=" * 50)
print("         SCRIPT TO LOAD PRODUCTS (JSON BATCHES)")
print("=" * 50)

config_f = pd.read_json("../config.json")
endpoint = "https://api.testing.lemunz.io/"
login_user = None
connID = None
error_categorising_products = []
succeed_categorising_products = []

# ------------------------------------------------------------------
# 2. Dynamically import all product arrays and flatten to records
# ------------------------------------------------------------------
all_records = []  # each dict: catid, prodcode, descr

batches = range(11, 12) 
letters = [chr(ord('A') + i) for i in range(26)]
#letters = [chr(ord('B') + i) for i in range(1)]

for batch in batches:
    for letter in letters:
        module_name = f"data.r{batch}.s{batch}_{letter}"
        try:
            module = importlib.import_module(module_name)
        except ModuleNotFoundError:
            continue
        except Exception as e:
            print(f"Error importing {module_name}: {e}")
            continue

        for attr_name in dir(module):
            if attr_name.startswith('_'):
                continue
            obj = getattr(module, attr_name)
            if not isinstance(obj, np.ndarray):
                continue

            print(f"Processing '{attr_name}' from {module_name}")

            # Extract records from the array
            if obj.dtype.names is not None:
                # Structured array with named fields
                for row in obj:
                    all_records.append({name: row[name] for name in obj.dtype.names})
            elif obj.ndim == 2:
                # Assume columns: [catid, prodcode, descr]
                for row in obj:
                    all_records.append({
                        'catid': row[0],
                        'prodcode': row[1],
                        'descr': row[2] if len(row) > 2 else ''
                    })
            elif obj.dtype == object:
                # Array of dicts, tuples, or lists
                for item in obj:
                    if isinstance(item, dict):
                        all_records.append(item)
                    elif isinstance(item, (list, tuple)) and len(item) >= 3:
                        all_records.append({
                            'catid': item[0],
                            'prodcode': item[1],
                            'descr': item[2]
                        })
                    else:
                        print(f"  Skipping unrecognised object: {item}")
            else:
                print(f"  Unhandled array dtype: {obj.dtype}")

if not all_records:
    print("No product records found. Exiting.")
    sys.exit(1)

# Convert to DataFrame and ensure columns
df = pd.DataFrame(all_records)
print(f"\nTotal product records loaded: {len(df)}")
print("Columns in DataFrame:", df.columns.tolist())

required_cols = ['catid', 'prodcode', 'descr']
missing = [col for col in required_cols if col not in df.columns]
if missing:
    if len(df.columns) >= 3:
        df.columns = required_cols
        print("Renamed columns to catid, prodcode, descr")
    else:
        raise KeyError(f"DataFrame missing required columns: {missing}. Available: {df.columns.tolist()}")

# ------------------------------------------------------------------
# 3. Group products by category – prepare comma-separated strings
# ------------------------------------------------------------------
grouped = df.groupby('catid').agg({
    'prodcode': list,
    'descr': list
}).reset_index()

print(f"Number of unique categories: {len(grouped)}")

# Convert lists to comma-separated strings
def join_list(lst):
    return ','.join(str(v) for v in lst if v is not None and v != '')

grouped['prodcode_str'] = grouped['prodcode'].apply(join_list)
#grouped['descr_str'] = grouped['descr'].apply(lambda x: ','.join(str(v) for v in x))

# ------------------------------------------------------------------
# 4. Login to the remote database
# ------------------------------------------------------------------
print("Login to connect to the database.")
username = input("Enter username: ")
password = input("Enter password: ")

print("\nConnecting to the database...")
data={
        "_req": "login",
        "org": config_f["payer"]["org"],
        "mid": config_f["payer"]["mid"],
        "midtype": config_f["payer"]["midtype"],
        "magik": config_f["payer"]["magik"],
        "user": username,
        "pass": password
    }
login = req.post(endpoint,data, headers=None)

if login.status_code == 200:
    response = login.json()
    print(f"Login response: {response}")
    login_user = response["result"]["value"]
    connID = login_user[0][0]["APPID"]
    print("Login successfully...")
else:
    print("Login failed. Error has occurred! Try again later.")
    sys.exit(1)

if login_user:
    print("\nLogging User")
    print("-" * 50)
    print(f"User:  {login_user[0][0]['SURNAME']} {login_user[0][0]['OTHERNAMES']}")
    print(f"Last Login: {login_user[0][0]['LASTLOGIN']}")
    print("-" * 50)

# ------------------------------------------------------------------
# 5. Post each category using the plural endpoint
# ------------------------------------------------------------------
def post_request(url, params, header=None):
    return req.post(url, params, headers=header)

for _, row in grouped.iterrows():
    catid = row['catid']
    prodcode_str = row['prodcode_str']
    #descr_str = row['descr_str']

    # Build the payload exactly as requested: prodcode as a list
    payload = {
        "_req": "n.acatprods",
        "catid": catid,
        "prodcode": prodcode_str,
        #"descr": descr_str
        "descr": ""  # Sending empty string for descr as per API spec
    }

    print(f"\nSending batch for catid={catid} ({len(row['prodcode'])} products)")
    print(f"Payload: {payload}")

    response = post_request(endpoint, payload, {"applicationid": connID})

    if response.status_code != 200:
        print("Error: ", response)
        for prod in row['prodcode']:
            error_categorising_products.append({
                "catid": catid,
                "prodcode": prod,
                "descr": "",  # we don't have per-product descr in error log
                "severity": "HTTP_ERROR",
                "error_message": f"Status code {response.status_code}"
            })
        continue

    res = response.json()
    print(f"Server response: {res}")

"""
    if res.get("error"):
        err_info = res["error"]
        print(f"Error from server: {err_info}")
        for prod in row['prodcode']:
            error_categorising_products.append({
                "catid": catid,
                "prodcode": prod,
                "descr": "",
                "severity": err_info.get("severity", ""),
                "error_message": err_info.get("msg", "Unknown error")
            })
        continue

    # Expect a list of IDs in the same order as prod_list
    
    result_value = res.get("result", {}).get("value")
    prod_list = row['prodcode']
    desc_list = row['descr']

    if isinstance(result_value, list):
        ids = [item.get("id") if isinstance(item, dict) else item for item in result_value]
    elif isinstance(result_value, dict) and "id" in result_value:
        # Unexpected: single ID – treat as error
        for prod in prod_list:
            error_categorising_products.append({
                "catid": catid,
                "prodcode": prod,
                "descr": "",
                "severity": "API_RESPONSE",
                "error_message": "Expected list of IDs, got single ID"
            })
        continue
    else:
        for prod in prod_list:
            error_categorising_products.append({
                "catid": catid,
                "prodcode": prod,
                "descr": "",
                "severity": "API_RESPONSE",
                "error_message": "No ID list in response"
            })
        continue

    if len(ids) != len(prod_list):
        for prod in prod_list:
            error_categorising_products.append({
                "catid": catid,
                "prodcode": prod,
                "descr": "",
                "severity": "MISMATCH",
                "error_message": f"Expected {len(prod_list)} IDs, got {len(ids)}"
            })
        continue

    # Record successes
    for prod, desc, pid in zip(prod_list, desc_list, ids):
        succeed_categorising_products.append({
            "catid": catid,
            "prodcode": prod,
            "descr": desc,
            "id": pid
        })
    """

# ------------------------------------------------------------------
# 6. Write logs to CSV files
# ------------------------------------------------------------------
if error_categorising_products:
    print("Error logs: ", error_categorising_products)
    error_f = pd.DataFrame(error_categorising_products)
    error_f.to_csv("output/error_categorising_products.csv", index=False)

if succeed_categorising_products:
    val_f = pd.DataFrame(succeed_categorising_products)
    val_f.to_csv("output/categorised_products.csv", index=False)

#print(f"\nTotal successful products: {len(succeed_categorising_products)}")
#print(f"Total errors: {len(error_categorising_products)}")

# ------------------------------------------------------------------
# 7. Logout
# ------------------------------------------------------------------
print("\n" + "-" * 50)
logout_user = req.post(endpoint, data={"_req": "logout"}, headers={"applicationid": connID})
if logout_user.status_code == 200:
    print("User logout successful...")
    print(logout_user.json())

print("\n")

"""
#-------------------------------------------------------------
# DATA MIGRATION: CATEGORISE PRODUCTS (ROBUST BATCH LOADER)
#-------------------------------------------------------------
import numpy as np
import pandas as pd
import requests as req
import importlib
import sys
import os

# ------------------------------------------------------------------
# 1. Configuration & paths
# ------------------------------------------------------------------
print("\n")
print("=" * 50)
print("         SCRIPT TO LOAD PRODUCTS (GROUPED BY CATEGORY)")
print("=" * 50)

config_f = pd.read_json("../config.json")
endpoint = "https://api.testing.lemunz.io/"
login_user = None
connID = None
error_categorising_products = []
succeed_categorising_products = []

# ------------------------------------------------------------------
# 2. Dynamically import all product arrays and flatten to records
# ------------------------------------------------------------------
all_records = []  # each element will be a dict with keys: catid, prodcode, descr

batches = range(11, 12) # Adjust the range as needed to cover all batches
#letters = [chr(ord('A') + i) for i in range(26)]
letters = [chr(ord('A') + i) for i in range(1)]

for batch in batches:
    for letter in letters:
        module_name = f"data.r{batch}.s{batch}_{letter}"
        try:
            module = importlib.import_module(module_name)
        except ModuleNotFoundError:
            continue
        except Exception as e:
            print(f"Error importing {module_name}: {e}")
            continue

        for attr_name in dir(module):
            if attr_name.startswith('_'):
                continue
            obj = getattr(module, attr_name)
            if not isinstance(obj, np.ndarray):
                continue

            print(f"Processing '{attr_name}' from {module_name}")

            # Extract records from this array
            if obj.dtype.names is not None:
                # Structured array with named fields
                for row in obj:
                    all_records.append({name: row[name] for name in obj.dtype.names})
            elif obj.ndim == 2:
                # 2D array: assume columns are [catid, prodcode, descr]
                for row in obj:
                    all_records.append({
                        'catid': row[0],
                        'prodcode': row[1],
                        'descr': row[2] if len(row) > 2 else ''
                    })
            elif obj.dtype == object:
                # Array of Python objects – could be dicts, tuples, or lists
                for item in obj:
                    if isinstance(item, dict):
                        # Use the dict as-is (must contain 'catid', 'prodcode', 'descr')
                        all_records.append(item)
                    elif isinstance(item, (list, tuple)) and len(item) >= 3:
                        all_records.append({
                            'catid': item[0],
                            'prodcode': item[1],
                            'descr': item[2]
                        })
                    else:
                        print(f"  Skipping unrecognised object: {item}")
            else:
                print(f"  Unhandled array dtype: {obj.dtype}")

if not all_records:
    print("No product records found. Exiting.")
    sys.exit(1)

# Convert to DataFrame
df = pd.DataFrame(all_records)
print(f"\nTotal product records loaded: {len(df)}")
print("Columns in DataFrame:", df.columns.tolist())

# Ensure we have the required columns
required_cols = ['catid', 'prodcode', 'descr']
missing = [col for col in required_cols if col not in df.columns]
if missing:
    # If 'catid' is missing, try to guess: maybe first column is catid?
    if len(df.columns) >= 3:
        df.columns = required_cols  # force rename
        print("Renamed columns to catid, prodcode, descr")
    else:
        raise KeyError(f"DataFrame missing required columns: {missing}. Available: {df.columns.tolist()}")

# ------------------------------------------------------------------
# 3. Group products by category
# ------------------------------------------------------------------
grouped = df.groupby('catid').agg({
    'prodcode': list,
    'descr': lambda x: ['' if pd.isna(v) or v is None else str(v) for v in x]
}).reset_index()

print(f"Number of unique categories: {len(grouped)}")

# ------------------------------------------------------------------
# 4. Login to the remote database
# ------------------------------------------------------------------
print("Login to connect to the database.")
username = input("Enter username: ")
password = input("Enter password: ")

print("\nConnecting to the database...")
params = {
            "_req":"login",
            "org" : config_f["payer"]["org"],
            "mid" : config_f["payer"]["mid"],
            "midtype" : config_f["payer"]["midtype"],
            "magik" : config_f["payer"]["magik"],
            "user" : username,
            "pass" : password
    }
login = req.post(endpoint, params, headers=None)

if login.status_code == 200:
    response = login.json()
    print(f"Login response: {response}")
    login_user = response["result"]["value"]
    connID = login_user[0][0]["APPID"]
    print("Login successfully...")
else:
    print("Login failed. Error has occurred! Try again later.")
    sys.exit(1)

if login_user:
    print("\nLogging User")
    print("-" * 50)
    print(f"User:  {login_user[0][0]['SURNAME']} {login_user[0][0]['OTHERNAMES']}")
    print(f"Last Login: {login_user[0][0]['LASTLOGIN']}")
    print("-" * 50)

# ------------------------------------------------------------------
# 5. Post each category's products as a batch
# ------------------------------------------------------------------
def post_request(url, params, header=None):
    return req.post(url, params, headers=header)

for _, row in grouped.iterrows():
    catid = row['catid']
    prod_list = row['prodcode']
    desc_list = row['descr']

    #prodcode_str = ','.join(str(p) for p in prod_list)
    prodcode_str = []
    for p in prod_list:
        if isinstance(p, (list, tuple)):
            prodcode_str.append(int(p[0]))  # Take the first element if it's a list/tuple
        else:
            prodcode_str.append(int(p))
    
    #descr_str = ','.join(str(d) for d in desc_list)
    descr_str = []

    params = {
        "_req": "n.acatprod",
        "catid": catid,
        "prodcode": prodcode_str,
        "descr": descr_str
    }

    print(f"\nSending batch for catid={catid} ({len(prod_list)} products)")
    print(params)

    response = post_request(endpoint, params, {"applicationid": connID})

    if response.status_code != 200:
        for prod, desc in zip(prod_list, desc_list):
            error_categorising_products.append({
                "catid": catid,
                "prodcode": prod,
                "descr": desc,
                "severity": "HTTP_ERROR",
                "error_message": f"Status code {response.status_code}"
            })
        continue

    res = response.json()
    print(f"Server response: {res}")

    if res.get("error"):
        err_info = res["error"]
        for prod, desc in zip(prod_list, desc_list):
            error_categorising_products.append({
                "catid": catid,
                "prodcode": prod,
                "descr": desc,
                "severity": err_info.get("severity", ""),
                "error_message": err_info.get("msg", "Unknown error")
            })
        continue

    # Expect a list of IDs in the same order as prod_list
    result_value = res.get("result", {}).get("value")
    if isinstance(result_value, list):
        ids = [item.get("id") if isinstance(item, dict) else item for item in result_value]
    elif isinstance(result_value, dict) and "id" in result_value:
        # Unexpected: single ID for a batch – treat as error
        for prod, desc in zip(prod_list, desc_list):
            error_categorising_products.append({
                "catid": catid,
                "prodcode": prod,
                "descr": desc,
                "severity": "API_RESPONSE",
                "error_message": "Expected list of IDs, got single ID"
            })
        continue
    else:
        for prod, desc in zip(prod_list, desc_list):
            error_categorising_products.append({
                "catid": catid,
                "prodcode": prod,
                "descr": desc,
                "severity": "API_RESPONSE",
                "error_message": "No ID list in response"
            })
        continue

    if len(ids) != len(prod_list):
        for prod, desc in zip(prod_list, desc_list):
            error_categorising_products.append({
                "catid": catid,
                "prodcode": prod,
                "descr": desc,
                "severity": "MISMATCH",
                "error_message": f"Expected {len(prod_list)} IDs, got {len(ids)}"
            })
        continue

    for prod, desc, pid in zip(prod_list, desc_list, ids):
        succeed_categorising_products.append({
            "catid": catid,
            "prodcode": prod,
            "descr": desc,
            "id": pid
        })

# ------------------------------------------------------------------
# 6. Write logs to CSV files
# ------------------------------------------------------------------
if error_categorising_products:
    error_f = pd.DataFrame(error_categorising_products)
    error_f.to_csv("output/error_categorising_products.csv", index=False)

if succeed_categorising_products:
    val_f = pd.DataFrame(succeed_categorising_products)
    val_f.to_csv("output/categorised_products.csv", index=False)

print(f"\nTotal successful products: {len(succeed_categorising_products)}")
print(f"Total errors: {len(error_categorising_products)}")

# ------------------------------------------------------------------
# 7. Logout
# ------------------------------------------------------------------
print("\n" + "-" * 50)
logout_user = post_request(endpoint, {"_req": "logout"}, {"applicationid": connID})
if logout_user.status_code == 200:
    print("User logout successful...")
    print(logout_user.json())

print("\n")
"""