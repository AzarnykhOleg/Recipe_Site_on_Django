from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from recipesapp.managers import PublishedManager


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название", null=False, blank=False)
    description = models.TextField(verbose_name="Описание продукта", null=False, blank=False)
    unit = models.CharField(max_length=45, verbose_name='Единица измерения')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'Продукт: {self.title}, описание: {self.description}'


class Category(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название категории', null=False, blank=False)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.title}'


class Recipe(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField(max_length=20, verbose_name='Название блюда', null=False, blank=False)
    description = models.TextField(verbose_name="Краткое описание рецепта", null=False, blank=False)
    # TODO: настроить нормальные отображение и вывод изображений
    image = models.ImageField(verbose_name="Изображение блюда", upload_to='images/', blank=True, null=True)
    cooking_steps = models.TextField(verbose_name='Шаги приготовления', null=False, blank=False)
    # TODO: добавить валидацию ввода времени приготовления блюда
    cooking_time = models.IntegerField(verbose_name='Время приготовления блюда, мин', default=1,
                                       validators=[MinValueValidator(1)])
    category = models.ForeignKey(Category, verbose_name='Категория рецепта', on_delete=models.CASCADE, null=True)
    # products = models.ManyToManyField(Product, verbose_name='Ингредиенты', through='RecipeProducts', null=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    status = models.CharField(verbose_name='Статус рецепта', max_length=10, choices=STATUS_CHOICES, default='draft')
    slug = models.SlugField(max_length=250, verbose_name='slug', unique_for_date='created_at')

    # Менеджер по умолчанию
    objects = models.Manager()
    # Опубликованные рецепты
    published_recipes = PublishedManager()

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def get_absolute_url(self):
        return reverse('recipe_details',
                       args=[self.created_at.strftime('%Y'),
                             self.created_at.strftime('%m'),
                             self.created_at.strftime('%d'),
                             self.slug,
                             ])

    def __str__(self):
        return f'Рецепт: {self.title}, описание: {self.description}'


class RecipeProducts(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(verbose_name='Количество')


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_category')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)






# class Steps(models.Model):
#     step_num = models.PositiveIntegerField(verbose_name="Порядковый номер шага")
#     description = models.TextField(verbose_name="Описание шага")
#     image = models.ImageField(upload_to='images/', default='1', verbose_name="Изображение шага")
#     cooking_steps = models.ForeignKey(Recipes, on_delete=models.PROTECT, default=None, verbose_name="Шаги")
#
#     def __str__(self):
#         return f'Шаг №: {self.step_num}, описание: {self.description}, изображение: {self.image}'
