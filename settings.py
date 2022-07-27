import logging.config
import os
from pathlib import Path

from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d - %(name)s : %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger("API")
logger.setLevel(logging.INFO)

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
