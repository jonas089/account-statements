import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lib import *
from constants import REVOLUT_REL_PATH
def test_solve_for_master_key():
    MASTER_KEY = 'Description'
    EXPECTED_VALUE = 'Coop'
    AMOUNT_KEY = 'Amount'
    parser = Parser(MASTER_KEY, EXPECTED_VALUE)
    expanses = parser.solve_directory_for_master_key(REVOLUT_REL_PATH)
    sum = calculate_sum(expanses[0], AMOUNT_KEY)
    #print("Sum: ", sum)

def test_solve_and_sort():
    MASTER_KEY = 'Description'
    TEST_DATA_PATH = os.path.join(REVOLUT_REL_PATH, "january_2025.csv")
    parser = Parser(MASTER_KEY, None)
    parser.parse_file(TEST_DATA_PATH)
    expanses = parser.solve_expanses()
    expanses = parser.sort_expanses(expanses)
    #print("Sorted: ", expanses)  

def test_solve_directory():
    MASTER_KEY = 'Description'
    parser = Parser(MASTER_KEY, None)
    expanses = parser.solve_directory(REVOLUT_REL_PATH)
    #print("Expanses: ", expanses)

def test_sum_sorted_expanses():
    MASTER_KEY = 'Description'
    AMOUNT_KEY = 'Amount'
    parser = Parser(MASTER_KEY, None)
    expanses = parser.solve_directory(REVOLUT_REL_PATH)
    expanses = parser.sort_expanses_dict(expanses)
    expanses = round_sorted_expanses(parser.sum_sorted_expanses(expanses, MASTER_KEY, AMOUNT_KEY))
    #print("Rounded: ", expanses)

test_solve_for_master_key()
test_solve_and_sort()
test_solve_directory()
test_sum_sorted_expanses()