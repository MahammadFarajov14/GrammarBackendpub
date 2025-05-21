from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


# Create your views here.

def home(request):
    return render(request, 'home.html')
