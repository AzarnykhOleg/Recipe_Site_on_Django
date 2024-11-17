import logging
import random

from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from recipesapp.forms import RecipeForm
from recipesapp.models import Recipe, Category

logger = logging.getLogger(__name__)


def recipe_full(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipesapp/recipe_full.html', {'recipe': recipe})


class Recipes(ListView):
    def get(self, request):
        if Recipe.objects.exists():
            recipes = list(Recipe.objects.all())
            recipes = random.sample(recipes, 6)
            return render(request,
                          'recipesapp/index.html',
                          {'recipes': recipes})
        else:
            return render(request, 'recipesapp/index.html')


class RecipeDelete(View):
    def post(self, request):
        if 'recipe_id' in request.POST:
            # Нажали кнопку УДАЛИТЬ - отображаем форму с подтверждением удаления

            recipe = Recipe.objects.filter(pk=request.POST['recipe_id']).first()
            messages.info(request, 'Подтверждение удаления')
            return render(request, 'recipesapp/recipe_delete.html',
                          {'recipe_id': str(request.POST['recipe_id']),
                           'recipe': recipe,
                           })
        else:
            # Подтвердили удаление в форме
            recipe_id = request.POST['id']
            recipe = Recipe.objects.filter(pk=recipe_id).first()
            if recipe is not None:
                logger.info(f'Successfully delete recipe (id={recipe_id}): {recipe}')
                recipe.delete()
            else:
                logger.warning(f'Client (id={recipe_id}) don\'t exist!')
            return redirect("/")


class RecipeDetail(View):
    def get(self, request):
        form = RecipeForm(initial={'id': '0',
                                   'title': '',
                                   'description': '',
                                   'cooking_steps': '',
                                   'cooking_time': 1,
                                   'image': '',
                                   # 'old_image': '',
                                   'category': '',
                                   # 'products': '',
                                   'author_id': request.user.id,
                                   })
        messages.info(request, 'Заполните форму')
        logger.info(f'Заполните форму')
        return render(request, 'recipesapp/recipe_detail.html', {'form': form})

    def post(self, request):
        """
        Обработка формы при редактировании или сохранении данных
        """
        if 'recipe_id' in request.POST:
            # Нажали кнопку РЕДАКТИРОВАТЬ - отображаем форму с редактируемыми данными
            # Вытаскиваем данные из базы данных
            recipe = Recipe.objects.filter(pk=request.POST['recipe_id']).first()
            initial = {'id': str(request.POST['recipe_id']),
                       'title': recipe.title,
                       'description': recipe.description,
                       'category': recipe.category,
                       'cooking_steps': recipe.cooking_steps,
                       'cooking_time': recipe.cooking_time,
                       'image': recipe.image,
                       # 'old_image': recipe.image,
                       'author_id': request.user.id
                       }
            form = RecipeForm(initial=initial)
            messages.info(request, f'Измените данные')
            return render(request, 'recipesapp/recipe_detail.html', {'form': form})
        else:
            # Пытаемся сохранить данные из формы
            form = RecipeForm(request.POST, request.FILES)

            if form.is_valid():
                recipe_id = form.cleaned_data['id']
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                category = form.cleaned_data['category']
                cooking_steps = form.cleaned_data['cooking_steps']
                cooking_time = form.cleaned_data['cooking_time']
                image = form.cleaned_data['image']
                author_id = form.cleaned_data['author_id']
                author = User.objects.filter(pk=author_id).first()
                fs = FileSystemStorage()
                category = Category.objects.get(title=category)

                if image:
                    fs.save(image.name, image)

                if recipe_id == 0:
                    # Вновь создаваемый рецепт
                    recipe = Recipe(title=title, description=description, cooking_steps=cooking_steps,
                                    cooking_time=cooking_time, image=image.name, author=author, category=category)
                else:
                    # Изменение данных уже существующего рецепта
                    recipe = Recipe.objects.filter(pk=recipe_id).first()
                    recipe.title = title
                    recipe.description = description
                    recipe.category = Category.objects.get(title=category)
                    recipe.cooking_steps = cooking_steps
                    recipe.cooking_time = cooking_time
                    # recipe.image = image.name if image else old_image
                    recipe.image = image.name
                    recipe.author = author
                recipe.save()
                logger.info(f'Successfully create recipe: {recipe}')
                return redirect("/")  # Переходим к таблице рецептов
            else:
                # если ошибка (или валидация не пройдена) - заново отображаем форму, с уже заполненными данными
                messages.warning(request, f'Ошибка в данных')
                return render(request, 'website/recipe_detail.html', {'form': form})
