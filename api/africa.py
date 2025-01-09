from flask import Blueprint, jsonify
from flask_restful import Api, Resource

africa_api = Blueprint('africa_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(africa_api)

class AfricaAPI:
    @staticmethod
    def get_restaurant(name):
        restaurant = {
            "Marble": {
                "name": "Marble Restaurant",
                "location": "South Africa",
            },
            "Piatto": {
                "name": "Piatto Farrarmare",
                "location": "South Africa",
            },
            
        }
        return restaurant.get(name)

    class _Marble(Resource):
        def get(self):
            # Use the helper method to get John's details
            marble_details = AfricaAPI.get_restaurant("Marble")
            return jsonify(marble_details)

    class _Piatto(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            piatto_details = AfricaAPI.get_restaurant("Piatto")
            return jsonify(piatto_details)

    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            Marble_details = AfricaAPI.get_restaurant("Marble")
            Piatto_details = AfricaAPI.get_restaurant("Piatto")
            return jsonify({"restaurant": [Marble_details, Piatto_details]})

    # Building REST API endpoints
    api.add_resource(_Marble, '/restaurant/marble')
    api.add_resource(_Piatto, '/restaurant/piatto')
    api.add_resource(_Bulk, '/restaurant')

# Instantiate the StudentAPI to register the endpoints
africa_api_instance = AfricaAPI()