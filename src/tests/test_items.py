from api.app import db
from api.models import Pricelist, Item
from tests.base_test_case import BaseTestCase


class ItemTests(BaseTestCase):
    def test_new_item(self):
        pricelist = Pricelist()
        db.session.add(pricelist)
        db.session.commit()
        rv = self.client.post('/api/items', json={
            'name': 'This is a test item',
            'price': 100,
            'pricelist_id': pricelist.id
        })
        assert rv.status_code == 201
        assert rv.json['name'] == 'This is a test item'
        assert rv.json['price'] == 100

        rv = self.client.get(f'/api/pricelists/{pricelist.id}/items')
        assert rv.status_code == 200
        assert rv.json['data'][0]['name'] == 'This is a test item'

        rv = self.client.get('/api/pricelists/2/items')
        assert rv.status_code == 404

    def test_edit_item(self):
        rv = self.client.post('/api/items', json={
            'name': 'This is a test item',
        })
        assert rv.status_code == 201
        assert rv.json['name'] == 'This is a test item'
        id = rv.json['id']

        rv = self.client.put(f'/api/items/{id}', json={
            'name': 'This is a test item edited',
        })
        assert rv.status_code == 200
        assert rv.json['name'] == 'This is a test item edited'

        rv = self.client.get(f'/api/items/{id}')
        assert rv.status_code == 200
        assert rv.json['name'] == 'This is a test item edited'

    def test_delete_item(self):
        rv = self.client.post('/api/items', json={
            'name': 'This is a test item',
        })
        assert rv.status_code == 201
        assert rv.json['name'] == 'This is a test item'
        id = rv.json['id']

        rv = self.client.delete(f'/api/items/{id}')
        assert rv.status_code == 204

        rv = self.client.get(f'/api/items/{id}')
        assert rv.status_code == 404
