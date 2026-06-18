# A1 — PostgreSQL from scratch

A simple Python script that manages a list of books. No ETL pipeline, no scheduling, no pandas — just raw psycopg2 against a real PostgreSQL database.

## What it does

1. Connects to the `postgresql_basics` database
2. Creates a `books` table (if it doesn't already exist) with columns: `id`, `title`, `author`, `year`, `genre`
3. Inserts sample books, skipping duplicates with `ON CONFLICT DO NOTHING`
4. Queries all books and prints them
5. Queries books filtered by genre
6. Closes the cursor and connection

## What this practises

- psycopg2 — `conn` vs `cur`, `conn.commit()`
- `SERIAL PRIMARY KEY`, `TEXT UNIQUE`
- Parameterized queries — `%s` and `%(key)s` named placeholders
- Avoiding duplicate inserts with `ON CONFLICT`
- `WHERE` filtering with parameters