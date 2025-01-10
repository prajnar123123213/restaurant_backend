from flask import Blueprint, jsonify
from flask_restful import Api, Resource

brazil_api = Blueprint('brazil_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(brazil_api)

class BrazilAPI:
    @staticmethod
    def get_restaurant(name):
        restaurant = {
            "Palace": {
                "name": "Churrascaria Palace",
                "location": "Brazil",
            },
            "Fogo": {
                "name": "Fogo de Chao",
                "location": "Brazil",
            },
            
        }
        return restaurant.get(name)

    class _Palace(Resource):
        def get(self):
            # Use the helper method to get John's details
            Palace_details = BrazilAPI.get_restaurant("Palace")
            return jsonify(Palace_details)

    class _Fogo(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Fogo_details = BrazilAPI.get_restaurant("Fogo")
            return jsonify(Fogo_details)

    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            Palace_details = BrazilAPI.get_restaurant("Palace")
            Fogo_details = BrazilAPI.get_restaurant("Fogo")
            return jsonify({"restaurant": [Palace_details, Fogo_details]})

    # Building REST API endpoints
    api.add_resource(_Palace, '/restaurant/palace')
    api.add_resource(_Fogo, '/restaurant/fogo')
    api.add_resource(_Bulk, '/restaurant')

# Instantiate the StudentAPI to register the endpoints
brazil_api_instance = BrazilAPI()