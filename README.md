# AI/ML Trainee Assessment

**Candidate:** Shourya Sharma
**Position:** AI/ML Trainee
**Assessment:** AccuKnox AI/ML Trainee Assessment

---

## Overview

This repo has my solutions for the AccuKnox AI/ML Trainee Assessment — Python, REST APIs, SQLite, CSV handling, and data visualization for Problem Statement 1, plus written answers on LLM/AI/ML concepts, chatbot architecture, and vector databases for Problem Statement 2.

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

## Quick Start

### 1. Clone and enter the repo
```
git clone <this-repository-url>
cd "Accuknox Assignment"
```

### 2. (Optional) Create a virtual environment
```
python -m venv venv
venv\Scripts\activate
```
*(macOS/Linux: `source venv/bin/activate`)*

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Move into the Problem Statement 1 folder
```
cd "Problem Statement 1"
```
All three scripts below assume you're running them from inside this folder, since `q3_csv.py` reads `users_data.csv` using a relative path.

### 5. Run Question 1
```
python q1_books.py
```

### 6. Run Question 2 (needs two terminals)

**Terminal 1** — start the mock API and leave it running:
```
python mock_scores_api.py
```

**Terminal 2** — fetch the data and generate the chart:
```
python q2_scores.py
```
A bar chart window will pop up with the average marked. Close it to end the script.

### 7. Run Question 3
```
python q3_csv.py
```

### 8. Questions 4 & 5
Written response, no code to run — see `PS1_Q4_Q5_Complex_Code.md`.

### 9. Problem Statement 2
Written answers, no code to run — see the `Problem Statement 2/` folder, one file per question.

---

## Assignment 1

### 1. API Data Retrieval and Storage

**Objective:** Fetch book data from an external REST API, store the required data in a local SQLite database, and display the stored records.

**API Used:** Open Library Search API — `https://openlibrary.org/search.json`, free and public, no key needed.

The following fields are extracted from each result:
- Book title
- Author
- First publication year

**Database Schema:**

The SQLite database contains a `books` table with the following columns:

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Primary key, auto-increment |
| `title` | TEXT | Book title |
| `author` | TEXT | Author name |
| `year` | INTEGER | First publication year |

**Approach:**
1. Connect to the SQLite database.
2. Create the `books` table if it doesn't already exist.
3. Send a GET request to the Open Library API.
4. Parse the JSON response and pull out the list of book records.
5. Handle records where the author name or publication year is missing (defaults to `"Unknown Author"` / `0` instead of crashing).
6. Insert the records into SQLite using parameterized queries.
7. Commit the transaction.
8. Retrieve and display the stored records.
9. Close the database connection.

**Key Concepts:** Python, REST API, `requests`, JSON, SQLite, parameterized SQL queries, error handling.

---

### 2. Data Processing and Visualization

**Objective:** Fetch student test-score data from an API, calculate the average score, and visualize the results using a bar chart.

**Assumption:** No public API exists for student test-score data, so hardcoding it directly wouldn't really satisfy "fetch from an API." Instead, I built a small local API with Flask (`mock_scores_api.py`) that serves the score data at a `/scores` endpoint, and fetched it with a genuine `requests.get()` call in `q2_scores.py` — the same way I'd fetch from any real API.

**Approach:**
1. Start the local Flask server, which exposes score data at `http://127.0.0.1:5000/scores`.
2. Send a GET request to this endpoint from the main script and parse the JSON response.
3. Extract each student's score into a list.
4. Calculate the average score.
5. Extract each student's name into a separate, aligned list.
6. Generate a bar chart using `matplotlib`.
7. Draw a horizontal line marking the average score, with a legend.

**Key Concepts:** Python, Flask, `requests`, JSON, `matplotlib`, basic statistics.

---

### 3. CSV Data Import to a Database

**Objective:** Read user information from a CSV file and insert the records into a local SQLite database.

**Input Data:**

The CSV file (`users_data.csv`) contains:
- Name
- Email

**Database Schema:**

The SQLite database contains a `users` table:

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Primary key, auto-increment |
| `name` | TEXT | User's name |
| `email` | TEXT | User's email address |

**Approach:**
1. Connect to the SQLite database.
2. Create the `users` table if it doesn't already exist.
3. Open the CSV file using a `with` block, so it closes automatically once reading is done.
4. Read each row using `csv.DictReader`, keyed by the CSV headers (`name`, `email`).
5. Insert each row into SQLite using a parameterized query.
6. Commit the transaction.
7. Retrieve and display the stored records.

**Key Concepts:** Python, `csv` module, `DictReader`, SQLite, safe file handling with `with`.

---

### 4 & 5. Complex Code Links

See `PS1_Q4_Q5_Complex_Code.md` for links and honest context on prior technical background.

## Assignment 2

Written responses to the conceptual questions (self-assessment, LLM chatbot architecture, and vector databases) are in the `Problem Statement 2/` folder, one file per question.

---

## Assumptions

1. No public REST API exists for student test-score data, so a local Flask server was built to genuinely satisfy the "fetch from an API" requirement (see Question 2).
2. Some book records from the API don't include an author name or publication year; these default to `"Unknown Author"` and `0` rather than crashing the script.
3. `books.db` and `users.db` are generated automatically when the respective scripts run and aren't included in this repo.

---

## Error Handling

The implementations account for common situations such as:
- Missing fields in the API response (missing author or publication year)
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

This repo reflects where I'm actually at right now with Python, REST APIs, SQLite, and data visualization — most of it learned and applied directly while working through this assessment. Problem Statement 2 has my reasoning on LLM-based chatbot architecture and vector databases.

Thanks for reviewing my submission.

**Shourya Sharma**
AI/ML Trainee Candidate