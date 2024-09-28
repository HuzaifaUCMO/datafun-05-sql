"""
This script performs various SQL operations on the SQLite database.
"""
import sqlite3
import logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', 
                    format='%(asctime)s - %(levelname)s - %(message)s')
def execute_sql_from_file(db_path, sql_file):
    with sqlite3.connect(db_path) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        logging.info(f"Executed SQL from {sql_file}")

def main():
    db_file_path = 'yourname_database.db'
    execute_sql_from_file(db_file_path, 'update_records.sql')
    execute_sql_from_file(db_file_path, 'delete_records.sql')
    execute_sql_from_file(db_file_path, 'query_aggregation.sql')
    execute_sql_from_file(db_file_path, 'query_filter.sql')
    execute_sql_from_file(db_file_path, 'query_sorting.sql')
    execute_sql_from_file(db_file_path, 'query_group_by.sql')
    execute_sql_from_file(db_file_path, 'query_join.sql')
    logging.info("All SQL operations completed successfully")

if __name__ == "__main__":
    main()
