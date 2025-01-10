from flask import Blueprint, jsonify
from flask_restful import Api, Resource

peru_api = Blueprint('peru_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(peru_api)

class PeruAPI:
    @staticmethod
    def get_restaurant(name):
        restaurant = {
            "Saha": {
                "name": "Saha Peruvian Kitchen",
                "location": "Peru",
            },
            "SABOR": {
                "name": "SABOR PERÚ",
                "location": "Peru",
            },
            
        }
        return restaurant.get(name)

    class _Saha(Resource):
        def get(self):
            # Use the helper method to get John's details
            Saha_details = PeruAPI.get_restaurant("Saha")
            return jsonify(Saha_details)

    class _SABOR(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            SABOR_details = PeruAPI.get_restaurant("SABOR")
            return jsonify(SABOR_details)

    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            Saha_details = PeruAPI.get_restaurant("Saha")
            SABOR_details = PeruAPI.get_restaurant("SABOR")
            return jsonify({"restaurant": [Saha_details, SABOR_details]})

    # Building REST API endpoints
    api.add_resource(_Saha, '/restaurant/saha')
    api.add_resource(_SABOR, '/restaurant/SABOR')
    api.add_resource(_Bulk, '/restaurant')

# Instantiate the StudentAPI to register the endpoints
peru_api_instance = PeruAPI()