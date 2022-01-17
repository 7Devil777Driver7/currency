from accounts.models import User

from currency.models import ContactUs, Rate, Source

from django.contrib import admin


class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'buy',
        'sale',
        'created',
        'cur_type',
        'source'
    )

    list_filter = [
        'cur_type'
    ]

    search_fields = (
        'buy',
        'sale',
        'cur_type',
        'source'
    )

    readonly_fields = (
        'buy',
        'sale'
    )


class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source_url',
        'name'
        )

    list_filter = [
        'name'
    ]


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_from',
        'subject',
        'message'
        )

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Rate, RateAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(User, UserAdmin)
