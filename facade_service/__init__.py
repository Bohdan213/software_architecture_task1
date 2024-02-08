from flask import Flask
from flask_restful import Api

app_facade = Flask(__name__)
api_facade = Api(app_facade)
