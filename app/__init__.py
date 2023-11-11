from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from config import Config


def create_app():

    """Construct core Flask Application"""
    app = Flask(__name__, instance_relative_config=False)

    """Load configs"""
    app.config.from_object("config.Config")

    """Test the Flask Application Factory"""
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Application Factory</h1>'

    """Return app"""
    return app


