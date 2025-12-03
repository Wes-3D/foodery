# app/core/log.py
import logging
import sys

def setup_logging():
    """Configure global logging for the app."""
    # Root logger configuration
    logging.basicConfig(
        level=logging.INFO,  # can use DEBUG for more detail
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),  # print to console
            logging.FileHandler("app/core/app.log", mode="a", encoding="utf-8")  # write to file
        ],
    )

    # Silence noisy libraries (optional)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)

    logging.info("Logging initialized successfully")
