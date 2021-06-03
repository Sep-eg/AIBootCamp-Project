from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

database_uri ='sqlite+pysqlite:///myapp.sqlite3'

def create_app(config = None):
    app = Flask(__name__)

    app.config.update(
        SQLALCHEMY_DATABASE_URI=database_uri,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import (main_route, user_route)

    app.register_blueprint(main_route.bp)
    app.register_blueprint(user_route.bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()