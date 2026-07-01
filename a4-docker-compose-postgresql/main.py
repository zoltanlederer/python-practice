import requests
import psycopg2
import os
import time
from dotenv import load_dotenv
from datetime import date, timedelta, datetime

load_dotenv()

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
    """Get 7 days of exchange rates"""
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

def transform_rates(data):
    """Convert API response into list of tuples"""
    formatted = []
    for date, rates in data['rates'].items():
        for currency, rate in rates.items():
            formatted.append((date, 'EUR', currency, rate, datetime.now()))

    return formatted

def insert_rates(data):
    """Takes a list of tuples and writes them into PostgreSQL"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        for item in data:
            cursor.execute("""
                INSERT INTO exchange_rates (date, base, target, rate, fetched_at)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (date, target) DO NOTHING
            """, item)

        conn.commit()
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        print(f'Database error: {e}')
        raise

def main():
    count = 0
    while count < 10:
        try:
            get_connection()
            setup_database()
            data = fetch_rates()
            transform = transform_rates(data)
            insert_rates(transform)
            break
        except psycopg2.OperationalError:
            print(f'There was an error during the connection. Trying to connect again. Please wait.')
            count += 1
            time.sleep(2)
    else:
        print("Sorry couldn't connect. Please try to connect later.")
        
if __name__ == "__main__":
    main()