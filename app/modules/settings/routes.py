from flask import render_template
from app.modules.settings import bp


@bp.route('/')
def index():
    return render_template('modules/settings/index.html')
