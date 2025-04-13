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
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=5)