

class Promotion(object):
    def __init__(self, discount_key, discount_price=None,
                 discount_product_id=None):
        self.discount_key = discount_key
        self.discount_price = discount_price
        self.discount_product_id = discount_product_id


class Item(object):
    """Items in the supermarket"""
    def __init__(self, item_id, price, promotions=None):
        self.item_id = item_id
        self.price = price
        self.promotions = promotions


class Cart(object):
    """
    Represents the current customer cart.
    """

    def __init__(self):
        self.items = {}
        self.bonus_items = {}

    def add_item_to_cart(self, item):
        """Adds item to cart or increments the quantity of that item."""
        if item.item_id in self.items:
            self.items[item.item_id]['quantity'] += 1
        else:
            self.items[item.item_id] = {'item': item, 'quantity': 1}

    def add_bonus_item_to_cart(self, item):
        """
        Adds item to bonus cart or increments the quantity of that item.
        Does not count to running total
        """
        if item.item_id in self.bonus_items:
            self.bonus_items[item.item_id]['quantity'] += 1
        else:
            self.bonus_items[item.item_id] = {'item': item, 'quantity': 1}

    def get_item_quantity_in_cart(self, item_id):
        return self.items[item_id]['quantity']

    def get_cart_items(self):
        return self.items.values()


class SuperMarket(object):
    """
    Supermarket class that contains items and runs the items to the cashier
    validating SKU's and applying discounts when available.
    """
    PRICE_TABLE = {
        'A': Item(item_id='A', price=50,
                  promotions=[Promotion(discount_key='AAAAA',
                                        discount_price=200),
                              Promotion(discount_key='AAA',
                                        discount_price=130),
                              ]),
        'B': Item(item_id='B', price=30,
                  promotions=[Promotion(discount_key='BB',
                                        discount_price=45)]),
        'C': Item(item_id='C', price=20, promotions=None),
        'D': Item(item_id='D', price=15, promotions=None),
        'E': Item(item_id='E', price=40,
                  promotions=[Promotion(discount_key='EE',
                                        discount_product_id='B')])
    }

    def __init__(self, cart_skus):
        self.running_total = 0
        self.cart = Cart()
        self.order = cart_skus

    def scan(self, sku):
        """
        Scans the item and adds it to the running total, applying discount if
        got to the discount quantity.

        @:return: True if it's a valid Stock Keeping Units, False otherwise.
        """
        item = self.PRICE_TABLE.get(sku)
        if item:
            self.running_total += item.price
            self.cart.add_item_to_cart(item=item)
            return True
        else:
            return False

    def apply_discounts(self):
        """
        Checks current quantity of items in cart and applies discount to
        running total if price discount or adds products to cart if bonus discount.
        If a discount is applied resets the cart count of that item to reapply
        discount.
        """
        for item in self.cart.items:
            number_of_promotions = len(item.promotions)
            applied_promotions = 0
            while applied_promotions != number_of_promotions:
                promotion = item.promotions[applied_promotions]
                if promotion.discount_key in self.order:
                    discount_price = promotion.discount_price
                    discount_product = promotion.discount_product_id
                    if discount_price:
                        discount = (len(promotion.discount_key) * item.price) - item.discount_price
                        self.running_total -= discount
                    else:
                        bonus_product = self.PRICE_TABLE.get(discount_product)
                        self.cart.add_bonus_item_to_cart(item=bonus_product)
                    self.order.replace(promotion.discount_key, '')
                else:
                    applied_promotions += 1

    def get_total(self):
        return self.running_total


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Supermarket checkout that calculates the total price of a number of
    items
    """
    supermarket = SuperMarket(sorted(skus))
    for sku in skus:
        valid_sku = supermarket.scan(sku)
        if not valid_sku:
            return -1
    supermarket.apply_discounts()
    return supermarket.get_total()
