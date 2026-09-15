# AI/ML Trainee Assessment

**Candidate:** Shourya Sharma
**Position:** AI/ML Trainee
**Assessment:** AccuKnox AI/ML Trainee Assessment

---

## Overview

This repository contains my solutions for the AccuKnox AI/ML Trainee Assessment. It covers practical implementation of Python, REST APIs, SQLite, CSV data processing, and data visualization (Problem Statement 1), along with written responses on LLM/AI/ML concepts, chatbot architecture, and vector databases (Problem Statement 2).

---

## Repository Structure

```
Accuknox Assignment/
├── README.md
├── requirements.txt
│
├── Problem Statement 1/
│   ├── q1_books.py
│   ├── mock_scores_api.py
│   ├── q2_scores.py
│   ├── q3_csv.py
│   ├── users_data.csv
│   └── PS1_Q4_Q5_Complex_Code.md
│
└── Problem Statement 2/
    ├── PS2_Q1_Self_Rating.md
    ├── PS2_Q2_Chatbot_Architecture.md
    └── PS2_Q3_Vector_Databases.md
```

---

## Problem Statement 1

### 1. API Data Retrieval and Storage (`q1_books.py`)

**Objective:** Fetch book data from an external REST API, store it in a local SQLite database, and display the stored records.

**API Used:** Open Library Search API (`https://openlibrary.org/search.json`) — free, public, no API key required. The following fields are extracted from each result: book title, author name, and first publication year.

**Database Schema — `books` table:**

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Primary key, auto-increment |
| `title` | TEXT | Book title |
| `author` | TEXT | Author name |
| `year` | INTEGER | First publication year |

**Approach:**
1. Send a GET request to the Open Library API with a search query.
2. Parse the JSON response and extract the list of book records (`docs` field).
3. Connect to the local SQLite database and create the `books` table if it doesn't already exist.
4. Loop through the first 10 fetched records, extracting title, author, and year for each.
5. Handle missing fields gracefully — if `author_name` or `first_publish_year` isn't present in a record, default to `"Unknown Author"` or `0` instead of letting the script crash.
6. Insert each record using a parameterized query (`?` placeholders) to prevent SQL injection.
7. Commit the transaction and read the records back with a `SELECT` query.
8. Display the retrieved records and close the database connection.

**Key Concepts:** Python, REST API, `requests`, JSON, SQLite, parameterized SQL queries, defensive error handling.

---

### 2. Data Processing and Visualization (`mock_scores_api.py` + `q2_scores.py`)

**Objective:** Fetch student test-score data from an API, calculate the average score, and visualize it with a bar chart.

**Assumption:** No public API exists for student test-score data. To genuinely satisfy the "fetch from an API" requirement — rather than hardcoding the data — a local REST API was built using Flask. `mock_scores_api.py` serves a list of student names and scores as JSON at the `/scores` endpoint. `q2_scores.py` fetches this using a real `requests.get()` HTTP call, exactly as it would with any live API.

**Approach:**
1. Start the local Flask server, which exposes student score data at `http://127.0.0.1:5000/scores`.
2. From the main script, send a GET request to this endpoint and parse the JSON response.
3. Extract each student's score into a list and calculate the average (`sum / count`).
4. Extract each student's name into a separate list, aligned by index with the scores.
5. Plot a bar chart using `matplotlib`, with student names on the x-axis and scores on the y-axis.
6. Draw a horizontal dashed line at the average score for quick visual reference, with a legend labeling it.

**Key Concepts:** Python, Flask (building a local REST API), `requests`, JSON, `matplotlib`, basic statistics.

---

### 3. CSV Data Import to a Database (`q3_csv.py`)

**Objective:** Read user information from a CSV file and insert it into a local SQLite database.

**Input Data:** `users_data.csv` contains two columns — `name` and `email`.

**Database Schema — `users` table:**

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Primary key, auto-increment |
| `name` | TEXT | User's name |
| `email` | TEXT | User's email address |

**Approach:**
1. Connect to the local SQLite database and create the `users` table if it doesn't already exist.
2. Open `users_data.csv` in read mode using a `with` block, so the file is automatically and safely closed after reading.
3. Use `csv.DictReader` to read each row as a dictionary, with the CSV headers (`name`, `email`) as keys.
4. Loop through each row and insert it into the `users` table using a parameterized query.
5. Commit the transaction, then read back and display all stored records.

**Key Concepts:** Python, `csv` module, `DictReader`, SQLite, safe file handling with `with`.

---

### 4 & 5. Complex Code Links

See `PS1_Q4_Q5_Complex_Code.md` for links and honest context on prior technical background.

## Problem Statement 2

Written responses to the conceptual questions (self-assessment, LLM chatbot architecture, and vector databases) are in the `Problem Statement 2/` folder, one file per question.

---

## How to Run

### 1. Clone the Repository
```
git clone <your-github-repository-url>
cd "Accuknox Assignment"
```

### 2. Create a Virtual Environment
```
python -m venv venv
```

**Windows:**
```
venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

**`requirements.txt`:**
```
requests
matplotlib
flask
```

### 4. Run the Programs

**API Data Retrieval and Storage:**
```
cd "Problem Statement 1"
python q1_books.py
```

**Data Processing and Visualization** (requires two terminals):

*Terminal 1 — start the mock API and leave it running:*
```
python mock_scores_api.py
```

*Terminal 2 — fetch the data and generate the chart:*
```
python q2_scores.py
```

**CSV Data Import to a Database:**
```
python q3_csv.py
```

---

## Assumptions

1. No public REST API exists for student test-score data, so a local Flask server was built to genuinely satisfy the "fetch from an API" requirement (see Question 2).
2. Some book records from the API do not include an author name or publication year; these fields default to `"Unknown Author"` and `0` respectively rather than causing the script to fail.
3. `books.db` and `users.db` are generated automatically when the respective scripts are run and are not included in this repository.

---

## Error Handling

The implementations account for common situations such as:
- Missing fields in the API response (e.g., missing author or publication year)
- Empty or malformed CSV rows
- Database connection and query errors

All database inserts use parameterized queries (`?` placeholders) to prevent SQL injection.

---

## Technologies Used

| Category | Technologies |
|---|---|
| Programming | Python |
| API | REST API, Requests, Flask |
| Database | SQLite |
| Visualization | Matplotlib |
| Version Control | Git, GitHub |

---

## Conclusion

This repository reflects my current, hands-on understanding of Python, REST APIs, SQLite, and data visualization — most of which was learned and applied directly while completing this assessment. Problem Statement 2 covers my research and reasoning on LLM-based chatbot architecture and vector databases.

Thank you for reviewing my submission.

**Shourya Sharma**
AI/ML Trainee Candidate
