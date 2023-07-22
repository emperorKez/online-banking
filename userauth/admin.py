from django.contrib import admin
from userauth.models import User
from import_export.admin import ImportExportModelAdmin

class UserAdmin(ImportExportModelAdmin):
    search_fields = ['email']


admin.site.register(User, UserAdmin)
