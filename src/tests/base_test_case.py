import unittest
from api.app import create_app, db
from config import Config


class TestConfig(Config):
    SERVER_NAME = 'localhost:5000'
    TESTING = True
    DISABLE_AUTH = True
    ALCHEMICAL_DATABASE_URL = 'sqlite://'


class BaseTestCase(unittest.TestCase):
    config = TestConfig

    def setUp(self):
        self.app = create_app(self.config)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        db.session.commit()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.close()
        db.drop_all()
        self.app_context.pop()
