from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

#cnx = mysql.connector.connect(user='<username>', password='<password>',  database='<database_name>')

@app.route('/', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():

    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Insert the data into the MySQL database
    # cursor = cnx.cursor()
    # insert_query = "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)"
    # data = (name, email, message)
    # cursor.execute(insert_query, data)
    # cnx.commit()
    # cursor.close()

    return redirect('/')

if __name__ == '__main__':
    app.run()