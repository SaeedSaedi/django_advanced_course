from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User

# Register your models here.


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("email",)


class CustomUserAdmin(UserAdmin):
    model = User
    # add_form = CustomUserCreationForm
    list_display = ("email", "is_staff", "is_active", "is_superuser", "is_verified")
    list_filter = ("email", "is_staff", "is_active", "is_superuser")
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        (
            "Permission",
            {"fields": ("is_staff", "is_active", "is_superuser", "is_verified")},
        ),
        ("Group permissions", {"fields": ("groups", "user_permissions")}),
        ("Logs", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
