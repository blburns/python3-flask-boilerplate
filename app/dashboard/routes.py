from flask import render_template
from app.dashboard import bp


@bp.route('/')
def index():
    return render_template('modules/dashboard/index.html')
