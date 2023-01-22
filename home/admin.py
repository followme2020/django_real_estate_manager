from django.contrib import admin
from home.models import LeadUser

class LeadUserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone_number', 'email', 'message')
# Register your models here.


admin.site.register(LeadUser, LeadUserAdmin)
