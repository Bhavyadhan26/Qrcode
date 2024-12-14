from django.contrib import admin
from .models import MenuItem, Order, OrderItem

# Inline model to show ordered items and their quantities within the Order page
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of empty forms to display initially in the admin
    
# Admin view for the Order model
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'created_at', 'get_order_items')
    inlines = [OrderItemInline]  # Include the order items inline form

    def get_order_items(self, obj):
        # Get a list of ordered items and their quantities in a readable format
        return ', '.join([f"{item.item.name} (x{item.quantity})" for item in obj.orderitem_set.all()])
    get_order_items.short_description = 'Ordered Items'

# Registering the models with the custom admin views
admin.site.register(MenuItem)  # Register MenuItem as is
admin.site.register(Order, OrderAdmin)  # Register Order with the custom admin
