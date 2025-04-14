from flask import Blueprint, request, jsonify, make_response
from app.services.user_service import UserService
from app.models.user import UserModel
from flask_jwt_extended import create_access_token, jwt_required, unset_jwt_cookies, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/register', methods=['POST'])
def register():
    """Registra un nuevo usuario."""

    data = request.json
    response, status_code = UserService.create_user(data)
    return jsonify(response), status_code


@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400
    
    user_information, status_code = UserService.get_user(email, password)
    print('user_information: ', user_information)
    if status_code == 200:
        email_validated = user_information.get('email')
        role = user_information.get('role')
        access_token = create_access_token(identity=email_validated, additional_claims={"role": role.get('name')})
        response = make_response(jsonify({"message": "Login successful", "status_code": 200}), 200)
        response.set_cookie('access_token', access_token, httponly=True, samesite='None', secure=True)
        return response
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/auth/me', methods=['GET'])
@jwt_required()
def get_current_user():
    # print('request: ', request)
    current_user = get_jwt_identity()
    return jsonify({"email": current_user}), 200

@auth_bp.route('/auth/logout', methods=['POST'])
@jwt_required()
def logout():
    """Cierra la sesión del usuario."""

    response = make_response(jsonify({"message": "Logout successful"}), 200)
    unset_jwt_cookies(response)
    return response
