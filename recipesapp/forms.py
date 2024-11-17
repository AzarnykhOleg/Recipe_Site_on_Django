from django import forms

from recipesapp.models import Category, Product


class RecipeForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())

    title = forms.CharField(max_length=100,
                            label='Наименование рецепта',
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Введите название рецепта',
                                                          }))
    description = forms.CharField(label='Описание рецепта',
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Описание рецепта',
                                                               }))
    cooking_steps = forms.CharField(label='Шаги приготовления',
                                    widget=forms.Textarea(attrs={'class': 'form-control',
                                                                 'placeholder': 'Шаги приготовления рецепта',
                                                                 }))
    cooking_time = forms.IntegerField(min_value=1,
                                      label='Время приготовления',
                                      widget=forms.NumberInput(attrs={'class': 'form-control'}))

    category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all())

    # products = forms.MultipleChoiceField(label='Продукты', choices=Product.objects.all())

    image = forms.ImageField(label='Изображение', required=False)
    author_id = forms.IntegerField(widget=forms.HiddenInput())





