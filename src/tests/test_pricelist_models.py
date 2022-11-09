from src.api.app import db
from api.models import Item, Pricelist
from tests.base_test_case import BaseTestCase


class ItemModelTests(BaseTestCase):

    def test_pricelist(self):
        p = Pricelist()
        db.session.add(p)
        db.session.commit()
        assert p.url == 'http://localhost:5000/api/pricelists/' + str(p.id)
