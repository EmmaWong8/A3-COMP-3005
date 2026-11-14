
import psycopg2
from getpass import getpass

# PostgreSQL connection settings
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "a3_db"
DB_USER = "postgres"

connection = None
cursor = None

def get_connection(password):
    """ Connect to PostgreSQL database and return connection object """
    global connection
    global cursor

    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=password,
    )

    # Object to interact with the database
    cursor = connection.cursor()

def getAllStudents():
    """ Retrieves and displays all records from the students table. """
    cursor.execute("SELECT * FROM students ORDER BY student_id;")

    students = cursor.fetchall()
    for student in students:
        print(student)

def addStudent(first_name, last_name, email, enrollment_date):
    """ Inserts a new student record into the students table. """
    query = """ 
                INSERT INTO students 
                (first_name, last_name, email, enrollment_date) 
                VALUES (%s, %s, %s, %s); 
            """

    cursor.execute(query,
            (first_name, last_name, email, enrollment_date))

    print("Student added successfully.")

def updateStudentEmail(student_id, new_email):
    """ Updates the email address for a student with the specified student_id. """
    query = """ 
                UPDATE students
                SET email = %s
                WHERE student_id = %s; 
            """

    cursor.execute(query, (new_email, student_id))

    if cursor.rowcount == 0:
        print("Student not found.")
    else:
        print("Student email updated successfully.")

def deleteStudent(student_id):
    """ Deletes the record of the student with the specified student_id. """
    query = """ 
                DELETE FROM students
                WHERE student_id = %s; 
            """

    cursor.execute(query, (student_id,))

    if cursor.rowcount == 0:
        print("Student not found.")
    else:
        print("Student deleted successfully.")

def main():
    """ Run application menu for student database management. """
    
    print("***********************************************************")
    print("     Welcome to the Student Database Management System     ")
    print("***********************************************************")

    # Verify database connection 
    try:
        password = getpass("Please enter your PostgreSQL password: ")
        get_connection(password)
        print("Successfully connected to PostgreSQL!")
    except psycopg2.Error as error:
        print(f"Database connection failed: {error}")
        return

    while True:
        print("-------------------------------")
        print("     Student Database Menu     ")
        print("-------------------------------")
        print("|  1. View all students       |")
        print("|  2. Add a student           |") 
        print("|  3. Update student email    |")
        print("|  4. Delete a student        |")
        print("|  5. Exit.                   |")
        print("-------------------------------")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                getAllStudents()

            elif choice == "2":
                first_name = input("First name: ")
                last_name = input("Last name: ")
                email = input("Email: ")
                date = input("Enrollment date (YYYY-MM-DD): ")

                addStudent(first_name, last_name, email, date)

            elif choice == "3":
                student_id = int(input("Student ID: "))
                new_email = input("New email: ")

                updateStudentEmail(student_id, new_email)

            elif choice == "4":
                student_id = int(input("Student ID: "))
                deleteStudent(student_id)

            elif choice == "5":
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Try again.")

        except (ValueError, psycopg2.Error) as error:
            print(f"Operation failed: {error}")

    connection.commit()  # Commit any changes made during the session
    connection.close()
    print("Database connection closed.")


if __name__ == "__main__":
    main()