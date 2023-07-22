from django.urls import path
from userauth import views

app_name = 'userauth'

urlpatterns = [
    path('signup/', views.Registerview, name='signup'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout')
]
