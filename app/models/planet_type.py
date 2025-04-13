from app.database import db

class PlanetType(db.Model):
    __tablename__ = 'planet_types'

    id_planet_type = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False, unique=True)

    # planets = db.relationship('Planet', backref='planet_type_rel', lazy=True)