from django.contrib import admin

from .models import AdminDataBase,userDashboardDataBase,UserDataBase

admin.site.register(AdminDataBase)
admin.site.register(userDashboardDataBase)
admin.site.register(UserDataBase)