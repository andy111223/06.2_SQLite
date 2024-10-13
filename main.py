import sqlite3
from sqlite3 import Error
from contextlib import contextmanager

# Step 1: Create a connection to the database
def create_connection(db_file):
    """create a database connection to an SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, SQLite version: {sqlite3.sqlite_version}")
        return conn
    except Error as e:
        print(e)
        return None

# Function to create tables
def create_table(conn, create_table_sql):
    """create a table using the provided SQL statement"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Table created successfully")
    except Error as e:
        print(e)

# Function to insert data into a table
def insert_data(conn, sql, data):
    """Insert data into table"""
    try:
        c = conn.cursor()
        c.execute(sql, data)
        conn.commit()
        print("Data inserted successfully")
    except Error as e:
        print(e)

# Function to select and display all rows in the Project table
def select_all_projects(conn):
    """Query all rows in the Project table"""
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM Project")
        rows = c.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)

# Context manager for database connection
@contextmanager
def manage_connection(db_file):
    """Context manager for SQLite connection"""
    conn = sqlite3.connect(db_file)
    try:
        yield conn
    finally:
        conn.close()
        print(f"Connection to {db_file} closed")

# SQL statements to create tables
sql_create_project_table = """
CREATE TABLE IF NOT EXISTS Project (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    start_date DATE,
    end_date DATE
);
"""

sql_create_task_table = """
CREATE TABLE IF NOT EXISTS Task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    status TEXT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (project_id) REFERENCES Project(id)
);
"""

# SQL statements to insert data
sql_insert_project = """
INSERT INTO Project (name, start_date, end_date)
VALUES (?, ?, ?);
"""

sql_insert_task = """
INSERT INTO Task (project_id, name, description, status, start_date, end_date)
VALUES (?, ?, ?, ?, ?, ?);
"""

# Sample data to insert
project_data = ('New Project', '2024-10-01', '2024-12-31')
task_data = (1, 'First Task', 'Description of the first task', 'In Progress', '2024-10-02', '2024-10-15')

# Usage example with context manager
with manage_connection("my_database.db") as conn:
    # Create tables
    create_table(conn, sql_create_project_table)
    create_table(conn, sql_create_task_table)

    # Insert sample data
    insert_data(conn, sql_insert_project, project_data)
    insert_data(conn, sql_insert_task, task_data)

    # Query and print all projects
    select_all_projects(conn)