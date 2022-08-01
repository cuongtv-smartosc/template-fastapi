import argparse

from app.common.logger import logger
from app.config.settings import ENVIRONMENT
from app.core.server import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn

    logger.info(f"ENVIRONMENT={ENVIRONMENT}")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-env",
        "--environment",
        help="environment variable parameter.",
    )
    args = parser.parse_args()

    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
