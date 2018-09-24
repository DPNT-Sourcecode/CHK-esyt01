
from collections import namedtuple

SKU = namedtuple('SKU', 'item_id price discount_quantity discount_price discount_product')

PRICE_TABLE = {
    'A': SKU(item_id='A', price=50, discount_quantity=3, discount_price=130,
             discount_product=None),
    'B': SKU(item_id='B', price=30, discount_quantity=2, discount_price=45,
             discount_product=None),
    'C': SKU(item_id='C', price=20, discount_quantity=None, discount_price=None,
             discount_product=None),
    'D': SKU(item_id='D', price=15, discount_quantity=None, discount_price=None,
             discount_product=None),
    'E': SKU(item_id='E', price=40, discount_quantity=2, discount_price=None,
             discount_product='B'),
}


class SuperMarket(object):
    """
    Supermarket class that contains items and runs the items to the cashier
    validating SKU's and applying discounts when available.
    """

    def __init__(self, cart_items):
        self.running_total = 0
        self.cart = {}

    def scan(self, sku):
        """
        Scans the item and adds it to the running total, applying discount if
        got to the discount quantity.

        @:return: True if it's a valid Stock Keeping Units, False otherwise.
        """
        item = PRICE_TABLE.get(sku)
        if item:
            self.running_total += item.price
            self._add_item_to_cart(item)
            self._apply_discount(item)
            return True
        else:
            return False

    def _add_item_to_cart(self, item):
        """Adds item to cart or increments the quantity of that item."""
        if item.item_id not in self.cart:
            self.cart[item.item_id]['quantity'] += 1
        else:
            self.cart[item.item_id] = {'item': item, 'quantity': 1}

    def _apply_discount(self, item):
        """
        Check current cart count for the specified item and apply discount to
        running total if price discount or add products to cart if bonus discount.
        If a discount is applied resets the cart count of that item to reapply
        discount.
        :param item: SKU item present in PRICE_TABLE
        """
        current_count = self.cart[item.item_id]['quantity']
        discount_quantity = item.discount_quantity
        discount_price = item.discount_price
        discount_product = item.discount_product
        if discount_quantity and current_count == discount_quantity:
            if discount_price:
                discount = (discount_quantity * item.price) - item.discount_price
                self.running_total -= discount
            else:
                bonus_product = PRICE_TABLE.get(discount_product)
                self._add_item_to_cart(bonus_product)
            self.cart[item.item_id] = 0

    def get_total(self):
        return self.running_total


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Supermarket checkout that calculates the total price of a number of
    items
    """
    supermarket = SuperMarket()
    for sku in skus:
        valid_sku = supermarket.scan(sku)
        if not valid_sku:
            return -1
    return supermarket.get_total()
