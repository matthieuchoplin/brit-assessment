from flask import Blueprint, abort
from apifairy import body, response, other_responses

from api import db
from api.models import Item, Pricelist
from api.schemas import ItemSchema
from api.decorators import paginated_response

items = Blueprint('items', __name__)
item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
update_item_schema = ItemSchema(partial=True)


@items.route('/items', methods=['POST'])
@body(item_schema)
@response(item_schema, 201)
def new(args):
    """Create a new item"""
    item = Item(**args)
    db.session.add(item)
    db.session.commit()
    return item


@items.route('/items/<int:id>', methods=['GET'])
@response(item_schema)
@other_responses({404: 'Item not found'})
def get(id):
    """Retrieve an item by id"""
    return db.session.get(Item, id) or abort(404)


@items.route('/items/<int:id>', methods=['PUT'])
@body(update_item_schema)
@response(item_schema)
@other_responses({403: 'Not allowed to edit this item',
                  404: 'Item not found'})
def put(data, id):
    """Edit an item"""
    item = db.session.get(Item, id) or abort(404)
    item.update(data)
    db.session.commit()
    return item


@items.route('/items/<int:id>', methods=['DELETE'])
@other_responses({403: 'Not allowed to delete the item'})
def delete(id):
    """Delete an item"""
    item = db.session.get(Item, id) or abort(404)
    db.session.delete(item)
    db.session.commit()
    return '', 204


@items.route('/pricelists/<int:id>/items', methods=['GET'])
@paginated_response(items_schema)
@other_responses({404: 'Pricelist not found'})
def pricelist_all(id):
    """Retrieve all items from a pricelist"""
    pricelist = db.session.get(Pricelist, id) or abort(404)
    return pricelist.items_select()
