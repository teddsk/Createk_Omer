from django.contrib import admin
from listings.models import Sign

# Register your models here.

class ConnectAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'password')
admin.site.register(Sign, ConnectAdmin)