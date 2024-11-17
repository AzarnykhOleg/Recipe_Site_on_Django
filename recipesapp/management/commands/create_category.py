from django.core.management.base import BaseCommand
from ...models import Category
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Работа с таблицей категорий: Создание категории
    """
    help = "Create category."

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Category name')

    def handle(self, *args, **kwargs):
        title = kwargs['title']
        category = Category(title=title)
        category.save()
        logger.info(f'Successfully create category: {category}')
        self.stdout.write(f'{category}')