from django import forms
from .models import User
class PopUpForm(forms.Form):
    name = forms.CharField()
    pet_name = forms.CharField()
    date = forms.DateField()
    email = forms.EmailField()
    phone = forms.CharField()
    service = forms.CharField()

    class Meta:
        model = User
        fields = ("name","pet_name","date","email","phone","service")


