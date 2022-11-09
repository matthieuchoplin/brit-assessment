from flask import Blueprint, abort
from apifairy import authenticate, body, response, other_responses

from api import db
from api.decorators import paginated_response
from api.models import  Pricelist
from api.schemas import PricelistSchema

pricelists = Blueprint('pricelists', __name__)
pricelist_schema = PricelistSchema()
pricelists_schema = PricelistSchema(many=True)
update_pricelist_schema = PricelistSchema(partial=True)


@pricelists.route('/pricelists', methods=['POST'])
@body(pricelist_schema)
@response(pricelist_schema, 201)
def new(args):
    """Create a new pricelist"""
    pricelist = Pricelist()
    db.session.add(pricelist)
    db.session.commit()
    return pricelist


@pricelists.route('/pricelists/<int:id>', methods=['GET'])
@response(pricelist_schema)
@other_responses({404: 'Pricelist not found'})
def get(id):
    """Retrieve a pricelist by id"""
    return db.session.get(Pricelist, id) or abort(404)


@pricelists.route('/pricelists', methods=['GET'])
@paginated_response(pricelists_schema)
def all():
    """Retrieve all pricelists"""
    return Pricelist.select()


@pricelists.route('/pricelists/<int:id>', methods=['DELETE'])
@other_responses({403: 'Not allowed to delete the pricelist'})
def delete(id):
    """Delete a pricelist"""
    pricelist = db.session.get(Pricelist, id) or abort(404)
    db.session.delete(pricelist)
    db.session.commit()
    return '', 204
