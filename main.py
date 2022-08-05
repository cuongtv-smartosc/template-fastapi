import argparse
import time
from fastapi import Request

from app.common.logger import logger
from app.config.settings import ENVIRONMENT
from app.core.server import create_app
from app.common import LogRequest

app = create_app()

@app.middleware("http")
async def log_request_params(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    body = {}
    if request.state.__dict__.get("_state").get("req_body"):
        body = request.state.req_body
    log_request = LogRequest(request, response, body, process_time)
    logger.info(log_request)
    return response


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
