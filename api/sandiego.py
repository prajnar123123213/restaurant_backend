from flask import Blueprint, jsonify
from flask_restful import Api, Resource

sandiego_api = Blueprint('sandiego_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(sandiego_api)

class sandiegoAPI:
    @staticmethod
    def get_food(name):
        food = {
            "Born": {
                "name": "Born & Raised",
                "location": "sandiego",
            },
            "Addison": {
                "name": "Addison",
                "location": "sandiego",
            },  
            "Herb": {
                "name": "Herb & Wood",
                "location": "sandiego",
            },
        }
        return food.get(name)
    
    class _Born(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Born_details = sandiegoAPI.get_food("Born & Raised")
            return jsonify(Born_details)
        
    class _Addison(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Addison_details = sandiegoAPI.get_food("Addison")
            return jsonify(Addison_details)
        
    class _Herb(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Herb_details = sandiegoAPI.get_food("Herb & Wood")
            return jsonify(Unity_details)
        
    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            Born_details = sandiegoAPI.get_food("Born & Raised")
            Addison_details = sandiegoAPI.get_food("Addison")
            Herb_details = sandiegoAPI.get_food("Herb & Wood")
            return jsonify({"food": [Born_details, Addison_details, Herb_details]})

    # Building REST API endpoints
    api.add_resource(_Born, '/food/born')
    api.add_resource(_Addison, '/food/Addison')
    api.add_resource(_Herb, '/food/Herb')
    api.add_resource(_Bulk, '/food')

# Instantiate the StudentAPI to register the endpoints
sandiego_api_instance = sandiegoAPI()