import psycopg2

# connection string for the db, establishes a connection to the db
def create_connection():
    
    try:
        #enter your own credentials here.
        connection = psycopg2.connect( user="postgres", password="postgres",
            host="localhost",
            port="5432",
            database="StudentDB"
        )
        return connection
    except:
        print("Unable to connect to the database")
        return None

# Function that retrieves all students from the DB
def getAllStudents(connection):
    try:
        query= connection.cursor()

        # Executes select query from students table
        query.execute("SELECT * FROM students;")

        #Fetch all students from the table and loop through each student
        students = query.fetchall()
        for student in students:

            print(student)

    except:
        print("Error fetching student data.")

# Function that adds a new student to the database
def addStudent(connection, first_name, last_name, email, enrollment_date):
    try:
        query = connection.cursor()

        # Inserts a new student into the student table with student info parameters
        query.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                       (first_name, last_name, email, enrollment_date))
       
        connection.commit()

        print(f"Student {first_name} {last_name} has been successfully added to the database")
    except:
        print(f"Could not add {first_name} {last_name} to the database")

# Function to update the the email of a student
def updateStudentEmail(connection, student_id, new_email):
    try:
        query= connection.cursor()

        #Updates the student's email in the students table with the given id
        query.execute("UPDATE students SET email = %s WHERE student_id = %s;",
                       (new_email, student_id))
        
        connection.commit()

        #Get the name of the student with the given ID
        query.execute("SELECT first_name, last_name FROM students WHERE student_id = %s;", (student_id,))
        student = query.fetchone()
        
        #Get the first and last name of the student if the student is found in the DB
        if student:
            fName, lName = student
            fullName = fName + " " + lName

        print(f"Email for {fullName} has been successfully updated to {new_email} in the database")
    except:
        print(f"Could not update email for {fullName} in the database")

# Function that deletes a student from the database
def deleteStudent(connection, student_id):
    try:
        query = connection.cursor()

        query.execute("SELECT first_name, last_name FROM students WHERE student_id = %s;", (student_id,))
        student = query.fetchone()

        if student:
            fName, lName = student
            fullName = fName + " " + lName

        # Deletes student from the student table with the given ID
        query.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
        
        connection.commit()

        print(f"The student {fullName} has been successfully deleted from the database")
    except:
        print(f"Could not delete student {fullName} from the database")

# Interact with the db using above functions.
def main():
    # Connecting to the DB
    connection = create_connection()
    
    #if connection is None:
        #return

    #display all students before adding, updating and deleting
    print("Here are all the students in the database: ")
    getAllStudents(connection)
    print("\n")

    #CRUD operations
    addStudent(connection, "Amy", "Smith", "amy.smith@example.com", "2023-09-03")
    updateStudentEmail(connection, 2, "new.email@example.com")
    deleteStudent(connection, 3)
    
    #display all students after adding, updating and deleting
    print("\nHere are all the students in the database after adding, updating and deleting: ")
    getAllStudents(connection)

    #close the connection to the database
    connection.close()

# Call the main function
if __name__ == "__main__":
    main()