from dotenv import load_dotenv
from sqlalchemy import create_engine, String, Integer
import os
import pandas as pd

load_dotenv()
host = os.getenv('DB_HOST')
dbname = os.getenv('DB_NAME')
engine = create_engine(f'postgresql+psycopg2://{host}/{dbname}')

print(engine)

data = {
    'title': ['Harry Potter', 'Dune', 'The Hobbit'],
    'author': ['Rowling', 'Herbert', 'Tolkien'],
    'year': [2001, 1998, 1954]
}
# Create DataFrame
df = pd.DataFrame(data=data)

print(df)

with engine.connect() as connection:
    print("Connected successfully")
    # Create a table
    df.to_sql(
        name='books',
        con=connection,
        if_exists='replace',
        index=False,
        dtype={'title': String(100), 'author': String(100), 'year': Integer}
    )
    print('=>', df)

    # new_df = pd.read_sql('books', connection)
    # new_df = pd.read_sql('SELECT * FROM books', connection)
    new_df = pd.read_sql("SELECT author FROM books WHERE title = 'Dune'", connection)
    print('===>', new_df)