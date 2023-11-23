from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorted_params = request.GET.get('sort')
    if sorted_params:
        if sorted_params == 'name':
            obj = Phone.objects.all().order_by('name')
        elif sorted_params == 'min_price':
            obj = Phone.objects.all().order_by('price')
        elif sorted_params == 'max_price':
            obj = Phone.objects.all().order_by('-price')
    else:
        obj = Phone.objects.all()
    context = {
        'phones': obj
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)[0]
    context = {'phone': phone}
    return render(request, template, context)
