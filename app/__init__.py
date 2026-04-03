from flask import Flask

from . import models
from .config import Config
from .extensions import db, migrate, jwt
from .jwt_callbacks import init_jwt_callbacks
from .routes import main_bp, auth_bp, product_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt.init_app(app)
    init_jwt_callbacks(jwt)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)

    return app