from django.urls import path
from userauth import views

app_name = 'userauth'

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/', views.delete_account, name='delete')
]
 