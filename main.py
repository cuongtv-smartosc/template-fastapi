import argparse

from app.common.logger import logger
from app.config.settings import ENVIRONMENT
from app.core.server import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn

    log_config = uvicorn.config.LOGGING_CONFIG
    logger.info(f"ENVIRONMENT={ENVIRONMENT}")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-env",
        "--environment",
        help="environment variable parameter.",
    )
    args = parser.parse_args()
    log_config["formatters"]["access"][
        "fmt"] = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] [trace_id=%(otelTraceID)s span_id=%(otelSpanID)s resource.service.name=%(otelServiceName)s] - %(message)s"
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True, log_config=log_config)
