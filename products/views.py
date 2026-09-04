from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):#index表示app的主页
    products = Product.objects.all()
    return render(request,
                  "index.html",
                  {"products":products})


def new_product(request):
    return HttpResponse("New products")

