from django.contrib import admin

from .models import Worker


class WorkersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name')


admin.site.register(Worker, WorkersAdmin)
