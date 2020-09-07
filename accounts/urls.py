from django.urls import path
from .views import logout_view, login_view, registration_view, activation_view


urlpatterns = [
    path('accounts/logout', logout_view, name='auth_logout'),
    path('accounts/login', login_view, name='auth_login'),
    path('accounts/register', registration_view, name='auth_register'),
    path('accounts/activate/<str:activation_key>', activation_view, name='activation_view'),
]

