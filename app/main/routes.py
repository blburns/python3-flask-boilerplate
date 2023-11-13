from flask import render_template, redirect
from app.main import bp


@bp.route('/')
def index():
    return redirect('/dashboard')
    # return render_template('modules/main/index.html')
