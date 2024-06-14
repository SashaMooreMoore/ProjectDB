from django.contrib import admin
from .models import InfoUsers

@admin.register(InfoUsers)
class InfoUsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'balance']
    list_display_links = ['name', 'age']
    list_filter = ['age']
    search_fields = ['name', 'message']
    list_per_page = 50
    
