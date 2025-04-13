from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.models.rocket_model import RocketModel
from app.models.rocket import Rocket

class RocketModelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RocketModel

class RocketSchema(SQLAlchemyAutoSchema):
    rocket_model = fields.Nested(RocketModelSchema, dump_only=True)
    id_model = fields.Integer(load_only=True)

    class Meta:
        model = Rocket

rocket_schema = RocketSchema()
rockets_schema = RocketSchema(many=True)