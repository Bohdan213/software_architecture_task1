from flask import Flask
from flask_restful import Api

hash_map = dict()


app_logging = Flask(__name__)
api_logging = Api(app_logging)
