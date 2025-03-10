from django.shortcuts import render
from django.http import JsonResponse
from .models import Tab, Product

def portfolio_view(request):
    tabs = Tab.objects.prefetch_related('products').all()
    return render(request, 'portfolio/index.html', {'tabs': tabs})

def get_products(request):
    tab_id = request.GET.get('tab_id')
    products = Product.objects.filter(tab_id=tab_id).values("title", "year", "url")
    return JsonResponse({"products": list(products)})