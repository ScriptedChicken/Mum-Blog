"""
Reads .env variables and stores them as a Config()
object.
"""

import subprocess
from os import environ, path
from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


class Config:
    """Configuration from environment variables."""

    ENVIRONMENT = environ.get("ENVIRONMENT")

    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    FLASK_APP = "wsgi.py"

    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = False

    if ENVIRONMENT == "development":
        LESS_BIN = subprocess.call("where lessc", shell=True)
        if LESS_BIN is None:
            raise ValueError("Flask requires `lessc` to be installed to compile styles.")
        else:
            NODE_JS = subprocess.call("where node", shell=True)
            if NODE_JS is None:
                raise ValueError(
                    "Application running in `development` mode cannot create assets without `node` installed."
                )

    PRODUCT_DATA_FILEPATH = f"{BASE_DIR}/data/products.json"