from flask import Blueprint, jsonify
from flask_restful import Api, Resource

ethiopia_api = Blueprint('ethiopia_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(ethiopia_api)

class EthiopiaAPI:
    @staticmethod
    def get_meal(name):
        meal = {
            "Mesti": {
                "name": "Mesti Restaurant",
                "location": "Ethiopia",
            },
       
        }
        return meal.get(name)
    
    class _Mesti(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Mesti_details = EthiopiaAPI.get_meal("Mesti")
            return jsonify(Mesti_details)
    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            Mesti_details = EthiopiaAPI.get_meal("Mesti")
            return jsonify({"meal": [Mesti_details]})

    # Building REST API endpoints
    api.add_resource(_Mesti, '/meal/mesti')
    api.add_resource(_Bulk, '/meal')

# Instantiate the StudentAPI to register the endpoints
ethiopia_api_instance = EthiopiaAPI()