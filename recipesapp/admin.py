from django.contrib import admin
from .models import Recipe, Category, Product


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'created_at', 'status']
    ordering = ['-category', '-created_at']
    list_filter = ['created_at', 'title']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание рецепта'


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
admin.site.register(Product)

# admin.site.register(Recipe)
# admin.site.register(Category)
# admin.site.register(Product)
