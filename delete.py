#Create the input html form to delete colleges and students from the database based on the college_id and student_id

import sqlite3
from flask import Flask, render_template, request, redirect

# connect to db and get cursor
connection = sqlite3.connect("data/education.db", check_same_thread=False)
cursor = connection.cursor()

# web application
app = Flask(__name__)

@app.route('/deleteform') #route to create the form to receive data from the browser and send it to the database
def delete():
        return render_template('delete.html')

@app.route('/delete', methods=['POST']) #we want to be able to catch what the user inputs in the form through the submit button
def delete():
        # get data from form Colleges and Students
        education = request.form
        #for Colleges 
        college_id = education['college_id'] 
        #for Students
        student_id = education['student_id']
        # delete data from table
        cursor.execute(f"DELETE FROM colleges WHERE college_id = ?", (college_id))
        cursor.execute(f"DELETE FROM students WHERE student_id = ?", (student_id))
        connection.commit()
        return redirect('/read')

#start server
if __name__ == '__main__':
        app.run(debug=True, port=5000)

# Path: delete.html
#Create the input html form to delete colleges and students from the database based on the college_id and student_id