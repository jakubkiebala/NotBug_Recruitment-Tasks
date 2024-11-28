from flask import Flask


from .config import connect_to_db # type: ignore
from .routes import register_routes # type: ignore


def create_app():
    app = Flask(__name__)
    app.db_connection = connect_to_db()

    register_routes(app)

    return app
