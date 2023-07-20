from django.urls import path
from userauth import views

app_name = 'userauth'

urlpatterns = [
    path('sign-up/', views.Registerview, name='sign-up'),
    path('sign-in/', views.Registerview, name='sign-in'),
    path('sign-out/', views.LogoutView, name='sign out')
]
