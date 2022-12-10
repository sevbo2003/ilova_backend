from django.contrib import admin

from .models import PhoneToken, PhoneNumberAbstactUser


class PhoneNumberAbstactUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_staff')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    readonly_fields = ('last_login', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'phone_number', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                   'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(PhoneNumberAbstactUser, PhoneNumberAbstactUserAdmin)



class PhoneTokenAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'otp', 'timestamp', 'attempts', 'used')
    search_fields = ('phone_number', )
    list_filter = ('timestamp', 'attempts', 'used')
    readonly_fields = ('phone_number', 'otp', 'timestamp', 'attempts')


admin.site.register(PhoneToken, PhoneTokenAdmin)