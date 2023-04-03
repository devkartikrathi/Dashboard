from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from database import *

app = Flask(__name__)
CORS(app)

@app.route('/') # type: ignore
def INDEX_1():
    return render_template('index.html')

@app.route('/register', methods = ['POST']) # type: ignore
def register():
    username = request.form['username']
    password = request.form['password']
    remember = request.form.get('remember', False)

    min_user_len = 5
    username_req = [
        lambda s: any(x.isupper() for x in s), 
        lambda s: any(x.islower() for x in s),
        lambda s: any(x.isdigit() for x in s) 
    ]

    if len(username) < min_user_len or not all(req(username) for req in username_req):
        error_mess = 'Invalid username! Username must be 5-15 characters, a-z, A-Z and 0-9!'

    minpasslen = 5

    if len(password) < minpasslen:
        error_msg = 'Password must be between 5-15 characters!'

@app.route('/login', methods = ['GET', 'POST']) # type: ignore
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = request.form.get('remember', False)

    if request.method == 'GET':
        return jsonify(course_data())

@app.route('/data', methods=['GET'])
def GET_DATA():
    data = get_data()
    return jsonify(data)

@app.route('/data', methods=['POST'])
def ADD_DATA():
    data = request.get_json()
    name = data['name']
    age = data['age']
    add_data(name, age)
    return "Data added successfully"

if __name__ == '__main__':
    app.run(debug=True)
