from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.auth import role_required
from app.services.planet_habitability_service import PlanetHabitabilityService

planet_habitability_bp = Blueprint('planet_habitability', __name__)

@planet_habitability_bp.route('/planets/<int:planet_id>/habitability', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Mission director', 'Planetary scientist')
def get_habitability_by_planet(planet_id):
    """
    Obtiene el índice de habitabilidad de un planeta por su ID.
    ---
    tags:
      - Planet Habitabilities
    security:
      - Bearer: []
    parameters:
      - name: planet_id
        in: path
        type: integer
        required: true
        description: ID del planeta
    responses:
      200:
        description: Índice de habitabilidad del planeta
        schema:
          type: object
          properties:
            planet_id:
              type: integer
            habitability_index:
              type: number
              format: float
            example:
              planet_id: 1
              habitability_index: 0.87
      404:
        description: Planeta no encontrado
    """
    message, status_code = PlanetHabitabilityService.get_habitability_by_planet(planet_id)
    return jsonify(message), status_code


@planet_habitability_bp.route('/planets/ranking', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Planetary scientist')
def get_planet_ranking():
    """
    Obtiene el ranking del índice de habitabilidad de los planetas.
    ---
    tags:
      - Planet Habitabilities
    security:
      - Bearer: []
    responses:
      200:
        description: Ranking de los planetas por índice de habitabilidad
        schema:
          type: array
          items:
            type: object
            properties:
              planet_id:
                type: integer
              name:
                type: string
              habitability_index:
                type: number
                format: float
            example:
              planet_id: 1
              name: "Tierra"
              habitability_index: 0.92
      500:
        description: Error interno del servidor
    """
    message, status_code = PlanetHabitabilityService.get_planet_ranking()
    return jsonify(message), status_code


@planet_habitability_bp.route('/planets/tendencies', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Planetary scientist')
def get_planet_tendencies():
    """
    Obtiene las tendencias de habitabilidad de los planetas.
    ---
    tags:
      - Planet Habitabilities
    security:
      - Bearer: []
    responses:
      200:
        description: Tendencias de habitabilidad de los planetas
        schema:
          type: array
          items:
            type: object
            properties:
              planet_id:
                type: integer
              name:
                type: string
              habitability_trend:
                type: string
            example:
              planet_id: 2
              name: "Marte"
              habitability_trend: "Mejorando"
      500:
        description: Error interno del servidor
    """
    message, status_code = PlanetHabitabilityService.get_planet_tendences()
    return jsonify(message), status_code