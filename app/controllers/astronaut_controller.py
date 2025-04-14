from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils.auth import role_required
from app.services.astronaut_service import AstronautService
from app.models.astronaut_specialties import AstronautSpecialty

astronaut_bp = Blueprint('astronaut', __name__)

@astronaut_bp.route('/astronauts', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Mission director', 'Astronaut')
def get_astronauts():
    """
    Obtiene todos los astronautas.
    ---
    tags:
      - Astronauts
    security:
      - Bearer: []
    responses:
      200:
        description: Lista de astronautas
        schema:
          type: array
          items:
            type: object
        examples:
          application/json:
            [
              {
                "id_astronaut": 1,
                "name": "Sofia Vargas",
                "experience": 5,
                "nationality": {
                  "id_nationality": 1,
                  "name": "Colombiana"
                },
                "specialty": {
                  "id_specialty": 1,
                  "name": "Piloto"
                }
              }
            ]
    """
    try:
        current_user_id = get_jwt_identity()
        astronauts = AstronautService.list_astronauts()
        return jsonify(astronauts), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@astronaut_bp.route('/astronauts/<int:astronaut_id>', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Astronaut', 'Mission director')
def get_astronaut_by_id(astronaut_id):
    """
    Obtiene un astronauta por ID.
    ---
    tags:
      - Astronauts
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
        description: Detalles del astronauta
        schema:
          type: object
        examples:
          application/json:
            {
              "id_astronaut": 1,
              "name": "Sofia Vargas",
              "experience": 5,
              "nationality": {
                "id_nationality": 1,
                "name": "Colombiana"
              },
              "specialty": {
                "id_specialty": 1,
                "name": "Piloto"
              }
            }
    """
    message, status_code = AstronautService.get_astronaut_by_id(astronaut_id)
    return jsonify(message), status_code

@astronaut_bp.route('/astronauts', methods=['POST'])
@jwt_required()
@role_required('Admin')
def create_astronaut():
    """
    Crea un nuevo astronauta.
    ---
    tags:
      - Astronauts
    security:
      - Bearer: []
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Sofia Vargas
            experience:
              type: integer
              example: 5
            id_nationality:
              type: integer
              example: 1
            id_specialty:
              type: integer
              example: 1
    responses:
      201:
        description: Astronauta creado exitosamente
    """
    data = request.json
    response, status_code = AstronautService.create_astronaut(data)
    return jsonify(response), status_code

@astronaut_bp.route('/astronauts/<int:astronaut_id>', methods=['PUT'])
@jwt_required()
@role_required('Admin')
def update_astronaut(astronaut_id):
    """
    Actualiza un astronauta existente.
    ---
    tags:
      - Astronauts
    security:
      - Bearer: []
    parameters:
      - name: astronaut_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Sofia Vargas
            experience:
              type: integer
              example: 6
            id_nationality:
              type: integer
              example: 2
            id_specialty:
              type: integer
              example: 3
    responses:
      200:
        description: Astronauta actualizado exitosamente
    """
    data = request.json
    response, status_code = AstronautService.update_astronaut(astronaut_id, data)
    return jsonify(response), status_code

@astronaut_bp.route('/astronauts/<int:astronaut_id>', methods=['DELETE'])
@jwt_required()
@role_required('Admin')
def delete_astronaut(astronaut_id):
    """
    Elimina un astronauta.
    ---
    tags:
      - Astronauts
    security:
      - Bearer: []
    parameters:
      - name: astronaut_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Astronauta eliminado correctamente
    """
    response, status_code = AstronautService.delete_astronaut(astronaut_id)
    return jsonify(response), status_code

@astronaut_bp.route('/astronauts/specialties', methods=['GET'])
@jwt_required()
@role_required('Admin')
def get_astronaut_specialties():
    """
    Obtiene todas las especialidades de los astronautas.
    ---
    tags:
      - Astronauts
    security:
      - Bearer: []
    responses:
      200:
        description: Lista de especialidades
        schema:
          type: array
          items:
            type: object
            properties:
              id_specialty:
                type: integer
              name:
                type: string
        examples:
          application/json:
            [
              {"id_specialty": 1, "name": "Piloto"},
              {"id_specialty": 2, "name": "Ingeniero"},
              {"id_specialty": 3, "name": "Científico"}
            ]
    """
    try:
        astronaut_specialties = AstronautSpecialty.query.all()
        astronaut_specialties_list = [{'id_specialty': s.id_specialty, 'name': s.name} for s in astronaut_specialties]
        return jsonify(astronaut_specialties_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500