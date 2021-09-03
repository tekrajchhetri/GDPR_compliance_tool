from flask import Flask
from flask_restful import Resource, Api, request

app = Flask(__name__)
api = Api(app)

class GEtNotifiedFake(Resource):
    def post(self):
        data = request.get_json(force=True)
        print(data)
        return {"expiry_notification":"received"},200

class FakeControllerRequest(Resource):
    def post(self):
        data = request.get_json(force=True)
        if data["ConsentID"] == "TEST110911134541145455":
            makeJSON = {"data":[{'mobilecat': {'data': ['m', 'd']}}, {'SensorDataCategory': {'data': ['GPS', 'speed']}}],
                "dataprocessing":[ 'whatever', 'storage', 'collection', 'Analysis'],
                "purpose":"Advertising"}
        else:
            makeJSON = {
                "data": [{'mobilecat': {'data': ['m', 'd']}}, {'SensorDataCategory': {'data': ['GPS', 'speed']}}],
                "dataprocessing": ['whatever', 'storage', 'collection', 'marketing'],
                "purpose": "Advertising"}
        return makeJSON

api.add_resource(GEtNotifiedFake, '/notify')
api.add_resource(FakeControllerRequest, '/controller')

if __name__ == '__main__':
    app.run(debug=True, port=5056)
    data ={'SensorDataCategory': [{'data': ['GPS', 'speed']}], 'mobilecat': [{'data': ['m', 'd']}]}





