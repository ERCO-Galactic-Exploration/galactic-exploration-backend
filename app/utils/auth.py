from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt

def role_required(*roles):
    """
    Decorador para verificar si el usuario tiene uno de los roles requeridos.
    """
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get('role') not in roles:
                return {'error': 'No tienes permiso para acceder a este recurso.'}, 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper