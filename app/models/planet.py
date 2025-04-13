from app.database import db
from app.models.planet_type import PlanetType
from app.models.galaxy import Galaxy
from app.models.solar_system import SolarSystem

class Planet(db.Model):
    __tablename__ = 'planets'

    id_planet = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    id_solar_system = db.Column(db.Integer, db.ForeignKey('solar_systems.id_solar_system'), nullable=False)
    id_galaxy = db.Column(db.Integer, db.ForeignKey('galaxies.id_galaxy'), nullable=False)
    id_planet_type = db.Column(db.Integer, db.ForeignKey('planet_types.id_planet_type'), nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    
    solar_system = db.relationship('SolarSystem', backref='planets', lazy=True)
    galaxy = db.relationship('Galaxy', backref='planets', lazy=True)
    planet_type = db.relationship('PlanetType', backref='planets', lazy=True)

    # def to_dict(self):
    #     """Convierte el objeto en un diccionario serializable."""

    #     return {
    #         "id_planet": self.id_planet,
    #         "name": self.name,
    #         "id_solar_system": self.id_solar_system,
    #         "id_galaxy": self.id_galaxy,
    #         "distance": self.distance,
    #         "id_planet_type": self.id_planet_type
    #     }