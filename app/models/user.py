from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    __tablename__ = 'users'

    id_user = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name_1 = db.Column(db.String(50), nullable=False)
    last_name_2 = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)
    id_role = db.Column(db.Integer, db.ForeignKey('roles.id_role'), nullable=False)

    role = db.relationship('RoleModel', backref='users')

    def set_password(self, password_hash):
        self.password = generate_password_hash(password_hash)

    def check_password(self, password_hash):
        return check_password_hash(self.password, password_hash)