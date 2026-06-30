import requests
import psycopg2
import os
from dotenv import load_dotenv

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