from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from app.repositories.astronaut_repository import AstronautRepository
from app.schemas.astronaut_schema import astronaut_schema, astronauts_schema
from app.models.astronaut import Astronaut

class AstronautService():
    """
    lógica de negocio y transformación de datos.
    """

    @staticmethod
    def list_astronauts():
        astronauts = AstronautRepository.get_all()
        return astronauts_schema.dump(astronauts)
    
    @staticmethod
    def get_astronaut_by_id(astronaut_id):
        astronaut = AstronautRepository.get_by_id(astronaut_id)
        
        if not astronaut:
            return {"error": "Astronaut not found"}, 404
        
        return astronaut_schema.dump(astronaut), 200
    
    @staticmethod
    def create_astronaut(data):
        try: 
            validated_data = astronaut_schema.load(data)
            # print(validated_data)
            astronaut = AstronautRepository.create(validated_data)

            return astronaut_schema.dump(astronaut), 201
        
        except ValidationError as err:
            return {"error": err.messages}, 400
        except IntegrityError:
            return {"error": "Invalid foreign key. One or more referenced entities do not exist."}, 400
        except Exception as err:
            return {"error": str(err)}, 500
    
    @staticmethod
    def update_astronaut(astronaut_id, data):
        astronaut = AstronautRepository.get_by_id(astronaut_id)

        if not astronaut:
            return {"error": "Astronaut not found"}, 404

        try: 
            validated_data = astronaut_schema.load(data, partial=True)
            
            updated_astronaut = AstronautRepository.update(astronaut_id, validated_data)
            
            return astronaut_schema.dump(updated_astronaut), 200
        
        except ValidationError as err:
            return {"error": err.messages}, 400
        except IntegrityError:
            return {"error": "Invalid foreign key. One or more referenced entities do not exist."}, 400
        except Exception as err:
            return {"error": str(err)}, 500
    
    @staticmethod
    def delete_astronaut(astronaut_id):
        astronaut = AstronautRepository.get_by_id(astronaut_id)
        
        if not astronaut:
            return {"error": "Astronaut not found"}, 404

        try:
            AstronautRepository.delete(astronaut_id)
            return {"message": "Astronaut deleted."}, 200
        except IntegrityError:
            return {"error": "Cannot delete astronaut. It is referenced in another record."}, 400