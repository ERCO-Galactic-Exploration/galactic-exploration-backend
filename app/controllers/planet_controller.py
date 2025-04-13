from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.auth import role_required
from app.services.planet_service import PlanetService

planet_bp = Blueprint('planet', __name__)

"""
    Define las rutas de la API y maneja las peticiones HTTP.
"""

@planet_bp.route('/planets', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Astronaut', 'Mission director', 'Planetary scientist', 'Flight operator')
def get_planets():
    """Obtiene todos los planetas."""

    try:
        planets = PlanetService.list_planets()
        return jsonify(planets), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@planet_bp.route('/planets/<int:planet_id>', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Astronaut', 'Mission director', 'Planetary scientist', 'Flight operator')
def get_planet_by_id(planet_id):
    """Obtiene un planeta por ID."""
    message, status_code = PlanetService.get_planet_by_id(planet_id)
    return jsonify(message), status_code

@planet_bp.route('/planets', methods=['POST'])
@jwt_required()
@role_required('Admin')
def create_planet():
    """Crea un nuevo planeta."""
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
    """Actualiza un planeta existente."""

    data = request.json
    response, status_code = PlanetService.update_planet(planet_id, data)
    return jsonify(response), status_code

@planet_bp.route('/planets/<int:planet_id>', methods=['DELETE'])
@jwt_required()
@role_required('Admin')
def delete_planet(planet_id):
    """Elimina un planeta."""

    response, status_code = PlanetService.delete_planet(planet_id)
    return jsonify(response), status_code
