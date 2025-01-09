from flask import Blueprint, jsonify
from flask_restful import Api, Resource

argentina_api = Blueprint('argentina_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(argentina_api)

class ArgentinaAPI:
    @staticmethod
    def get_restaurant(name):
        restaurant = {
            "The Argentinian Experience": {
                "name": "The Argentinian Experience",
                "location": "Argentina",
            },
            "Mercado": {
                "name": "Mercado de Liniers Restaurante",
                "location": "Argentina",
            },
            
        }
        return restaurant.get(name)

    class _theArgentinianExperience(Resource):
        def get(self):
            # Use the helper method to get John's details
            theargentinianexperience_details = ArgentinaAPI.get_restaurant("The Argentinian Experience")
            return jsonify(theargentinianexperience_details)

    class _Mercado(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Mercado_details = ArgentinaAPI.get_restaurant("Mercado")
            return jsonify(Mercado_details)

    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            theargentinianexperience_details = ArgentinaAPI.get_restaurant("The Argentinian Experience")
            Mercado_details = ArgentinaAPI.get_restaurant("Mercado")
            return jsonify({"restaurant": [theargentinianexperience_details, Mercado_details]})

    # Building REST API endpoints
    api.add_resource(_theArgentinianExperience, '/restaurant/theArgentinianExperience')
    api.add_resource(_Mercado, '/restaurant/mercado')
    api.add_resource(_Bulk, '/restaurant')

# Instantiate the StudentAPI to register the endpoints
argentina_api_instance = ArgentinaAPI()