from django.contrib import admin

from account.models import Account, KYC



class AccounAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_number', 'account_status', 'account_balance', 'date_created']
    search_fields = ['account_number']
    list_editable = ['account_status', 'account_balance']
    list_filter = ['account_status']
    
class KYCAdmin(admin.ModelAdmin):
    search_fields = ['full_name']
    list_display = ['user', 'full_name']
    
admin.site.register(Account, AccounAdmin)
admin.site.register(KYC, KYCAdmin)

