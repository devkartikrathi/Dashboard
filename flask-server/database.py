import mysql.connector
from key import *

db = mysql.connector.connect(
    host=HOST,
    user=USERNAME,
    password=PASSWORD,
    database=DATABASE
)

cursor = db.cursor()

def get_data():
    cursor.execute("SELECT * FROM studentdata")
    result = cursor.fetchall()
    data = []
    for row in result:
        data.append({'id': row[0], 'name': row[1], 'age': row[2]})
    return data

def add_data(name, age):
    cursor = db.cursor()
    query = "INSERT INTO yourtable (name, age) VALUES (%s, %s)"
    values = (name, age)
    cursor.execute(query, values)
    db.commit()
    return "Data added successfully"

def course_data():
    cursor.execute("SELECT * FROM courses")
    result = cursor.fetchall()
    return result
