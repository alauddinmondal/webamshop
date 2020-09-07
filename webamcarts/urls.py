from django.urls import path
from .views import cartmenview, remove_from_cart ,cartwomenview, cartkidsview, cartaccryview, update_cartmen

urlpatterns = [
    path('cartmen/', cartmenview, name='cartmen'),
    path('cartmen/<str:slug>/', update_cartmen, name='update_cartmen'),
    path('remove_from_cart/<int:id>/', remove_from_cart, name='remove_from_cart'),
    path('cartwomen/', cartwomenview, name='cartwomen'),
    path('cartkids/', cartkidsview, name='cartkids'),
    path('cartaccessory/', cartaccryview, name='cartaccessory'),
] 