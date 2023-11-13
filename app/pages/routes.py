from flask import render_template
from app.pages import bp


@bp.route('/')
def index():
    return render_template('modules/pages/index.html')
