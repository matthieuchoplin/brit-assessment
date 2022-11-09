from src.api.app import db
from api.models import Item, Pricelist
from tests.base_test_case import BaseTestCase


class ItemModelTests(BaseTestCase):

    def test_pricelist(self):
        p = Pricelist()
        db.session.add(p)
        db.session.commit()
        assert p.url == 'http://localhost:5000/api/pricelists/' + str(p.id)

    def test_pricelist_summary(self):
        p = Pricelist()
        db.session.add(p)
        db.session.commit()
        i1 = Item(name="book", price=10, pricelist_id=p.id)
        i2 = Item(name="car", price=10000, pricelist_id=p.id)
        db.session.add_all([i1, i2])
        db.session.commit()
        assert p.summary == 10010, p.summary
