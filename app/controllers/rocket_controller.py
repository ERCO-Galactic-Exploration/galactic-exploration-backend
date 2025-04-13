from flask import Blueprint, request, jsonify
from app.services.rocket_service import RocketService

rocket_bp = Blueprint('rocket', __name__)

"""
    Define las rutas de la API y maneja las peticiones HTTP.
"""

@rocket_bp.route('/rockets', methods=['GET'])
def get_rockets():
    """Obtiene todos los cohetes."""

    try:
        rockets = RocketService.list_rockets()
        return jsonify(rockets), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@rocket_bp.route('/rockets/<int:rocket_id>', methods=['GET'])
def get_rocket_by_id(rocket_id):
    """Obtiene un cohete por ID."""

    message, status_code = RocketService.get_rocket_by_id(rocket_id)
    return jsonify(message), status_code

@rocket_bp.route('/rockets', methods=['POST'])
def create_rocket():
    """Crea un nuevo cohete."""

    data = request.json
    response, status_code = RocketService.create_rocket(data)
    return jsonify(response), status_code


@rocket_bp.route('/rockets/<int:rocket_id>', methods=['PUT'])
def update_rocket(rocket_id):
    """Actualiza un cohete existente."""

    data = request.json
    response, status_code = RocketService.update_rocket(rocket_id, data)
    return jsonify(response), status_code

@rocket_bp.route('/rockets/<int:rocket_id>', methods=['DELETE'])
def delete_rocket(rocket_id):
    """Elimina un cohete."""

    response, status_code = RocketService.delete_rocket(rocket_id)
    return jsonify(response), status_code
