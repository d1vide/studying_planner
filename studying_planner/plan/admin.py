from django.contrib import admin

from .models import Category, Priority, Plan

admin.site.register(Category)
admin.site.register(Priority)
admin.site.register(Plan)
