from django.urls import path
from core import views, transfer

app_name = 'core'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('search-account/', transfer.search_account, name='search-account'),
    path('transfer-amount/<account_number>/', transfer.transfer_amount, name='transfer-amount')
]
