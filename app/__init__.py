from flask import Flask
from config import Config
from flask import Blueprint
# from flask_debugtoolbar import DebugToolbarExtension


def create_app():

    """Construct core Flask Application"""
    app = Flask(__name__, instance_relative_config=False)

    """Load configs"""
    app.config.from_object("config.Config")

    """Register Blueprints for All Application Modules"""
    # >>> main_bp
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # >>> pages_bp
    from app.pages import bp as pages_bp
    app.register_blueprint(pages_bp, url_prefix='/pages')

    # >>> settings_bp
    from app.settings import bp as settings_bp
    app.register_blueprint(settings_bp, url_prefix='/settings')

    # >>> reports_bp
    from app.reports import bp as reports_bp
    app.register_blueprint(reports_bp, url_prefix='/reports')

    # >>> dashboard_bp
    from app.dashboard import bp as dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    """Test the Flask Application Factory"""
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Application Factory</h1>'

    """Return app"""
    return app


