from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        required=True,
        help_text='в формате +79993334455', label='Номер телефона')
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Заглавные и прописные буквы, знаки и символы',
    )

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email', 'password1', 'password2',)
