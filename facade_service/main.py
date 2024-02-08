from facade_service import app_facade, api_facade
from facade_service.routes import FacadeService

api_facade.add_resource(FacadeService, '/api/v1/facade_service')

if __name__ == "__main__":
    app_facade.run(port=8080)
