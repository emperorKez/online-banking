from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages

from account.models import Account

def search_account(request):
    account = Account.objects.filter(account_status='inactive')
    query = request.POST.get('search_account')
    if query:
        account = account.filter(Q(account_number=query) | Q(account_id=query) | Q(user__email=query)).distinct()
        
    context = {
        'account': account,
        'query': query
    }
    return render(request, 'transfer/search-account.html', context)

def transfer_amount(request, account_number):
    try:
        account = Account.objects.get(account_number=account_number)
    except:
        messages.warning(request, 'Account does not exist')
        return redirect('core:search-account')
        
    context = {
        'account': account
    }
    return render(request, 'transfer/transfer-amount.html', context)