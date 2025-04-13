from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.models.astronaut_specialties import AstronautSpecialty
from app.models.nationality import Nationality
from app.models.astronaut import Astronaut

class SpecialtySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AstronautSpecialty

class NationalitySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Nationality

class AstronautSchema(SQLAlchemyAutoSchema):
    specialty = fields.Nested(SpecialtySchema, dump_only=True)
    id_specialty = fields.Integer(load_only=True)

    nationality = fields.Nested(NationalitySchema, dump_only=True)
    id_nationality = fields.Integer(load_only=True)

    class Meta:
        model = Astronaut

astronaut_schema = AstronautSchema()
astronauts_schema = AstronautSchema(many=True)