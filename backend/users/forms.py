from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"main__block-input",
        "placeholder":"Username"
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class":"main__block-input",
        "placeholder":"Имя"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class":"main__block-input",
        "placeholder":"Фамилия"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class":"main__block-input",
        "placeholder":"Email"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"main__block-input",
        "placeholder":"Пароль"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"main__block-input",
        "placeholder":"Повторный пароль"
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class AuthtorizationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'main__block-input',
        'placeholder':'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"main__block-input",
        'placeholder':'Пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

class ProfileForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email')