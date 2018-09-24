

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

    def add_item_to_cart(self, item):
        """Adds item to cart or increments the quantity of that item."""
        if item.item_id in self.items:
            self.items[item.item_id]['quantity'] += 1
        else:
            self.items[item.item_id] = {'item': item, 'quantity': 1}

    def get_item_quantity_in_cart(self, item_id):
        return self.items[item_id]['quantity']

    def get_cart_items(self):
        return sorted(self.items.values(), key=lambda x: x['item'].item_id,
                      reverse=True)


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
                                        discount_product_id='B')]),
        'F': Item(item_id='F', price=10,
                  promotions=[Promotion(discount_key='FF',
                                        discount_product_id='F')]),
        'G': Item(item_id='F', price=20, promotions=None),
        'H': Item(item_id='H', price=10,
                  promotions=[Promotion(discount_key='HHHHHHHHHH',
                                        discount_price=80),
                              Promotion(discount_key='HHHHH',
                                        discount_price=45)]),
        'I': Item(item_id='I', price=35, promotions=None),
        'J': Item(item_id='J', price=60, promotions=None),
        'K': Item(item_id='K', price=80,
                  promotions=[Promotion(discount_key='KK',
                                        discount_price=150)]),
        'L': Item(item_id='L', price=90, promotions=None),
        'M': Item(item_id='M', price=15, promotions=None),
        'N': Item(item_id='N', price=40,
                  promotions=[Promotion(discount_key='NNN',
                                        discount_product_id='M')]),
        'O': Item(item_id='O', price=10, promotions=None),
        'P': Item(item_id='P', price=50,
                  promotions=[Promotion(discount_key='PPPPP',
                                        discount_price=200)]),
        'Q': Item(item_id='Q', price=30,
                  promotions=[Promotion(discount_key='QQQ',
                                        discount_price=80)]),
        'R': Item(item_id='R', price=50,
                  promotions=[Promotion(discount_key='RRR',
                                        discount_product_id='Q')]),
        'S': Item(item_id='S', price=30, promotions=None),
        'T': Item(item_id='T', price=20, promotions=None),
        'U': Item(item_id='U', price=40,
                  promotions=[Promotion(discount_key='UUU',
                                        discount_product_id='U')]),
        'V': Item(item_id='V', price=50,
                  promotions=[Promotion(discount_key='VVV',
                                        discount_price=130),
                              Promotion(discount_key='VV',
                                        discount_price=90)]),
        'W': Item(item_id='W', price=20, promotions=None),
        'X': Item(item_id='X', price=90, promotions=None),
        'Y': Item(item_id='Y', price=10, promotions=None),
        'Z': Item(item_id='Z', price=50, promotions=None)
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

    def _apply_price_discount(self, promotion, item):
        """Apply price discount to specific item quantity"""
        discount = (len(promotion.discount_key) * item.price) - promotion.discount_price
        self.running_total -= discount

    def _apply_product_discount(self, discount_product):
        """Add bonus product because of specific quantity"""
        bonus_product = self.PRICE_TABLE.get(discount_product)
        if discount_product in self.order:
            discount = bonus_product.price
            self.running_total -= discount
            self.order = self.order.replace(discount_product, '', 1)

    def apply_discounts(self):
        """
        Checks current quantity of items in cart and applies discount to
        running total if price discount or adds products to cart if bonus discount.
        If a discount is applied resets the cart count of that item to reapply
        discount.
        """
        for cart_item in self.cart.get_cart_items():
            item = cart_item['item']
            # only apply to items with promotions
            if item.promotions:
                number_of_promotions = len(item.promotions)
                applied_promotions = 0
                # checks all promotions,
                # passes to other promotion when hasn't found any more to apply
                while applied_promotions < number_of_promotions:
                    promotion = item.promotions[applied_promotions]
                    # checks the pattern is in the order
                    if promotion.discount_key in self.order:
                        # removes the items from the order since
                        # we are already applying promotion
                        self.order = self.order.replace(promotion.discount_key, '', 1)
                        discount_price = promotion.discount_price
                        discount_product = promotion.discount_product_id
                        # check if it's a price discount or product discount
                        if discount_price:
                            self._apply_price_discount(promotion, item)
                        else:
                            self._apply_product_discount(discount_product)
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
    supermarket = SuperMarket(''.join(sorted(skus)))
    for sku in skus:
        valid_sku = supermarket.scan(sku)
        if not valid_sku:
            return -1
    supermarket.apply_discounts()
    return supermarket.get_total()

