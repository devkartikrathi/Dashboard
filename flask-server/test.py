from flask import Flask, jsonify, request, render_template, redirect, url_for, make_response
import jwt
import datetime
from functools import wraps
from database import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'

# Decorator for authentication
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = users.find_one({'_id': data['id']})
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

# Authenticate user route
@app.route('/auth', methods=['POST'])
def auth():
    username = request.form['username']
    password = request.form['password']

    user = check_user(username=username, password=password)

    if not user:
        return jsonify({'message': 'Invalid username or password!'})

    token_ = jwt.encode({'username': 'admin', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

    # return jsonify({'token': token})
    resp = make_response(redirect(url_for('admin_dashboard')))
    resp.headers['x-access-token'] = token_
    return resp
    # return redirect(url_for('admin'), headers={'x-access-token': token})

# Admin dashboard route
@app.route('/admin', methods=['GET', 'POST'])
@token_required
def admin_dashboard(current_user):
    if current_user['role'] != 'admin':
        return jsonify({'message': 'You do not have access to this page!'})

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        teacher_id = request.form['teacher_id']

        course = {'name': name, 'description': description, 'teacher_id': teacher_id}
        courses.insert_one(course)

    courses_list = list(courses.find())

    return render_template('admin.html', courses=courses_list)

# Teacher dashboard route
@app.route('/teacher', methods=['GET'])
@token_required
def teacher_dashboard(current_user):
    if current_user['role'] != 'teacher':
        return jsonify({'message': 'You do not have access to this page!'})

    courses_list = list(courses.find({'teacher_id': str(current_user['_id'])}))

    return render_template('teacher.html', courses=courses_list)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
