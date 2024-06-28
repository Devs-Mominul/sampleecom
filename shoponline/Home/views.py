from django.shortcuts import render
from Home.models import *

# Create your views here.
def home(request):
    categories = Category.objects.all()
    return render(request, 'home/index.html',locals())
