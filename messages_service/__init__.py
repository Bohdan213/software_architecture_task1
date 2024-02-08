from flask import Flask
from flask_restful import Api

app_messages = Flask(__name__)
api_messages = Api(app_messages)
