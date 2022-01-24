from django.contrib import admin
from .models import lib
# Register your models here.
@admin.register(lib)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')