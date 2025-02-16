from lib import *
from cs import sum_merchant_MMYYYY
from constants import REVOLUT_REL_PATH

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
    revolut_expanses = round_sorted_expanses(revolut_parser.sum_sorted_expanses(revolut_expanses, 'Description', 'Amount'))
    credit_suisse_expanses = round_sorted_expanses(sum_merchant_MMYYYY(mmyyyy))
    revolut_statement = format_statement(revolut_expanses)
    credit_suisse_statement = format_statement(credit_suisse_expanses)
    if not os.path.exists('out'):
        os.makedirs('out')

    # Export revolut statement
    revolut_filename = 'out/Revolut_{month}_{year}.txt'.format(month=month, year=year)
    write_statement(revolut_filename, revolut_statement)

    # Export credit suisse statement
    credit_suisse_filename = 'out/CreditSuisse_{month}_{year}.txt'.format(month=month, year=year)
    write_statement(credit_suisse_filename, credit_suisse_statement)


def format_statement(statement):
    lines = ""
    for merchant in statement:
        out = "{name}: {value} CHF".format(name=merchant, value=statement[merchant])
        lines += out
        lines += '\n'
    return lines

def write_statement(filename, statement):
    try:
        open(filename, 'x')
    except Exception as exists:
        print('[Error]: Statement exists, try again!')
        main()
    with open(filename, 'w') as file:
        file.write(statement)

main()