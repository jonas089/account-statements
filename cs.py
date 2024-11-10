# Credit suisse scripts
from lib import *
from constants import CREDIT_SUISSE_REL_PATH
def test_cs_parser():
    MASTER_KEY = 'Unknown'
    parser = Parser(MASTER_KEY, None)
    parser.parse_file(os.path.join(CREDIT_SUISSE_REL_PATH, "account.csv"))
    print(parser.file_cache.keys())

test_cs_parser()