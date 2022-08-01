import os
from pathlib import Path

from dotenv import load_dotenv

from app.config import config

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


BASE_PATH = os.getenv('BASE_PATH')

TITLE = "Template FastApi"
DESCRIPTION = "Template fast api"
ORIGINS = ["*"]
VERSION = "0.1.0"


class Settings:

    def __init__(self, env):
        self.env = env

    def get_config_env(self):
        yml = config.YMLConfig(env=self.env, config_file_path=f"{BASE_PATH}/src/config/config_env.yml")
        yml.get_yml_config()
        return yml.yml_config


setting = Settings(env="default")
