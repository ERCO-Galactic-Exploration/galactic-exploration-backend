from app.database import db

class RoleModel(db.Model):
    __tablename__ = 'roles'
    
    id_role = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)