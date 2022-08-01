import os
import time

import logging.config

from app.config import settings

log_path = os.path.join(settings.BASE_PATH, 'app/logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d - %(name)s : %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    # filename=log_path,
    # encoding="utf-8",
)

logger = logging.getLogger("API")
logger.setLevel(logging.INFO)
