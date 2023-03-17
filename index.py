#combining all the tiers together, to run the program index.py

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

#call all the functions from the other files to run the program on rendered index.html
@app.route('/')
def index():
        return render_template('index.html')

if __name__ == '__main__':
        app.run(debug=True, port=5000)

# Path: index.html
# #combining all the tiers together, to run the program index.py

