from flask import Blueprint, jsonify
from flask_restful import Api, Resource

chile_api = Blueprint('chile_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(chile_api)

class ChileAPI:
    @staticmethod
    def get_restaurant(name):
        restaurant = {
            "Jardin Oriental": {
                "name": "Jardin Oriental",
                "location": "Chile",
            },
            "Sabor Calderino": {
                "name": "Sabor Calderino",
                "location": "Chile",
            },
            
        }
        return restaurant.get(name)

    class _Jardin(Resource):
        def get(self):
            # Use the helper method to get John's details
            Jardin_details = ChileAPI.get_restaurant("Jardin Oriental")
            return jsonify(Jardin_details)

    class _Sabor(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Sabor_details = ChileAPI.get_restaurant("Sabor Calderino")
            return jsonify(Sabor_details)

    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            Jardin_details = ChileAPI.get_restaurant("Jardin Oriental")
            Sabor_details = ChileAPI.get_restaurant("Sabor Calderino")
            return jsonify({"restaurant": [Jardin_details, Sabor_details]})

    # Building REST API endpoints
    api.add_resource(_Jardin, '/restaurant/jardin')
    api.add_resource(_Sabor, '/restaurant/sabor')
    api.add_resource(_Bulk, '/restaurant')

# Instantiate the StudentAPI to register the endpoints
chile_api_instance = ChileAPI()