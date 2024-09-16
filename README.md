# MySQL Database Connection Example in Python

This repository contains a Python script that connects to a **MySQL database** and fetches all rows from a specified table. It demonstrates how to establish a connection to a MySQL database using the `mysql-connector-python` library, execute queries, and handle the connection lifecycle properly.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Error Handling](#error-handling)
- [License](#license)

## Overview

This script connects to a MySQL database and executes a simple query to fetch all rows from a table named `Sheet1`. The main steps include:
1. Establishing a connection to the database.
2. Executing a SQL query to retrieve data.
3. Closing the connection after execution.

## Prerequisites

Before running the script, ensure that you have:
- **MySQL** installed and running.
- A MySQL database named `Historic_ftse`.
- A table named `Sheet1` in the `Historic_ftse` database.
- Python 3 installed on your machine.
- The `mysql-connector-python` library installed.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/mysql-connection-example.git
   cd mysql-connection-example
   ```

2. **Install dependencies**:
   Install the required MySQL connector library using pip:
   ```bash
   pip install mysql-connector-python
   ```

3. **Set up MySQL**:
   Make sure that your MySQL server is running and that you have the necessary database (`Historic_ftse`) and table (`Sheet1`) configured.

## Usage

To run the script, follow these steps:

1. **Configure MySQL connection**:
   Update the connection parameters in the script with your MySQL server details (if necessary):
   ```python
   conn = mysql.connector.connect(
       host='127.0.0.1',    # MySQL server host
       port=3306,           # MySQL server port
       database='Historic_ftse',  # Database name
       user='root',         # MySQL user
       password=''          # MySQL password
   )
   ```

2. **Run the script**:
   Execute the script to fetch all rows from the `Sheet1` table:
   ```bash
   python mysql_connection.py
   ```

   The output will display the rows fetched from the table.

### Example Output:
```bash
Connected to MySQL database
(1, 'FTSE 100', '2024-01-01', 7500)
(2, 'FTSE 100', '2024-01-02', 7600)
MySQL connection is closed
```

## Customization

You can customize the script to suit your needs:

1. **Change the database or table**:
   If you're working with a different database or table, simply update the `database` and query:
   ```python
   conn = mysql.connector.connect(
       host='127.0.0.1',
       port=3306,
       database='YourDatabaseName',
       user='root',
       password=''
   )
   cursor.execute('SELECT * FROM YourTableName')
   ```

2. **Modify the SQL query**:
   You can customize the SQL query to fetch specific data or use more complex queries:
   ```python
   cursor.execute('SELECT column1, column2 FROM Sheet1 WHERE column1 = "value"')
   ```

3. **Add data manipulation or logging**:
   You can add more functionality, such as logging, data transformation, or saving the fetched data to a file.

## Error Handling

The script includes basic error handling to ensure that:
- Any connection errors are caught and printed.
- The database connection is closed properly, even if an error occurs during execution.

Example of error handling:
```python
except Error as e:
    print(f"Error: {e}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print('MySQL connection is closed')
```

This ensures that your MySQL connection is gracefully closed after each operation, preventing any potential issues with unclosed connections.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

---

Feel free to modify the script and adapt it to your specific use case. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
