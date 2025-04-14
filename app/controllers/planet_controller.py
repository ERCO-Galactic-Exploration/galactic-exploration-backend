from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.auth import role_required
from app.services.planet_service import PlanetService
from app.models.solar_system import SolarSystem
from app.models.galaxy import Galaxy
from app.models.planet_type import PlanetType

planet_bp = Blueprint('planet', __name__)

"""
    Define las rutas de la API y maneja las peticiones HTTP.
"""

@planet_bp.route('/planets', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Astronaut', 'Mission director', 'Planetary scientist', 'Flight operator')
def get_planets():
    """
    Obtiene todos los planetas.
    ---
    tags:
      - Planets
    security:
      - Bearer: []
    responses:
      200:
        description: Lista de planetas
        schema:
          type: array
          items:
            type: object
        examples:
          application/json: [{"id": 1, "name": "Tierra"}, {"id": 2, "name": "Marte"}]
    """

    try:
        planets = PlanetService.list_planets()
        return jsonify(planets), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@planet_bp.route('/planets/<int:planet_id>', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Astronaut', 'Mission director', 'Planetary scientist', 'Flight operator')
def get_planet_by_id(planet_id):
    """
    Obtiene un planeta por ID.
    ---
    tags:
      - Planets
    parameters:
      - name: planet_id
        in: path
        type: integer
        required: true
        description: ID del planeta
    responses:
      200:
        description: Información del planeta
        schema:
          type: object
        examples:
          application/json: { "id": 1, "name": "Tierra" }
    """


    message, status_code = PlanetService.get_planet_by_id(planet_id)
    return jsonify(message), status_code

@planet_bp.route('/planets', methods=['POST'])
@jwt_required()
@role_required('Admin')
def create_planet():
    """
    Crea un nuevo planeta.
    ---
    tags:
      - Planets
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            mass:
              type: number
            radius:
              type: number
    responses:
      201:
        description: Planeta creado exitosamente
    """
    data = request.json
    response, status_code = PlanetService.create_planet(data)
    return jsonify(response), status_code
    # try:
        
    # except ValueError as e:
    #     return jsonify({"error": str(e)}), 400

@planet_bp.route('/planets/<int:planet_id>', methods=['PUT'])
@jwt_required()
@role_required('Admin')
def update_planet(planet_id):
    """
    Actualiza un planeta existente.
    ---
    tags:
      - Planets
    parameters:
      - name: planet_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Planeta actualizado
    """

    data = request.json
    response, status_code = PlanetService.update_planet(planet_id, data)
    return jsonify(response), status_code

@planet_bp.route('/planets/<int:planet_id>', methods=['DELETE'])
@jwt_required()
@role_required('Admin')
def delete_planet(planet_id):
    """
    Elimina un planeta.
    ---
    tags:
      - Planets
    parameters:
      - name: planet_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Eliminación exitosa
    """

    response, status_code = PlanetService.delete_planet(planet_id)
    return jsonify(response), status_code


@planet_bp.route('/planets/solar-systems', methods=['GET'])
@jwt_required()
@role_required('Admin')
def get_solar_systems():
    """
    Obtiene todos los sistemas solares.
    ---
    tags:
      - Planets
    responses:
      200:
        description: Lista de sistemas solares
        schema:
          type: array
          items:
            type: object
            properties:
              id_solar_system:
                type: integer
              name:
                type: string
    """
    try:
        
        solar_systems = SolarSystem.query.all()
        
        solar_systems_list = [{'id_solar_system': s.id_solar_system, 'name': s.name} for s in solar_systems]
        return jsonify(solar_systems_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@planet_bp.route('/planets/galaxies', methods=['GET'])
@jwt_required()
@role_required('Admin')
def get_galaxies():
    """
    Obtiene todas las galaxias.
    ---
    tags:
      - Planets
    responses:
      200:
        description: Lista de galaxias
        schema:
          type: array
          items:
            type: object
            properties:
              id_galaxy:
                type: integer
              name:
                type: string
    """
    try:
        
        galaxies = Galaxy.query.all()
        
        galaxies_list = [{'id_galaxy': s.id_galaxy, 'name': s.name} for s in galaxies]
        return jsonify(galaxies_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@planet_bp.route('/planets/planet-types', methods=['GET'])
@jwt_required()
@role_required('Admin')
def get_planet_types():
    """
    Obtiene todos los tipos de planetas.
    ---
    tags:
      - Planets
    responses:
      200:
        description: Lista de tipos de planetas
        schema:
          type: array
          items:
            type: object
            properties:
              id_planet_type:
                type: integer
              name:
                type: string
    """
    try:
        
        planet_types = PlanetType.query.all()
        
        planet_types_list = [{'id_planet_type': s.id_planet_type, 'name': s.name} for s in planet_types]
        return jsonify(planet_types_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500