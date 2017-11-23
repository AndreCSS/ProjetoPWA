from django.http import  HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    #return HttpResponse('sorry. web site in maintenance !!!')
    return render(request, 'index.html')


def contato(request):
    #return HttpResponse('sorry. web site in maintenance !!!')
    return render(request, 'contato.html')

def produto(request):
    #return HttpResponse('sorry. web site in maintenance !!!')
    return render(request, 'produto.html')

def produtos(request):
    #return HttpResponse('sorry. web site in maintenance !!!')
    return render(request, 'produtos.html')