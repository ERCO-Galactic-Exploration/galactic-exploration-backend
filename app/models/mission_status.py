from app.database import db

class MissionStatus(db.Model):
    __tablename__ = 'mission_statuses'

    id_mission_status = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
