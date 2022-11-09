from api.app import db
from api.models import Pricelist
from tests.base_test_case import BaseTestCase


class PricelistTests(BaseTestCase):
    def test_new_pricelist(self):
        rv = self.client.post('/api/pricelists', json={})
        assert rv.status_code == 201
        id = rv.json['id']

        rv = self.client.get(f'/api/pricelists/{id}')
        assert rv.status_code == 200
        assert rv.json['id'] == id

        rv = self.client.get('/api/pricelists')
        assert rv.status_code == 200
        assert rv.json['pagination']['total'] == 1
        assert rv.json['data'][0]['id'] == id

    def test_delete_pricelist(self):
        rv = self.client.post('/api/pricelists', json={})
        assert rv.status_code == 201
        id = rv.json['id']

        rv = self.client.delete(f'/api/pricelists/{id}')
        assert rv.status_code == 204

        rv = self.client.get(f'/api/pricelists/{id}')
        assert rv.status_code == 404
