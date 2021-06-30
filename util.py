import pandas as pd


def get_tables(path):
    tables = pd.read_csv('table_list.txt', sep=':')
    return tables.query('to_be_loaded == "yes"')