from app.database import db

class PlanetaryScan(db.Model):
    """
    Modelo de datos para el escaneo planetario.
    """

    __tablename__ = 'planetary_scans'
    
    # id_planetary_scanning = db.Column(db.Integer, primary_key=True)
    id_planet = db.Column(db.Integer, db.ForeignKey('planets.id_planet'), primary_key=True)
    id_mission = db.Column(db.Integer, db.ForeignKey('missions.id_mission'), primary_key=True)
    scanning_date = db.Column(db.Date, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    atmosphere = db.Column(db.Float, nullable=False)
    resources = db.Column(db.Float, nullable=False)

    planet = db.relationship('Planet', backref='planetary_scans')
    mission = db.relationship('Mission', backref='planetary_scans')