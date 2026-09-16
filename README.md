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
A bar chart window will pop up with the average marked, and a copy is saved as `scores_chart.png` in the same folder. Close the window to end the script.

If `mock_scores_api.py` isn't running yet, `q2_scores.py` will print a clear message telling you to start it, instead of crashing.

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
2. Create the `books` table if it doesn't already exist, with a `UNIQUE(title, author, year)` constraint so re-running the script doesn't create duplicate rows.
3. Send a GET request to the Open Library API, with a timeout and a check for a failed response.
4. Parse the JSON response and pull out the list of book records.
5. Handle records where the author name or publication year is missing (defaults to `"Unknown Author"`, and `NULL` instead of a misleading `0` for the year).
6. Insert the records into SQLite using `INSERT OR IGNORE` with parameterized queries, so duplicates are skipped rather than doubling up on repeat runs.
7. Commit the transaction.
8. Retrieve and display the stored records.

**Key Concepts:** Python, REST API, `requests`, JSON, SQLite, parameterized SQL queries, error handling, idempotent inserts.

---

### 2. Data Processing and Visualization

**Objective:** Fetch student test-score data from an API, calculate the average score, and visualize the results using a bar chart.

**Assumption:** No public API exists for student test-score data, so hardcoding it directly wouldn't really satisfy "fetch from an API." Instead, I built a small local API with Flask (`mock_scores_api.py`) that serves the score data at a `/scores` endpoint, and fetched it with a genuine `requests.get()` call in `q2_scores.py` — the same way I'd fetch from any real API.

**Approach:**
1. Start the local Flask server, which exposes score data at `http://127.0.0.1:5000/scores` (and a `/health` endpoint for a quick check).
2. Send a GET request to this endpoint from the main script, with a timeout and a friendly message if the server isn't running.
3. If data comes back, extract names and scores from it.
4. Calculate the average score (with a guard against dividing by zero if the list is empty).
5. Generate a bar chart using `matplotlib`.
6. Draw a horizontal line marking the average score, with a legend.
7. Save the chart as `scores_chart.png` and display it.

**Key Concepts:** Python, Flask, `requests`, JSON, `matplotlib`, basic statistics, error handling.

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
2. Create the `users` table if it doesn't already exist, with `email` marked `UNIQUE` so the same user can't be inserted twice.
3. Open the CSV file with explicit UTF-8 encoding, using a `with` block so it closes automatically once reading is done.
4. Read each row using `csv.DictReader`, keyed by the CSV headers (`name`, `email`), skipping any row with a blank name or email.
5. Insert each valid row into SQLite using `INSERT OR IGNORE` with a parameterized query, so re-running the script doesn't create duplicates.
6. Commit the transaction.
7. Retrieve and display the stored records.

**Key Concepts:** Python, `csv` module, `DictReader`, SQLite, safe file handling with `with`, idempotent inserts, input validation.

---

### 4 & 5. Complex Code Links

See `PS1_Q4_Q5_Complex_Code.md` for links and honest context on prior technical background.

## Assignment 2

Written responses to the conceptual questions (self-assessment, LLM chatbot architecture, and vector databases) are in the `Problem Statement 2/` folder, one file per question.

---

## Assumptions

1. No public REST API exists for student test-score data, so a local Flask server was built to genuinely satisfy the "fetch from an API" requirement (see Question 2).
2. Some book records from the API don't include an author name or publication year; these default to `"Unknown Author"` and `NULL` rather than crashing the script or storing a misleading `0`.
3. `books.db`, `users.db`, and `scores_chart.png` are generated automatically when the respective scripts run and aren't included in this repo.

---

## Error Handling

The scripts are written to fail gracefully rather than crash with a raw traceback:
- API requests use a timeout and check the response status; connection failures print a clear message instead of a stack trace
- Missing fields in API responses (author, publication year) fall back to sensible defaults instead of raising errors
- Blank or incomplete CSV rows are skipped rather than inserted
- An empty score list is handled without attempting to divide by zero or plot an empty chart
- Re-running Q1 or Q3 won't create duplicate rows, thanks to `UNIQUE` constraints and `INSERT OR IGNORE`

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