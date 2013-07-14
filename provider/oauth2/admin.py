from django.contrib import admin
from .models import AccessToken, Grant, Client, RefreshToken


class AccessTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'token', 'expires', 'scope',)
    raw_id_fields = ('user',)


class GrantAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'code', 'expires',)
    raw_id_fields = ('user',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('url', 'user_names', 'redirect_uri', 'client_id', 'client_type')

    def user_names(self, obj):
        return ', '.join(obj.users.all().values_list('username', flat=True))
    user_names.short_description = 'Users'

admin.site.register(AccessToken, AccessTokenAdmin)
admin.site.register(Grant, GrantAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(RefreshToken)
