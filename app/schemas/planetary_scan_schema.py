from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.models.planet import Planet
from app.schemas.mission_schema import MissionSchema
from app.schemas.planet_schema import PlanetSchema
from app.models.planetary_scan import PlanetaryScan

# class PlanetSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = Planet

class PlanetaryScanSchema(SQLAlchemyAutoSchema):
    planet = fields.Nested(PlanetSchema, dump_only=True)
    id_planet = fields.Integer(load_only=True)

    mission = fields.Nested(MissionSchema,dump_only=True)
    id_mission = fields.Integer(load_only=True)

    class Meta:
        model = PlanetaryScan

planetary_scan_schema = PlanetaryScanSchema()
planetary_scans_schema = PlanetaryScanSchema(many=True) # Para listas de escaneos planetarios

