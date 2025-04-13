from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.astronaut_service import AstronautService

astronaut_bp = Blueprint('astronaut', __name__)

"""
    Define las rutas de la API y maneja las peticiones HTTP.
"""

@astronaut_bp.route('/astronauts', methods=['GET'])
@jwt_required()
def get_astronauts():
    """Obtiene todos los astronautas."""

    try:

        current_user_id = get_jwt_identity()
        print('current_user_id: ', current_user_id)

        astronauts = AstronautService.list_astronauts()
        return jsonify(astronauts), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@astronaut_bp.route('/astronauts/<int:astronaut_id>', methods=['GET'])
def get_astronaut_by_id(astronaut_id):
    """Obtiene un astronauta por ID."""

    message, status_code = AstronautService.get_astronaut_by_id(astronaut_id)
    return jsonify(message), status_code

@astronaut_bp.route('/astronauts', methods=['POST'])
def create_astronaut():
    """Crea un nuevo astronauta."""

    data = request.json
    # print(data)
    response, status_code = AstronautService.create_astronaut(data)
    return jsonify(response), status_code


@astronaut_bp.route('/astronauts/<int:astronaut_id>', methods=['PUT'])
def update_astronaut(astronaut_id):
    """Actualiza un astronauta existente."""

    data = request.json
    response, status_code = AstronautService.update_astronaut(astronaut_id, data)
    return jsonify(response), status_code

@astronaut_bp.route('/astronauts/<int:astronaut_id>', methods=['DELETE'])
def delete_astronaut(astronaut_id):
    """Elimina un astronauta."""

    response, status_code = AstronautService.delete_astronaut(astronaut_id)
    return jsonify(response), status_code
