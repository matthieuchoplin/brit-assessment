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
    return app
