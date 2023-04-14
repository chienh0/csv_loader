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
1. Install the Python packages (pandas, pyscopg2) using pip:
```
pip install pandas psycopg2
```
2. Create a local Postgresql database. 
3. To use the script, run the following command:
```
python3 main.py
```

### Configuration file
The config.json file contains the following keys: 
* host: the hostname or IP address of the PostgreSQL server 
* port: the port number of the PostgreSQL server 
* database: the name of the PostgreSQL database to connect to 
* user: the username to use for authentication 
* password: the password to use for authentication

### Limitations
By default, the script will create a table with the same name as the CSV file and with the columns column1, column2, and column3, all of type TEXT. 