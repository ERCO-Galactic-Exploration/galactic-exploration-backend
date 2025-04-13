from app.database import db
from app.models.rocket import Rocket

class RocketRepository:
    """
    consultas a la base de datos.
    """

    @staticmethod
    def get_all():
        return Rocket.query.all()
    
    @staticmethod
    def get_by_id(rocket_id):
        return Rocket.query.get(rocket_id)

    @staticmethod
    def create(rocket_data):
        rocket = Rocket(**rocket_data)
        db.session.add(rocket)
        db.session.commit()
        return rocket

    @staticmethod
    def update(rocket_id, rocket_data):
        rocket = Rocket.query.get(rocket_id)
        if not rocket:
            return None
        for key, value in rocket_data.items():
            setattr(rocket, key, value)
        db.session.commit()
        return rocket

    @staticmethod
    def delete(rocket_id):
        rocket = Rocket.query.get(rocket_id)
        if not rocket:
            return False
        db.session.delete(rocket)
        db.session.commit()
        return True