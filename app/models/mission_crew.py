from app.database import db

class MissionCrew(db.Model):
    __tablename__ = 'mission_crew'

    id_astronaut = db.Column(db.Integer, db.ForeignKey('astronauts.id_astronaut'), primary_key=True)
    id_mission = db.Column(db.Integer, db.ForeignKey('missions.id_mission'), primary_key=True)

    astronaut = db.relationship('Astronaut', backref='mission_crew', lazy=True)
    mission = db.relationship('Mission', backref='mission_crew', lazy=True)