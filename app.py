import sys
from config import DB_DETAILS
from util import get_tables


def main():
    """Program takes at least one argument"""
    venv = sys.argv[1]
    db_details = DB_DETAILS[venv]
    tables = get_tables('table_list.txt')


if __name__ == '__main__':
    main()
