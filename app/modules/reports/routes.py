from flask import render_template
from app.modules.reports import bp


@bp.route('/')
def index():
    return render_template('modules/reports/index.html')
