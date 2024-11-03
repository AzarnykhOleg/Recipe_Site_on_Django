from django.db import models
from django.contrib.auth.models import User


class Steps(models.Model):
    step_num = models.PositiveIntegerField(verbose_name="Порядковый номер шага")
    description = models.TextField(verbose_name="Описание шага")
    image = models.ImageField(upload_to='images/', default='1', verbose_name="Изображение шага")

    def __str__(self):
        return f'Шаг №: {self.step_num}, описание: {self.description}, изображение: {self.image}'


class Product(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название")
    description = models.TextField(verbose_name="Описание продукта")

    def __str__(self):
        return f'Продукт: {self.title}, описание: {self.description}'


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название категории')

    def __str__(self):
        return f'Категория: {self.name}'


class Recipes(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название блюда')
    description = models.TextField(verbose_name="Краткое описание рецепта")
    # TODO: добавить валидацию ввода времени приготовления блюда
    cooking_time = models.CharField(max_length=20, verbose_name='Время приготовления блюда')
    image = models.ImageField(upload_to='images/', default='2', verbose_name="Изображение блюда")
    recipe_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    cooking_steps = models.ManyToManyField(Steps, verbose_name="Шаги")

    def __str__(self):
        return f'Рецепт: {self.name}, описание: {self.description}, категория: {self.recipe_category}'
