from django.urls import path
from Accounts.views import *
urlpatterns = [
    path('registers/', registers, name='registers'),
    path('login/', login_view, name='login'),
    path('logout_user/',logout_user, name='logout_user'),
]  
