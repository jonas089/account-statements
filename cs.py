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

def extract_transactions():
    df = pd.read_csv("banks/cs/account.csv", header=None)
    df[['Date', 'Transaction Name', 'Price']] = df.apply(extract_fields, axis=1)
    df = df.dropna(subset=['Date', 'Transaction Name', 'Price'])
    for index, row in df.iterrows():
        date = row['Date']
        transaction_name = row['Transaction Name']
        price = row['Price']
        
        # Access each component individually
        print(f"Transaction {index + 1}:")
        print(f"  Date: {date}")
        print(f"  Transaction Name: {transaction_name}")
        print(f"  Price: {price}")

extract_transactions()