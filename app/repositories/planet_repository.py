from app.database import db
from app.models.planet import Planet

class PlanetRepository:
    """
    consultas a la base de datos.
    """

    @staticmethod
    def get_all():
        return Planet.query.all()
    
    @staticmethod
    def get_by_id(planet_id):
        return Planet.query.get(planet_id)

    @staticmethod
    def create(planet_data):
        planet = Planet(**planet_data)
        db.session.add(planet)
        db.session.commit()
        return planet

    @staticmethod
    def update(planet_id, planet_data):
        planet = Planet.query.get(planet_id)
        if not planet:
            return None
        for key, value in planet_data.items():
            setattr(planet, key, value)
        db.session.commit()
        return planet

    @staticmethod
    def delete(planet_id):
        planet = Planet.query.get(planet_id)
        if not planet:
            return False
        db.session.delete(planet)
        db.session.commit()
        return True