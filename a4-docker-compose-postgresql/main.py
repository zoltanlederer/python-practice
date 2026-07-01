import requests
# import psycopg2
import os
# from dotenv import load_dotenv
from datetime import date, timedelta

# load_dotenv()

def get_connection():
    """Create and return a connection"""
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    name = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    return psycopg2.connect(host=host, port=port, dbname=name, user=user, password=password)

def setup_database():
    """Create the exchange_rates table if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            base CHAR(3) NOT NULL,
            target CHAR(3) NOT NULL,
            rate FLOAT NOT NULL,
            fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE (date, target)
        )                   
    """)
    conn.commit()
    cursor.close()
    conn.close()

def fetch_rates():
    today = date.today()
    seven_days_ago = today - timedelta(days=7)
    try:
        url = f'https://api.frankfurter.app/{seven_days_ago}..{today}?from=EUR&to=USD,HUF,AUD'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Connection failed: {e}')
        raise

print(fetch_rates())

# def transform_rates():
# def insert_rates():
# def main():

# if __name__ == "__main__":
#     main()