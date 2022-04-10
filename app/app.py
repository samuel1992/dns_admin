from flask import Flask

from extensions import db
from config import Config


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)

    # TODO: Register our app modules/blueprints

    db.init_app(flask_app)

    return flask_app


app = create_app()
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'], host='0.0.0.0')
