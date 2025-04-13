from app.database import db
from app.models.rocket_model import RocketModel

class Rocket(db.Model):
    __tablename__ = 'rockets'

    id_rocket = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    id_model = db.Column(db.Integer, db.ForeignKey('rocket_models.id_model'), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    autonomy = db.Column(db.Numeric(10, 6), nullable=False)

    rocket_model = db.relationship('RocketModel', backref='rockets', lazy=True)
