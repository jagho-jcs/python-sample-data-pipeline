import sys
from config import DB_DETAILS


def main():
    """Program takes at least one argument"""
    venv = sys.argv[1]
    db_details = DB_DETAILS[venv]
    print(db_details)


if __name__ == '__main__':
    main()
