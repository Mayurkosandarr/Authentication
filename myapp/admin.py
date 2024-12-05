from django.contrib import admin
from .models import Item

# Define a custom admin interface for the Item model
class ItemAdmin(admin.ModelAdmin):
    # Use valid fields that exist in the Item model
    list_display = ['title', 'description', 'created_at', 'owner']

# Register the Item model with the custom admin class
admin.site.register(Item, ItemAdmin)
