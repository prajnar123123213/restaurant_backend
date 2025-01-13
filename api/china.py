from flask import Blueprint, jsonify
from flask_restful import Api, Resource

china_api = Blueprint('china_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(china_api)

class ChinaAPI:
    @staticmethod
    def get_chinese(name):
        chinese = {
            "West Lake Restaurant": {
                "name": "West_Lake_Restaurant",
                "location": "China",
            },
            "Silk Road Cuisine": {
                "name": "Silk_Road_Cuisine",
                "location": "China",
            },              
        }
        return chinese.get(name)
    
    class _West_Lake_Restaurant(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            West_Lake_Restaurant_details = ChinaAPI.get_chinese("West_Lake_Restaurant")
            return jsonify(West_Lake_Restaurant_details)
        
    class _Silk_Road_Cuisine(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            Silk_Road_Cuisine_details = ChinaAPI.get_chinese("Silk_Road_Cuisine")
            return jsonify(Silk_Road_Cuisine_details)
        
    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            West_Lake_Restaurant_details = ChinaAPI.get_chinese("West_Lake_Restaurant")
            Silk_Road_Cuisine_details = ChinaAPI.get_chinese("Silk_Road_Cuisine")
            return jsonify({"chinese": [West_Lake_Restaurant_details, Silk_Road_Cuisine_details]})

    # Building REST API endpoints
    api.add_resource(_West_Lake_Restaurant, '/chinese/west_lake_restaurant')
    api.add_resource(_Silk_Road_Cuisine, '/chinese/silk_road_cuisine')
    api.add_resource(_Bulk, '/chinese')

# Instantiate the StudentAPI to register the endpoints
china_api_instance = ChinaAPI()