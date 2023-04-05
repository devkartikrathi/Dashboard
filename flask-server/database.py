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
        data.append({'stdid': row[0], 'name': row[1], 'course': row[2], 'email': row[3]})
    return data

def add_data(stdid, name, course, email):
    cursor = db.cursor()
    query = "INSERT INTO studentdata (stdid, name, course, email) VALUES (%s, %s, %s, %s)"
    values = (stdid, name, course, email)
    cursor.execute(query, values)
    db.commit()
    return get_data()

def course_data():
    cursor.execute("SELECT * FROM courses")
    result = cursor.fetchall()
    return result
