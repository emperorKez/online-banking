from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html')

def account(request):
    return render(request, 'core/account.html')

def contact(request):
    return render(request, 'core/contact.html')
