import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask
from alchemical.flask import Alchemical
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from config import Config


db = Alchemical()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    if app.config['LOG_TO_STDOUT']:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
    else:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/pricelist.log',
                                           maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    # extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    if app.config['USE_CORS']:  # pragma: no branch
        cors.init_app(app)

    # blueprints
    from api.pricelist import pricelists
    app.register_blueprint(pricelists, url_prefix='/api')
    from api.items import items
    app.register_blueprint(items, url_prefix='/api')
    from api.fake import fake
    app.register_blueprint(fake)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Pricelist manager start up')
    return app
