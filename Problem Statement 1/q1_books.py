import requests
import sqlite3


def fetch_books(query="python programming"):
    # pulling books from Open Library, added a timeout + status check
    # so this doesn't just hang or silently fail if the API is slow/down
    url = "https://openlibrary.org/search.json"
    try:
        response = requests.get(url, params={"q": query}, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get("docs", [])
    except requests.exceptions.RequestException as e:
        print("Couldn't reach the Open Library API:", e)
        return []
    except ValueError:
        print("Got a response back but it wasn't valid JSON.")
        return []


def create_table(cursor):
    # UNIQUE constraint so running this script twice doesn't just double up the rows
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        author TEXT,
                        year INTEGER,
                        UNIQUE(title, author, year)
                    )
    ''')


def save_books(cursor, books_list, limit=10):
    for book in books_list[:limit]:
        title = book.get("title", "Unknown Title")

        # author_name can be missing, or present but empty - handle both
        authors = book.get("author_name") or []
        author = authors[0] if authors else "Unknown Author"

        # leaving this as None when missing instead of 0, since 0 looks like a real year
        year = book.get("first_publish_year")

        if year is None:
            # SQLite treats NULL as never equal to itself, so the UNIQUE(title, author, year)
            # constraint doesn't catch duplicates when year is missing. Check manually here
            # so re-running the script doesn't insert the same no-year book twice.
            cursor.execute(
                "SELECT 1 FROM books WHERE title = ? AND author = ? AND year IS NULL",
                (title, author)
            )
            if cursor.fetchone():
                continue  # already exists, skip

        cursor.execute(
            "INSERT OR IGNORE INTO books (title, author, year) VALUES (?, ?, ?)",
            (title, author, year)
        )


def display_books(cursor):
    cursor.execute("SELECT * FROM books")
    all_books = cursor.fetchall()

    print("\n ======= Books in the DB =======")
    for book in all_books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")


def main():
    books_list = fetch_books()
    if not books_list:
        print("Didn't get any books back, nothing to insert.")
        return

    with sqlite3.connect('books.db') as conn:
        cursor = conn.cursor()
        create_table(cursor)
        save_books(cursor, books_list)
        conn.commit()
        print("Books inserted into the DB successfully.")
        display_books(cursor)


if __name__ == "__main__":
    main()