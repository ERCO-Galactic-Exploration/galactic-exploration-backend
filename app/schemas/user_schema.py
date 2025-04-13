from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.models.role import RoleModel
from app.models.user import UserModel

class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RoleModel

class UserSchema(SQLAlchemyAutoSchema):
    role_model = fields.Nested(RoleSchema, dump_only=True)
    id_role = fields.Integer(load_only=True)

    password = fields.Str(load_only=True)
    
    class Meta:
        model = UserModel

user_schema = UserSchema()
users_schema = UserSchema(many=True)