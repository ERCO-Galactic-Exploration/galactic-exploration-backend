from app.database import db

class RocketModel(db.Model):
    __tablename__ = 'rocket_models'

    id_model = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
