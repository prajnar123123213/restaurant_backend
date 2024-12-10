from flask import Flask, jsonify
from flask_cors import CORS

# initialize a flask application (app)
app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')  # Allow all origins (*)

# ... your existing Flask

# add an api endpoint to flask app
@app.route('/api/data')
def get_data():
    # start a list, to be used like a information database
    InfoDb = []

    # add a row to list, an Info record
    InfoDb.append({
        "FirstName": "Zoe",
        "LastName": "He",
        "DOB": "April 11",
        "Role": "Developer",
        "Residence": "San Diego",
        "Email": "zoeqinhe@gmail.com",
        # "Owns_Cars": ["2015-Fusion", "2011-Ranger", "2003-Excursion", "1997-F350", "1969-Cadillac"]
    })
    # add a row to list, an Info record
    InfoDb.append({
        "FirstName": "Claire",
        "LastName": "Lee",
        "DOB": "March 15",
        "Role": "Developer",
        "Residence": "Los Angeles",
        "Email": "clairelee@example.com",
        # "Owns_Cars": ["2018-Civic", "2016-Accord"]
    })
    # add a row to list, an Info record
    InfoDb.append({
        "FirstName": "Prajna",
        "LastName": "Raj",
        "DOB": "March 15",
        "Role": "Assistant Scrum",
        "Residence": "Los Angeles",
        "Email": "clairelee@example.com",
        # "Owns_Cars": ["2018-Civic", "2016-Accord"]
    })
    # add a row to list, an Info record
    InfoDb.append({
        "FirstName": "Arshia",
        "LastName": "Deb Roy",
        "Role": "Scrum",
        "DOB": "March 15",
        "Residence": "Los Angeles",
        "Email": "clairelee@example.com",
        #"Owns_Cars": ["2018-Civic", "2016-Accord"]
    })
    # add a row to list, an Info record
    InfoDb.append({
        "FirstName": "Mirabelle",
        "LastName": "Andersen",
        "Role": "Integrator",
        "DOB": "February 27",
        "Residence": "San Diego",
        "Email": "slopez@powayusd.com",
        # "Owns_Cars": ["2021-Insight"]
    })
    # add a row to list, an Info record
    InfoDb.append({
        "FirstName": "Sanya",
        "LastName": "Kapoor",
        "Role": "Developer",
        "DOB": "March 15",
        "Residence": "Los Angeles",
        "Email": "clairelee@example.com",
        # "Owns_Cars": ["2018-Civic", "2016-Accord"]
    })
    
    return jsonify(InfoDb)

# add an HTML endpoint to flask app
@app.route('/')
def say_hello():
    html_content = """
    <html>
    <head>
        <title>Hellox</title>
    </head>
    <body>
        <h2>Hello, World!</h2>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    # starts flask server on default port, http://127.0.0.1:5001
    app.run(port=5001)
    
    
    
    
from flask import Blueprint, jsonify
from flask_restful import Api, Resource

student_api = Blueprint('student_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(student_api)

class StudentAPI:
    @staticmethod
    def get_student(name):
        students = {
            "John": {
                "name": "John",
                "age": 21,
                "major": "Computer Science",
                "university": "XYZ University"
            },
            "Jeff": {
                "name": "Jeff",
                "age": 22,
                "major": "Mechanical Engineering",
                "university": "ABC University"
            }
        }
        return students.get(name)

    class _John(Resource):
        def get(self):
            # Use the helper method to get John's details
            john_details = StudentAPI.get_student("John")
            return jsonify(john_details)

    class _Jeff(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            jeff_details = StudentAPI.get_student("Jeff")
            return jsonify(jeff_details)

    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            john_details = StudentAPI.get_student("John")
            jeff_details = StudentAPI.get_student("Jeff")
            return jsonify({"students": [john_details, jeff_details]})

    # Building REST API endpoints
    api.add_resource(_John, '/student/john')
    api.add_resource(_Jeff, '/student/jeff')
    api.add_resource(_Bulk, '/students')

# Instantiate the StudentAPI to register the endpoints
student_api_instance = StudentAPI()