from .user_models import *


class Categories(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=40)
    media = models.FileField(upload_to='categories/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Brands(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=40)
    media = models.FileField(upload_to='brands/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Stores(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=40)
    media = models.FileField(upload_to='stores/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    delivery_charges = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    media = models.FileField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    charges = models.DecimalField(max_digits=10, decimal_places=2)
    itemsAvailable = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name='products')
    store = models.ForeignKey(Stores, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


class Sliders(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=40, blank=True)
    media = models.FileField(upload_to='sliders', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Faqs(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Faq(models.Model):
    type = models.ForeignKey(Faqs, on_delete=models.CASCADE, related_name='children')
    question = models.TextField()
    answer = models.TextField()


payment_statuses = (('Payment Pending', 'Payment Pending'),
                    ('Cash on Delivery', 'Cash on Delivery'),
                    ('Debit Card', 'Debit Card'),
                    ('Credit Card', 'Credit Card'),
                    ('Net Banking', 'Net Banking'))

order_statuses = (('Order Received', 'Order Received'),
                  ('Order Accepted', 'Order Accepted'),
                  ('Order Rejected', 'Order Rejected'),
                  ('Order Dispatched', 'Order Dispatched'),
                  ('Order Shipped', 'Order Shipped'),
                  ('Order Delivered', 'Order Delivered'),
                  ('Order Cancelled', 'Order Cancelled'))


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=20, choices=order_statuses, default='Payment Pending')
    payment_status = models.CharField(max_length=20, choices=payment_statuses, default='Order Received')
