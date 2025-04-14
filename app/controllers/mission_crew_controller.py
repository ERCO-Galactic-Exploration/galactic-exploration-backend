from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.auth import role_required
from app.services.mission_crew_service import MissionCrewService

mission_crew_bp = Blueprint('mission_crew', __name__)

@mission_crew_bp.route('/missions/<int:mission_id>/assign_astronaut', methods=['POST'])
@jwt_required()
@role_required('Admin', 'Mission director')
def assign_astronaut(mission_id):
    """
    Asigna uno o varios astronautas a una misión.
    ---
    tags:
      - Mission Crews
    security:
      - Bearer: []
    parameters:
      - name: mission_id
        in: path
        type: integer
        required: true
        description: ID de la misión
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            astronaut_ids:
              type: array
              items:
                type: integer
            example:
              astronaut_ids: [1, 2, 3]
    responses:
      200:
        description: Astronautas asignados a la misión
      400:
        description: Error al asignar astronautas
    """
    data = request.json
    message, status_code = MissionCrewService.assign_astronaut_to_mission(mission_id, data)
    return jsonify(message), status_code


@mission_crew_bp.route('/missions/<int:mission_id>/astronauts', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Mission director', 'Flight operator')
def get_astronauts_by_mission_id(mission_id):
    """
    Obtiene los astronautas asignados a una misión.
    ---
    tags:
      - Mission Crews
    security:
      - Bearer: []
    parameters:
      - name: mission_id
        in: path
        type: integer
        required: true
        description: ID de la misión
    responses:
      200:
        description: Lista de astronautas asignados a la misión
        schema:
          type: array
          items:
            type: object
            properties:
              astronaut_id:
                type: integer
              name:
                type: string
              specialty:
                type: string
            example:
              astronaut_id: 1
              name: Sofia Vargas
              specialty: Piloto
      404:
        description: Misión no encontrada
    """
    message, status_code = MissionCrewService.list_astronauts_for_mission(mission_id)
    return jsonify(message), status_code

@mission_crew_bp.route('/missions/<int:astronaut_id>/missions', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Mission director')
def get_missions_by_astronaut_id(astronaut_id):
    """
    Obtiene las misiones asignadas a un astronauta.
    ---
    tags:
      - Mission Crews
    security:
      - Bearer: []
    parameters:
      - name: astronaut_id
        in: path
        type: integer
        required: true
        description: ID del astronauta
    responses:
      200:
        description: Lista de misiones asignadas al astronauta
        schema:
          type: array
          items:
            type: object
            properties:
              mission_id:
                type: integer
              mission_name:
                type: string
            example:
              mission_id: 1
              mission_name: Misión Marte 2030
      404:
        description: Astronauta no encontrado
    """
    message, status_code = MissionCrewService.list_missions_by_astronauts(astronaut_id)
    return jsonify(message), status_code

@mission_crew_bp.route('/missions/<int:mission_id>/astronauts/<int:astronaut_id>', methods=['DELETE'])
@jwt_required()
@role_required('Admin', 'Mission director')
def unassign_astronaut(mission_id, astronaut_id):
    """
    Desasigna un astronauta de una misión.
    ---
    tags:
      - Mission Crews
    security:
      - Bearer: []
    parameters:
      - name: mission_id
        in: path
        type: integer
        required: true
        description: ID de la misión
      - name: astronaut_id
        in: path
        type: integer
        required: true
        description: ID del astronauta
    responses:
      200:
        description: Astronauta desasignado de la misión
      404:
        description: Misión o astronauta no encontrados
    """
    message, status_code = MissionCrewService.unassign_astronaut_from_mission(mission_id, astronaut_id)
    return jsonify(message), status_code
