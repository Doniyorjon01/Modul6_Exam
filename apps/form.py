from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField

from apps.models import User


class FormRegister(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'username', 'password']

    def clean_email(self, email):
        if not email.endswith('@gmail.com'):
            raise ValidationError("This email is not valid!")
        return email

    def clean_password(self, password):
        if len(password)<4:
            raise ValidationError("This password is not valid!")
        return password

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = "username", "password"

    def is_authenticate(self) -> User:
        data = self.clean()
        username = data.get("username")
        password = data.get("password")
        find_user = User.objects.filter(username).first()
        if not find_user:
            raise ValidationError("Not found user")
        if not check_password(password, find_user.password):
            raise ValidationError("Your password is wrong!")
        return find_user













