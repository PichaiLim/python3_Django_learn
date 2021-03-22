from django.shortcuts import render
from django.http import HttpResponse

from .models import AllProduct

# Create your views here.


def Home(request):
    # return HttpResponse('Hello');
    return render(request=request, template_name='product/home.html', context={})


def Aboutme(request):
    return render(request=request, template_name='product/about.html', context={})


def Mobile(request):
    allProduct = AllProduct.objects.all()
    contexts = {
        'allProduct': allProduct
    }
    return render(request=request, template_name='product/mobile.html', context=contexts)
