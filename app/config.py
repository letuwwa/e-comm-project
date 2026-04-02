import os
from dotenv import load_dotenv
from datetime import timedelta


load_dotenv()


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)