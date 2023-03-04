from django.contrib import admin

from menu.models import Component, Menu, MenuItem

admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Component)
