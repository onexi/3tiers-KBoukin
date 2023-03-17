#Create the server and route to receive data from the browser and send it to the database
# imports
from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

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
        college_id = int(education['college_id'])
        name = education['name']
        students = int(education['students'])
        city = education['city']
        region = education['region']
        country = education['country']
        #for Students
        student_id = int(education['student_id'])
        print(student_id) #print to check
        firstname = education['firstname']
        lastname = education['lastname']
        #cast string to date
        birth_date = datetime.strptime(education['birth_date'], '%Y-%m-%d')
        print(birth_date) #print to check
        email = education['email']
        city_s = education['city_s']
        region_s = education['region_s']
        country_s = education['country_s']
        college_id = int(education['college_id'])
        # insert data into table
        cursor.execute(f"INSERT INTO colleges VALUES (?, ?, ?, ?, ?, ?)", (college_id, name, students, city, region, country))
        cursor.execute(f"INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (student_id, firstname, lastname, birth_date, email, city_s, region_s, country_s, college_id))
        print(cursor.execute(f"INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (student_id, firstname, lastname, birth_date, email, city_s, region_s, country_s, college_id))) #print to check
        connection.commit() #save changes
        return redirect('/read') #redirect to the read page
#start server
if __name__ == '__main__':
        app.run(debug=True, port=5000)

# Path: read.py