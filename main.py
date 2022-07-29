import argparse

from src.common.logger import logger
from src.config.settings import ENVIRONMENT
from src.core.server import create_app

logger.info(f"ENVIRONMENT={ENVIRONMENT}")

parser = argparse.ArgumentParser()
app = create_app()

# if __name__ == '__main__':
#     import uvicorn
#
#     uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True)
