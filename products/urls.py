from django.urls import path
from products.views import home, productmen, productwomen, productkids, productaccessory, productmendetails, productwomendetails, productkidsdetails, productaccessdetails, search

urlpatterns = [
    path('s/', search, name='search'),
    path('', home, name='home'),
    
    path('male-dresses/', productmen, name='productmen'),
    path('male-dress-details/<str:slug>/', productmendetails, name='mdressdetails'),
    path('female-dresses/', productwomen, name='productwomen'),
    path('female-dress-details/<str:slug>/', productwomendetails, name='femaledressdetails'),
    path('child-dresses/', productkids, name='productkids'),
    path('kids-dress-details/<str:slug>/', productkidsdetails, name='kidsdressdetails'),
    path('accessories/', productaccessory, name='productaccessory'),
    path('accessories-dress-details/<str:slug>/', productaccessdetails, name='accessdressdetails'),
]