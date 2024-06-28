from django.urls import path
from test_mominul.views import *
urlpatterns = [
    path('base/', test_mominul, name='mominul'),
]  
