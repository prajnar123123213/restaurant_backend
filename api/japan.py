from flask import Blueprint, jsonify
from flask_restful import Api, Resource

japan_api = Blueprint('japan_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(japan_api)

class JapanAPI:
    @staticmethod
    def get_japanese(name):
        japanese = {
            "Hakumarut": {
                "name": "Hakumaru",
                "location": "Japan",
            },             
        }
        return japanese.get(name)
    
    class _Hakumaru(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Hakumaru_details = JapanAPI.get_japanese("Hakumaru")
            return jsonify(Hakumaru_details)
        
    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            Hakumaru_details =JapanAPI.get_japanese("Hakumaru")
            return jsonify({"japanese": [Hakumar_details]})

    # Building REST API endpoints
    api.add_resource(_Hakumaru, '/japanese/hakumaru')
    api.add_resource(_Bulk, '/japanese')

# Instantiate the StudentAPI to register the endpoints
japan_api_instance = JapanAPI()