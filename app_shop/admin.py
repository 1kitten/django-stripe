from django.contrib import admin
from .models import Item
from django.template.defaultfilters import truncatechars


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """ Add Item model to admin panel. """
    list_display = ['id', 'name', '_truncate_description']

    @staticmethod
    def _truncate_description(obj):
        return truncatechars(obj.description, 35)
