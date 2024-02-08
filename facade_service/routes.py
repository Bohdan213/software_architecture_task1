from flask_restful import Resource, reqparse
from flask import Response
from facade_service.services.utils import generate_uuid, perform_get_request, perform_post_request


class FacadeService(Resource):

    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('msg', type=str, help='Message to be sent')

        self.get_parser = reqparse.RequestParser()

    def post(self):
        args = self.post_parser.parse_args()
        msg = args["msg"]
        uuid = generate_uuid()
        print(f"POST request, msg: {msg}, generated uuid: {uuid}")
        response_logging = perform_post_request(url="http://127.0.0.1:8081/api/v1/logging_service",
                                        data={"msg": msg, "uuid": uuid})
        print(f"RESPONSE from the post request to logging service, status: {response_logging.status_code}")
        return {"Status": "Success"}, 200

    def get(self):
        response_logging = perform_get_request(url="http://127.0.0.1:8081/api/v1/logging_service",
                                               params=None)
        print(f"RESPONSE from the get request to logging service, status: {response_logging.status_code}")

        response_messages= perform_get_request(url="http://127.0.0.1:8082/api/v1/messages_service",
                                               params=None)
        print(f"RESPONSE from the get request to messages service, status: {response_messages.status_code}")

        return {"Result": "Success", "msgs": response_logging.json()["msgs"] + response_messages.json()["msgs"]}
