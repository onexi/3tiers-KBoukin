#Read the data in the “colleges” and “students” table. Write the “read” server route
import sqlite3
from flask import Flask, render_template, request, redirect

# connect to db and get cursor
connection = sqlite3.connect("data/education.db", check_same_thread=False)
cursor = connection.cursor()

# web application
app = Flask(__name__)

@app.route('/read') #route to read the data in the “colleges” and “students” table
def read():
        # get data from table
        cursor.execute("SELECT * FROM colleges")
        colleges = cursor.fetchall()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        # render template
        return render_template('read.html', colleges=colleges, students=students)

#start server
if __name__ == '__main__':
        app.run(debug=True, port=5000)

# Path: read.html
#Read the data in the “colleges” and “students” table. Write the “read” server route
