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
    '09': 'september',
    '10': 'october',
    '11': 'november',
    '12': 'december'
}

def main():
    mmyyyy = input("Enter MMYYY (example 092024, September 2024): ")
    try:
        int(mmyyyy)
    except Exception as TypeError:
        print("[Error]: Invalid Input Type, try again!")
        main()

    if len(mmyyyy) != 6:
        print("[Error]: Invalid Input Length, try again!")
        main()
    
    # Description is Merchant Description for Revolut
    revolut_parser = Parser('Description', None)
    month = revolut_mmyyyy[mmyyyy[0:2]]
    year = mmyyyy[2:]
    revolut_parser.parse_file("{revolut_path}{month}_{year}.csv".format(revolut_path=REVOLUT_REL_PATH,month=month, year=year))
    revolut_expanses = revolut_parser.solve_expanses()
    revolut_expanses = revolut_parser.sort_expanses(revolut_expanses)
    revolut_expanses = revolut_parser.sum_sorted_expanses(revolut_expanses, 'Description', 'Amount')
    credit_suisse_expanses = sum_merchant_MMYYYY(mmyyyy)
    print_revolut_statement(revolut_expanses)
    print_credit_suisse_statement(credit_suisse_expanses)

def print_revolut_statement(statement):
    print(statement)
def print_credit_suisse_statement(statement):
    print(statement)

main()