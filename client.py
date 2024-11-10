from lib import *
from cs import sum_merchant_MMYYYY

revolut_mmyyyy = {
    '01': 'january',
    '02': 'february',
    '03': 'march',
    '04': 'april',
    '05': 'may',
    '06': 'june',
    '07': 'july',
    '08': 'august',
    '09': 'september'
}

def main():
    mmyyyy = input("Enter MMYYY (example 092024, September 2024): ")
    # Description is Merchant Description for Revolut
    revolut_parser = Parser('Description', None)
    

main()