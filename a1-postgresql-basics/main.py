import psycopg2 # pyright: ignore[reportMissingModuleSource]

conn = psycopg2.connect(
    host='localhost',
    dbname='postgresql_basics'
)

cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS books (id SERIAL PRIMARY KEY, title TEXT UNIQUE, author TEXT, year INTEGER, genre TEXT)')
conn.commit()


# data = (
#     {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'year': 1937, 'genre': 'Fantasy'},
#     {'title': '1984', 'author': 'George Orwell', 'year': 1949, 'genre': 'Dystopian'},
#     {'title': 'Dune', 'author': 'Frank Herbert', 'year': 1965, 'genre': 'Sci-Fi'},
#     {'title': 'The Pragmatic Programmer', 'author': 'David Thomas', 'year': 1999, 'genre': 'Technology'},
#     {'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'year': 2011, 'genre': 'Non-Fiction'}
# )

data = (
    ('The Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasy'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('Dune', 'Frank Herbert', 1965, 'Sci-Fi'),
    ('The Pragmatic Programmer', 'David Thomas', 1999, 'Technology'),
    ('Sapiens', 'Yuval Noah Harari', 2011, 'Non-Fiction')
)

cur.executemany('INSERT INTO books (title, author, year, genre) VALUES (%s, %s, %s, %s) ON CONFLICT (title) DO NOTHING', data)
conn.commit()
cur.execute('SELECT * FROM books')
rows = cur.fetchall()
print(rows)