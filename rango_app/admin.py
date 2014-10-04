from django.contrib import admin

# Register your models here.

from rango_app.models import Category, Page, UserProfile

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)