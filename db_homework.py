import sqlite3

conn = sqlite3.connect('employees.db')
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        age INTEGER,
        job TEXT
    )
""")

while True:
    user_input = input("Enter user information (name, surname, age, job), or print 'stop' to exit: ")

    if user_input.lower() == 'stop':
        break

    name, surname, age, job = user_input.split(',')
    cur.execute("INSERT INTO user (name, surname, age, job) VALUES (?, ?, ?, ?)",
                (name.strip(), surname.strip(), int(age.strip()), job.strip()))

    conn.commit()
    print("User data inserted successfully.")

conn.close()
