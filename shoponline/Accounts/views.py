from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()

# Create your views here.
def registers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        password1 = request.POST.get('pass1')
        if not name:
            messages.error(request, 'Please enter a name')
        if not email:
            messages.error(request, 'Please enter a email')
        if password is not None:
            if password == password1:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.save()
                messages.error(request, 'passwore not match')
               
                return redirect('login')
                
            
      
    return render(request, 'accounts/register.html')
def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            
            messages.success(request,'User successfully logigged in')
            return redirect('home')
        else:
            messages.error(request,'User fail logigged in')
            return redirect('registers')
               
          
                   
    return render(request, 'accounts/login.html')
def logout_user(request):
    logout(request)
    return redirect('login')
