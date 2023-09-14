# Import libraries required for connecting to mysql
# Install it using the below command
# python3 -m pip install mysql-connector-python==8.0.31
import mysql.connector

# Connect to MySQL
# connect to database
connection = mysql.connector.connect(user='root', password='MzIxMjQtZ2lhbmdm',host='127.0.0.1',database='sales')

# create cursor
cursor = connection.cursor()

# Import libraries required for connecting to DB2 or PostgreSql
# This program requires the python module ibm-db to be installed.
# Install it using the below command
# python3 -m pip install ibm-db==3.1.4

import ibm_db

# connecttion details

dsn_hostname = "hostname_here" # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_uid = "username_here"        # e.g. "abc12345"
dsn_pwd = "password_here"      # e.g. "7dBZ3wWt9XN6$o0J"
dsn_port = "port_here"                # e.g. "50000" 
dsn_database = "bludb"            # i.e. "BLUDB"
dsn_driver = "{IBM DB2 ODBC DRIVER}" # i.e. "{IBM DB2 ODBC DRIVER}"           
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_security = "SSL"              # i.e. "SSL"

#Create the dsn connection string
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd, dsn_security)

# Connect to DB2 or PostgreSql
# create connection
conn = ibm_db.connect(dsn, "", "")
print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)


# Find out the last rowid from DB2 data warehouse or PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database or PostgreSql.

def get_last_rowid():
    SQL = "select max(rowid) from sales_data"
    stmt = ibm_db.exec_immediate(conn, SQL)
    res = ibm_db.fetch_both(stmt)
    print(res)
    return int(res[0])

last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
    SQL = "select * from sales_data where rowid > %s"
    cursor.execute(SQL, [rowid])
    new_recs = cursor.fetchall()
    for row in new_recs:
        print(row)
    return new_recs

new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 or PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database or PostgreSql.

def insert_records(records):
    SQL = "insert into sales_data(rowid, product_id, customer_id, quantity) values(?,?,?,?);"
    stmt = ibm_db.prepare(conn, SQL)

    for record in records:
        ibm_db.execute(stmt, record)

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse

# disconnect from DB2 or PostgreSql data warehouse 

# End of program
