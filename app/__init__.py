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
    from app.modules.pages import bp as pages_bp
    app.register_blueprint(pages_bp, url_prefix='/sections')

    # >>> settings_bp
    from app.modules.settings import bp as settings_bp
    app.register_blueprint(settings_bp, url_prefix='/settings')

    # >>> reports_bp
    from app.modules.reports import bp as reports_bp
    app.register_blueprint(reports_bp, url_prefix='/reports')

    # >>> dashboard_bp
    from app.modules.dashboard import bp as dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    # >>> toolbox_bp
    from app.modules.toolbox import bp as toolbox_bp
    app.register_blueprint(toolbox_bp, url_prefix='/toolbox')

    """Test the Flask Application Factory"""
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Application Factory</h1>'

    """Return app"""
    return app


