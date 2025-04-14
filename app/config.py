import os
from dotenv import load_dotenv
import datetime

load_dotenv()

class Config:
    user=os.getenv('USER_DB')
    passw=os.getenv('PASS_DB')
    data_base=os.getenv('DATA_BASE')
    schema=os.getenv('SCHEMA')
    host=os.getenv('HOST')
    port=os.getenv('PORT')

    DATABASE_URL = f"postgresql://{user}:{passw}@{host}:{port}/{data_base}"
    # print('DATABASE_URL: ', DATABASE_URL)
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=2)

    JWT_TOKEN_LOCATION = ['cookies']
    JWT_ACCESS_COOKIE_NAME = 'access_token'  # Se ajusta para que use el nombre que estableces manualmente

    # Para solicitudes cross-site, el token debe usar SameSite=None
    JWT_COOKIE_SAMESITE = 'None'  # Recuerda: si usas 'None' en producción se debe utilizar HTTPS
    JWT_COOKIE_SECURE = False  # En desarrollo puede ser False, pero en producción debe ser True si usas HTTPS

    # Si deseas, puedes desactivar la protección CSRF para cookies (aunque en producción es recomendable configurarla)
    JWT_COOKIE_CSRF_PROTECT = False