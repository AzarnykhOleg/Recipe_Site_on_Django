from django.core.management.base import BaseCommand
from ...models import Product
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('-T', type=str, help='title')
        parser.add_argument('-D', type=str, help='description')
        parser.add_argument('-U', type=str, help='unit')

    def handle(self, *args, **kwargs):
        title = kwargs.get('T')
        description = kwargs.get('D')
        unit = kwargs.get('U')
        product = Product(title=title, description=description, unit=unit)
        product.save()
        logger.info(f'Successfully create product: {product}')
        self.stdout.write(f'{product}')
