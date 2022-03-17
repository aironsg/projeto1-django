from django.contrib import admin

from .models import Category, Recipe


# Register your models here.
# forma 1 de fazer o registro
class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)

# forma 2 de fazer o registro


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...
