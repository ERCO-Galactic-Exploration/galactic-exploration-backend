from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.auth import role_required
from app.services.mission_service import MissionService
from app.models.mission_status import MissionStatus

mission_bp = Blueprint('mission', __name__)

@mission_bp.route('/missions', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Mission director', 'Planetary scientist', 'Flight operator', 'Astronaut')
def get_missions():
    """
    Obtiene todas las misiones.
    ---
    tags:
      - Missions
    security:
      - Bearer: []
    responses:
      200:
        description: Lista de misiones
        schema:
          type: array
          items:
            type: object
    """
    try:
        missions = MissionService.list_missions()
        return jsonify(missions), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@mission_bp.route('/missions/<int:mission_id>', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Mission director', 'Planetary scientist', 'Flight operator')
def get_mission_by_id(mission_id):
    """
    Obtiene una misión por ID.
    ---
    tags:
      - Missions
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
        description: Misión encontrada
    """
    message, status_code = MissionService.get_mission_by_id(mission_id)
    return jsonify(message), status_code

@mission_bp.route('/missions', methods=['POST'])
@jwt_required()
@role_required('Admin', 'Mission director')
def create_mission():
    """
    Crea una nueva misión.
    ---
    tags:
      - Missions
    security:
      - Bearer: []
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          example:
            name: Misión Marte 2030
            launch_date: "2030-05-21"
            mission_status_id: 1
            planet_id: 2
    responses:
      201:
        description: Misión creada
    """
    data = request.json
    response, status_code = MissionService.create_mission(data)
    return jsonify(response), status_code

@mission_bp.route('/missions/<int:mission_id>', methods=['PUT'])
@jwt_required()
@role_required('Admin', 'Mission director')
def update_mission(mission_id):
    """
    Actualiza una misión existente.
    ---
    tags:
      - Missions
    security:
      - Bearer: []
    parameters:
      - name: mission_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          example:
            name: Misión Marte 2035
            mission_status_id: 2
    responses:
      200:
        description: Misión actualizada
    """
    data = request.json
    response, status_code = MissionService.update_mission(mission_id, data)
    return jsonify(response), status_code

@mission_bp.route('/missions/<int:mission_id>', methods=['DELETE'])
@jwt_required()
@role_required('Admin', 'Mission director')
def delete_mission(mission_id):
    """
    Elimina una misión.
    ---
    tags:
      - Missions
    security:
      - Bearer: []
    parameters:
      - name: mission_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Misión eliminada
    """
    response, status_code = MissionService.delete_mission(mission_id)
    return jsonify(response), status_code

@mission_bp.route('/missions/statuses', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Mission director', 'Planetary scientist', 'Flight operator', 'Astronaut')
def get_mission_statuses():
    """
    Obtiene todos los estados de las misiones.
    ---
    tags:
      - Missions
    security:
      - Bearer: []
    responses:
      200:
        description: Lista de estados
        schema:
          type: array
          items:
            type: object
            properties:
              id_mission_status:
                type: integer
              name:
                type: string
          example:
            - id_mission_status: 1
              name: Planificada
            - id_mission_status: 2
              name: En curso
    """
    try:
        statuses = MissionStatus.query.all()
        statuses_list = [{'id_mission_status': s.id_mission_status, 'name': s.name} for s in statuses]
        return jsonify(statuses_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500