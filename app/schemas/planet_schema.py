from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.models.planet import Planet
from app.models.solar_system import SolarSystem
from app.models.galaxy import Galaxy
from app.models.planet_type import PlanetType

class SolarSystemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SolarSystem

class GalaxySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Galaxy

class PlanetTypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PlanetType

class PlanetSchema(SQLAlchemyAutoSchema):
    solar_system = fields.Nested(SolarSystemSchema, dump_only=True)
    id_solar_system = fields.Integer(load_only=True)

    galaxy = fields.Nested(GalaxySchema, dump_only=True)
    id_galaxy = fields.Integer(load_only=True)
    
    planet_type = fields.Nested(PlanetTypeSchema, dump_only=True)
    id_planet_type= fields.Integer(load_only=True)

    class Meta:
        model = Planet
        # include_fk = True
        # load_instance = True #devuelva instancias del modelo

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True) # Para listas de planetas