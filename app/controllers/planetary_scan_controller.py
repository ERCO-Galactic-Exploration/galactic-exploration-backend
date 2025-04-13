from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils.auth import role_required
from app.services.planetary_scan_service import PlanetaryScanService


"""
    Define las rutas de la API y maneja las peticiones HTTP.
"""

planetary_scan_bp = Blueprint('planetary_scan', __name__)

@planetary_scan_bp.route('/planets/<int:planet_id>/scans', methods=['POST'])
@jwt_required()
@role_required('Admin', 'Planetary scientist')
def create_scan(planet_id):
    """
    Crea un escaneo planetario.
    """

    data = request.json
    
    message, status_code = PlanetaryScanService.create_scan(planet_id, data)
    print('message: ', message)
    return jsonify(message), status_code

@planetary_scan_bp.route('/planets/<int:planet_id>/scans', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Mission director', 'Planetary scientist', 'Flight operator')
def list_scans_by_planet(planet_id):
    """
    Lista los escaneos de un planeta.
    """

    message, status_code = PlanetaryScanService.list_scans_by_planet(planet_id)
    return jsonify(message), status_code


@planetary_scan_bp.route('/planets/<int:planet_id>/scans/<int:mission_id>', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Planetary scientist')
def get_scan_by_mission(planet_id, mission_id):
    """
    Obtiene un escaneo planetario por ID de misión.
    """

    message, status_code = PlanetaryScanService.get_scan_by_mission(planet_id, mission_id)
    return jsonify(message), status_code


@planetary_scan_bp.route('/planets/<int:planet_id>/scans/<int:mission_id>', methods=['PUT'])
@jwt_required()
@role_required('Admin', 'Planetary scientist')
def update_scan(planet_id, mission_id):
    """
    Actualiza un escaneo planetario.
    """

    data = request.json
    message, status_code = PlanetaryScanService.update_scan(planet_id, mission_id, data)
    return jsonify(message), status_code

@planetary_scan_bp.route('/planets/<int:planet_id>/scans/<int:mission_id>', methods=['DELETE'])
@jwt_required()
@role_required('Admin', 'Planetary scientist')
def delete_scan(planet_id, mission_id):
    """
    Elimina un escaneo planetario.
    """

    message, status_code = PlanetaryScanService.delete_scan(planet_id, mission_id)
    return jsonify(message), status_code
