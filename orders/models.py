from django.db import models
from webamcarts.models import Cartmen
from django.contrib.auth import get_user_model

User = get_user_model()



STATUS_CHOICES = (
    ('Started','Started'),
    ('Abandoned','Abandoned'),
    ('Finished','Finished'),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    cartmen = models.ForeignKey(Cartmen, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Started')
    sub_total = models.DecimalField(max_digits=1000, decimal_places=2, default=10.99)
    tax_total = models.DecimalField(max_digits=1000, decimal_places=2, default=0.00)
    final_total = models.DecimalField(max_digits=1000, decimal_places=2, default=10.99)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id


