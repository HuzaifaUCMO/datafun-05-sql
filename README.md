# datafun-05-sql
Project 5: Python and SQL Integration
Overview
This project demonstrates the integration of Python and SQLite for database management, schema creation, and executing complex SQL queries. The project includes creating and managing a database, designing a schema with related tables, and performing various SQL operations such as filtering, joining, and aggregating data. Additionally, it incorporates logging to provide a record of program execution and aid in debugging.

Project Structure
db_initialize_yourname.py: Script to initialize the database, create tables, and populate them with initial data.
db_operations_yourname.py: Script to perform various SQL operations, including updates, deletions, and queries with aggregation and joins.
SQL Scripts:
create_tables.sql: Creates the database schema with related tables.
insert_records.sql: Inserts initial records into the tables.
update_records.sql: Updates specific records in the tables.
delete_records.sql: Deletes specific records from the tables.
query_aggregation.sql: Executes queries with aggregation functions like COUNT, AVG, SUM.
query_filter.sql: Performs queries with filters using WHERE clauses.
query_sorting.sql: Sorts query results using ORDER BY.
query_group_by.sql: Groups query results with the GROUP BY clause.
query_join.sql: Executes join operations between related tables.
Getting Started
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/datafun-05-sql.git
cd datafun-05-sql
Set Up the Virtual Environment:

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # For Windows: .\.venv\Scripts\activate
Install Dependencies:

bash
Copy code
pip install pandas pyarrow sqlite3
Initialize the Database: Run the db_initialize_huzaifanadeem.py script to create the database and populate it with initial data.

bash
Copy code
python db_initialize_huzaifanadeem.py
Perform SQL Operations: Execute the db_operations_huzaifanadeem.py script to perform additional SQL operations, including updates, deletions, and complex queries.

bash
Copy code
python db_operations_huzaifanadeem.py
Logging
All major events and exceptions are logged to log.txt to help trace program execution and debug any issues.

Documentation
Refer to the individual SQL files and Python scripts for detailed implementation and comments.