from django.contrib import admin

from ads.models import Category, ExtraFields


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ExtraFields)
class ExtraFieldsAdmin(admin.ModelAdmin):
    pass
