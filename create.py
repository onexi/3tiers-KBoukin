#Create the server and route to receive data from the browser and send it to the database
# imports
from flask import Flask, render_template, request, redirect
import sqlite3

# connect to db and get cursor
connection = sqlite3.connect("data/education.db", check_same_thread=False)
cursor = connection.cursor()

# web application
app = Flask(__name__)

@app.route('/createform') #route to create the form to receive data from the browser and send it to the database
def add():
        return render_template('create.html')
#we want to be able to catch what the user inputs in the form through the submit button
@app.route('/create', methods=['POST']) #we want to be able to catch what the user inputs in the form through the submit button
def create():
        # get data from form Colleges and Students
        education = request.form
        #for Colleges 
        college_id = education['college_id'] 
        name = education['name']
        students = education['students']
        city = education['city']
        region = education['region']
        country = education['country']
        #for Students
        student_id = education['student_id']
        firstname = education['firstname']
        lastname = education['lastname']
        birth_date = education['birth_date']
        email = education['email']
        city_s = education['city_s']
        region_s = education['region_s']
        country_s = education['country_s']
        college_id = education['college_id']
        # insert data into table
        cursor.execute(f"INSERT INTO colleges VALUES (?, ?, ?, ?, ?, ?)", (college_id, name, students, city, region, country))
        cursor.execute(f"INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (student_id, firstname, lastname, birth_date, email, city_s, region_s, country_s, college_id))
        connection.commit()
        return redirect('/read')
#start server
if __name__ == '__main__':
        app.run(debug=True, port=5000)

# Path: read.py