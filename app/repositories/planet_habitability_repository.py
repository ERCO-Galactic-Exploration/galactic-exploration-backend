from app.models.planet_habitability_view import PlanetHabitabilityView

class PlanetHabitabilityRepository:
    """
    Repositorio para consultas de habitabilidad planetaria.
    """

    @staticmethod
    def get_by_id(planet_id):
        return PlanetHabitabilityView.query.filter_by(id_planet=planet_id).all()
    
    @staticmethod
    def get_all():
        return PlanetHabitabilityView.query.all()
    
    # @staticmethod
    # def get_habitability():
    #     habitability = PlanetHabitabilityView.query.all()
    #     return [{
    #         "id_planet": habitability.id_planet,
    #         "name": habitability.name,
    #         "distance": habitability.distance,
    #         "ihp": habitability.ihp,
    #     }]