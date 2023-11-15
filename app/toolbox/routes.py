from flask import render_template
from app.toolbox import bp
from config import Config


@bp.route('/')
def index():
    return render_template('modules/toolbox/index.html')
