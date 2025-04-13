from app.database import db

class Mission(db.Model):
    __tablename__ = 'missions'

    id_mission = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    id_mission_status = db.Column(db.Integer, db.ForeignKey('mission_statuses.id_mission_status'), nullable=False)
    id_rocket = db.Column(db.Integer, db.ForeignKey('rockets.id_rocket'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)

    mission_status = db.relationship('MissionStatus', backref='missions', lazy=True)
    rocket = db.relationship('Rocket', backref='missions', lazy=True)
