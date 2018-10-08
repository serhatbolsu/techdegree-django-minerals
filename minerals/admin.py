from django.contrib import admin

from .models import Mineral


# Register your models here.


class MineralAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'group')


admin.site.register(Mineral, MineralAdmin)
