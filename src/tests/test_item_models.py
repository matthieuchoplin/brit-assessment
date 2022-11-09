from src.api.app import db
from api.models import Item, Pricelist
from tests.base_test_case import BaseTestCase


class ItemModelTests(BaseTestCase):

    def test_item(self):
        p = Pricelist()
        item_name = 'test item'
        i = Item(name=item_name, price=10)
        db.session.add_all([p, i])
        db.session.commit()
        assert i.name == item_name
        assert i.url == 'http://localhost:5000/api/items/' + str(i.id)
