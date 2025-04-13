from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.models.astronaut import Astronaut
from app.models.mission import Mission

class AstronautSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Astronaut

class MissionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Mission

class MissionCrewSchema(SQLAlchemyAutoSchema):
    astronaut = fields.Nested(AstronautSchema, dump_only=True)
    id_astronaut = fields.Integer(load_only=True)

    mission = fields.Nested(MissionSchema, dump_only=True)
    id_mission = fields.Integer(load_only=True)

mission_crew_schema = MissionCrewSchema()
mission_crews_schema = MissionCrewSchema(many=True)