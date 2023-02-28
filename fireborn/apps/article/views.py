from django.shortcuts import render
from .models import *
from support.models import *
from article.models import *

# Create your views here.
def index(request):
    
    return render(request, 'article.html')