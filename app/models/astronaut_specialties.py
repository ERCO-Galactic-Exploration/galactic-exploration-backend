from app.database import db

class AstronautSpecialty(db.Model):
    __tablename__ = 'astronaut_specialties'

    id_specialty = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)