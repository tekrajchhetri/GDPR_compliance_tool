import os

from flask import Flask
from flask_restful import Api
from resources.Test import Test

app = Flask(__name__)

api = Api(app)
#
api.add_resource(Test,"/")
# api.add_resource(ClassName, "/compliance_verify/<string:name>")


if __name__ == '__main__':
    app.run(debug=True)
