from app.database import db
from app.models.astronaut import Astronaut

class AstronautRepository:
    """
    consultas a la base de datos.
    """

    @staticmethod
    def get_all():
        return Astronaut.query.all()
    
    @staticmethod
    def get_by_id(astronaut_id):
        return Astronaut.query.get(astronaut_id)

    @staticmethod
    def create(astronaut_data):
        astronaut = Astronaut(**astronaut_data)
        db.session.add(astronaut)
        db.session.commit()
        return astronaut

    @staticmethod
    def update(astronaut_id, astronaut_data):
        astronaut = Astronaut.query.get(astronaut_id)
        if not astronaut:
            return None
        for key, value in astronaut_data.items():
            setattr(astronaut, key, value)
        db.session.commit()
        return astronaut

    @staticmethod
    def delete(astronaut_id):
        astronaut = Astronaut.query.get(astronaut_id)
        if not astronaut:
            return False
        db.session.delete(astronaut)
        db.session.commit()
        return True