from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
# from app.models import *
from flasgger import Swagger
from app.controllers.planet_controller import planet_bp
from app.controllers.astronaut_controller import astronaut_bp
from app.controllers.rocket_controller import rocket_bp
from app.controllers.mission_controller import mission_bp
from app.controllers.mission_crew_controller import mission_crew_bp
from app.controllers.planetary_scan_controller import planetary_scan_bp
from app.controllers.planet_habitability_controller import planet_habitability_bp
from app.controllers.auth_controller import auth_bp

"""
    Define las rutas de la API y maneja las peticiones HTTP.
"""


def create_app():
    app = Flask(__name__)

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "API de Planetas",
            "description": "Documentación de la API",
            "version": "1.0"
        },
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "Introduce tu token JWT como: **Bearer &lt;tu_token&gt;**"
            }
        },
        "security": [{"Bearer": []}]
    }
    
    swagger = Swagger(app, template=swagger_template)

    app.config.from_object('app.config.Config')

    CORS(app, supports_credentials=True)
    # CORS(app, resources={r"/api/*": {"origins": "*"}})  # Permitir CORS para todas las rutas de la API
    # CORS(app, supports_credentials=True)  # Permitir CORS con credenciales    

    jwt = JWTManager(app)

    from app.database import db
    db.init_app(app)
    
    app.register_blueprint(planet_bp, url_prefix='/api/v1')
    app.register_blueprint(astronaut_bp, url_prefix='/api/v1')
    app.register_blueprint(rocket_bp, url_prefix='/api/v1')
    app.register_blueprint(mission_bp, url_prefix='/api/v1')
    app.register_blueprint(mission_crew_bp, url_prefix='/api/v1')
    app.register_blueprint(planetary_scan_bp, url_prefix='/api/v1')
    app.register_blueprint(planet_habitability_bp, url_prefix='/api/v1')
    app.register_blueprint(auth_bp, url_prefix='/api/v1')

    return app