from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.models.mission_status import MissionStatus
from app.models.rocket import Rocket
from app.models.mission import Mission

class MissionStatusSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = MissionStatus

class RocketSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Rocket

class MissionSchema(SQLAlchemyAutoSchema):
    mission_status = fields.Nested(MissionStatusSchema, dump_only=True)
    id_mission_status = fields.Integer(load_only=True)

    rocket = fields.Nested(RocketSchema, dump_only=True)
    id_rocket = fields.Integer(load_only=True)

    class Meta:
        model = Mission

mission_schema = MissionSchema()
missions_schema = MissionSchema(many=True)