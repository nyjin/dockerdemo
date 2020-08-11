from flask import Flask, Blueprint
from flask_restful import Resource, Api

app = Flask(__name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)

class Helloworld(Resource):
    def get(self):
        return 'hello world', 200

api.add_resource(Helloworld, '/')
app.register_blueprint(api_bp)