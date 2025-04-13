from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.auth import role_required
from app.services.rocket_service import RocketService

rocket_bp = Blueprint('rocket', __name__)

"""
    Define las rutas de la API y maneja las peticiones HTTP.
"""

@rocket_bp.route('/rockets', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Astronaut', 'Mission director', 'Flight operator')
def get_rockets():
    """Obtiene todos los cohetes."""

    try:
        rockets = RocketService.list_rockets()
        return jsonify(rockets), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@rocket_bp.route('/rockets/<int:rocket_id>', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Astronaut', 'Mission director', 'Flight operator')
def get_rocket_by_id(rocket_id):
    """Obtiene un cohete por ID."""

    message, status_code = RocketService.get_rocket_by_id(rocket_id)
    return jsonify(message), status_code

@rocket_bp.route('/rockets', methods=['POST'])
@jwt_required()
@role_required('Admin')
def create_rocket():
    """Crea un nuevo cohete."""

    data = request.json
    response, status_code = RocketService.create_rocket(data)
    return jsonify(response), status_code


@rocket_bp.route('/rockets/<int:rocket_id>', methods=['PUT'])
@jwt_required()
@role_required('Admin')
def update_rocket(rocket_id):
    """Actualiza un cohete existente."""

    data = request.json
    response, status_code = RocketService.update_rocket(rocket_id, data)
    return jsonify(response), status_code

@rocket_bp.route('/rockets/<int:rocket_id>', methods=['DELETE'])
@jwt_required()
@role_required('Admin')
def delete_rocket(rocket_id):
    """Elimina un cohete."""

    response, status_code = RocketService.delete_rocket(rocket_id)
    return jsonify(response), status_code
