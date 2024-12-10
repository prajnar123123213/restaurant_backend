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