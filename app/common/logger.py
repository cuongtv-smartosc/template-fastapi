import logging
from logging import DEBUG, INFO, ERROR
import os
import time

base_path = os.getcwd()
path = f"{base_path}/app/logs"
log_path = os.path.join(path)
if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}.log')

class Logger:

    def __init__(self, level=None, name=None):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s.%(msecs)03d - %(name)s : %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            # filename=log_path,
            # encoding="utf-8",
        )
        self.level = level
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(self.level)
        self.logger_query = None


    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    def log_query(self):
        self.logger_query = logging.getLogger('sqlalchemy')
        self.logger_query.setLevel(INFO)

    # def remove_log_query(self):
    #     self.logger_query.disabled = True

    def log_request(self, request):
        request.state.log_request = True



logger = Logger(level=INFO, name="LOG APP")
