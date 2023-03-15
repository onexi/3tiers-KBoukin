import sqlite3

#connect to database education.db
conn = sqlite3.connect('data/education.db')

#create a cursor
c = conn.cursor()

#create input for table students
studentID = input("Enter student ID: ")
collegeID = input("Enter college ID: ")
firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
birthDate = input("Enter birth date: ")
email = input("Enter email: ")
city = input("Enter city: ")
region = input("Enter region: ")
country = input("Enter country: ")

#create input for table colleges
collegeID = input("Enter college ID: ")
name = input("Enter college name: ")
students = input("Enter number of students: ")
city = input("Enter city: ")
region = input("Enter region: ")
country = input("Enter country: ")

#writing to table students
c.execute("INSERT INTO students VALUES (:studentID, :collegeID, :firstName, :lastName, :birthDate, :email, :city, :region, :country)",
        { 'studentID': studentID, 'collegeID': collegeID, 'firstName': firstName, 'lastName': lastName, 'birthDate': birthDate, 'email': email, 'city': city, 'region': region, 'country': country})

#writing to table colleges
c.execute("INSERT INTO colleges VALUES (:collegeID, :name, :students, :city, :region, :country)",
        { 'collegeID': collegeID, 'name': name, 'students': students, 'city': city, 'region': region, 'country': country})

#commit changes
conn.commit()

#verify changes
c.execute("SELECT * FROM students")
print(c.fetchall())

c.execute("SELECT * FROM colleges")
print(c.fetchall())

#close connection
cursor.close()
conn.close()