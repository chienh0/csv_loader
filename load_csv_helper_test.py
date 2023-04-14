import pytest
import pandas as pd
import psycopg2
from load_csv_helper import load_csv_file, get_db_connection, create_table, insert_data

@pytest.fixture
def test_data():
    df = pd.DataFrame({
        'column1': ['a', 'b', 'c'],
        'column2': [1, 2, 3],
        'column3': [1.0, 2.0, 3.0]
    })
    return df

def test_load_csv_file(test_data):
    csv_file_path = 'test.csv'
    test_data.to_csv(csv_file_path, index=False)
    df = load_csv_file(csv_file_path)
    assert df.equals(test_data)

def test_get_db_connection():
    db_params = {
        'host': 'localhost',
        'port': 5432,
        'user': 'myuser',
        'password': 'mypassword',
        'database': 'mydb'
    }
    conn = get_db_connection(db_params)
    assert isinstance(conn, psycopg2.extensions.connection)

def test_create_table():
    db_params = {
        'host': 'localhost',
        'port': 5432,
        'user': 'myuser',
        'password': 'mypassword',
        'database': 'mydb'
    }
    conn = get_db_connection(db_params)
    cur = conn.cursor()
    table_name = 'test_table'
    create_table(cur, table_name)
    cur.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = %s", (table_name,))
    result = cur.fetchone()[0]
    cur.close()
    conn.close()
    assert result == 1

def test_insert_data():
    db_params = {
        'host': 'localhost',
        'port': 5432,
        'user': 'myuser',
        'password': 'mypassword',
        'database': 'mydb'
    }
    conn = get_db_connection(db_params)
    cur = conn.cursor()
    table_name = 'test_table'
    create_table(cur, table_name)
    data = [('a', 1, 1.0), ('b', 2, 2.0), ('c', 3, 3.0)]
    insert_data(cur, table_name, data)
    cur.execute("SELECT COUNT(*) FROM {table_name}".format(table_name=table_name))
    result = cur.fetchone()[0]
    cur.close()
    conn.close()
    assert result == 3
