from django.core.management.base import BaseCommand
from ...models import Recipe
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Работа с таблицей рецептов: Создание рецепта
    """
    help = "Create recipe."

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Recipe title')
        parser.add_argument('description', type=str, help='Recipe description')
        parser.add_argument('cooking_steps', type=str, help='Cooking_steps')
        parser.add_argument('cooking_time', type=int, help='Recipe required time')
        parser.add_argument('image', type=str, help='Recipe image')
        parser.add_argument('author_id', type=int, help='Recipe author id')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        cooking_steps = kwargs.get('cooking_steps')
        cooking_time = kwargs.get('cooking_time')
        image = kwargs.get('image')
        author_id = kwargs.get('author_id')

        author = User.objects.filter(pk=author_id).first()

        recipe = Recipe(name=name, description=description, cooking_steps=cooking_steps,
                        cooking_time=cooking_time, image=image, author=author)
        recipe.save()
        logger.info(f'Successfully create recipe: {recipe}')