from django.contrib import admin

from .models import *
from .models import ClientProfile, OrderSave, OrderProduct, Product

class OrderProductInline(admin.StackedInline):
    model = OrderProduct
    can_delete = False
    readonly_fields = ('order', 'product', 'quantity', 'reduced_price_order', 'created_date', 'updated_date', 'total_price_order')
    extra = 0  # To prevent adding extra blank forms

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class OrderSaveAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]

    # Optionally, customize the list display in the OrderSave admin
    list_display = ('id', 'client', 'address', 'get_client_phone', 'created_date', 'updated_date')
    list_display_links = ['client', 'address']
    # Optionally, customize the search fields and filters
    search_fields = ('client__first_name', 'client__last_name', 'client__email')
    list_filter = ('created_date', 'updated_date')

    def get_client_phone(self, obj):
        if obj.client and obj.client.phone_number:
            return obj.client.phone_number
        return 'No phone number'
    get_client_phone.short_description = 'telefon raqami'

admin.site.register(ClientProfile)
admin.site.register(OrderSave, OrderSaveAdmin)
admin.site.register(Address)