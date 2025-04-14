from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate
from app.models.planet import Planet
from app.schemas.mission_schema import MissionSchema
from app.schemas.planet_schema import PlanetSchema
from app.models.planetary_scan import PlanetaryScan

class PlanetaryScanSchema(SQLAlchemyAutoSchema):
    planet = fields.Nested(PlanetSchema, dump_only=True)
    id_planet = fields.Integer(load_only=True)
    mission = fields.Nested(MissionSchema,dump_only=True)
    id_mission = fields.Integer(load_only=True)

    temperature = fields.Float(
        required=True,
        validate=validate.Range(min=0, max=1, error="Temperature must be between 0 and 1.")
    )
    atmosphere  = fields.Float(
        required=True,
        validate=validate.Range(min=0, max=1, error="Atmosphere  must be between 0 and 1.")
    )
    resources = fields.Float(
        required=True,
        validate=validate.Range(min=0, max=1, error="Resources must be between 0 and 1.")
    )

    class Meta:
        model = PlanetaryScan

planetary_scan_schema = PlanetaryScanSchema()
planetary_scans_schema = PlanetaryScanSchema(many=True)

