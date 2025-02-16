import pandas as pd
import re

def extract_fields(row):
    line = ','.join(map(str, row))  # Convert row to a single line string
    match = re.search(r"^(\d{2}\.\d{2}\.\d{4}),[^,]*?,\d{2}\.\d{2}\.\d{4} \d{2}:\d{2} ([^,]+),[^,]*?,([^,]+),", line)
    if match:
        date = match.group(1).strip()
        transaction_name = match.group(2).strip()
        price = match.group(3).strip()
        return pd.Series([date, transaction_name, price])
    return pd.Series([None, None, None])

import pandas as pd

def extract_fields(row):
    """Assume extract_fields processes the row and extracts Date, Transaction Name, and Price."""
    try:
        date, transaction_name, price = row[0], row[1], row[2]
        return pd.Series([date, transaction_name, price])
    except Exception as e:
        return pd.Series([None, None, None])

def extract_transactions():
    try:
        df = pd.read_csv("banks/cs/account.csv", header=None)
    except Exception as e:
        print(f"Error reading file: {e}")
        return []    
    if df.shape[1] < 3:
        print("CSV format incorrect, expecting at least 3 columns.")
        return []
    df[['Date', 'Transaction Name', 'Price']] = df.apply(extract_fields, axis=1)
    df = df.dropna(subset=['Date', 'Transaction Name', 'Price'])
    transactions = df[['Date', 'Transaction Name', 'Price']].to_dict(orient='records')
    return transactions

# example: 092024 = 09.2024 (SEPTEMBER 2024)
def sum_merchant_MMYYYY(mmyyyy):
    out = {}
    transactions = extract_transactions()
    for transaction in transactions:
        try:
            if transaction['Date'][3:5] != mmyyyy[0:2] or transaction['Date'][6:10] != mmyyyy[2:6]:
                continue
            if transaction['Transaction Name'] in out.keys():
                out[transaction['Transaction Name']] += float(transaction['Price'])
            else:
                out[transaction['Transaction Name']] = float(transaction['Price'])
        except Exception as e:
            print("Warning: ", e)
    return out
    # sum amounts by merchant and return
    # todo: make client that will do this for revolut + credit suisse, 
    # the only input will be MMYY.