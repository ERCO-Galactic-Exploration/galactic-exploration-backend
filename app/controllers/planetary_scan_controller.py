from flask import Blueprint, request, jsonify
from app.services.planetary_scan_service import PlanetaryScanService


"""
    Define las rutas de la API y maneja las peticiones HTTP.
"""

planetary_scan_bp = Blueprint('planetary_scan', __name__)

@planetary_scan_bp.route('/planets/<int:planet_id>/scans', methods=['POST'])
def create_scan(planet_id):
    """
    Crea un escaneo planetario.
    """

    data = request.json
    
    message, status_code = PlanetaryScanService.create_scan(planet_id, data)
    print('message: ', message)
    return jsonify(message), status_code

@planetary_scan_bp.route('/planets/<int:planet_id>/scans', methods=['GET'])
def list_scans_by_planet(planet_id):
    """
    Lista los escaneos de un planeta.
    """

    message, status_code = PlanetaryScanService.list_scans_by_planet(planet_id)
    return jsonify(message), status_code
