import os
from dotenv import load_dotenv


class Config:
    load_dotenv()
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECTION = os.getenv("DATABASE_CONNECTION")

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("MYSQL_PRIVATE_URL")