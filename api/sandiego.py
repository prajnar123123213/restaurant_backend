from flask import Blueprint, jsonify
from flask_restful import Api, Resource

sandiego_api = Blueprint('sandiego_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(sandiego_api)

class sandiegoAPI:
    @staticmethod
    def get_food(name):
        food = {
            "Kilimanjaro": {
                "name": "Kilimanjaro Restaurant",
                "location": "sangiego",
            },
            "McFestine": {
                "name": "McFestine's",
                "location": "sandiego",
            },  
            "Unity": {
                "name": "Unity Restaurant",
                "location": "sandiego",
            },
            
        }
        return food.get(name)
    
    class _Kilimanjaro(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Kilimanjaro_details = sandiegoAPI.get_food("Kilimanjaro")
            return jsonify(Kilimanjaro_details)
        
    class _McFestine(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            McFestine_details = sandiegoAPI.get_food("McFestine")
            return jsonify(McFestine_details)
        
    class _Unity(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Unity_details = sandiegoAPI.get_food("Unity")
            return jsonify(Unity_details)
        
    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            Kilimanjaro_details = sandiegoAPI.get_food("Kilimanjaro")
            McFestine_details = sandiegoAPI.get_food("McFestine")
            Unity_details = sandiegoAPI.get_food("Unity")
            return jsonify({"food": [Kilimanjaro_details, McFestine_details, Unity_details]})

    # Building REST API endpoints
    api.add_resource(_Kilimanjaro, '/food/kilimanjaro')
    api.add_resource(_McFestine, '/food/mcfestine')
    api.add_resource(_Unity, '/food/unity')
    api.add_resource(_Bulk, '/food')

# Instantiate the StudentAPI to register the endpoints
sandiego_api_instance = sandiegoAPI()