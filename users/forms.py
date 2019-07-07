from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#Create a class 'UserRegisterForm' and pass a parameter 'UserCreationForm' so that it can inherit form from it.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
