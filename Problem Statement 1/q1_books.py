import requests
import sqlite3

response = requests.get("https://openlibrary.org/search.json?q=python+programming")


data = response.json()
books_list = data['docs']



conn = sqlite3.connect('books.db')
cursor = conn.cursor()



cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author TEXT,
                    year INTEGER
                )
''')


for book in books_list[:10]:
    title = book.get("title", "Unknown Title")

    if "author_name" in book:
        author = book["author_name"][0]
    else:
        author = "Unknown Author"

    year = book.get("first_publish_year", 0)

    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year) )



conn.commit()



print("Books inserted into the DB successfully.")

cursor.execute("SELECT * FROM books") 
all_books = cursor.fetchall()


print("\n ======= Books in the DB =======")


for book in all_books:
    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")



conn.close()