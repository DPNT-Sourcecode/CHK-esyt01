
from collections import namedtuple

SKU = namedtuple('SKU', 'item_id price discount_quantity discount_price')

PRICE_TABLE = {
    'A': SKU(item_id='A', price=50, discount_quantity=3, discount_price=130),
    'B': SKU(item_id='B', price=30, discount_quantity=2, discount_price=45),
    'C': SKU(item_id='C', price=20),
    'D': SKU(item_id='D', price=15),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()
