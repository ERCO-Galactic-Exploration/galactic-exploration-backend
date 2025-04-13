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
    
    @staticmethod
    def get_by_id(planet_id, mission_id):
        return PlanetaryScan.query.filter_by(id_planet=planet_id, id_mission=mission_id).first()
    
    @staticmethod
    def update(planet_id, mission_id, scan_data):
        scan = PlanetaryScan.query.filter_by(id_planet=planet_id, id_mission=mission_id).first()

        if not scan:
            return None
        for key, value in scan_data.items():
            setattr(scan, key, value)
        db.session.commit()
        return scan
    
    @staticmethod
    def delete(planet_id, mission_id):
        scan = PlanetaryScan.query.filter_by(id_planet=planet_id, id_mission=mission_id).first()
        if not scan:
            return False
        db.session.delete(scan)
        db.session.commit()
        return True