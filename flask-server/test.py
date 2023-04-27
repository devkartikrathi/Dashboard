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
            token = request.headers.get('x-access-token')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            #data = jwt.decode(token, app.config['SECRET_KEY'])
            # current_user = users.find_one({'role': data['username']})
            current_user = {'role' : 'admin'}
            print('done')
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

    return jsonify({'token': token_})
    # resp = make_response(redirect(url_for('admin_dashboard')))
    # resp.headers['x-access-token'] = token_
    # return resp
    # return redirect(url_for('admin'), headers={'x-access-token': token})

# Admin dashboard route
# @app.route('/admin', methods=['GET', 'POST'])
# @token_required
# def admin_dashboard(current_user):
#     if current_user['role'] != 'admin':
#         return jsonify({'message': 'You do not have access to this page!'})

#     if request.method == 'POST':
#         name = request.form['name']
#         description = request.form['description']
#         teacher_id = request.form['teacher_id']

#         course = {'name': name, 'description': description, 'teacher_id': teacher_id}
#         #courses.insert_one(course)

#     courses_list = [1, 2, 3]

#     return render_template('admin.html', courses=courses_list)

# Teacher dashboard route
# @app.route('/teacher', methods=['GET'])
# @token_required
# def teacher_dashboard(current_user):
#     if current_user['role'] != 'teacher':
#         return jsonify({'message': 'You do not have access to this page!'})

#     courses_list = list(courses.find({'teacher_id': str(current_user['_id'])}))

#     return render_template('teacher.html', courses=courses_list)

# Add course
@app.route('/addcourse', methods=['POST']) # type: ignore
@token_required
def add_course(current_user):
    if current_user['role'] != 'admin':
        return jsonify({'message': 'You do not have access to this page!'})

    if request.method == 'POST':
        program = request.form['program']
        course_code = request.form['course_code']
        course_name = request.form['course_name']
        course_type = request.form['course_type']

        course = {'program': program, 'course_code': course_code, 'course_name': course_name, 'course_type': course_type}
        #courses.insert_one(course)
        return jsonify({'course': course})

# Add members
@app.route('/addmember', methods=['POST']) # type: ignore
@token_required
def add_member(current_user): # type: ignore
    if current_user['role'] != 'admin':
        return jsonify({'message': 'You do not have access to this page!'})

    course_code = request.form['course_code']
    course_name = request.form['course_name']
    coordinator = request.form['coordinator']
    member1 = request.form['member1']
    member2 = request.form['member2']
    member3 = request.form['member3']
    member4 = request.form['member4']
    members = [member1, member2, member3, member4]

    member = {'course_code': course_code, 'course_name': course_name, 'coordinator': coordinator, 'members': members}
    #courses.insert_one(course)
    return jsonify({'members': member})

@app.route('/locf', methods=['POST']) # type: ignore
@token_required
def LOCF(current_user):
    if current_user['role'] != 'admin':
        return jsonify({'message': 'You do not have access to this page!'})

    lo = request.form['lo']
    course_name = request.form['course_name']
    coordinator = request.form['coordinator']

    locf = {'lo': lo, 'course_name': course_name, 'coordinator': coordinator}
    #courses.insert_one(course)
    return jsonify({'locf': locf})


# Run the app
if __name__ == '__main__':
    app.run(debug=True)


# {"program": "program", "course_code": "course_code", "course_name": "course_name", "course_type": "course_type"}
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjgyMDU4NDAxfQ.V6YQlftOt8S20Sivc4wLRpcT3voTw5I2CnbvlE55xXw
# /MANAGE_CONTENT = > 