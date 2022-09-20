from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ("username", "id", "first_name", "last_name",
                    "email")


admin.site.register(User, UserAdmin)
