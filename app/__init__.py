from flask import Flask
from config import Config
# from flask_debugtoolbar import DebugToolbarExtension


def create_app():

    """Construct core Flask Application"""
    app = Flask(__name__, instance_relative_config=False)

    """Load configs"""
    app.config.from_object("config.Config")

    """Register Blueprints"""
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    """Test the Flask Application Factory"""
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Application Factory</h1>'

    """Return app"""
    return app


