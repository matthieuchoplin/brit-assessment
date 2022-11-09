import sqlalchemy as sqla
from sqlalchemy import orm as sqla_orm
from api.app import db

from flask import url_for


class Updateable:
    def update(self, data):
        for attr, value in data.items():
            setattr(self, attr, value)


class Pricelist(Updateable, db.Model):
    __tablename__ = 'pricelists'

    id = sqla.Column(sqla.Integer, primary_key=True)
    items = sqla_orm.relationship('Item', back_populates='pricelist',
                                      lazy='noload', cascade="all, delete-orphan")

    @property
    def summary(self):
        result = db.session.execute(self.items_select())
        items = [i[0] for i in result.fetchall()]
        return sum(i.price for i in items)

    def items_select(self):
        return Item.select().where(sqla_orm.with_parent(self, Pricelist.items))


    def __repr__(self):  # pragma: no cover
        return '<Pricelist {}>'.format(self.id)

    @property
    def url(self):
        return url_for('pricelists.get', id=self.id)


class Item(Updateable, db.Model):
    __tablename__ = 'items'

    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String(64), nullable=False)
    price = sqla.Column(sqla.Integer, default=0, nullable=False)
    pricelist_id = sqla.Column(sqla.Integer, sqla.ForeignKey(Pricelist.id), index=True)
    pricelist = sqla_orm.relationship('Pricelist', back_populates='items')

    def __repr__(self):  # pragma: no cover
        return '<Item {}>'.format(self.name)

    @property
    def url(self):
        return url_for('items.get', id=self.id)
