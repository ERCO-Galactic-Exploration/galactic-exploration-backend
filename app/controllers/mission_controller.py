from flask import Blueprint, request, jsonify
from app.services.mission_service import MissionService

"""
    Define las rutas de la API y maneja las peticiones HTTP.
"""

mission_bp = Blueprint('mission', __name__)

@mission_bp.route('/missions', methods=['GET'])
def get_missions():
    """Obtiene todas las misiones."""

    try:
        missions = MissionService.list_missions()
        return jsonify(missions), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@mission_bp.route('/missions/<int:mission_id>', methods=['GET'])
def get_mission_by_id(mission_id):
    """Obtiene una misión por ID."""

    message, status_code = MissionService.get_mission_by_id(mission_id)
    return jsonify(message), status_code

@mission_bp.route('/missions', methods=['POST'])
def create_mission():
    """Crea una nueva misión."""
    
    data = request.json
    response, status_code = MissionService.create_mission(data)
    return jsonify(response), status_code

@mission_bp.route('/missions/<int:mission_id>', methods=['PUT'])
def update_mission(mission_id):
    """Actualiza una misión existente."""

    data = request.json
    response, status_code = MissionService.update_mission(mission_id, data)
    return jsonify(response), status_code

@mission_bp.route('/missions/<int:mission_id>', methods=['DELETE'])
def delete_mission(mission_id):
    """Elimina una misión."""

    response, status_code = MissionService.delete_mission(mission_id)
    return jsonify(response), status_code
