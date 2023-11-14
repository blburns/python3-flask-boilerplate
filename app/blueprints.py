import app
from flask import Blueprint

bp = Blueprint('main', __name__)


class Blueprints:
    app.Blueprint()
    bp = Blueprint('main', __name__)

    import bp as main_bp
    app.register_blueprint(main_bp)

    # >>> pages_bp
    from app.blueprints import bp as pages_bp
    app.register_blueprint(pages_bp)

    # >>> dashboard_bp
    from app.blueprints import bp as dashboard_bp

    app.register_blueprint(dashboard_bp)