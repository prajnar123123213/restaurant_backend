from flask import Blueprint, jsonify
from flask_restful import Api, Resource

southafrica_api = Blueprint('southafrica_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(southafrica_api)

class southafricaAPI:
    @staticmethod
    def get_food(name):
        food = {
            "Born": {
                "name": "Born & Raised",
                "location": "southafrica",
            },
            "Addison": {
                "name": "Addison",
                "location": "southafrica",
            },  
            "Herb": {
                "name": "Herb & Wood",
                "location": "southafrica",
            },
        }
        return food.get(name)
    
    class _Born(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Born_details = southafricaAPI.get_food("Born & Raised")
            return jsonify(Born_details)
        
    class _Addison(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Addison_details = southafricaAPI.get_food("Addison")
            return jsonify(Addison_details)
        
    class _Herb(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Herb_details = southafricaAPI.get_food("Herb & Wood")
            return jsonify(Herb_details)
        
    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            Born_details = southafricaAPI.get_food("Born & Raised")
            Addison_details = southafricaAPI.get_food("Addison")
            Herb_details = southafricaAPI.get_food("Herb & Wood")
            return jsonify({"food": [Born_details, Addison_details, Herb_details]})

    # Building REST API endpoints
    api.add_resource(_Born, '/food/born')
    api.add_resource(_Addison, '/food/Addison')
    api.add_resource(_Herb, '/food/Herb')
    api.add_resource(_Bulk, '/food')

# Instantiate the StudentAPI to register the endpoints
southafrica_api_instance = southafricaAPI()