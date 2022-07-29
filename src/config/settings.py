import os
from pathlib import Path

from dotenv import load_dotenv


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

ENVIRONMENT = os.getenv('ENVIRONMENT')

API_PREFIX = "/api"


# get env db
class EnvDB:
    DB_URL = os.getenv('DB_URL')
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    DB_NAME = os.getenv('DB_NAME')
    DB_HOST = os.getenv('DB_HOST')
    DB_POST = os.getenv('DB_POST')


TITLE = "Template FastApi"
DESCRIPTION = "Template fast api"
ORIGINS = ["*"]
BASE_PATH = "/Users/tranvancuong/Project/template-fastapi/src/"
VERSION = "0.1.0"
