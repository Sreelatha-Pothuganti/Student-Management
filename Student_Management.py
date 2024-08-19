import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hareesh",
        database="hari"
    )
    return connection

def initialize_database():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT,
            grade VARCHAR(10)
        )
    ''')
    connection.commit()
    connection.close()

def add_student(name, age, grade):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)
    ''', (name, age, grade))
    connection.commit()
    connection.close()

def update_student(student_id, name, age, grade):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s
    ''', (name, age, grade, student_id))
    connection.commit()
    connection.close()

def get_all_students():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        SELECT * FROM students
    ''')
    students = cursor.fetchall()
    connection.close()
    return students

if __name__ == "__main__":
    initialize_database()

    while True:
        print("\nStudent Database Management")
        print("1. Add New Student")
        print("2. Update Student Information")
        print("3. Retrieve All Students")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            add_student(name, age, grade)
            print("Student added successfully!")

        elif choice == "2":
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter updated student name: ")
            age = int(input("Enter updated student age: "))
            grade = input("Enter updated student grade: ")
            update_student(student_id, name, age, grade)
            print("Student information updated successfully!")

        elif choice == "3":
            students = get_all_students()
            if not students:
                print("No students found in the database.")
            else:
                print("\nStudent Details:")
                for student in students:
                    print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
