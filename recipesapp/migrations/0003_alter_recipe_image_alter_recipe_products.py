# Generated by Django 5.1.2 on 2024-11-16 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapp', '0002_recipecategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='2', upload_to='images/', verbose_name='Изображение блюда'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(null=True, through='recipesapp.RecipeProducts', to='recipesapp.product', verbose_name='Ингредиенты'),
        ),
    ]