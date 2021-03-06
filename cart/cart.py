from shop.models import Product


class Cart(object):
    # Helper class for the cart session
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart', False)
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add_to_cart(self, product_id):
        product = Product.objects.get(pk=product_id)
        product_info = {
            "price": str(product.price),
            "quantity": 1,
        }
        if self.cart.get(str(product.id), False):
            self.cart[str(product.id)]['quantity'] += 1
        else:
            self.cart[str(product.id)] = product_info
        self.save_session()

    def remove_from_cart(self, product_id):
        self.cart[str(product_id)]['quantity'] -= 1

        if self.cart[str(product_id)]['quantity'] <= 0:
            del self.cart[str(product_id)]

        self.save_session()

    def redirect_page(self):
        current_page = self.request.POST.get('next', '/')
        return current_page

    def save_session(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def __iter__(self):
        for key, item in self.cart.items():
            item['id'] = int(key)
            item['quantity'] = int(item['quantity'])
            item['price'] = float(item['price'])
            yield item

    def __len__(self):
        ret = sum([item['quantity'] for item in self])
        print(ret)
        return ret

    def get_total_price(self):
        return int(sum(item['price'] * item['quantity'] for item in self))

    def clear(self):
        self.cart = {}
        self.save_session()

    def get_items_in_cart(self):

        products = [(Product.objects.get(id=item['id']), item['quantity']) for item in self]

        return products
