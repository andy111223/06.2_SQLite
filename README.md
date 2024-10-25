# SQLite Project and Task Manager

This project demonstrates how to use SQLite in Python to manage a simple database of projects and tasks. It creates a one-to-many relationship between the Project and Task tables and allows users to insert and retrieve data from the database.

## Features

Create a database and establish a connection using SQLite.
Create tables for Project and Task with foreign key relationships.
Insert sample data into both tables.
Retrieve and display all projects.

## Requirements

Python 3.x
SQLite (no additional installation needed as Python has built-in SQLite support)

## Setup Instructions

Clone the repository:

`git clone https://github.com/andy111223/06.2_SQLite.git`

`cd 06.2_SQLite`

Install necessary dependencies:

No external dependencies are required beyond Python's built-in libraries.

Run the script:

`python3 main.py`

The main script will create the my_database.db SQLite database if it doesn't exist, along with the required tables.

### Database schema: 

The project creates two tables:

1. Project: Stores project details.
2. Task: Stores tasks associated with a project, with a foreign key linking back to the Project table.

Insert and retrieve data:

Sample data is inserted into both the Project and Task tables.
The script prints out all projects after data insertion.

## Example Usage

Inserting data into the Project and Task tables is demonstrated within the script using SQL insert statements.
Use the context manager to ensure proper database connection management:

```
with manage_connection("my_database.db") as conn:
    insert_data(conn, sql_insert_project, project_data)
    select_all_projects(conn)```