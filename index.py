#combining all the tiers together, to run the program index.py

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

#call all the functions from the other files to run the program on rendered index.html
@app.route('/', methods=["GET", "POST"])
def post_redirect_get():
        if request.method == "GET":
                return render_template('index.html')
        else: #request.method == "POST" redirect to the read / delete / update / create pages
                if request.form['submit'] == 'read':
                        return redirect('/read', code=303)
                elif request.form['submit'] == 'delete':
                        return redirect('/deleteform', code=303)
                elif request.form['submit'] == 'update':
                        return redirect('/updateform', code=303)
                elif request.form['submit'] == 'create':
                        return redirect('/createform', code=303)


if __name__ == '__main__':
        app.run(debug=True, port=5000)

# Path: index.html
# #combining all the tiers together, to run the program index.py

