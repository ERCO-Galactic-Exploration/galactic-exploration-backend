from app.database import db
from app.models.planetary_scan import PlanetaryScan

class PlanetaryScanRepository:
    """
    consultas a la base de datos.
    """

    @staticmethod
    def create(scan_data):
        scan = PlanetaryScan(**scan_data)
        db.session.add(scan)
        db.session.commit()
        return scan
    
    @staticmethod
    def get_by_planet(planet_id):
        return PlanetaryScan.query.filter_by(id_planet=planet_id).all()