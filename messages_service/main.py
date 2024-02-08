from messages_service import app_messages, api_messages
from messages_service.routes import MessagesService

api_messages.add_resource(MessagesService, '/api/v1/messages_service')

if __name__ == "__main__":
    app_messages.run(port=8082)
