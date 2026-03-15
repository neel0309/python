import sqlite3


conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY,
    name TEXT)''')

print("Successfully created table")

cursor.execute('''INSERT INTO test (id,name) VALUES (21,'das')''')

print("Successfully inserted table")

cursor.execute('''SELECT name FROM test ORDER BY id''')
print(cursor.fetchall())
