from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Orders ,Works, Comments , Commands

admin.site.site_header = 'Админ панель(SECOND)'


# admin.site.unregister(User)
# admin.site.unregister(Group)


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):


    list_display = ('phone', 'email', 'created', 'prosmotr',)
    # list_editable = ('active',)
    list_filter = ('prosmotr','obrabotka','obrabotka_scklad','obrabotka_end','created',)
    search_fields = ('email', 'phone')
    ordering = ('-created',)
    readonly_fields = ['created']
    fields = ('email', 'phone', 'name','type', 'prosmotr', 'obrabotka', 'obrabotka_scklad', 'obrabotka_end','created',)

@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'created','prosmotr',)
    # list_editable = ('active',)
    list_filter = ('prosmotr','created',)
    search_fields = ('email', 'phone')
    ordering = ('-created',)
    readonly_fields = ['created']
    fields = ('email', 'phone', 'name','prosmotr','message' ,'created',)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name_user', 'message_text', 'created','moderation',)
    # list_editable = ('active',)
    list_filter = ('moderation','created',)
    search_fields = ('name_user',)
    ordering = ('-created',)
    readonly_fields = ['created']
    fields = ('name_user', 'message_text', 'created','moderation',)


@admin.register(Commands)
class CommandsAdmin(admin.ModelAdmin):
    list_display = ('name_user', 'message_text', 'created','phone','prosmotr')
    # list_editable = ('active',)
    list_filter = ('prosmotr','created',)
    search_fields = ('name_user','phone',)
    ordering = ('-created',)
    readonly_fields = ['created']
    fields = ('name_user', 'message_text', 'created','phone','prosmotr',)
