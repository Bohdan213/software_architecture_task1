from flask_restful import Resource, reqparse
from flask import Response


class MessagesService(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()

    def post(self):
        pass

    def get(self):
        print("GET request")
        return {"msgs": "Not implemented yet."}, 200