from flask import Flask, render_template

from extensions import db
from config import Config

from record.api import app as record_app
from power_dns.api import app as power_dns_app


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)

    flask_app.register_blueprint(record_app, url_prefix='/records')
    flask_app.register_blueprint(power_dns_app, url_prefix='/dns')

    db.init_app(flask_app)

    return flask_app


app = create_app()
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'], host='0.0.0.0')
