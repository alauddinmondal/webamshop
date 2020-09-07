from django.db import models
from products.models import ProductMen, Variation, ProductWomen, ProductKids, ProductAccessory


class Cartmen(models.Model):
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Cart men id: %s' %(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cartmen, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(ProductMen, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(max_digits=1000, decimal_places=2, default=10.99)
    notes = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title


class Cartwomen(models.Model):
    productwomen = models.ManyToManyField(ProductWomen)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    titmestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Cart women id: %s' %(self.id)

class Cartkids(models.Model):
    productkids = models.ManyToManyField(ProductKids)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Cart kids id: %s' %(self.id)

class Cartaccessry(models.Model):
    productaccessry = models.ManyToManyField(ProductAccessory)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Cart Accessory id: %s' %(self.id)

