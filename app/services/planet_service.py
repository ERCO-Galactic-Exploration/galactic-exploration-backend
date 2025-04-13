from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from app.repositories.planet_repository import PlanetRepository
from app.schemas.planet_schema import planet_schema, planets_schema
from app.models.planet import Planet

class PlanetService():
    """
    lógica de negocio y transformación de datos.
    """

    @staticmethod
    def list_planets():
        planets = PlanetRepository.get_all()
        return planets_schema.dump(planets) # Serializa la lista de planetas
    
    @staticmethod
    def get_planet_by_id(planet_id):
        planet = PlanetRepository.get_by_id(planet_id)
        
        if not planet:
            return {"error": "Planet not found"}, 404
        
        return planet_schema.dump(planet), 200
    
    @staticmethod
    def create_planet(data):
        try: 
            validated_data = planet_schema.load(data)
            # new_planet = Planet(
            #     name=validated_data["name"],
            #     distance=validated_data["distance"],
            #     id_solar_system=validated_data["id_solar_system"],
            #     id_galaxy=validated_data["id_galaxy"],
            #     id_planet_type=validated_data["id_planet_type"]
            # )

            planet = PlanetRepository.create(validated_data)

            return planet_schema.dump(planet), 201
        
        except ValidationError as err:
            return {"error": err.messages}, 400
        except IntegrityError:
            return {"error": "Invalid foreign key. One or more referenced entities do not exist."}, 400
        except Exception as err:
            return {"error": str(err)}, 500
    
    @staticmethod
    def update_planet(planet_id, data):
        planet = PlanetRepository.get_by_id(planet_id)

        if not planet:
            return {"error": "Planet not found"}, 404

        try: 
            validated_data = planet_schema.load(data, partial=True)
            
            updated_planet = PlanetRepository.update(planet_id, validated_data)
            
            return planet_schema.dump(updated_planet), 200
        
        except ValidationError as err:
            return {"error": err.messages}, 400
        except IntegrityError:
            return {"error": "Invalid foreign key. One or more referenced entities do not exist."}, 400
        except Exception as err:
            return {"error": str(err)}, 500
    
    @staticmethod
    def delete_planet(planet_id):
        planet = PlanetRepository.get_by_id(planet_id)
        
        if not planet:
            return {"error": "Planet not found"}, 404

        try:
            PlanetRepository.delete(planet_id)
            return {"message": "Planet deleted."}, 200
        except IntegrityError:
            return {"error": "Cannot delete planet. It is referenced in another record."}, 400