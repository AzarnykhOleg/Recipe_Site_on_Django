# Generated by Django 5.1.2 on 2024-11-18 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapp', '0010_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Название блюда'),
        ),
    ]
