from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import user_schema, users_schema
from app.models.user import UserModel, generate_password_hash, check_password_hash

class UserService():
    """
    lógica de negocio y transformación de datos.
    """

    @staticmethod
    def get_user(user_email, password):
        user = UserRepository.get_by_id(user_email)
        
        if not user:
            return {"error": "User not found"}, 404

        if user and user.check_password(password):
            return user_schema.dump(user), 200
        else: 
            return {"error": "Invalid credentials"}, 401
        
    
    @staticmethod
    def create_user(data):
        try:
            # print('data: ', data)
            validated_data = user_schema.load(data)

            hashed_password = generate_password_hash(validated_data["password"])
            print('hashed_password: ', hashed_password)
            validated_data["password"] = hashed_password
            user = UserRepository.create(validated_data)
            # user.set_password(validated_data["password"])

            return user_schema.dump(user), 201
        
        except ValidationError as err:
            return {"error": err.messages}, 400
        except IntegrityError:  
            return {"error": "Invalid foreign key. One or more referenced entities do not exist."}, 400
        except Exception as err:
            return {"error": str(err)}, 500
        