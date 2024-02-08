from logging_service import app_logging, api_logging
from logging_service.routes import LoggingService

api_logging.add_resource(LoggingService, '/api/v1/logging_service')

if __name__ == "__main__":
    app_logging.run(port=8081)
