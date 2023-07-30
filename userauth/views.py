from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from userauth.forms import UserRegisterForm
from userauth.models import User


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            # username = request.POST.get('username')
            messages.success(
                request, f"Hey {username} , your account was created successfully"
            )
            new_user = authenticate(
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
            )
            # new_user = authenticate(username = form.cleaned_data.get('email'))

            login(request, new_user)
            return redirect("account:account")

    if request.user.is_authenticated:
        messages.warning(request, " you are already logged in")
        return redirect("account:account")

    else:
        form = UserRegisterForm()

    context = {"signup_form": form}
    return render(request, "userauth/signup.html", context)


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in")
                return redirect("account:account")
            else:
                messages.warning(request, "Email or password is incorrect")
                return redirect("userauth:signin")
        except:
            messages.warning(request, "User does not exist")
            return redirect("userauth:signup")

    return render(request, "userauth/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("core:index")

def delete_account(request):
    messages.success(request, 'You have successfully deleted your account')
    return redirect('core:index')
