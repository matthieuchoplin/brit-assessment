import click
from flask import Blueprint
from faker import Faker
from api.app import db
from api.models import Item, Pricelist
fake = Blueprint('fake', __name__)
faker = Faker()


@fake.cli.command()
def pricelist():  # pragma: no cover
    pricelist = Pricelist()
    db.session.add(pricelist)
    db.session.commit()
    item1 = Item(name="Apples", price=5, pricelist_id=pricelist.id)
    item2 = Item(name="Books", price=10, pricelist_id=pricelist.id)
    item3 = Item(name="Car", price=10000, pricelist_id=pricelist.id)
    db.session.add_all([item1, item2, item3])
    db.session.commit()
    print(f'Pricelist {pricelist.id} added.')
