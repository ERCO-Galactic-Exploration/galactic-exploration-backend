from app.database import db

class PlanetHabitabilityView(db.Model):

    __tablename__ = 'planet_habitability_view'
    __table_args__ = {'extend_existing': True}  # Para evitar conflictos

    id_mission = db.Column(db.Integer, primary_key=True)
    id_planet = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    distance = db.Column(db.Integer)
    scanning_date = db.Column(db.Date)
    ihp = db.Column(db.Float)