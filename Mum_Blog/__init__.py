"""Initialises Flask app"""
from flask import Flask
from flask_assets import Environment

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        from .assets import compile_static_assets
        from .home import home
        from .profile import profile

        app.register_blueprint(home.home_blueprint)
        app.register_blueprint(profile.profile_blueprint)

        compile_static_assets(assets)

        return app