import logging.config
import os
import time

base_path = os.getcwd()
path = f"{base_path}/app/logs"
log_path = os.path.join(path)
if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}.log')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d - %(name)s : %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    # filename=log_path,
    # encoding="utf-8",
)


class EndpointFilter(logging.Filter):
    # Uvicorn endpoint access log filter
    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().find("GET /metrics") == -1


logging.getLogger("uvicorn.access").addFilter(EndpointFilter())

logger = logging.getLogger("API")
logger.setLevel(logging.INFO)
