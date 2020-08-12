from flask import Flask, Blueprint
from flask_restful import Resource, Api

def create_app():
    app = Flask(__name__)
    
    api_bp = Blueprint('api', __name__, url_prefix='/api')
    api = Api(api_bp)
    api.add_resource(Helloworld, '/')
    
    app.register_blueprint(api_bp)
    return app


class Helloworld(Resource):
    def get(self):
        return 'hello world', 200

