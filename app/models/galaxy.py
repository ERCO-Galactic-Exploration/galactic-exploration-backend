from app.database import db

class Galaxy(db.Model):
    __tablename__ = 'galaxies'

    id_galaxy = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    # planets = db.relationship('Planet', backref='galaxy_rel', lazy=True)