from flask import Flask
from flask_restful import Resource, Api, request

app = Flask(__name__)
api = Api(app)

class GEtNotifiedFake(Resource):
    def post(self):
        data = request.get_json(force=True)
        return {"expiry_notification":"received"},200

api.add_resource(GEtNotifiedFake, '/notify')

if __name__ == '__main__':
    app.run(debug=True, port=5056)
