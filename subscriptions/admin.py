from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from import_export.admin import ExportActionMixin
from .models import Orders ,Works, Comments , Commands,TypesItem

admin.site.site_header = 'Админ панель(SECOND)'


# admin.site.unregister(User)
# admin.site.unregister(Group)



@admin.register(TypesItem)
class TypesItemAdmin(ExportActionMixin,admin.ModelAdmin):

    
    list_display = ('id','title', 'price','заявка')
    # list_editable = ('active',)
    list_filter = ('id','title', 'price',)
    search_fields = ('id','title',)
    ordering = ('-id',)
    readonly_fields = ['заявка']
    fields = ('id','title', 'price','заявка',)



@admin.register(Orders)
class OrdersAdmin(ExportActionMixin,admin.ModelAdmin):
    

    list_display = ('id','phone', 'email','manager','вещи','итого', 'created', 'prosmotr', 'obrabotka', 'obrabotka_scklad', 'obrabotka_end',)
    # list_editable = ('active',)
    list_filter = ('prosmotr','obrabotka','obrabotka_scklad','obrabotka_end','created',)
    search_fields = ('email', 'phone')
    ordering = ('-created',)
    readonly_fields = ['created','id','вещи', 'итого']
    fields = ('id','email', 'phone', 'name','type','typevesch','вещи','итого','manager','data_succes', 'prosmotr', 'obrabotka', 'obrabotka_scklad', 'obrabotka_end','created',)

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
    list_display = ('id','name_user', 'message_text', 'created','moderation',)
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
