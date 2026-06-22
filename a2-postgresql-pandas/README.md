# A2 — PostgreSQL + pandas
 
Practises moving data between pandas and PostgreSQL using SQLAlchemy.
A small synthetic dataset is created directly in Python — no CSV, no download.
 
## What it does
 
- Creates a SQLAlchemy engine to connect to a local PostgreSQL database
- Builds a DataFrame from a Python dictionary
- Writes the DataFrame to PostgreSQL using `.to_sql()` with explicit column types via `dtype`
- Experiments with `if_exists` behaviour — `replace`, `append`, and `fail`
- Reads data back from PostgreSQL into a new DataFrame using `pd.read_sql()`
## What this practises
 
- SQLAlchemy `create_engine()` — why pandas needs an engine, not a raw psycopg2 connection
- `.to_sql()` — `if_exists`, `index=False`, `dtype` overrides
- `.read_sql()` — table name vs. full SQL query
- SQL quoting rules — single quotes for values, double quotes for identifiers
- Context managers — `with engine.connect() as connection:`
## How to run it
 
1. Create and activate a virtual environment:
```
   python3 -m venv .venv
   source .venv/bin/activate
```
2. Install dependencies:
```
   pip install -r requirements.txt
```
3. Create a PostgreSQL database, then create a `.env` file in this folder:
```
   DB_HOST=localhost
   DB_NAME=your_database_name
```
4. Run the script:
```
   python3 main.py
```