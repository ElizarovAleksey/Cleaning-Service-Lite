from django.contrib import admin
from django.utils.html import format_html
from .models import Service, Order, OrderStatus


admin.site.site_header = "Панель администратора — Мой Не Сам"
admin.site.site_title = "Мой Не Сам — Админка"
admin.site.index_title = "Управление системой"


class CustomAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('admin/custom_admin.css',)
        }


@admin.register(Service)
class ServiceAdmin(CustomAdmin):
    list_display = ("id", "name")


@admin.register(OrderStatus)
class OrderStatusAdmin(CustomAdmin):
    list_display = ("id", "name")


@admin.register(Order)
class OrderAdmin(CustomAdmin):
    list_display = ("id", "user", "service", "colored_status", "created_at")
    list_filter = ("status", "service")
    search_fields = ("user__username", "address")

    def colored_status(self, obj):
        name = obj.status.name.lower()

        if "нов" in name:
            color = "#3498db"
        elif "работ" in name:
            color = "#f39c12"
        elif "выполн" in name:
            color = "#27ae60"
        elif "отмен" in name:
            color = "#e74c3c"
        else:
            color = "#555"

        return format_html(
            '<span style="color:{}; font-weight:bold;">{}</span>',
            color,
            obj.status.name
        )

    colored_status.short_description = "Статус"