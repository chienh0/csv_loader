## CVS Loader: Loading CSV files into local database using Python

### Project Goal 
To create a Python script that can automatically load a CSV file into a local Postgresql database. The script will use a config file to pass through the input file path and the pytest library to test.

### Tech Stack
<p float='left'>
  <img src='/logos/logo_excel.png' width='170' />&nbsp;&nbsp;&nbsp;&nbsp;
  <img src='/logos/logo_postgres.png' width='150' />&nbsp;&nbsp;&nbsp;&nbsp; 
  <img src='/logos/logo_python.png' width='130' />
</p>

### Steps
1. Install the necessary packages. To accomplish this, you can run the following command in your terminal: 
```python
pip install pandas psycopg2-binary
```
2. Create a local Postgresql database. 
3. Create a new Python script called load_csv_to_postgresql.py.
4. Import the necessary libraries at the top of the script:
```python
import pandas as pd
import psycopg2
import configparser
```
5. Define a function to read the configuration file. In this function, we will use the configparser library to read the values from the config file.
```python
def read_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config['DEFAULT']
```
6. Define a function to create a connection to the Postgresql database. In this function, we will use the psycopg2 library to create a connection object.
```python
def create_connection(config):
    conn = psycopg2.connect(
        host=config['host'],
        database=config['database'],
        user=config['user'],
        password=config['password'],
        port=config['port']
    )
    return conn
```
7. Define a function to load the CSV file into a pandas DataFrame.
```python
def load_csv_file(file_path):
    return pd.read_csv(file_path)
```
8. Define a function to insert the data into the Postgresql database. In this function, we will use the psycopg2 library to create a cursor object and execute the SQL statement to insert the data into the database.
```python
def insert_data(conn, df, table_name):
    cursor = conn.cursor()
    for index, row in df.iterrows():
        sql = f"INSERT INTO {table_name} VALUES {tuple(row.values)};"
        cursor.execute(sql)
    conn.commit()
```
9.  Define a main function that will tie everything together. In this function, we will call the other functions in the correct order.
```python
def main():
    config = read_config('config.ini')
    conn = create_connection(config)
    df = load_csv_file(config['input_file_path'])
    insert_data(conn, df, config['table_name'])
```
10. Create a configuration file called config.ini. In this file, we will specify the input file path, database details, and table name.
11. Create a data.csv file in the same directory as your Python script. This file should contain the data that we want to insert into the database.
12. Test our script using the pytest library. In the same directory as our Python script, create a file called test_load_csv_to_postgresql.py. In this file, we will write unit tests to ensure that the script is working as expected. Here's an example test:
```python
def test_insert_data():
    config = read_config('config.ini')
```
