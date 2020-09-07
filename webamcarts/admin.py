from django.contrib import admin
from .models import Cartmen, CartItem, Cartwomen, Cartkids, Cartaccessry

# Register your models here.

admin.site.register(Cartmen)
admin.site.register(CartItem)
admin.site.register(Cartwomen)
admin.site.register(Cartkids)
admin.site.register(Cartaccessry)