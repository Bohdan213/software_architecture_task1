from flask_restful import Resource, reqparse
from flask import Response
from logging_service import hash_map


class LoggingService(Resource):

    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('msg', type=str, help='Message to be logged')
        self.post_parser.add_argument('uuid', type=str, help='uuid of the message')

        self.get_parser = reqparse.RequestParser()

    def post(self):
        args = self.post_parser.parse_args()

        msg = args["msg"]
        uuid = args["uuid"]

        hash_map[uuid] = msg
        print(f"POST request: msg={msg}, uuid={uuid}")
        return {"Result": "Message logged successfully."}, 200


    def get(self):
        result = hash_map.values()
        result = "".join(result)
        print("GET request")
        return {"msgs": result}, 200
