import csv
import sqlite3


#---------------DB connection + Tbale creation-----------------------
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT
                    )
                    ''')


#------------------ Read CSV--------------
with open('users_data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        name = row["name"]
        email = row["email"]

        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))


#----------------------------- Commit and Fetch Data -----------------------
conn.commit()
print("CSV data inserted into the DB successfully.")


# Display all data from the DB

cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()

print("\n ======= Users in the DB =======")

for user in all_users:
    print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

conn.close()