from flask import Flask, jsonify, request, render_template, redirect, url_for, make_response
from flask_cors import CORS
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'your_secret_key'

# Auth Decorator
def token_required(f):
    @wraps(f)

    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            current_user = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)
    return decorated


# Authenticate user
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    username = username.lower()

    # user = check_user(username=username, password=password)
    # if not user:
    #     return jsonify({'message': 'Invalid username or password!'})
    
    if username not in ['admin', 'faculty', 'dean']:
        return jsonify({'status': 401})

    token_ = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

    return jsonify({'token': token_})


# Home
@app.route('/home', methods=['GET'])
@token_required

def home(current_user):
    user = current_user['username']

    return jsonify({
        'username': user,
        'name': 'Abhishek Bisht',
        'department': 'School of Engineering and Technology',
        
        'role': 'Administrator',
        'designation': 'Administrator',

        # 'role': 'Faculty',
        # 'designation': 'Associate Professor',
        
        # 'role': 'Dean',
        # 'designation': 'Dean',
    })

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

if __name__ == '__main__':
    app.run(debug=True)