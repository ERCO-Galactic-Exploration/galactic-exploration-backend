from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from app.repositories.rocket_repository import RocketRepository
from app.schemas.rocket_schema import rocket_schema, rockets_schema
from app.models.rocket import Rocket

class RocketService():
    """
    lógica de negocio y transformación de datos.
    """

    @staticmethod
    def list_rockets():
        rockets = RocketRepository.get_all()
        return rockets_schema.dump(rockets)
    
    @staticmethod
    def get_rocket_by_id(rocket_id):
        rocket = RocketRepository.get_by_id(rocket_id)
        
        if not rocket:
            return {"error": "Rocket not found"}, 404
        
        return rocket_schema.dump(rocket), 200
    
    @staticmethod
    def create_rocket(data):
        try: 
            validated_data = rocket_schema.load(data)
            
            rocket = RocketRepository.create(validated_data)

            return rocket_schema.dump(rocket), 201
        
        except ValidationError as err:
            return {"error": err.messages}, 400
        except IntegrityError:
            return {"error": "Invalid foreign key. One or more referenced entities do not exist."}, 400
        except Exception as err:
            return {"error": str(err)}, 500
    
    @staticmethod
    def update_rocket(rocket_id, data):
        rocket = RocketRepository.get_by_id(rocket_id)

        if not rocket:
            return {"error": "Rocket not found"}, 404

        try: 
            validated_data = rocket_schema.load(data, partial=True)
            
            updated_rocket = RocketRepository.update(rocket_id, validated_data)
            
            return rocket_schema.dump(updated_rocket), 200
        
        except ValidationError as err:
            return {"error": err.messages}, 400
        except IntegrityError:
            return {"error": "Invalid foreign key. One or more referenced entities do not exist."}, 400
        except Exception as err:
            return {"error": str(err)}, 500
    
    @staticmethod
    def delete_rocket(rocket_id):
        rocket = RocketRepository.get_by_id(rocket_id)
        
        if not rocket:
            return {"error": "Rocket not found"}, 404

        try:
            RocketRepository.delete(rocket_id)
            return {"message": "Rocket deleted."}, 200
        except IntegrityError:
            return {"error": "Cannot delete rocket. It is referenced in another record."}, 400