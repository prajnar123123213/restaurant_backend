from flask import Blueprint, jsonify
from flask_restful import Api, Resource

india_api = Blueprint('india_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(india_api)

class IndiaAPI:
    @staticmethod
    def get_indian(name):
        indian = {
            "Indian_Accent": {
                "name": "Indian_Accent",
                "location": "India",
            },             
        }
        return indian.get(name)
    
    class _Indian_Accent(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Indian_Accent_details = IndiaAPI.get_indian("Indian_Accent")
            return jsonify(Indian_Accent_details)
        
    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            Indian_Accent_details = IndiaAPI.get_find("Indian_Accent")
            return jsonify({"indian": [Indian_Accent_details]})

    # Building REST API endpoints
    api.add_resource(_Indian_Accent, '/indian/indian_accent')
    api.add_resource(_Bulk, '/indian')

# Instantiate the StudentAPI to register the endpoints
india_api_instance = IndiaAPI()