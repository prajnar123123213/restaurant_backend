from flask import Blueprint, jsonify
from flask_restful import Api, Resource

japan_api = Blueprint('japan_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(japan_api)

class JapanAPI:
    @staticmethod
    def get_food(name):
        food = {
            "Hakumarut": {
                "name": "Hakumaru",
                "location": "Japan",
            },             
        }
        return food.get(name)
    
    class _Hakumaru(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Hakumaru_details = JapanAPI.get_food("Hakumaru")
            return jsonify(Hakumaru_details)
        
    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            Hakumaru_details =JapanAPI.get_food("Hakumaru")
            return jsonify({"food": [Hakumaru_details]})

    # Building REST API endpoints
    api.add_resource(_Hakumaru, '/food/hakumaru')
    api.add_resource(_Bulk, '/food')

# Instantiate the StudentAPI to register the endpoints
japan_api_instance = JapanAPI()