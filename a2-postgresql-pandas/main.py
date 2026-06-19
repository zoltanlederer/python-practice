from dotenv import load_dotenv
from sqlalchemy import create_engine
import os
import pandas as pd

load_dotenv()
host = os.getenv('DB_HOST')
dbname = os.getenv('DB_NAME')
engine = create_engine(f'postgresql+psycopg2://{host}/{dbname}')

print(engine)

data = {'title': ['Harry Potter', 'Dune', 'The Hobbit'], 'author': ['Rowling', 'Herbert', 'Tolkien']}
# Create DataFrame
df = pd.DataFrame(data=data)

print(df)

with engine.connect() as connection:
    print("Connected successfully")
    # Create a table
    df.to_sql(name='books', con=connection, if_exists='replace', index=False)