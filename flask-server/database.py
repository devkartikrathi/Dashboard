from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from key import URI
uri = URI
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['mydatabase']

users = db['users']

courses = db['courses']

# user = {
#     'username': 'john',
#     'password': 'password123',
#     'role': 'admin'
# }

# result = users.delete_one(user)
# result = users.delete_one(user)

# print(result.inserted_id)

# course = {
#     'course_id': 'CS101',
#     'course_name': 'Introduction to Computer Science'
# }

# result = courses.insert_one(course)

# print(result.inserted_id)
##################################################
# for document in users.find():
#     print(document)
# {'_id': ObjectId('643f71e2d2768df739e78545'), 'username': 'john', 'password': 'password123', 'role': 'admin'}


def course_data():
    course = []
    for document in courses.find():
        document['_id'] = str(document['_id'])
        course.append(document)
    return(course)