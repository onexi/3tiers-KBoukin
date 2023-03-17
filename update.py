# Create the input html form to update colleges and students from the database based on the college_id and student_id

import sqlite3
from flask import Flask, render_template, request, redirect

# connect to db and get cursor
connection = sqlite3.connect("data/education.db", check_same_thread=False)
cursor = connection.cursor()

# web application
app = Flask(__name__)

@app.route('/updateform') #route to create the form to receive data from the browser and send it to the database
def updateform():
        return render_template('update.html')

@app.route('/update', methods=['POST']) #we want to be able to catch what the user inputs in the form through the submit button
def update():
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
        # update data in table
        cursor.execute(f"UPDATE colleges SET name = ?, students = ?, city = ?, region = ?, country = ? WHERE college_id = ?", (name, students, city, region, country, college_id))
        cursor.execute(f"UPDATE students SET firstname = ?, lastname = ?, birth_date = ?, email = ?, city_s = ?, region_s = ?, country_s = ?, college_id = ? WHERE student_id = ?", (firstname, lastname, birth_date, email, city_s, region_s, country_s, college_id, student_id))
        connection.commit()
        return redirect('/read', code=303) #redirect to the read page

#start server
if __name__ == '__main__':
        app.run(debug=True, port=5000)

# Path: update.html
#Create the input html form to update colleges and students from the database based on the college_id and student_id
