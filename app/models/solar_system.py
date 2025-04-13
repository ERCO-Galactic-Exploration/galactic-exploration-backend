from app.database import db

class SolarSystem(db.Model):
    __tablename__ = 'solar_systems'

    id_solar_system = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    # planets = db.relationship('Planet', backref='solar_system_rel', lazy=True)