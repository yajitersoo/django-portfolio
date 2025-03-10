from django.urls import path
from .views import portfolio_view, get_products

urlpatterns = [
    path('', portfolio_view, name='portfolio'),
    path('get-products/', get_products, name='get_products'),
]
