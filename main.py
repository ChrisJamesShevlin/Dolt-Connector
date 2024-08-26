import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='Historic_ftse',
        user='root',
        password=''
    )

    if conn.is_connected():
        print('Connected to MySQL database')
        
        # Create a cursor object
        cursor = conn.cursor()
        
        # Execute a query
        cursor.execute('SELECT * FROM Sheet1')
        
        # Fetch all rows from the last executed statement
        rows = cursor.fetchall()
        
        # Print the rows
        for row in rows:
            print(row)

except Error as e:
    print(f"Error: {e}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print('MySQL connection is closed')
