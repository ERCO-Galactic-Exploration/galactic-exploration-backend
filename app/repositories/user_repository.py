from app.database import db
from app.models.user import UserModel

class UserRepository:

    @staticmethod
    def get_by_id(user_email):
        return UserModel.query.filter_by(email=user_email).first()
    
    @staticmethod
    def create(user_data):
        user = UserModel(**user_data)
        db.session.add(user)
        db.session.commit()
        return user
    
    