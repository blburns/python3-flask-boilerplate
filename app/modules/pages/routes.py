from flask import render_template
from app.modules.pages import bp


@bp.route('/')
def index():
    return render_template('modules/sections/index.html')
