from app.database import db
from app.models.astronaut_specialties import AstronautSpecialty
from app.models.nationality import Nationality

class Astronaut(db.Model):
    __tablename__ = 'astronauts'

    id_astronaut = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    id_specialty = db.Column(db.Integer, db.ForeignKey('astronaut_specialties.id_specialty'), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    id_nationality = db.Column(db.Integer, db.ForeignKey('nationalities.id_nationality'), nullable=False)

    specialty = db.relationship('AstronautSpecialty', backref='astronauts', lazy=True)
    nationality = db.relationship('Nationality', backref='astronauts', lazy=True)
