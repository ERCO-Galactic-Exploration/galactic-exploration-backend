from app.database import db
from app.models.mission import Mission

class MissionRepository:
    """
    consultas a la base de datos.
    """

    @staticmethod
    def get_all():
        return Mission.query.all()
    
    @staticmethod
    def get_by_id(mission_id):
        return Mission.query.get(mission_id)

    @staticmethod
    def create(mission_data):
        mission = Mission(**mission_data)
        db.session.add(mission)
        db.session.commit()
        return mission

    @staticmethod
    def update(mission_id, mission_data):
        mission = Mission.query.get(mission_id)
        if not mission:
            return None
        for key, value in mission_data.items():
            setattr(mission, key, value)
        db.session.commit()
        return mission

    @staticmethod
    def delete(mission_id):
        mission = Mission.query.get(mission_id)
        if not mission:
            return False
        db.session.delete(mission)
        db.session.commit()
        return True