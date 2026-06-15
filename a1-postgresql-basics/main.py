import psycopg2 # pyright: ignore[reportMissingModuleSource]

conn = psycopg2.connect(
    host='localhost',
    dbname='postgresql_basics'
)

cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS books (id SERIAL PRIMARY KEY, title TEXT, author TEXT, year INTEGER, genre TEXT)')
conn.commit()
cur.execute('SELECT * FROM books;')
rows = cur.fetchall()
print(rows)