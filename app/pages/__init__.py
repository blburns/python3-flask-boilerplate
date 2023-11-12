from flask import Blueprint

bp = Blueprint('sections', __name__)

from app.pages import routes
