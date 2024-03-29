from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserDepartament

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Пользовательский заголовок (Custom)',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'position', 'date_of_birth', 'user_pic', 'department', 'info'
                ),
            },
        ),
    )
 
from .models import User
 
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserDepartament)


# admin.site.register(UserAdmin)
# Register your models here.
