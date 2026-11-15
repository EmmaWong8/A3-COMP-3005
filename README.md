# COMP 3005 - Assignment 3 Question 1
# Student Database System and Application
# Author: Emma Wong (101297761)

## Description
This application connects to a PostgreSQL database and performs CRUD (Create, Read, Update, Delete) operations on a `students` table using Python and the `psycopg2` library.

The application provides a command-line menu that allows users to:
1. **View all students**: Retrieve and display all student records.
2. **Add a student**: Insert a new student record.
3. **Update student email**: Modify an existing student's email address.
4. **Delete a student**: Remove a student record by student ID.
5. **Exit**: Close the database connection and terminate the application.

## Prerequisites
Ensure the following are installed:
- Python 3
- PostgreSQL
- pgAdmin 4 
- pip 

## Setup Instructions

### 1. Clone the Repository

Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/EmmaWong8/A3-COMP-3005
```

### 2. Install Dependencies
Install the required Python library using:

```bash
python3 -m pip install -r requirements.txt
```

### 3. Set Up the PostgreSQL Database
1. Open pgAdmin 4 and connect to your PostgreSQL server.
2. Create a new database named `a3_db`.
3. Open the Query Tool for `a3_db`.
4. Execute the provided `a3_db.sql` script to create the `students` table and insert the three initial student records.

The table should initially contain John Doe, Jane Smith, and Jim Beam.x

## Running the Application
Run the application from the project directory:

```bash
python3 app.py
```

If your system uses `python` instead of `python3`, use:

```bash
python app.py
```

After entering your PostgreSQL password, the application will connect to the database and display the following menu:

```text
-------------------------------
     Student Database Menu
-------------------------------
|  1. View all students       |
|  2. Add a student           |
|  3. Update student email    |
|  4. Delete a student        |
|  5. Exit.                   |
-------------------------------
```

Enter a number from 1 to 5 to perform the corresponding operation.

For adding students, enter the enrollment date in `YYYY-MM-DD` format.

## Demonstration Video

