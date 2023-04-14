from load_csv_helper import load_config_file, load_csv_file, create_table, insert_data, get_db_connection

def main():
    # Load the configuration file
    config = load_config_file('config.json')

    # Extract the CSV file path from the configuration file
    csv_file_path = config['csv_file_path']

    # Load the CSV file into a pandas DataFrame
    df = load_csv_file(csv_file_path)

    # Define our PostgreSQL database connection parameters
    db_params = config['database']

    # Connect to the PostgreSQL database
    conn = get_db_connection(db_params)

    # Create a cursor object to execute SQL statements
    cur = conn.cursor()

    # Define the name of the table we want to create in the database
    table_name = 'mytable'

    # Create the table in the database
    create_table(cur, table_name)

    # Extract the data from the DataFrame as a list of tuples
    data = [tuple(x) for x in df.to_records(index=False)]

    # Insert the data into the database
    insert_data(cur, table_name, data)

    # Commit the changes to the database
    conn.commit()

    # Close the database connection and cursor
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
