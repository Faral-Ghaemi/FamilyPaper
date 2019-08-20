from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('Name',)

@admin.register(models.Childrens)
class ChildrensAdmin(admin.ModelAdmin):
    list_display = ('Name', 'family','age')
    list_filter = ('family',)
