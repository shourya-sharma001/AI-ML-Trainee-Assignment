import csv
import sqlite3


def create_table(cursor):
    # email marked UNIQUE so re-running this doesn't insert the same user twice
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE
        )
    ''')


def load_users_from_csv(filepath):
    # skips any row that's missing a name or email instead of inserting blanks
    valid_rows = []
    with open(filepath, "r", encoding="utf-8", newline="") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            name = (row.get("name") or "").strip()
            email = (row.get("email") or "").strip()

            if not name or not email:
                continue

            valid_rows.append((name, email))

    return valid_rows


def save_users(cursor, users):
    for name, email in users:
        cursor.execute(
            "INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )


def display_users(cursor):
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()

    print("\n ======= Users in the DB =======")
    for user in all_users:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")


def main():
    users = load_users_from_csv("users_data.csv")
    if not users:
        print("No valid rows found in the CSV, nothing to insert.")
        return

    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        create_table(cursor)
        save_users(cursor, users)
        conn.commit()
        print("CSV data inserted into the DB successfully.")
        display_users(cursor)


if __name__ == "__main__":
    main()