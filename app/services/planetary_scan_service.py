from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from app.models.planet import Planet
from app.models.mission import Mission
from app.repositories.planetary_scan_repository import PlanetaryScanRepository
from app.repositories.planet_repository import PlanetRepository
from app.schemas.planetary_scan_schema import planetary_scan_schema, planetary_scans_schema


class PlanetaryScanService():
    """
    lógica de negocio y transformación de datos.
    """

    @staticmethod
    def create_scan(planet_id, data):

        try:
            planet = Planet.query.get(planet_id)
            if not planet:
                return {"error": "Planet not found"}, 404
            mission_id = data.get('id_mission')
            if not mission_id:
                return {"error": "Missing id_mission."}, 400
            
            mission = Mission.query.get(mission_id)
            if not mission:
                return {"error": "Mission not found"}, 404
            
            data["id_planet"] = planet_id
            validated_data = planetary_scan_schema.load(data)

            scan = PlanetaryScanRepository.create(validated_data)
            return planetary_scan_schema.dump(scan), 201
        
        except ValidationError as err:
            return {"error": err.messages}, 400
        except IntegrityError:
            return {"error": "Invalid foreign key. One or more referenced entities do not exist."}, 400
        except Exception as err:
            return {"error": str(err)}, 500
        
    @staticmethod
    def list_scans_by_planet(planet_id):
        planet = Planet.query.get(planet_id)
        if not planet:
            return {"error": "Planet not found"}, 404
        
        scans = PlanetaryScanRepository.get_by_planet(planet_id)
        return planetary_scans_schema.dump(scans), 200
    
    @staticmethod
    def get_scan_by_mission(planet_id, mission_id):
        planet = Planet.query.get(planet_id)
        print('planet: ', planet)
        if not planet:
            return {"error": "Planet not found"}, 404
        
        mission = Mission.query.get(mission_id)
        if not mission:
            return {"error": "Mission not found"}, 404
        
        scan = PlanetaryScanRepository.get_by_id(planet_id, mission_id)
        if not scan:
            return {"error": "Scan not found"}, 404
        
        return planetary_scan_schema.dump(scan), 200
    
    @staticmethod
    def update_scan(planet_id, mission_id, data):
        scan = PlanetaryScanRepository.get_by_id(planet_id, mission_id)
        print('scan: ', scan)
        if not scan:
            return {"error": "Scan not found"}, 404
        
        try:
            validated_data = planetary_scan_schema.load(data, partial=True)
            
            updated_scan = PlanetaryScanRepository.update(planet_id, mission_id, validated_data)
            
            return planetary_scan_schema.dump(updated_scan), 200
        except ValidationError as err:
            return {"error": err.messages}, 400
        except IntegrityError:
            return {"error": "Invalid foreign key. One or more referenced entities do not exist."}, 400
        except Exception as err:
            return {"error": str(err)}, 500
        
    
    @staticmethod
    def delete_scan(planet_id, mission_id):
        scan = PlanetaryScanRepository.get_by_id(planet_id, mission_id)
        
        if not scan:
            return {"error": "Scan not found"}, 404

        try:
            PlanetaryScanRepository.delete(planet_id, mission_id)
            return {"message": "Scan deleted successfully"}, 200
        except Exception as err:
            return {"error": str(err)}, 500