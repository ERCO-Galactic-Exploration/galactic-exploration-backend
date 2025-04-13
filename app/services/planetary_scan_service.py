from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from app.models.planet import Planet
from app.models.mission import Mission
from app.repositories.planetary_scan_repository import PlanetaryScanRepository
# from app.services.planet_service import PlanetService
from app.schemas.planetary_scan_schema import planetary_scan_schema, planetary_scans_schema


class PlanetaryScanService():
    """
    lógica de negocio y transformación de datos.
    """

    @staticmethod
    def create_scan(planet_id, data):

        try:
            # print('planet_id: ', planet_id)
            # print('data: ', data)
            planet = Planet.query.get(planet_id)
            if not planet:
                return {"error": "Planet not found"}, 404
            # print('planet: ', planet)
            mission_id = data.get('id_mission')
            if not mission_id:
                return {"error": "Missing id_mission."}, 400
            
            mission = Mission.query.get(mission_id)
            if not mission:
                return {"error": "Mission not found"}, 404
            # print('mission: ', mission)
            
            data["id_planet"] = planet_id
            print('data: ', data)
            validated_data = planetary_scan_schema.load(data)
            print('validated_data: ', validated_data)

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