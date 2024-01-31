from flask import Blueprint

bp = Blueprint('toolbox', __name__)

from app.modules.toolbox import routes
