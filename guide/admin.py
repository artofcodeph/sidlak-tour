from django.contrib import admin
from .models import Guide


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'contact_number', 'area', 'specialization')
    search_fields = ('full_name', 'area', 'specialization')
    
