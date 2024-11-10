import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cs import sum_merchant_MMYYYY
from lib import round_sorted_expanses

def test_sum_merchant():
    print(round_sorted_expanses(sum_merchant_MMYYYY("102024")))

test_sum_merchant()