from django.shortcuts import render, redirect
from userauth.forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def Registerview(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # username = request.POST.get('username')
            messages.success(request, f'Hey {username} , your account was created successfully')
            new_user = authenticate(username = form.cleaned_data['email'], password= form.cleaned_data['password1'])
            # new_user = authenticate(username = form.cleaned_data.get('email'))
            
            login(request, new_user)
            return redirect('core:index')
        
    if request.user.is_authenticated:
        messages.warning(request, ' you are already logged in')
        return redirect('core:index')
    
    else:
        form = UserRegisterForm()
            
    context = {
        'signup_form': form
    }
    return render(request, 'userauth/sign-up.html', context)

# def LoginView(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')

def LogoutView(request):
    logout(request.user)
    messages.success(request, 'You have successfully logged out')
    return redirect('userauth:sign-in')