"""
This script initializes the SQLite database and populates it with the initial schema and data.
"""
import sqlite3
import logging
import pathlib
from pathlib import Path
import pandas as pd

logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', 
                    format='%(asctime)s - %(levelname)s - %(message)s')
def create_database(db_path):
    """Create a new SQLite database."""
    conn = sqlite3.connect(db_path)
    logging.info(f"Database created at {db_path}")
    conn.close()

def execute_sql_from_file(db_path, sql_file):
    """Execute SQL commands from a given file."""
    with sqlite3.connect(db_path) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        logging.info(f"Executed SQL from {sql_file}")

def main():
    db_file_path = 'yourname_database.db'
    create_database(db_file_path)
    execute_sql_from_file(db_file_path, 'create_tables.sql')
    execute_sql_from_file(db_file_path, 'insert_records.sql')
    logging.info("Database initialization completed")

if __name__ == "__main__":
    main()

