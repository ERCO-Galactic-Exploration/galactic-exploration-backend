from flask import Blueprint, request, jsonify
from app.services.mission_crew_service import MissionCrewService

"""
    Define las rutas de la API y maneja las peticiones HTTP.
"""

mission_crew_bp = Blueprint('mission_crew', __name__)

@mission_crew_bp.route('/missions/<int:mission_id>/assign_astronaut', methods=['POST'])
def assign_astronaut(mission_id):
    """
    Asigna uno o varios astronautas a una misión.
    """

    data = request.json
    
    message, status_code = MissionCrewService.assign_astronaut_to_mission(mission_id, data)
    return jsonify(message), status_code


@mission_crew_bp.route('/missions/<int:mission_id>/astronauts', methods=['GET'])
def get_astronauts_by_mission_id(mission_id):
    """
    Obtiene los astronautas de una misión.
    """

    message, status_code = MissionCrewService.list_astronauts_for_mission(mission_id)
    return jsonify(message), status_code

@mission_crew_bp.route('/missions/<int:astronaut_id>/missions', methods=['GET'])
def get_missions_by_astronaut_id(astronaut_id):
    """
    Obtiene las misiones de un astronauta.
    """

    message, status_code = MissionCrewService.list_missions_by_astronauts(astronaut_id)
    return jsonify(message), status_code

@mission_crew_bp.route('/missions/<int:mission_id>/astronauts/<int:astronaut_id>', methods=['DELETE'])
def unassign_astronaut(mission_id, astronaut_id):
    """
    Desasigna un astronauta de una misión.
    """

    message, status_code = MissionCrewService.unassign_astronaut_from_mission(mission_id, astronaut_id)
    return jsonify(message), status_code