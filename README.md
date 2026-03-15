# SQLite Example in Python

This script demonstrates how to create a database, create a table, insert data, and retrieve records using Python and SQLite.

It uses Python’s built-in sqlite3 module to interact with a local database file.

# Step 1 — Import SQLite Library
import sqlite3

The sqlite3 module allows Python programs to interact with SQLite databases.

SQLite is a lightweight file-based database, meaning it does not require a separate server.

# Step 2 — Create or Connect to a Database
conn = sqlite3.connect('test.db')

This line:

Connects to a database file called test.db

If the file does not exist, SQLite automatically creates a new database

# Step 3 — Create a Cursor
cursor = conn.cursor()

A cursor is used to execute SQL commands on the database.

It acts as a control interface between Python and the database.

# Step 4 — Create a Table
cursor.execute('''CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY,
    name TEXT)''')

This SQL command creates a table named test.


The clause IF NOT EXISTS ensures the table is only created if it does not already exist.

This prevents errors if the script runs multiple times.

# Step 5 — Confirmation Message
print("Successfully created table")

This simply prints a message indicating that the table creation step completed.

# Step 6 — Insert Data into the Table
cursor.execute('''INSERT INTO test (id,name) VALUES (21,'das')''')

This SQL statement inserts a new record into the table.

Values inserted:

id	name
21	das
Step 7 — Confirmation Message
print("Successfully inserted table")

This prints a message confirming that the record was inserted successfully.

# Step 8 — Retrieve Data
cursor.execute('''SELECT name FROM test ORDER BY id''')

This query retrieves the name column from the table.

The results are sorted by the id column in ascending order.

# Step 9 — Display Results
print(cursor.fetchall())

fetchall() retrieves all rows returned by the query.

Example output:

[('das',)]

This output means that the table contains one record with the name "das".

Example Table Content

After running the script, the table will look like this:

id	name
21	das