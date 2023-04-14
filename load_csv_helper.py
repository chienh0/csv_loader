import psycopg2
import pandas as pd
import json


def load_config_file(config_file_path):
    with open(config_file_path, 'r') as f:
        config = json.load(f)
    return config


def load_csv_file(csv_file_path):
    df = pd.read_csv(csv_file_path)
    return df


def get_db_connection(db_params):
    conn = psycopg2.connect(**db_params)
    return conn


def create_table(cur, table_name):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS {table_name} (
        column1 TEXT,
        column2 TEXT,
        column3 TEXT
    )
    """.format(table_name=table_name)
    cur.execute(create_table_sql)


def insert_data(cur, table_name, data):
    insert_data_sql = """
    INSERT INTO {table_name} (column1, column2, column3) VALUES (%s, %s, %s)
    """.format(table_name=table_name)
    for row in data:
        cur.execute(insert_data_sql, (str(row[0]), str(row[1]), str(row[2])))
