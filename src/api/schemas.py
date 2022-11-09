from marshmallow import validates_schema, ValidationError

from api import ma
from api.models import Item, Pricelist

paginated_schema_cache = {}

class PricelistSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Pricelist
        include_relationships = True
        load_instance = True

    id = ma.auto_field(dump_only=True)
    items_url = ma.URLFor('items.pricelist_all', values={'id': '<id>'})


class ItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Item
        include_fk = True
        ordered = True

    id = ma.auto_field()
    name = ma.auto_field()
    price = ma.auto_field()
    pricelist_id = ma.Int()
    pricelist = ma.Nested(PricelistSchema, dump_only=True)


class StringPaginationSchema(ma.Schema):
    class Meta:
        ordered = True

    limit = ma.Integer()
    offset = ma.Integer()
    after = ma.String(load_only=True)
    count = ma.Integer(dump_only=True)
    total = ma.Integer(dump_only=True)

    @validates_schema
    def validate_schema(self, data, **kwargs):
        if data.get('offset') is not None and data.get('after') is not None:
            raise ValidationError('Cannot specify both offset and after')


def PaginatedCollection(schema, pagination_schema=StringPaginationSchema):
    if schema in paginated_schema_cache:
        return paginated_schema_cache[schema]

    class PaginatedSchema(ma.Schema):
        class Meta:
            ordered = True

        pagination = ma.Nested(pagination_schema)
        data = ma.Nested(schema, many=True)

    PaginatedSchema.__name__ = 'Paginated{}'.format(schema.__class__.__name__)
    paginated_schema_cache[schema] = PaginatedSchema
    return PaginatedSchema
