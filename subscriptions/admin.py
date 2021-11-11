from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Orders

admin.site.site_header = 'Админ панель(SECOND)'


# admin.site.unregister(User)
# admin.site.unregister(Group)


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):


    list_display = ('phone', 'email', 'created', 'prosmotr',)
    # list_editable = ('active',)
    list_filter = ('prosmotr','obrabotka','obrabotka_scklad','obrabotka_end')
    search_fields = ('email', 'phone')
    ordering = ('-created',)
    readonly_fields = ['created']
    fields = ('email', 'phone', 'name', 'prosmotr', 'obrabotka', 'obrabotka_scklad', 'obrabotka_end','created',)
