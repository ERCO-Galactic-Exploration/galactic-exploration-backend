from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from app.repositories.mission_repository import MissionRepository
from app.schemas.mission_schema import mission_schema, missions_schema
from app.models.mission import Mission

class MissionService():
    """
    lógica de negocio y transformación de datos.
    """

    @staticmethod
    def list_missions():
        missions = MissionRepository.get_all()
        return missions_schema.dump(missions)
    
    @staticmethod
    def get_mission_by_id(mission_id):
        mission = MissionRepository.get_by_id(mission_id)
        
        if not mission:
            return {"error": "Mission not found"}, 404
        
        return mission_schema.dump(mission), 200
    
    @staticmethod
    def create_mission(data):
        try: 
            validated_data = mission_schema.load(data)

            mission = MissionRepository.create(validated_data)

            return mission_schema.dump(mission), 201
        
        except ValidationError as err:
            return {"error": err.messages}, 400
        except IntegrityError:
            return {"error": "Invalid foreign key. One or more referenced entities do not exist."}, 400
        except Exception as err:
            return {"error": str(err)}, 500
    
    @staticmethod
    def update_mission(mission_id, data):
        mission = MissionRepository.get_by_id(mission_id)

        if not mission:
            return {"error": "Mission not found"}, 404

        try: 
            validated_data = mission_schema.load(data, partial=True)
            
            updated_mission = MissionRepository.update(mission_id, validated_data)
            
            return mission_schema.dump(updated_mission), 200
        
        except ValidationError as err:
            return {"error": err.messages}, 400
        except IntegrityError:
            return {"error": "Invalid foreign key. One or more referenced entities do not exist."}, 400
        except Exception as err:
            return {"error": str(err)}, 500
    
    @staticmethod
    def delete_mission(mission_id):
        mission = MissionRepository.get_by_id(mission_id)
        
        if not mission:
            return {"error": "Mission not found"}, 404

        try:
            MissionRepository.delete(mission_id)
            return {"message": "Mission deleted."}, 200
        except IntegrityError:
            return {"error": "Cannot delete mission. It is referenced in another record."}, 400