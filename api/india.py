from flask import Blueprint, jsonify
from flask_restful import Api, Resource

india_api = Blueprint('india_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(india_api)

class IndiaAPI:
    @staticmethod
    def get_food(name):
        food = {
            "Indian_Accent": {
                "name": "Indian_Accent",
                "location": "India",
            },             
        }
        return food.get(name)
    
    class _Indian_Accent(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            West_Lake_Restaurant_details = IndiaAPI.get_food("Indian_Accent")
            return jsonify(West_Lake_Restaurant_details)
        
    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            Indian_Accent_details = IndiaAPI.get_food("Indian_Accent")
            return jsonify({"food": [Indian_Accent_details]})

    # Building REST API endpoints
    api.add_resource(_Indian_Accent, '/food/indian_accent')
    api.add_resource(_Bulk, '/food')

# Instantiate the StudentAPI to register the endpoints
india_api_instance = IndiaAPI()