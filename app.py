import os

from flask import Flask
from flask_restful import Api


app = Flask(__name__)

api = Api(app)
#
# api.add_resource(Class,"/query/<string:name>")
# api.add_resource(ClassName, "/compliance_verify/<string:name>")


if __name__ == '__main__':
    app.run(debug=True)
