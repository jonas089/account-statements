import pandas as pd
import re
from lib import round_sorted_expanses

def extract_fields(row):
    line = ','.join(map(str, row))  # Convert row to a single line string
    match = re.search(r"^(\d{2}\.\d{2}\.\d{4}),[^,]*?,\d{2}\.\d{2}\.\d{4} \d{2}:\d{2} ([^,]+),[^,]*?,([^,]+),", line)
    if match:
        date = match.group(1).strip()
        transaction_name = match.group(2).strip()
        price = match.group(3).strip()
        return pd.Series([date, transaction_name, price])
    return pd.Series([None, None, None])

def extract_transactions():
    # path is fixed, replace file upon change
    df = pd.read_csv("banks/cs/account.csv", header=None)
    df[['Date', 'Transaction Name', 'Price']] = df.apply(extract_fields, axis=1)
    df = df.dropna(subset=['Date', 'Transaction Name', 'Price'])
    transactions = []
    for _, row in df.iterrows():
        date = row['Date']
        transaction_name = row['Transaction Name']
        price = row['Price']
        
        transaction = {}
        transaction['date'] = date
        transaction['name'] = transaction_name
        transaction['price'] = price
        transactions.append(transaction)
    return transactions
# example: 092024 = 09.2024 (SEPTEMBER 2024)
def sum_merchant_MMYYYY(mmyyyy):
    out = {}
    transactions = extract_transactions()
    for transaction in transactions:
        try:
            if transaction['date'][3:5] != mmyyyy[0:2] or transaction['date'][6:10] != mmyyyy[2:6]:
                continue
            if transaction['name'] in out:
                out[transaction['name']] += float(transaction['price'])
            else:
                out[transaction['name']] = float(transaction['price'])
        except Exception as e:
            print("Warning: ", e)
    return out
    # sum amounts by merchant and return
    # todo: make client that will do this for revolut + credit suisse, 
    # the only input will be MMYY.