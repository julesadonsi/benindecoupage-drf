from django.contrib import admin

from .models import Department, District, Neighborhoods, Town

admin.site.register(Department)
admin.site.register(Town)
admin.site.register(District)
admin.site.register(Neighborhoods)
