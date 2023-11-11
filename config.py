import os
from os import environ, path, system
from typing import Any
from dotenv import load_dotenv


BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


class Config:
    """Set Flask configuration variables from .env file."""

    # General Config
    ENVIRONMENT = environ.get("ENVIRONMENT")

    # Flask Config
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = environ.get('SECRET_KEY')

    # Flask-Assets (Optional)
    LESS_BIN = system("which lessc")
    ASSETS_DEBUG = False
    LESS_RUN_IN_DEBUG = False
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = environ.get("COMPRESSOR_DEBUG")