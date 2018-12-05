from django.contrib import admin
from date_rls.models import Movie
from django.contrib.auth.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser')


admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Movie)
