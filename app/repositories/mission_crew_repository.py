from app.database import db
from app.models.mission_crew import MissionCrew

class MissionCrewRepository:

    @staticmethod
    def existing_crew(mission_id, astronaut_id):
        return MissionCrew.query.filter_by(id_mission=mission_id, id_astronaut=astronaut_id).first() is not None

    @staticmethod
    def assign_crew(mission_id, astronaut_id):
        #existing = MissionCrew.query.filter_by(id_mission=mission_id, id_astronaut=astronaut_id).first()
        existing = MissionCrewRepository.existing_crew(mission_id, astronaut_id)
        if existing:
            return None
        
        mission_crew = MissionCrew(id_mission=mission_id, id_astronaut=astronaut_id)
        db.session.add(mission_crew)
        db.session.commit()
        return mission_crew
    
    @staticmethod
    def get_by_mission(mission_id):
        return MissionCrew.query.filter_by(id_mission=mission_id).all()
    
    @staticmethod
    def get_by_astronaut(astronaut_id):
        return MissionCrew.query.filter_by(id_astronaut=astronaut_id).all()
    
    @staticmethod
    def unassign_crew(mission_id, astronaut_id):
        mission_crew = MissionCrew.query.filter_by(id_mission=mission_id, id_astronaut=astronaut_id).first()
        if not mission_crew:
            return False
        db.session.delete(mission_crew)
        db.session.commit()
        return True