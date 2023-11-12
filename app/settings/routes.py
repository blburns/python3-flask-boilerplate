from flask import render_template
from app.settings import bp


@bp.route('/')
def index():
    return render_template('modules/settings/index.html')
