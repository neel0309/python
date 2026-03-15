import psycopg2


def getConnection():
    conn = psycopg2.connect(
        host="localhost",
        database="testdb",
        user="postgres",
        password="yourpassword"
    )
    return conn


def table():
    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test (
            id SERIAL PRIMARY KEY,
            name TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO test (name) VALUES (%s)
    """, ("das",))

    cursor.execute("SELECT name FROM test ORDER BY id")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.commit()
    cursor.close()
    conn.close()


table()