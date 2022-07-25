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

# get env db
DB_URI = os.getenv('db_uri')
DB_USER = os.getenv('user')
DB_PASS = os.getenv('password')
DB_NAME = os.getenv('db_name')
DB_HOST = os.getenv('host')
DB_POST = os.getenv('port')
