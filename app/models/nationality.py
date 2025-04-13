from app.database import db

class Nationality(db.Model):
    __tablename__ = 'nationalities'

    id_nationality = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
