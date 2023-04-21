from flask import Flask, jsonify, request, render_template
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from database import *

app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
jwt = JWTManager(app)

teachers = [
    {'id': 1, 'name': 'John Doe', 'subject': 'Math'},
    {'id': 2, 'name': 'Jane Smith', 'subject': 'English'},
    {'id': 3, 'name': 'Bob Johnson', 'subject': 'Science'},
]

@app.route('/') # type: ignore
def INDEX_1():
    return render_template('index.html')

@app.route('/admin/login', methods=['POST'])
def admin_login():
    # Replace with your own authentication logic
    username = request.form['username']
    password = request.form['password']

    if username != 'admin' or password != 'admin':
        return jsonify({'msg': 'Invalid username or password'}), 401

    access_token = create_access_token(identity=username, additional_claims={'role': 'admin'})
    return jsonify({'access_token': access_token}), 200

# def get_user_role():
#     claims = get_jwt()
#     return claims['role'] if claims else None

@app.route('/teachers', methods=['POST'])
@jwt_required(optional=True)
def add_teacher():
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({'msg': 'Admin privileges required'}), 403

    teacher = {'id': len(teachers) + 1, 'name': request.form['name'], 'subject': request.form['subject']}
    teachers.append(teacher)

    return jsonify({'msg': 'Teacher added successfully'}), 200

@app.route('/teachers', methods=['GET'])
@jwt_required(optional=True)
def get_teachers():
    teachers_list = [{'name': t['name'], 'subject': t['subject']} for t in teachers]
    return jsonify(teachers_list), 200

# @app.route('/login', methods = ['GET', 'POST']) # type: ignore
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         if not username or not password:
#             return jsonify({'msg': 'Invalid credentials'}), 400

#         user = check_user(username=username)
#         if not user or not check_password_hash(user['password'], password):
#             return jsonify({'msg': 'Invalid credentials'}), 401

#         access_token = create_access_token(identity=user['_id'], expires_delta=timedelta(hours=1), additional_claims={'role': user['role']})
#         return jsonify({'access_token': access_token}), 200

#     if request.method == 'GET' or 'POST':
#         return jsonify(course_data())

def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user, expires_delta=timedelta(hours=1), additional_claims={'role': 'user'})
    return jsonify({'access_token': access_token}), 200

@app.errorhandler(401)
def handle_unauthorized_error(error):
    return jsonify({'msg': 'Missing or invalid access token'}), 401

if __name__ == '__main__':
    app.run(debug=True)
