from app.models.mission import Mission
from app.models.astronaut import Astronaut
from app.schemas.mission_crew_schema import mission_crew_schema, mission_crews_schema
from app.repositories.mission_crew_repository import MissionCrewRepository


class MissionCrewService():
    """
    lógica de negocio y transformación de datos.
    """

    @staticmethod
    def assign_astronaut_to_mission(mission_id, data):

        ids_astronaut = data.get('id_astronaut')

        if not ids_astronaut:
            return {"error": "Missing id_astronaut."}, 400
        
        if isinstance(ids_astronaut, int):
            ids_astronaut = [ids_astronaut]

        if not isinstance(ids_astronaut, list):
            return {"error": "id_astronaut must be an integer or a list of integers."}, 400
        
        mission = Mission.query.get(mission_id)
        if not mission:
            return {"error": "Mission not found"}, 404
        
        assigned = []
        skipped = []

        for astronaut_id in ids_astronaut:
            astronaut = Astronaut.query.get(astronaut_id)
            if not astronaut:
                return {"error": "Astronaut not found"}, 404
        
            result = MissionCrewRepository.assign_crew(mission_id, astronaut_id)
            if not result:
                skipped.append(astronaut_id)
            else:
                assigned.append(astronaut_id)
            
        #return mission_crew_schema.dump(result), 201
        return {
            "message": "Astronauts assigned successfully",
            "assigned": assigned,
            "skipped_already_assigned": skipped
        }, 201
    
    @staticmethod
    def list_astronauts_for_mission(mission_id):
        mission = Mission.query.get(mission_id)

        if not mission:
            return {"error": "Mission not found"}, 404

        crew = MissionCrewRepository.get_by_mission(mission_id)
        return mission_crews_schema.dump(crew), 200
    
    @staticmethod
    def list_missions_by_astronauts(astronaut_id):
        astronaut = Astronaut.query.get(astronaut_id)

        if not astronaut:
            return {"error": "Astronaut not found"}, 404

        crew = MissionCrewRepository.get_by_astronaut(astronaut_id)
        return mission_crews_schema.dump(crew), 200
    
    @staticmethod
    def unassign_astronaut_from_mission(mission_id, astronaut_id):
        mission = Mission.query.get(mission_id)
        astronaut = Astronaut.query.get(astronaut_id)

        if not mission:
            return {"error": "Mission not found"}, 404
        
        if not astronaut:
            return {"error": "Astronaut not found"}, 404
        
        result = MissionCrewRepository.unassign_crew(mission_id, astronaut_id)

        if not result:
            return {"error": "Astronaut not assigned to this mission"}, 400
        
        return {"message": "Astronaut unassigned successfully"}, 200