from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.auth import role_required
from app.services.planet_habitability_service import PlanetHabitabilityService

"""
    Define las rutas de la API y maneja las peticiones HTTP.
"""

planet_habitability_bp = Blueprint('planet_habitability', __name__)

@planet_habitability_bp.route('/planets/<int:planet_id>/habitability', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Mission director', 'Planetary scientist')
def get_habitability_by_planet(planet_id):
    """
    Obtiene el índice de habitabilidad de un planeta por su ID.
    """

    message, status_code = PlanetHabitabilityService.get_habitability_by_planet(planet_id)
    return jsonify(message), status_code

@planet_habitability_bp.route('/planets/ranking', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Planetary scientist')
def get_planet_ranking():
    """
    Obtiene el ranking del índice de habitabilidad de los planetas.
    """

    message, status_code = PlanetHabitabilityService.get_planet_ranking()
    # print(message)
    return jsonify(message), status_code


@planet_habitability_bp.route('/planets/tendencies', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Planetary scientist')
def get_planet_tendencies():
    """
    Obtiene las tendencias de habitabilidad de los planetas.
    """

    message, status_code = PlanetHabitabilityService.get_planet_tendences()
    return jsonify(message), status_code