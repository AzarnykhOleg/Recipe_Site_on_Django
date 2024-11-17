from django.urls import path
from . import views
from .views import Recipes, RecipeDetail, RecipeDelete, recipe_full

urlpatterns = [
    path('', Recipes.as_view(), name='index'),
    path('recipes/', Recipes.as_view(), name='recipes'),
    path('recipe/', RecipeDetail.as_view(), name='recipe_form'),
    path('delete/', RecipeDelete.as_view(), name='recipe_delete'),
    path('recipe_full/<int:recipe_id>/', recipe_full, name='recipe_full'),
]