from flask import Flask, jsonify, request
from flask_cors import CORS
from database import *

app = Flask(__name__)
CORS(app)

@app.route('/') # type: ignore
def INDEX_1():
    pass

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
