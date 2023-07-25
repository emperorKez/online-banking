from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages

from account.models import Account, KYC
from account.forms import KYCForm

def kyc_registration(request):
    user = request.user
    account = Account.objects.get(user=user)
    
    try:
        kyc = KYC.objects.get(user=user)
    except:
        kyc = None
        
    if request.method == 'POST':
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, 'KYC Form submitted successfully, in review now')
            return redirect('core:index')
    else:
          form = KYCForm(instance=kyc)
            
    context = {'account': account,
               'form': form,
               'kyc': kyc}
    return render(request, 'account/kyc-form.html', context)